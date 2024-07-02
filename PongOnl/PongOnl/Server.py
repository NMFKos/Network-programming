import socket
import threading
import pickle

# Server settings
HOST = 'localhost'  # Or your server IP address
PORT = 5555

# Game state
player_positions = [150, 150]  # Initial positions for two players
ball_position = [340, 200]     # Initial ball position
ball_speed = [2, 2]
player_scores = [0, 0]         # Player scores

# Lock for synchronizing access to game state
game_state_lock = threading.Lock()

# Function to handle client connections
def handle_client(conn, player_id):
    global player_positions
    global ball_position
    global ball_speed
    global player_scores
    
    conn.send(pickle.dumps((player_id, ball_position, player_positions, player_scores)))
    
    while True:
        try:
            data = pickle.loads(conn.recv(1024))
            if not data:
                break
            player_positions[player_id] = data['position']
            
            with game_state_lock:
                # Update ball position only on the server side
                ball_position[0] += ball_speed[0]
                ball_position[1] += ball_speed[1]
                # Simple collision with walls
                if ball_position[1] <= 0 or ball_position[1] >= 400:
                    ball_speed[1] = -ball_speed[1]
                if ball_position[0] <= 0:
                    player_scores[1] += 1
                    ball_position = [340, 200]
                if ball_position[0] >= 680:
                    player_scores[0] += 1
                    ball_position = [340, 200]

                # Handle ball and paddle collisions
                if ball_position[0] <= 30 and player_positions[0] < ball_position[1] < player_positions[0] + 100:
                    ball_speed[0] = -ball_speed[0]
                if ball_position[0] >= 650 and player_positions[1] < ball_position[1] < player_positions[1] + 100:
                    ball_speed[0] = -ball_speed[0]

            game_state = (ball_position, player_positions, player_scores)
            conn.sendall(pickle.dumps(game_state))
        except:
            break
    
    conn.close()

# Main server function
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)  # We expect two players
    
    print("Server started. Waiting for connections...")
    
    player_id = 0
    while player_id < 2:
        conn, addr = server.accept()
        print(f"Player {player_id} connected from {addr}")
        thread = threading.Thread(target=handle_client, args=(conn, player_id))
        thread.start()
        player_id += 1
    
    server.close()

if __name__ == "__main__":
    main()
