import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0",9998))

while True:
    l, address = s.recvfrom(1024)
	
    print address
    i=1
    f = open('file_'+ str(i)+".jpg",'wb') #open in binary
    i=i+1
    while (len(l)>= 1024):
    	f.write(l)
    	l,address = s.recvfrom(1024)
    print "out"
    f.write(l)
    
    f.close()

s.close()
