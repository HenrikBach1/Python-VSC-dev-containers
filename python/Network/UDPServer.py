port = 9999
BUFFER_SIZE = 1024

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get local machine name
host = socket.gethostname()

serversocket.bind((host, port))
print("Ready to receive...")
while True:
    (cmd, clientAddr) = serversocket.recvfrom(BUFFER_SIZE)
    jarvisCmd = cmd.decode()
    print("Got a connection from '{}' with command '{}'".format(clientAddr, jarvisCmd))

    # Jarvis code: <--
    jarvisMsg = jarvisCmd.upper()
    # Jarvis code: -->

    serversocket.sendto(jarvisMsg.encode(), clientAddr)
