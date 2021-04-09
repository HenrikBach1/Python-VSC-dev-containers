port = 9999
BUFFER_SIZE = 1024

import socket

# Get local machine name
host = socket.gethostname()

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Communicate with Jarvis: <--
# Send command
jarvisCmd = "Hello"
clientsocket.sendto(jarvisCmd.encode(), (host,port))

# Receive answer
(jarvisMsg, serverAddr) = clientsocket.recvfrom(BUFFER_SIZE)
print("Received message: {}".format(jarvisMsg.decode()))
# Communicate with Jarvis: -->

# Close socket
clientsocket.close()