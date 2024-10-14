# Chat Server

import socket

# Define constants
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12134
ENCODER = "utf-8"
BYTESIZE = 1024

# server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# acknowledge incoming connections
print("server is running .. \n")
client_socket, client_address = server_socket.accept()
client_socket.send("you are connected to the server... \n".encode(ENCODER))

# send and receive message
while True:
    # receive information
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    # Quit if Client wants to stop
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat___now")
        break
    else:
        print(f"\n{message}")
        message = input("message: ")
        client_socket.send(message.encode(ENCODER))

# close server socket
server_socket.close()

