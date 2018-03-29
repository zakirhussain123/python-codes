#!/usr/bin/python

# Author:  SoMutchToDo
# Feel free to reuse my work
# Last Updated 2012-02-27

# Read a text file and send a signal to arduino via a serial connection


import time, os, re, urllib
import msvcrt
import sys      # needed to end the program
import serial   # use pyserial to send commands to arduino
from datetime import datetime
import os
import serial.tools.list_ports
import binascii
import numpy as np
PORT="COM3"     # This port will need to be adjusted to match your installation
TARGET="C:/debug/ver20.0.0_163_DEV/"

global ser

def list_and_open_comport():
	global ser
	comports = list(serial.tools.list_ports.comports( ))
	for p in comports:
		print ("%s\n"%p)
	PORT=input("select Available COM port\n")
	try :
		ser = serial.Serial(PORT, 9600,timeout=0.05)
		return 1
	except:
		print("check COM port selected ")

	

#************************************************************************
#get keypress form kerboard
def kbfunc():

	x = msvcrt.kbhit()
	if x:
		ret = ord(msvcrt.getch())
	else:
		ret = 1
	return ret
 #**********************************************************************  
	
	
def show_COM_Error():
	print("COM Port Error");
	print("check COM port or Reconnect");
	sys.exit()
	
# Send pass argument string to COM port
def commandarduino(sendvalue):
	#print (" Sending Value: %s\n" % sendvalue)
	try:
		ser.write( sendvalue)
	except:
		  show_COM_Error()
		  
	#ser.write( sendvalue.encode('ascii','ignore'))

    
	
def Delay_and_check_Keypress(delaycount):
	sleepiter=0
	while sleepiter<delaycount:
		time.sleep(0.001)
		X=kbfunc()  # This allows the user to push Z to exit
		if X==0x1b:
			sys.exit()
		sleepiter=sleepiter+1
	return 
	


fotafolder=""


#os.chdir('../')
cwd=os.getcwd()
print(cwd)
	
while True:
	TARGET=cwd+'/';
	filename=TARGET+'logData.txt'
	print(filename)
	try:
		txtfile=open(filename,"rb")
		break
	except:
		print(TARGET)
		print("Error:Folder or File Not Found ")
		Delay_and_check_Keypress(10);

		
print("timeStamp,a1,A2,A3,A4,PRF,AZ,AL")
#sys.stdout = open('out2.csv', 'w')				
lineno=0
array=txtfile.readline()
while( array != ""):
#while( lineno <10):
	array=txtfile.read(24)
	lineno+=1;
	try :
		time1=((array[0]<<24)|(array[1]<<16)|(array[2]<<8)|array[3])
		a1=((array[5]<<8) | array[6])
		a2=((array[7]<<8) | array[8])
		a3=((array[9]<<8) | array[10])
		a4=((array[11]<<8) | array[12])
		prf=((array[13]<<8) | (array[14]))
		az=((array[15]<<24)|(array[16]<<16)|(array[17]<<8)|array[18])
		al=((array[19]<<24)|(array[20]<<16)|(array[21]<<8)|array[22])    		
		print("%d,%d,%d,%d,%d,%d,%d,%d,%d" % (lineno,time1, a1,a2,a3,a4,prf,(az/100000),(al/100000)))
		#print(array)
	except:
			i=0

	Delay_and_check_Keypress(10);
sys.exit()


# string=""
# while ( retry<100) :
	# try:
		# ser.write( startupadte.encode('ascii','ignore'))
	# except:
		  # show_COM_Error()
			
	# responseTimeout=0;
	# ResponseRecived=0;
	# while (responseTimeout<1):
		# Delay_and_check_Keypress(10) # wait for 1 sec
		# waitTimeout+=1
		# if waitTimeout==20:
			# print("\nwaiting for response\n")
			# waitTimeout=0
		# try:
			# text= ser.readline()
		# except:
			# print("COM PORT Error")	
		
		# try:
			# string =text.decode('ascii')
		# except:
			 # print("")
			 
			 
		# if (string!=""):
			# print("\n Response Received\n")
			# ResponseRecived=1 
			# retry=50
			# break;
		# responseTimeout+=1
		
	# retry+=1
	# if ResponseRecived:
		# break;
	# print("\nresend start command\n")
	
# if ResponseRecived==0:
	# print("Device Not detected Please Retry...")
	# time.sleep(5)
	# sys.exit()
# responseTimeout=0
# while (filecount<totalParts):
	# try:
		# text=ser.readline()
	# except:
		  # show_COM_Error()
	
	# try:
		# string =text.decode('ascii')
	# except:
		# print("currupted string received ")
	
	# if string != "":
		# partno=int(string)
		# filecount=partno;
		# print("partNo=%d"%(partno))
		# filename=TARGET+'part_'+str(filecount)+'.zip';
		# txtfile=open(filename,"rb")
		# text=txtfile.read(1500)
		# commandarduino(text)
		# txtfile.close()	
		# #print(filename) 
		# #print("Press any Key to Stop")
	# else :
			# responseTimeout+=1
			# if responseTimeout==10 :
				# print ('\nwaiting for next part request\n')
				# responseTimeout=0
	# Delay_and_check_Keypress(10)	
			
	# if(filecount>=totalParts):
		# break
	
# time.sleep(1)		
# retry=0
# while ( retry<5) :
	# try:
		# text=ser.readline()
	# except:
		  # show_COM_Error()
	
	# try:
		# string =text.decode('ascii')
	# except:
		# print("currupted string received ")
	
	# if string != "":
		# #print("Device Response=%s" %string)
		# response=string[:7]
	# if response == "DWNLDOK":
		# print("\nFirmware Download OK\nPlease wait while firmware is being updated....")
		# time.sleep(45)		
		# print("\nFirmware Updated....\n")
		# break;
	# time.sleep(1)
	# retry+=1;   
# if(retry>=5):
	# print("\n******Eror In firmware download***** \n")
# #print ("Ending Program\n")
# while(True):
	# time.sleep(1)
# sys.exit()


