import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "10.100.55.173"
port = 9998
f=open ("1.jpg", "rb") 
l = f.read(1024)
while (l):
    s.sendto(l,(host,port))
    l = f.read(1024)

s.close()
