import socket
import sys

s = socket.socket()
s.connect(("10.100.54.147",9998))
f=open ("1.jpg", "rb") 
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)

s.close()
