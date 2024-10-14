# CHAT SIDE

import socket

# Define constants
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12134
ENCODER = "utf-8"
BYTESIZE = 1024

# create a client side to connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

# sending and receiving messages
while True:
    # receive message
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    # Quit message if connected server wants to stop
    if message == "quit":
        client_socket.send('quit'.encode(ENCODER))
        print("\nEnding the chat___now")
        break
    else:
        print(f"\n{message}")
        message = input("message: ")
        client_socket.send(message.encode(ENCODER))

# Close chat socket
client_socket.close()
