#!/usr/bin/python3

import socket
import threading

# Function to send messages
def send_msg(client_socket):
    while True:
        try:
            msg = input("You: ").encode()  # Add user prompt
            client_socket.send(msg)
        except (BrokenPipeError, ConnectionResetError):
            print("Connection closed by client.")
            break

# Function to receive messages
def recv_msg(client_socket):
    while True:
        try:
            received = client_socket.recv(1024)
            if not received:
                print("Client disconnected.")
                break
            print(f"Client: {received.decode()}")
        except (ConnectionResetError, OSError):
            print("Connection closed by client.")
            break

def main():
    # Initialize and configure the server socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 8888))
    print("Listening on 127.0.0.1:8888...")
    s.listen(1)

    # Accept client connection
    client_socket, addr = s.accept()
    print(f"Connected to {addr}.")

    # Create and start threads
    t1 = threading.Thread(target=send_msg, args=(client_socket,))
    t2 = threading.Thread(target=recv_msg, args=(client_socket,))
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

    # Clean up sockets
    client_socket.close()
    s.close()

if __name__ == "__main__":
    main()
