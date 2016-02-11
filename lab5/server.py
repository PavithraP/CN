import socket
import sys
from pygame import mixer # Load the required library
from thread import *

s = socket.socket()
s.bind(("0.0.0.0",9998))
s.listen(10) # Acepta hasta 10 conexiones entrantes.
print s

def music():
    mixer.init()
    mixer.music.load('file_1.mp3')
    mixer.music.play()

while True:
    sc, address = s.accept()
	
    print address
    i=1
    f = open('file_'+ str(i)+".mp3",'wb') #open in binary
    i=i+1
   # while (True):       
    # recibimos y escribimos en el fichero
    l = sc.recv(1024)
    while (l):
    	f.write(l)
    	l = sc.recv(1024)
    f.close()
    sc.close()
    start_new_thread(music ,())
    print "here"

s.close()
