import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "10.100.55.173"
port = 9998
f=open ("1.mp3", "rb") 
l = f.read(1024)
while (l):
    s.sendto(l,(host,port))
    l = f.read(1024)

time.sleep(8)

f=open ("1.jpeg", "rb") 
l = f.read(1024)
while (l):
    s.sendto(l,(host,port))
    l = f.read(1024)

time.sleep(5)

f=open ("2.jpeg", "rb") 
l = f.read(1024)
while (l):
    s.sendto(l,(host,port))
    l = f.read(1024)

time.sleep(5)

f=open ("3.jpeg", "rb") 
l = f.read(1024)
while (l):
    s.sendto(l,(host,port))
    l = f.read(1024)


time.sleep(5)

f=open ("5.jpeg", "rb") 
l = f.read(1024)
while (l):
    s.sendto(l,(host,port))
    l = f.read(1024)

time.sleep(5)

f=open ("4.jpeg", "rb") 
l = f.read(1024)
while (l):
    s.sendto(l,(host,port))
    l = f.read(1024)
s.close()
