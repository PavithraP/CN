import sys
import fileinput
import ipaddress
import crcmod

def getInterface(filename):
	if len(filename) < 0:
		print "Enter the packet"
		sys.exit()

	file = open(filename, "r")
	filelen = len(file.read())-1
	file.seek(28,0)
	version=int(file.read(1),16)
	if version != 4:
		print "Invalid IP version"
		sys.exit()
		
	headerLen=int(file.read(1),16)*4
	if headerLen < 20:
		print "Header length is less than 20 bytes"
		sys.exit()


#	file.seek(32,0)
#	packetLen=int(file.read(4),16)
#	if (filelen/2)-14 != packetLen:
#		print "Packet length does not match Invalid packet"
#		sys.exit()


	file.seek(44,0)
	ttl=int(file.read(2),16)
	if ttl < 1:
		print "Invalid packet. Discarding it"
		sys.exit()

	
	file.seek(0,0)
	crc32 = crcmod.Crc(0x104c11db7, initCrc=0, xorOut=0xFFFFFFFF)
	crc32.update(str(int(file.read(108),16)))
	crc = file.read(8)
	if crc != crc32.hexdigest():
		print "Invalid packet. Discarding it"
                sys.exit()

	print hex(crc32.crcValue)
	print crc32.hexdigest()


	file.seek(52,0)
	sourceIp=str(int(file.read(2),16))+"."+str(int(file.read(2),16))+"."+str(int(file.read(2),16))+"."+str(int(file.read(2),16))
	destIp=str(int(file.read(2),16))+"."+str(int(file.read(2),16))+"."+str(int(file.read(2),16))+"."+str(int(file.read(2),16))
	interface = 0

	file.seek(24,0)
	ethType = int(file.read(4))
	if ethType == 800:
		file.seek(46,0)
		protocol = int(file.read(2),16)
		if protocol == 6:
			file.seek(28+headerLen*2,0)
			sourcePort = int(file.read(4),16)
			destPort = int(file.read(4),16)
			if sourcePort == 80:
				print "flow 1: IP TCP HTTP"
			elif sourcePort == 443:
				print "flow 2:IP TCP HTTPS"
		elif protocol == 11:
			file.seek(headerLen*2,0)
			sourcePort = int(file.read(4),16)
			destPort = int(file.read(4),16)
			if sourcePort == 80:
				print "flow 3:IP UDP HTTP"
			elif sourcePort == 443:
				print "flow 4:IP UDP HTTPS"

		elif protocol == 01:
			file.seek(headerLen*2,0)
			sourcePort = int(file.read(4),16)
			destPort = int(file.read(4),16)
			if sourcePort == 80:
				print "flow 5:ICMP echo reply"
			elif sourcePort == 443:
				print "flow 6:ICMP"


	file.close()
	with open("routerVssource.csv","r") as f:
		for line in f:
			values = [x.rstrip('\n') for x in line.split(',')]
			address = ipaddress.ip_network(values[0].decode('utf-8'))
			if ipaddress.ip_address(sourceIp.decode('utf-8')) in address.hosts():
				destFile = values[1]
				sourceNw = values[0]
	if ipaddress.ip_address(destIp.decode('utf-8')) in ipaddress.ip_network(sourceNw.decode('utf-8')).hosts():
		print "Receiver and sender are in same network"
	else:
		filename = "routing_table_"+destFile+".txt"
		flag=0
		print filename
		with open(filename,"r") as f:
			for line in f:
				if flag==0:
					values = [x.rstrip('\n') for x in line.split(',')]
					if(values[1] != values[2]): 
						if ipaddress.ip_address(destIp.decode('utf-8')) in ipaddress.ip_network(values[2].decode('utf-8')).hosts() and sourceIp == values[0]:
							flag =1
							print "source is",sourceIp
							print "Destination is",destIp
							print "interface is",values[3]
							print "next hop is",values[1]
							return values[3]
		if flag == 0:
			print "forwarding through default gateway"
			return -1
