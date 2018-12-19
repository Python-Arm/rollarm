#serial per comunicazione seriale, lettura tasto tastiera
import serial
#from serial import Serial
from time import sleep
import msvcrt

#mettere il codice 12 cifre
#com=input("Inserire numero com")
#com="COM"+str(com)
ard=serial.Serial("COM5",9600)
ard.write("090090090170")

tasto='g'


ang1="090"
ang2="090"
ang3="090"
ang4="170"
m=0

while 1:
	tasto=msvcrt.getch()
	if  tasto == 'x':
		print("Arrivederci!")
		break
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
#		ard.write(ang4)
		print(ang4)
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
	ard.write(ang5)