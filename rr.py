import sys
import time

noOfInterface = int(raw_input("Enter the number of port "))
inputport = [[] for i in range(noOfInterface)]
flag = 1
grantPtr = [0 for i in range(noOfInterface)]
acceptPtr = [0 for i in range(noOfInterface)]
for i in range(noOfInterface):
	str1=raw_input('Output ports for interface '+str(i+1)+' ')
	inputport[i]=str1.split(" ")
	inputport[i] = [int(j)-1 for j in inputport[i]]

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
			print "grant ",i,grantPtr[i]
	return grant

def callAcceptance(grant,noOfInterface):
	for i in range(noOfInterface):
		if(len(grant[i]) > 0):
			while acceptPtr[i] not in grant[i]:
				acceptPtr[i] = acceptPtr[i] + 1
			print "Input port ",i+1,"accepted grant from ",acceptPtr[i]+1
			del inputport[i][:]
			for k in range(noOfInterface):
				if acceptPtr[i] in inputport[k]:
					inputport[k].remove(acceptPtr[i])
	return inputport			

while flag == 1:
	grant = [[] for i in range(noOfInterface)]
	request = [[] for i in range(noOfInterface)]
	request = callRequest(inputport,noOfInterface)	
	print "returned from request"
	grant = callGrant(request,noOfInterface)
	inputport = callAcceptance(grant,noOfInterface)
	flag = 0 
	for i in range(noOfInterface):
		if (len(inputport[i]) != 0):
			flag = 1
