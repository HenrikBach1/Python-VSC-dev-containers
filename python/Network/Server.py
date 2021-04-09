#!/usr/bin/env python3

# Globals
port = 9999
BUFFER_SIZE = 1024

# To make this file executable, run below:
#     chmod a+x ./Server.py

# Inspired from:
#     A Simple Server: https://www.tutorialspoint.com/python3/python_networking.htm
#     Testing the code [with PuTTY]: https://techtutorialsx.com/2018/06/02/esp8266-arduino-socket-server/
#     How to Expose Ports in Docker: https://www.whitesourcesoftware.com/free-developer-tools/blog/docker-expose-port/
#     Forwarding or publishing a port [in Docker]: https://code.visualstudio.com/docs/remote/containers#_forwarding-or-publishing-a-port
#     VS Code with Python in Docker - Quickstart: https://dev.to/siaarzh/vs-code-with-python-in-docker-quickstart-3ph4#:~:text=Say%20you%20started%20your%20server%20with%20python%20manage.py,%22port%22%20and%20select%20%22Remote-Containers%3A%20Forward%20Port%20from%20Container...%22.
#     Remote debugging Python with VSCode: https://www.benoitpatra.com/2017/11/27/remote-debugging-python-with-vscode/
#     [shebang for Python3]: https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

import socket

def jarvis(cmd):
   print("'{}'".format(cmd))
   msg = 'Thank you for connecting'+ "\r\n"
   return msg

# Create a socket object
serversocket = \
   socket.socket(
      socket.AF_INET       # Address Family: Internet Protocol v4
      ,socket.SOCK_STREAM  # TCP protocol
      )

# Get local machine name
host = socket.gethostname()

# Bind to the port
serversocket.bind((host, port))

# Create a buffer to queue up to 5 requests
serversocket.listen(5)

while True:
   cmd = [BUFFER_SIZE]

   # Establish a connection
   clientsocket,addr = serversocket.accept()
   print("Got a connection from %s" % str(addr))   
   print("Reading input...")
   cmd = clientsocket.recv(BUFFER_SIZE)
   print("Read input: '{}'".format(cmd))

   # Jarvis code: <--
   msg = jarvis(cmd)
   # Jarvis code: -->
    
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()