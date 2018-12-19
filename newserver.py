import socket
import time
import serial

#ard=serial.Serial("COM5",9600)
#ard.write("090090090170")

tasto='g'


ang1="090"
ang2="090"
ang3="090"
ang4="170"
m=0  
hostname = socket.gethostname()    
host = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + host) 
#host = '192.168.0.111'
port = 5000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

quitting = False
print "Server Started."
while not quitting:
    try:
		data, addr = s.recvfrom(1024)
		if "x" in str(data):
			quitting = True
		if addr not in clients:
			clients.append(addr)
		
		tasto=str(data)
		print str(data)
		if  tasto == 'x':
			print("Arrivederci!")
		elif tasto=='w':
			ang2=int(ang2)+5
			if ang2>180:
				ang2=180
			elif ang2<0:
				ang2=0
			print(ang2)
		elif tasto=='a':
			ang1=int(ang1)-5
			if ang1>180:
				ang1=180
			elif ang1<0:
				ang1=0
			print(ang1)
		elif tasto=='e':
			ang3=int(ang3)+5
			if ang3>180:
				ang3=180
			elif ang3<0:
				ang3=0
			print(ang3)
		elif tasto=='q':
			ang3=int(ang3)-5
			if ang3>180:
				ang3=180
			elif ang3<0:
				ang3=0
			print(ang3)
		elif tasto=='s':
			ang2=int(ang2)-5
			if ang2>180:
				ang2=180
			elif ang2<0:
				ang2=0
			print(ang2)
		elif tasto=='d':
			ang1=int(ang1)+5
			if ang1>180:
				ang1=180
			elif ang1<0:
				ang1=0
			print (ang1)
		elif tasto=='z':
			ang4="000"
			print(ang4)
		elif tasto=='c':
			ang4="170"
#			ard.write(ang4) omae wa mu shjinderu NANI!
		if ang1<100 and ang1>9:
			ang1="0"+str(ang1)
		elif ang1<10:
			ang1="00"+str(ang1)
		if ang2<100 and ang2>9:
			ang2="0"+str(ang2)
		elif ang2<10:
			ang2="00"+str(ang2)
		if ang3<100 and ang3>9:
			ang3="0"+str(ang3)
		elif ang3<10:
			ang3="00"+str(ang3)
		if ang4<100 and ang4>9:
			ang4="0"+str(ang4)
		elif ang4<10:
			ang4="00"+str(ang4)
		ang5=str(ang1)+str(ang2)+str(ang3)+str(ang4)
#		ard.write(ang5)
		print ang5
		for client in clients:
			s.sendto(data+" "+ang5, client)
    except:
        pass
s.close()