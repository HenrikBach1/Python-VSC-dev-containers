# Inspired from:
#     Computer Networking - A Top-Down Approach, p. 187+

port = 6666
BUFFER_SIZE = 1024

import socket

# Get local machine name
host = socket.gethostname()

# Create a socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ("Connecting to {}:{}".format(host, port))

# <-- Communicate with Jarvis:
# Send command
jarvisCmd = "Hello"
print("Sending: '{}'".format(jarvisCmd))
clientSocket.sendto(jarvisCmd.encode(), (host, port))

# Receive answer
(jarvisMsg, serverAddr) = clientSocket.recvfrom(BUFFER_SIZE)
print("Received message: '{}'".format(jarvisMsg.decode()))
# Communicate with Jarvis: -->

# Close socket
clientSocket.close()
