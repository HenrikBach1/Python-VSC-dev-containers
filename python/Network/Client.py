#!python3           # This is client.py file

import socket

print ("Client started...")

# Globals
port = 9999

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

print ("Connecting to {}:{}".format(host, port))

# Connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
msg = s.recv(1024)                                     

s.close()

# Print received message
print (msg.decode('ascii'))