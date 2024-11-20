#!/usr/bin/python3

import socket
import threading

# Function to send messages to the server
def send_msg(server_socket):
    while True:
        try:
            msg = input("You: ").encode()  # Add user prompt
            server_socket.send(msg)
        except (BrokenPipeError, ConnectionResetError):
            print("Connection closed by server.")
            break

# Function to receive messages from the server
def recv_msg(server_socket):
    while True:
        try:
            received = server_socket.recv(1024)
            if not received:
                print("Server disconnected.")
                break
            print(f"Server: {received.decode()}")
        except (ConnectionResetError, OSError):
            print("Connection closed by server.")
            break

def main():
    # Create and connect the client socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1", 8888)
    
    try:
        server_socket.connect(server_address)
        print(f"Connected to server at {server_address}.")
    except ConnectionRefusedError:
        print(f"Could not connect to server at {server_address}.")
        return

    # Create and start threads
    t1 = threading.Thread(target=send_msg, args=(server_socket,))
    t2 = threading.Thread(target=recv_msg, args=(server_socket,))
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

    # Clean up sockets
    server_socket.close()

if __name__ == "__main__":
    main()
