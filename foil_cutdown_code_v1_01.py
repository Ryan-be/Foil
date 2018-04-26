###################################################################
#							          #
#        GPS controuled cutdown program to be used with           #
#          the respberry pi and pi in the sky module  		  #
#							          #
#   For a full list of instructions of how to use this program 	  #	
# please refer to the readme.txt file included in this repository #
#								  #
#       Ryan Bradley-Evans @University of Leicester 2017          #
#						  		  #		
###################################################################

#initioal set up and imports.
import os
import subprocess
import time 
import sys
import RPi.GPIO as GPIO
from decimal import *
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#User defined values:
t_min = 60 
t_max = 120 #Max time before cutdown in minuets 

#define global varables
count = 0
t_max = t_max - t_min
t_min = t_min*60

###################################################################
#								  #	
#                       Define functions:			  #	
#								  #
###################################################################

def cutdown():
	#set up GPIO using BCM numbering
	#GPIO.setmode(GPIO.BOARD)
	#set up GPIO using Board numbering
	print("snip snip snip")
	GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)
	GPIO.output(38, 1)
	time.sleep(60) #time the cutdown is active
	GPIO.output(38, 0)
	GPIO.output(40,0)
	time.sleep(60)
	sys.exit()
def error_check():

    GPIO.setwarnings(False)
    GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
    #check program is running.
        
    gpslog = open("pits/tracker/telemetry.txt", "r")
    lineList = gpslog.readlines()   
    gpslog.close()
    lastlinegps =  lineList[len(lineList)-1]
      #latitude
    d = lastlinegps[11:18]
    d = Decimal(d)#longitude
    if (d > 10):
         lastlinegps[11:19]
         lastlinegps[21:28]
    else:
         lastlinegps[11:18]
         lastlinegps[19:26]
    d = Decimal(d)
    e = Decimal(e)
    
    if (d == 0.00):
        
        while (d == 0.00):
            gpslog = open("pits/tracker/telemetry.txt", "r")
            lineList = gpslog.readlines()   
            gpslog.close()
            lastlinegps =  lineList[len(lineList)-1]
            d = lastlinegps[11:18]
            d = Decimal(d)
            GPIO.output(36, 1)
            time.sleep(0.5)
            GPIO.output(36, 0)
            time.sleep(0.5)
            
    else:
        GPIO.output(36, 1)
        time.sleep(15)
        GPIO.output(36, 0)
def gonogo():
    
    GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
    count = 0
    while (count < t_max):
    	 #subprocess.call("cd", shell = True)
    	 #subprocess.call("cd pits/tracker", shell = True)    	
        gpslog = open("pits/tracker/telemetry.txt", "r")
        lineList = gpslog.readlines()   
        gpslog.close()
        lastlinegps =  lineList[len(lineList)-1]
        x = lastlinegps[11:18]  #latitude
        y = lastlinegps[19:26]  #longitude
        x = Decimal(x)
        y = Decimal(y)
        #the following 8 lines are only needed if the dp stays the same and not sf
        if (x > 10):
            x = lastlinegps[11:19]
            y = lastlinegps[20:28]
        else:
            x = lastlinegps[11:18]   
            y = lastlinegps[20:28]
        
        x = Decimal(x)
        y = Decimal(y)
        print(x)
        print(y)
        #y = 53.0000
        #x = -3.0000
        
        if (x > 54.040038):
            print("Lancaster grid")
            GPIO.output(40, 1)
            cutdown()
    
        elif (y >-1.5298462 and x>53.807139):
            print("Leeds grid") 
            GPIO.output(40, 1)
            cutdown()
    
        elif (y>-1.1288454 and x>53.527248):
            print("Doncaster grid") 
            GPIO.output(40, 1)
            cutdown()
    
        elif (y > -0.0225219701 and x > 52.589701):
            print("Petabrough Grid")
            GPIO.output(40, 1)
            cutdown()    
        
        elif (y > 0.10437012):
            print("Cambridge Line") 
            GPIO.output(40, 1)
            cutdown()
    
        elif (y>-0.42160034 and x<51.862924):
            if (x == 0.00000 and y == 0.00000):
                time.sleep(15)
                gonogo()
            else:
                print("Luton grid")
                GPIO.output(40, 1)
                cutdown()         

        elif (x<52.589701):
            if (x == 0.00000 and y == 0.00000):
                time.sleep(15)
                gonogo()
            else:
                print("South line")
                GPIO.output(40, 1)
                cutdown()
                
        else:    
            count = count + 1
            print("recycle")
            time.sleep(60)

    cutdown()
###########################################################  
#							  #
#			Main Program:			  #
#							  #
###########################################################
#count = 0
time.sleep(30)
#time.sleep(t_min)
error_check()
#time.sleep(t_min)
gonogo()
