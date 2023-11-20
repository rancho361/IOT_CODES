
import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time 

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering

ControlPin=[24,25,26,27]

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)

seq=[[1,0,0,0],
     [1,1,0,0],
     [0,1,0,0],
     [0,1,1,0],
     [0,0,1,0],
     [0,0,1,1],
     [0,0,0,1],
     [1,0,0,1]]

anti_seq=[[1,0,0,1],
         [0,0,0,1],
         [0,0,1,1],
         [0,0,1,0],
         [0,1,1,0],
         [0,1,0,0],
         [1,1,0,0],
         [1,0,0,0]]

#clear GPIOs
def destroy():
    for pin in ControlPin:
        GPIO.output(pin,False)
    GPIO.cleanup()

def Clockwise():
    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin],seq[halfstep][pin])
            time.sleep(0.005)

def AntiClockwise():
    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin],anti_seq[halfstep][pin])
            time.sleep(0.005)

    
if __name__ == '__main__':     # Program start from here
    try:
        while True:                    # Loop will run forever
            Clockwise()
            time.sleep(0.5)
            AntiClockwise()
            time.sleep(0.5)
            
            
                    
    # If keyboard Interrupt (CTRL-C) is pressed
    except KeyboardInterrupt:
        
        destroy()

    
    
