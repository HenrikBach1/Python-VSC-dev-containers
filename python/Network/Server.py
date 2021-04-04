#!/usr/bin/python3           # This is server.py file

# Inspired from:
#     A Simple Server: https://www.tutorialspoint.com/python3/python_networking.htm
#     Testing the code [with PuTTY]: https://techtutorialsx.com/2018/06/02/esp8266-arduino-socket-server/
#     How to Expose Ports in Docker: https://www.whitesourcesoftware.com/free-developer-tools/blog/docker-expose-port/
#     Forwarding or publishing a port [in Docker]: https://code.visualstudio.com/docs/remote/containers#_forwarding-or-publishing-a-port
import socket                                         

# Create a socket object
serversocket = \
   socket.socket(
      socket.AF_INET       # Address Family: Internet Protocol v4
      ,socket.SOCK_STREAM  # TCP protocol
      )

# Get local machine name
host = socket.gethostname()                           

port = 9999                                           

# Bind to the port
serversocket.bind((host, port))                                  

# Create a buffer queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # Establish a connection
   clientsocket,addr = serversocket.accept()      

   print("Got a connection from %s" % str(addr))
    
   msg = 'Thank you for connecting'+ "\r\n"
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()