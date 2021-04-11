# Inspired from
#     https://python-forum.io/Thread-BrokenPipeError-Errno-32-Broken-pipe

# Globals
port = 6666

# Echo client program
import socket
import sys
 
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Get local machine name
host = socket.gethostname()
server_address = (host, port)

print("Connecting to '{}'".format(server_address))
sock.connect(server_address)
 
try:
    # Send data
    message = ('This is the message.  It will be repeated.')
    enc_mes = message.encode('utf-8')
    print("Sending '{}'".format(message))
    sock.sendall(enc_mes)
 
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
 
    while amount_received < amount_expected:
        chunk = 1024
        data = sock.recv(chunk)
        amount_received += len(data)
        dec_data = data.decode('utf-8')
        print("Received {}".format(dec_data))
 
finally:
    sock.close()
    print('Socket closed')
