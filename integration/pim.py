import thread
import sys
import time
from random import randint
import turtle
from turtle import *
import math
from forwarding import *

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

def initialiseDraw(array,noOfInterface,isGrant,val,sub_slot):
	x = list()
	y = list()
	count = 0
	acceptCount = 0
	for i in range(noOfInterface):
		for j in array[i]:
			x.append(10+i*90)
			y.append(10+j*90)
			count+=1
	if isGrant == 0 and sub_slot == 0:
		acceptCount = count+1
		for i in range(noOfInterface):
			for j in range(noOfInterface):
				if j in acceptance[i]:
					acceptance[i].remove(j)
				if(sending[i][j] == 1):	#acceptance = [[0 for j in range(n)] for i in range(n)]
					x.append(10+i*90)
					y.append(10+j*90)
					count += 1
					sending[i][j]=0
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
	screen.setup( width = 1366, height = 768, startx = 0, starty = 0) 
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
				time.sleep(0.01)
			j=j+1
		screen.update()

noOfInterface = int(raw_input("Enter the number of port "))
Speed_Up_Factor = int(raw_input("Enter the speed up factor "))
#speedup_factor = int(raw_input("Enter the speed up factor "))
inputport = [[] for i in range(noOfInterface)]
voqList = [[] for i in range(noOfInterface)]
sending = [[0 for j in range(noOfInterface)] for i in range(noOfInterface)]
acceptance = [[] for i in range(noOfInterface)]
send_count = 0
flag = 1
if noOfInterface < 1 or noOfInterface > 4:
	print "Enter valid number of ports"
	sys.exit()

if noOfInterface == 1:
	n = randint(1,4)
	filename = "EthernetDump_"+str(n)+".txt" 
	print "filename = ",filename
	no = (int(getInterface(filename))-1) % noOfInterface
	if no!= -1:
		drawText("SENDING",300,225)
		drawcicle(noOfInterface,300)
		x = []
		y = []
		x.append(10)
		y.append(10)
		draw(x,y,1,0,300,1)
	turtle.exitonclick()
else:
	for i in range(noOfInterface):
		ports = randint(0,noOfInterface)
		for l in range(ports):
			n = randint(1,5)
			#no = (int(getInterface("EthernetDump.txt"))-1) % noOfInterface
			filename = "EthernetDump_"+str(n)+".txt" 
			print "filename = ",filename
			no = (int(getInterface(filename))-1) % noOfInterface
			print no
			if no not in inputport[i] and no!= -1:
				inputport[i].append(no)
				voqList[i].append(no)
		print "input = ",inputport[i]

def callRequest (inputport,noOfInterface):
	for i in range(noOfInterface):
		for j in inputport[i]:
			request[j].append(i)
			#print "*****************request ",i,"to ",j
	return request

def callGrant(request,noOfInterface):
	for i in range(noOfInterface):
		if(len(request[i]) > 0):
			rand = randint(0,len(request[i])-1)
			grant[request[i][rand]].append(i)
			#print "***************** grant ",request[i][rand],i
	return grant

def callAcceptance(grant,noOfInterface):
	count = 0
	x = list()
	y = list()
	drawText("ACCEPT",-350,225)
	drawcicle(noOfInterface,-300)
	drawVOQ(noOfInterface,-250)
	for i in range(noOfInterface):
		if(len(grant[i]) > 0):
			rand = randint(0,len(grant[i])-1)
			print "Input port ",i+1,"accepted grant from ",grant[i][rand]+1
			acceptance[i].append(grant[i][rand])
			sending[i][grant[i][rand]] = 1
			del inputport[i][:]
			for j in range(noOfInterface):
				if grant[i][rand] in inputport[j]:
					inputport[j].remove(grant[i][rand])
	initialiseDraw(acceptance,noOfInterface,2,-300,-1)	
	return inputport		
itr = 1
user_input = 1
time_slot = 4
no_of_itr = time_slot / Speed_Up_Factor
cycles = 0
sub_slot = 0
while(user_input == 1 and noOfInterface > 1):
	grant = [[] for i in range(noOfInterface)]
	request = [[] for i in range(noOfInterface)]
	acceptance = [[] for i in range(noOfInterface)]
	txt = "ITERATION "+str(itr)
	drawText(txt,150,300)
	if sub_slot != no_of_itr:
		drawText("REQUEST",550,225)
		drawVOQ(noOfInterface,600)
	else:
		drawText("REQUEST AND SENDING",550,225)
		sub_slot = 0
		for i in range(noOfInterface):
			ports = randint(0,noOfInterface)
			for l in range(ports):
				n = randint(1,5)
				#no =  (int(thread.start_new_thread( getInterface, ("EthernetDump.txt",)))) % noOfInterface
				filename = "EthernetDump_"+str(n)+".txt" 
				print "filename = ",filename
				no = (int(getInterface(filename))-1) % noOfInterface
				if no not in inputport[i] and no!= -1: 
					inputport[i].append(no)
					voqList[i].append(no)
			print "input = ",inputport[i]
	
	drawcicle(noOfInterface,550)
	request = callRequest(inputport,noOfInterface)
	initialiseDraw(inputport,noOfInterface,0,550,sub_slot)	
	sub_slot += 1
	grant = callGrant(request,noOfInterface)
	drawText("GRANT",100,225)
	drawcicle(noOfInterface,125)
	drawVOQ(noOfInterface,175)
	initialiseDraw(grant,noOfInterface,1,-150,-1)
	inputport = callAcceptance(grant,noOfInterface)
	#print "send_count", send_count
#	if itr != 1:
#		thread.start_new_thread(drawSending, (noOfInterface,acceptance) )
	flag = 0 
	for i in range(noOfInterface):
		if (len(inputport[i]) != 0):
			flag = 1
	itr+=1
	if sub_slot == no_of_itr:
		cycles += 1
	if(cycles == Speed_Up_Factor):
		cycles = 0
		user_input = int(raw_input("do you wanna continue\n"))
	turtle.exitonclick()
