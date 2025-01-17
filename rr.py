import thread
import sys
import time
from random import randint
import turtle
from turtle import *
import numpy as np
import math

### Get the cursor position to the correct position###
def setPos(turt,back,up):
	turt.up()
	turt.back(back)
	turt.left(90)
	turt.forward(up)
	turt.down()
	
def drawcicle(noOfInterface,val):
	tlist = list()
	screen = turtle.getscreen()	
	screen.tracer(0)
	for i in range(noOfInterface):
	    	tlist.append(turtle.Turtle())
		setPos(tlist[i],val,200-(10+90*i))
		tlist[i].begin_fill()
		tlist[i].circle(15)
		tlist[i].end_fill()
		tlist[i].hideturtle() 
	for i in range(noOfInterface):
		turt = turtle.Turtle()
		setPos(turt,val-300,200-(10+90*i))
		turt.begin_fill()
		turt.circle(15)
		turt.end_fill() 
		turt.hideturtle()
	screen.update()
	

def drawVOQ(noOfInterface,val):
	tlist = list()
	screen = turtle.getscreen()	
	screen.tracer(0)
	count = 0 
	for i in range(noOfInterface):
		for j in range(noOfInterface):
	  	  	tlist.append(turtle.Turtle())
			setPos(tlist[count],val+5,210-(10+90*i+j*10))
			if j in voqList[i]:
				tlist[count].begin_fill()
			for k in range(2):
				tlist[count].forward(7)
				tlist[count].left(90)
				tlist[count].forward(30)
				tlist[count].left(90)
			if j in voqList[i]:
				tlist[count].end_fill()
			tlist[count].hideturtle() 
			count += 1
	screen.update()

def initialiseDraw(array,noOfInterface,isGrant,val):
	x = list()
	y = list()
	count = 0
	acceptCount = 0
	for i in range(noOfInterface):
		for j in array[i]:
			x.append(10+i*90)
			y.append(10+j*90)
			count+=1
	if isGrant == 0:
		suf = 0
		acceptCount = count+1
		for i in range(noOfInterface):
			for j in range(noOfInterface):
				if j in acceptance[i]:
					acceptance[i].remove(j)
				if(sending[i][j] == 1 and suf < speedup_factor):	#acceptance = [[0 for j in range(n)] for i in range(n)]
					x.append(10+i*90)
					y.append(10+j*90)
					count += 1
					sending[i][j]=0
					suf += 1
					voqList[i].remove(j)

		drawVOQ(noOfInterface,600)
	if isGrant == 1:
		draw(y,x,count,1,val,acceptCount)
	else:
		draw(x,y,count,isGrant,val,acceptCount)

def drawText(text,back,up):
	screen = turtle.getscreen()
	turt = turtle.Turtle()
	screen.tracer(0)
	setPos(turt,back,up)
	turt.write(text,font=("Arial", 20, "normal"))
	turt.hideturtle()
	screen.update()
	
def draw(x,y,count,isGrant,val,acceptCount):
	tlist = list()
	p = list()
	screen = turtle.getscreen()
	screen.setup( width = 2000, height = 2000, startx = None, starty = None) 
	for i in range(count):
	    screen.tracer(10)
	    tlist.append(turtle.Turtle())
	    #print "here",i,acceptCount,count
	    tlist[i].color("red")
	    if i >= acceptCount-1 and acceptCount!= 0:
		tlist[i].shape("square")
	    	tlist[i].color("green")
	    tlist[i].speed(1)
	    tlist[i].width(4)
	    angle = math.atan((y[i]-x[i])/300.0)
	    p.append(math.sqrt(90000+(x[i]-y[i])*(x[i]-y[i])))
	    if val == 200:
		setPos(tlist[i],val-275,200-x[i])
	    else:
		setPos(tlist[i],val,200-x[i])
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
speedup_factor = int(raw_input("Enter the speed up factor "))
inputport = [[] for i in range(noOfInterface)]
voqList = [[] for i in range(noOfInterface)]
sending = [[0 for j in range(noOfInterface)] for i in range(noOfInterface)]
acceptance = [[] for i in range(noOfInterface)]
send_count = 0
flag = 1
grantPtr = [0 for i in range(noOfInterface)]
acceptPtr = [0 for i in range(noOfInterface)]
for i in range(noOfInterface):
	ports = randint(0,noOfInterface)
	for l in range(ports):
		no = randint(0,noOfInterface-1)
		if no not in inputport[i]:
			inputport[i].append(no)
			voqList[i].append(no)
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
			while grantPtr[i] not in request[i]:
				grantPtr[i] = grantPtr[i] + 1
			grant[grantPtr[i]].append(i)
			#print "grant ",i,grantPtr[i]
	return grant

def callAcceptance(grant,noOfInterface, send_count):
	count = 0
	x = list()
	y = list()
	drawText("ACCEPT",-350,225)
	drawcicle(noOfInterface,-300)
	drawVOQ(noOfInterface,-250)
	for i in range(noOfInterface):
		if(len(grant[i]) > 0):
			while acceptPtr[i] not in grant[i]:
				acceptPtr[i] = acceptPtr[i] + 1
			print "Input port ",i+1,"accepted grant from ",acceptPtr[i]+1
			acceptance[i].append(acceptPtr[i])
			sending[i][acceptPtr[i]] = 1
			send_count += 1
			del inputport[i][:]
			for k in range(noOfInterface):
				if acceptPtr[i] in inputport[k]:
					inputport[k].remove(acceptPtr[i])
	initialiseDraw(acceptance,noOfInterface,2,-300)	
	return inputport,send_count			
itr = 1
while flag == 1:
	txt = "ITERATION "+str(itr)
	drawText(txt,150,300)
	grant = [[] for i in range(noOfInterface)]
	request = [[] for i in range(noOfInterface)]
	if itr == 1:
		drawText("REQUEST",550,225)
	else:
		drawText("REQUEST AND SENDING",550,225)
		send_count -= speedup_factor
	
	drawcicle(noOfInterface,550)
	request = callRequest(inputport,noOfInterface)
	initialiseDraw(inputport,noOfInterface,0,550)	
	grant = callGrant(request,noOfInterface)
	drawText("GRANT",100,225)
	drawcicle(noOfInterface,125)
	drawVOQ(noOfInterface,175)
	initialiseDraw(grant,noOfInterface,1,-150)
	inputport,send_count = callAcceptance(grant,noOfInterface, send_count)
	flag = 0 
	for i in range(noOfInterface):
		if (len(inputport[i]) != 0):
			flag = 1
	itr+=1
	turtle.exitonclick()
while(send_count > 0):
	drawText("SENDING",550,225)
	drawcicle(noOfInterface,550)
	send_count -= speedup_factor
	initialiseDraw(inputport,noOfInterface,0,550)	
	turtle.exitonclick()
