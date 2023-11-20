# Install the MQTT Publisher
# sudo pip3 install paho-mqtt


# open the MQTT browser client in web browser
# https://mqtthq.com/client

#The broker and port are provided by https://mqtthq.com/

MQTTServer = 'public.mqtthq.com'

TCPPort = 1883

WebSocketPort = 8083

import os
import sys
import time
import board
import adafruit_dht
import paho.mqtt.client as mqtt
import json

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D19, use_pulseio=False)

sensor_data = {'temperature': 0, 'humidity': 0}



client = mqtt.Client()

client.connect(MQTTServer, TCPPort, WebSocketPort)

client.loop_start()

if __name__ == '__main__':
    while True:
        try:        
            # Print the values to the serial port
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity
            print("Temp: {:.1f} C    Humidity: {}% ".format( temperature, humidity))
            time.sleep(2.0)
            sensor_data['temperature'] = temperature
            sensor_data['humidity'] = humidity

            # Sending humidity and temperature data to HIVEMQ
            client.publish('RPI4_MQTT', json.dumps(sensor_data), 1)
            
            time.sleep(5)
        
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue

        except KeyboardInterrupt:
            client.loop_stop()
            client.disconnect()
            print ('Exiting Program')
            exit()
        

