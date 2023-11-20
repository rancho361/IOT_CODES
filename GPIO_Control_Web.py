#	Raspberry Pi GPIO Status and Control

import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define sensors GPIOs
button = 26
senPIR = 27

#define actuators GPIOs
ledRed = 19
ledGrn = 20
ledBlu = 21


#initialize GPIO status variables
buttonSts = 0
senPIRSts = 0
ledRedSts = 0
ledGrnSts = 0
ledBluSts = 0

actuator = 0

# Define button and PIR sensor pins as an input
GPIO.setup(button, GPIO.IN)   
GPIO.setup(senPIR, GPIO.IN)

# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGrn, GPIO.OUT) 
GPIO.setup(ledBlu, GPIO.OUT) 


# turn leds OFF 
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledGrn, GPIO.LOW)
GPIO.output(ledBlu, GPIO.LOW)

	
@app.route("/")
def index():
	# Read GPIO Status
	buttonSts = GPIO.input(button)
	senPIRSts = GPIO.input(senPIR)
	ledRedSts = GPIO.input(ledRed)
	ledGrnSts = GPIO.input(ledGrn)
	ledBluSts = GPIO.input(ledBlu)

	templateData = {
      'button'  : buttonSts,
      'senPIR'  : senPIRSts,
      'ledRed'  : ledRedSts,
      'ledGrn'  : ledGrnSts,
      'ledBlu'  : ledBluSts,
      }
	return render_template('GPIO_Control_Web.html', **templateData)
	
# The function below is executed when someone requests a URL with the actuator name and action in it:
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'ledRed':
		actuator = ledRed
	if deviceName == 'ledGrn':
		actuator = ledGrn
	if deviceName == 'ledBlu':
		actuator = ledBlu
   
	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		     
	buttonSts = GPIO.input(button)
	senPIRSts = GPIO.input(senPIR)
	ledRedSts = GPIO.input(ledRed)
	ledGrnSts = GPIO.input(ledGrn)
	ledBluSts = GPIO.input(ledBlu)
   
	templateData = {
	  'button'  : buttonSts,
      'senPIR'  : senPIRSts,
      'ledRed'  : ledRedSts,
      'ledGrn'  : ledGrnSts,
      'ledBlu'  : ledBluSts,
	}
	return render_template('GPIO_Control_Web.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)