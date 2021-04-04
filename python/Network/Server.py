#!/usr/bin/python3           # This is server.py file

# Inspired from:
#     https://www.tutorialspoint.com/python3/python_networking.htm
#     https://techtutorialsx.com/2018/06/02/esp8266-arduino-socket-server/
#     https://www.whitesourcesoftware.com/free-developer-tools/blog/docker-expose-port/
import socket                                         

# create a socket object
serversocket = \
   socket.socket(
      socket.AF_INET       # Address Family: Internet Protocol v4
      ,socket.SOCK_STREAM  # TCP protocol
      )

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# Create a buffer queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      

   print("Got a connection from %s" % str(addr))
    
   msg = 'Thank you for connecting'+ "\r\n"
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()