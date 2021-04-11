# Inspired from:
#     Computer Networking - A Top-Down Approach, p. 187+

port = 6666
BUFFER_SIZE = 1024

import socket

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get local machine name
host = socket.gethostname()

# Bind
serversocket.bind((host, port))
print("Listening...")

while True:
    (msg, clientAddr) = serversocket.recvfrom(BUFFER_SIZE)
    jarvisCmd = msg.decode()
    print("Got a connection from '{}' with command '{}'".format(clientAddr, jarvisCmd))

    # <-- Jarvis code:
    jarvisMsg = jarvisCmd.upper()
    # Jarvis code: -->

    serversocket.sendto(jarvisMsg.encode(), clientAddr)
