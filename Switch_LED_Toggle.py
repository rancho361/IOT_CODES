#Toggle the LED whenever switch is pressed
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(20, GPIO.FALLING)
GPIO.setup(19, GPIO.OUT)  

flag = 0

if __name__ =='__main__':
    try:
        while True:
            if GPIO.event_detected(20):
                flag = not flag             
                GPIO.output(19, flag)
                print('Button Pressed...')
                time.sleep(1)
            
    except KeyboardInterrupt:
        GPIO.cleanup()

