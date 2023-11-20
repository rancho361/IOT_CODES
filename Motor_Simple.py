
import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time 
EN1 = 25           # Initializing the GPIO pin 25 for the enable 1 
IN1 = 26           # Initializing the GPIO pin 26 for input 1 of the motor driver
IN2 = 27           # Initializing the GPIO pin 27 for input 2 of the motor driver   

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering

GPIO.setup(EN1,GPIO.OUT)        ## Declaring as EN1 output pin
GPIO.setup(IN1,GPIO.OUT)        ## Declaring as IN1 output pin
GPIO.setup(IN2, GPIO.OUT)       ## Declaring as IN2 output pin

    
#clear GPIOs
def destroy():
    GPIO.output(25, False)
    GPIO.output(26, False)
    GPIO.output(27, False)
    GPIO.cleanup()

def Clockwise():
    GPIO.output(25, True)
    GPIO.output(26, True)
    GPIO.output(27, False)

def AntiClockwise():
    GPIO.output(25, True)
    GPIO.output(26, False)
    GPIO.output(27, True)

def Stop():
    GPIO.output(25, False)
    GPIO.output(26, False)
    GPIO.output(27, False)
    
if __name__ == '__main__':     # Program start from here
    try:
        while True:                    # Loop will run forever
            Clockwise()
            time.sleep(2)
            Stop()
            time.sleep(1)
            AntiClockwise()
            time.sleep(2)
            Stop()
            time.sleep(1)
            
                    
    # If keyboard Interrupt (CTRL-C) is pressed
    except KeyboardInterrupt:
        
        destroy()

    
    