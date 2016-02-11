import socket
import sys
from pygame import mixer # Load the required library
from thread import *
from PIL import Image
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0",9998))

def music():
    mixer.init()
    mixer.music.load('file_1.mp3')
    mixer.music.play()

l, address = s.recvfrom(1024)
	
print address
f = open("file_1.mp3",'wb') #open in binary
while (len(l)>= 1024):
	f.write(l)
	l,address = s.recvfrom(1024)
	print len(l)
print "out"
f.write(l)
f.close()
start_new_thread(music ,())

while True:
	l, address = s.recvfrom(1024)
	print address
	i = 0
	f = open("file_"+str(i)+".jpg",'wb') #open in binary
	i+= 1
	while (len(l)>= 1024):
		f.write(l)
		l,address = s.recvfrom(1024)
	print "out"
	f.write(l)
	f.close()
	img = Image.open("file_"+str(i-1)+".jpg")
	img.show()
	print "showing image"
s.close()
