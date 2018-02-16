'''
Raspberry Nixie Shield Basic Example 2 
This example shows how to control a nixie tube with a Raspberry Pi using Nixie Shield
An example of using a state array and for loop
Nixie Shield uses five digital outputs to drive nixie tube 
Pin 29 as on/off (EN) line, 31, 33, 35, 37 as an address (A, B, C, D) of nixie tube digit/cathode
This example code is in the public domain
https://www.nixietester.com
'''
import time                   # Import time module
import RPi.GPIO as GPIO       # Import RPi.GPIO module as just GPIO

GPIO.setmode(GPIO.BOARD)      # Declare the type of GPIO numbering system
GPIO.setwarnings(False)       # Disable warnings

# Pin Definitons / Nixie tube digit address:
EN = 29                       # On/Off Nixie tube
A = 37      
B = 33
C = 31
D = 35

# Pin assignments: 35, 31, 33, 37
address = [D, C, B, A]

# Pattern table for 10 digits
digit = [(0, 0, 0, 0), # '0'
         (0, 0, 0, 1), # '1'
         (0, 0, 1, 0), # '2'
         (0, 0, 1, 1), # '3'
         (0, 1, 0, 0), # '4'
         (0, 1, 0, 1), # '5'
         (0, 1, 1, 0), # '6'
         (0, 1, 1, 1), # '7'
         (1, 0, 0, 0), # '8'
         (1, 0, 0, 1)] # '9'

#Setup pins as an outputs, initially low
GPIO.setup(EN,GPIO.OUT, initial=0) 
GPIO.setup(address, GPIO.OUT, initial=0)

GPIO.output(EN,GPIO.LOW)      # Turn on the Nixie Tube
 
for d in range(10):
    GPIO.output(address, digit[d])
    time.sleep(1)
    
GPIO.output(EN,GPIO.HIGH)     # Turn off the Nixie Tube
GPIO.cleanup()
