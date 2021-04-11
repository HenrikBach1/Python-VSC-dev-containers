# Inspired from
#     https://python-forum.io/Thread-BrokenPipeError-Errno-32-Broken-pipe

# Globals
port = 6666

# Echo server program
import socket
import sys
 
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Get local machine name
host = socket.gethostname()
server_address = (host, port)

# Bind the socket to the port
print ("Listening on '{}'...".format(server_address))
sock.bind(server_address)
sock.listen(1)
 
while True:
    print('Waiting for a client connection...')
    (clientSocket, client_address) = sock.accept()
 
    try:
        print ("Connected to client: '{}'".format(client_address))
 
        # Receive the data in small chunks and retransmit it
        while True:
            chunk = 1024
            data = clientSocket.recv(chunk)
            dec_data = data.decode('utf-8')
            print("Data received: '{}'".format(dec_data))
            if dec_data:
                # <-- Jarvis code:
                print('Sending data to the client...')
                enc_data = dec_data.encode()
                # Jarvis code: -->
                clientSocket.sendall(enc_data)
            else:
                print("No more data from client: '{}'.".format(client_address))
                break
 
    finally:
        # Clean up the connection
        clientSocket.close()
        print('Client socket closed.')
