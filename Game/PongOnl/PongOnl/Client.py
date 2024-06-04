import pygame, sys, random, socket, pickle

# Initial ball speed
initial_ball_speed = 6

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = screen_width/2 - 10
    ball.y = random.randint(10, 100)
    ball_speed_x = initial_ball_speed  # Reset the ball speed
    ball_speed_y = initial_ball_speed  # Reset the ball speed
    ball_speed_x *= random.choice([-1, 1])
    ball_speed_y *= random.choice([-1, 1])

def point_won(winner):
    global ball_speed, player2_points, player1_points

    if winner == "player2":
        player2_points += 1
    if winner == "player1":
        player1_points += 1
    ball_speed = initial_ball_speed
    reset_ball()

def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for a collision with the item
    if ball.colliderect(item):
        ball_speed_x *= 1.2
        ball_speed_y *= 1.2
        # Move the item to a new random position
        item.x = random.randint(0, screen_width)
        item.y = random.randint(0, screen_height)

    # Check for a collision with the second item
    if ball.colliderect(item2):
        ball_speed_x *= 0.8
        ball_speed_y *= 0.8
        # Move the second item to a new random position
        item2.x = random.randint(0, screen_width)
        item2.y = random.randint(0, screen_height)

    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1

    if ball.right >= screen_width:
        point_won("player2")

    if ball.left <= 0:
        point_won("player1")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

def animate_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1.y += player1_speed
    if keys[pygame.K_DOWN]:
        player1.y += player1_speed

    if keys[pygame.K_w]:
        player2.y -= player2_speed
    if keys[pygame.K_s]:
        player2.y += player2_speed

    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

# Network settings
HOST = 'localhost'  # Or the server's IP address
PORT = 5555

pygame.mixer.init()
pygame.init()

screen_width = 680
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pong Game!")

clock = pygame.time.Clock()

ball = pygame.Rect(0, 0, 30, 30)
ball.center = (screen_width / 2, screen_height / 2)

player2 = pygame.Rect(0, 0, 20, 100)
player2.centery = screen_height / 2

player1 = pygame.Rect(0, 0, 20, 100)
player1.midright = (screen_width, screen_height / 2)

ball_speed_x = 6
ball_speed_y = 6
player1_speed = 0
player2_speed = 6

player2_points, player1_points = 0, 0
score_font = pygame.font.Font(None, 100)

# Load background
background_image = pygame.image.load('img/background1.jpg').convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Load the item image
item_image = pygame.image.load('img/Icon.jpg')
item_image = pygame.transform.scale(item_image, (30, 30)).convert_alpha()

# Create the item
item = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)

# Load the second item image
item2_image = pygame.image.load('img/Icon2.jpg')
item2_image = pygame.transform.scale(item2_image, (30, 30)).convert_alpha()  # Corrected this line

# Create the second item
item2 = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 30, 30)

# Load and play background music:
pygame.mixer.music.load('sounds/background_music.mp3')
pygame.mixer.music.play(-1)  # The -1 makes the music loop indefinitely

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

player_id, ball_position, player_positions = pickle.loads(client.recv(1024))

while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_speed = -6
            if event.key == pygame.K_DOWN:
                player1_speed = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1_speed = 0

    # If the game is over, stop the background music
    game_over = False
    if game_over:
        pygame.mixer.music.stop()
    
    animate_ball()
    animate_player()

    # Update player position
    player_positions[player_id] = player1.y if player_id == 0 else player2.y

    # Send updated position to the server
    client.send(pickle.dumps({'position': player_positions[player_id]}))

    # Receive game state from server
    ball_position, player_positions = pickle.loads(client.recv(1024))

    # Update local game state
    ball.x, ball.y = ball_position
    player1.y, player2.y = player_positions

    # Change the positions of the game objects
    # animate_ball()
    # animate_player()

    # Check if a player has reached 10 points
    if player1_points >= 10:
        win_surface = score_font.render("You win!", True, "white")
        screen.blit(win_surface, (screen_width / 2, screen_height / 2))
        pygame.display.update()
        pygame.time.wait(6000)
        break
    elif player2_points >= 10:
        win_surface = score_font.render("You win!", True, "white")
        screen.blit(win_surface, (screen_width / 4, screen_height / 2))
        pygame.display.update()
        pygame.time.wait(6000)
        break

    # Clear the screen
    screen.fill('black')

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the score
    player2_score_surface = score_font.render(str(player2_points), True, "white")
    player1_score_surface = score_font.render(str(player1_points), True, "white")
    screen.blit(player2_score_surface, (screen_width / 4, 20))
    screen.blit(player1_score_surface, (3 * screen_width / 4, 20))

    # Draw the game objects
    pygame.draw.aaline(screen, 'white', (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.ellipse(screen, 'white', ball)
    pygame.draw.rect(screen, 'white', player2)
    pygame.draw.rect(screen, 'white', player1)

    # Draw the item
    screen.blit(item_image, item)

    # Draw the second item
    screen.blit(item2_image, item2)

    # Update the display
    pygame.display.flip()

    clock.tick(60)
