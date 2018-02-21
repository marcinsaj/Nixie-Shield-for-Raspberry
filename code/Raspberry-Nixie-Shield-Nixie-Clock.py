'''
Raspberry Nixie Shield - Nixie Clock 
This example shows how to display time on the nixie tube using Nixie Shield with the Raspberry Pi
Nixie Shield uses five digital outputs to drive nixie tube 
Pin 29 as on/off (EN) line, 31, 33, 35, 37 as an address (A, B, C, D) of nixie tube digit/cathode
This example code is in the public domain
https://www.nixietester.com
'''
import time                   # Import time module
import RPi.GPIO as GPIO       # Import RPi.GPIO module as just GPIO

GPIO.setmode(GPIO.BOARD)      # Declare the type of GPIO numbering system
GPIO.setwarnings(False)       # Disable warnings

# Pin definitions / Nixie tube digit address:
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


while True:
    # Get current local time
    nixietime = time.strftime("%H%M")   
        
    # Display each digit in local time string
    for d in range(4):
        # Lookup each digit in time string and output corresponding pattern
        GPIO.output(address, digit[int(nixietime[d])])
        GPIO.output(EN,GPIO.LOW)  # Turn on the Nixie tube
        time.sleep(0.500)
        GPIO.output(EN,GPIO.HIGH) # Turn on the Nixie tube
        
        if d == 1:                
            time.sleep(1)         # After second digit wait longer  
        else:
            time.sleep(0.500)        
        
    time.sleep(1.500)             # Wait and repeate
        
GPIO.cleanup()
