import socket
import threading
import pickle

# Server settings
HOST = 'localhost'  # Or your server IP address
PORT = 5555

# Game state
player_positions = [0, 0]
ball_position = [640, 400]
ball_speed = [0.00001, 0.00001]

# Function to handle client connections
def handle_client(conn, player_id):
    global player_positions
    global ball_position
    global ball_speed
    
    conn.send(pickle.dumps((player_id, ball_position, player_positions)))
    
    while True:
        try:
            data = pickle.loads(conn.recv(1024))
            if not data:
                break
            player_positions[player_id] = data['position']
            
            if player_id == 0:  # Only the first player controls the ball in this example
                ball_position[0] += ball_speed[0]
                ball_position[1] += ball_speed[1]
                # Simple collision with walls
                if ball_position[1] <= 0 or ball_position[1] >= 800:
                    ball_speed[1] = -ball_speed[1]
                if ball_position[0] <= 0 or ball_position[0] >= 1280:
                    ball_speed[0] = -ball_speed[0]
            
            game_state = (ball_position, player_positions)
            conn.sendall(pickle.dumps(game_state))
        except:
            break
    
    conn.close()

# Main server function
def main():
    global player_positions
    
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
