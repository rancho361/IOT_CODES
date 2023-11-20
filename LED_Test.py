import RPi.GPIO as GPIO
import time

LED = 5

GPIO.setmode (GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.HIGH)

def blink():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(1)

def destroy():
    GPIO.output(LED, GPIO.LOW)
    GPIO.cleanup()
    
if __name__ == '__main__':
    try:
        while True:
            blink()
    except KeyboardInterrupt:
        destroy()
        