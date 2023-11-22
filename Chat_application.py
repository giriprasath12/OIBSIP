import socket
import threading

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{username}: {message}")
        except Exception as e:
            print(f"Error receiving message from {username}: {e}")
            break

def main():
    host = '127.0.0.1'
    port = 55555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    clients = []

    def broadcast(message, sender_username):
        for client, username in clients:
            if username != sender_username:
                try:
                    client.send(f"{sender_username}: {message}".encode('utf-8'))
                except Exception as e:
                    print(f"Error sending message to {username}: {e}")

    def handle_client_connections():
        while True:
            client_socket, addr = server_socket.accept()
            username = client_socket.recv(1024).decode('utf-8')
            clients.append((client_socket, username))
            print(f"{username} connected from {addr}")

            client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
            client_thread.start()

    connections_thread = threading.Thread(target=handle_client_connections)
    connections_thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            break
        broadcast(message, 'Server')

    for client_socket, username in clients:
        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    main()
