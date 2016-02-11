#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "10.100.55.173" # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect(("10.100.55.173", 12345))
while True:
	txt = "Hello"
	s.send(txt)
	#raw_input()
	s.send("Hi")
	#print s.recv(1024)
s.close 
