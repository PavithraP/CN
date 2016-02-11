#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
from thread import *

s = socket.socket()         # Create a socket object
host = '0.0.0.0' # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

def clientthread(conn):
    #Sending message to connected client
#    conn.send("Welcome to the server. Type something and hit enter") #send only takes string
     
    while True:
        data = conn.recv(1024)
	print data
	print "Break"
        reply = 'OK...' + data
        if not data: 
            break
     
        #conn.sendall(reply)
     
    #came out of loop
    conn.close()



while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   #c.send("Welcome to the server. Type something and hit enter") #send only takes string
   start_new_thread(clientthread ,(c,))
   #c.close()
