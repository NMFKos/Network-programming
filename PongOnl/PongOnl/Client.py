import pygame
import sys
import socket
import pickle

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 680
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Multiplayer Pong Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Game objects
player_width = 10
player_height = 50
ball_size = 10

# Player rectangles
player1 = pygame.Rect(25, screen_height // 2 - player_height // 2, player_width, player_height)
player2 = pygame.Rect(screen_width - 25 - player_width, screen_height // 2 - player_height // 2, player_width, player_height)

# Ball rectangle
ball = pygame.Rect(screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2, ball_size, ball_size)

# Scores
player1_score = 0
player2_score = 0

# Load background
background_image = pygame.image.load('img/background1.jpg').convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Network settings
HOST = 'localhost'  # Server IP address
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Receive initial game state from server
data = pickle.loads(client.recv(1024))
player_id, ball_position, player_positions, player_scores = data
ball.x, ball.y = ball_position
player1.y, player2.y = player_positions
player1_score, player2_score = player_scores

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            client.close()
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if player_id == 0:  # Controls for player 1
        if keys[pygame.K_w] and player1.top > 0:
            player1.y -= 6
        if keys[pygame.K_s] and player1.bottom < screen_height:
            player1.y += 6
    else:  # Controls for player 2
        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= 6
        if keys[pygame.K_DOWN] and player2.bottom < screen_height:
            player2.y += 6

    # Send the new position to the server
    player_positions[player_id] = player1.y if player_id == 0 else player2.y
    client.send(pickle.dumps({'position': player_positions[player_id]}))

    # Receive updated game state from server
    data = pickle.loads(client.recv(1024))
    ball_position, player_positions, player_scores = data
    ball.x, ball.y = ball_position
    player1.y, player2.y = player_positions
    player1_score, player2_score = player_scores

    # Drawing everything on the screen
    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, white, player1)
    pygame.draw.rect(screen, white, player2)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height))

    # Display scores
    font = pygame.font.Font(None, 74)
    score_text = font.render(f"{player1_score}  {player2_score}", True, white)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 10))

    pygame.display.flip()
    clock.tick(60)
