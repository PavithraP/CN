import sys
import time
from random import randint
import turtle
from turtle import *
import numpy as np
import math

def drawcicle(noOfInterface,val):
	tlist = list()
	screen = turtle.getscreen()
	screen.tracer(0)
	for i in range(noOfInterface):
	    	tlist.append(turtle.Turtle())
		tlist[i].up()
		tlist[i].back(val)
		tlist[i].left(90)
		tlist[i].forward(200-(10+90*i))
		tlist[i].begin_fill()
		tlist[i].down()
		tlist[i].circle(15)
		tlist[i].end_fill()
		tlist[i].hideturtle() 
	for i in range(noOfInterface):
	    	turt = turtle.Turtle()
		turt.up()
		turt.back(val-300)
		turt.left(90)
		turt.forward(200-(10+90*i))
		turt.begin_fill()
		turt.down()
		turt.circle(15)
		turt.end_fill() 
		turt.hideturtle()
	screen.update()
	

def initialiseDraw(array,noOfInterface,isGrant,val):
	x = list()
	y = list()
	count = 0
	for i in range(noOfInterface):
		for j in array[i]:
			x.append(10+i*90)
			y.append(10+j*90)
			count+=1
	if isGrant == 0:
		draw(x,y,count,0,val)
	else:
		draw(y,x,count,1,val)

def drawText(text,back,up):
	screen = turtle.getscreen()
	screen.tracer(0)
	turt = turtle.Turtle()
	turt.up()
        turt.back(back)
        turt.left(90)
        turt.forward(up)
	turt.down()
	turt.write(text,font=("Arial", 20, "normal"))
	turt.hideturtle()
	screen.update()
	
def draw(x,y,count,isGrant,val):
	tlist = list()
	p = list()
	screen = turtle.getscreen()
	screen.setup( width = 2000, height = 2000, startx = None, starty = None) 
	for i in range(count):
	    screen.tracer(10)
	    tlist.append(turtle.Turtle())
	    tlist[i].color("red")
	    tlist[i].speed(1)
	    tlist[i].width(4)
	    angle = math.atan((y[i]-x[i])/300.0)
	    p.append(math.sqrt(90000+(x[i]-y[i])*(x[i]-y[i])))
	    tlist[i].up()
	    if val == 200:
	    	tlist[i].back(val-275)
	    else:
	    	tlist[i].back(val)
	    tlist[i].left(90)
	    tlist[i].forward(200-x[i])
	    if isGrant == 1:
		    tlist[i].right(180-math.degrees(angle)+90)
	    else:
		    tlist[i].right(math.degrees(angle)+90)
	    screen.update()
    
	for i in xrange(100):
		j=0
		for t in tlist:
			t.down()
			if (i*(i+1))/2 < p[j]:
				t.forward(i)
			j=j+1
		screen.update()

noOfInterface = int(raw_input("Enter the number of port "))
inputport = [[] for i in range(noOfInterface)]
flag = 1
for i in range(noOfInterface):
	ports = randint(0,noOfInterface)
	for l in range(ports):
		inputport[i].append(randint(0,noOfInterface-1))
	print "input = ",inputport[i]

def callRequest (inputport,noOfInterface):
	for i in range(noOfInterface):
		for j in inputport[i]:
			request[j].append(i)
	#		print "request ",i,"to ",j
	return request

def callGrant(request,noOfInterface):
	for i in range(noOfInterface):
		if(len(request[i]) > 0):
			rand = randint(0,len(request[i])-1)
			grant[request[i][rand]].append(i)
	#		print "grant ",request[i][rand],i
	return grant

def callAcceptance(grant,noOfInterface):
	count = 0
	x = list()
	y = list()
	for i in range(noOfInterface):
		if(len(grant[i]) > 0):
			rand = randint(0,len(grant[i])-1)
			print "Input port ",i+1,"accepted grant from ",grant[i][rand]+1
			x.append(10+i*90)
			y.append(10+grant[i][rand]*90)
			count+= 1
			del inputport[i][:]
			for j in range(noOfInterface):
				if grant[i][rand] in inputport[j]:
					inputport[j].remove(grant[i][rand])
	drawText("ACCEPT",-350,225)
	#drawcicle(noOfInterface,-200)
	drawcicle(noOfInterface,-300)
	draw(x,y,count,0,-300)
	return inputport			
itr = 1
while flag == 1:
	txt = "ITERATION "+str(itr)
	drawText(txt,150,300)
	grant = [[] for i in range(noOfInterface)]
	request = [[] for i in range(noOfInterface)]
	drawText("REQUEST",550,225)
	#drawcicle(noOfInterface,600)
	drawcicle(noOfInterface,550)
	request = callRequest(inputport,noOfInterface)
	initialiseDraw(inputport,noOfInterface,0,550)	
	grant = callGrant(request,noOfInterface)
	drawText("GRANT",100,225)
	#drawcicle(noOfInterface,200)
	drawcicle(noOfInterface,125)
	initialiseDraw(grant,noOfInterface,1,-150)
	inputport = callAcceptance(grant,noOfInterface)
	flag = 0 
	for i in range(noOfInterface):
		if (len(inputport[i]) != 0):
			flag = 1
	itr+=1
	turtle.done()
