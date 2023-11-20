# Install Python Serial Package
# sudo pip3 install pyserial
# Check the COM PORT Number
# sudo dmesg|grep tty
# Use ttyS0 for on-board Serial
# Use ttyUSB0  or ttyUSB1 for USB to serial converter
# after checking the com port number




import time
import serial

ser = serial.Serial(
    port='/dev/ttyUSB2',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1             
 )
counter=0       

print ("Entering into AT Command Mode")
ser.write(b'+++')
x=ser.readline().strip()
print("+++",x)
ser.write(b'AT\r')
x=ser.readline().strip()
print("Attention:",x)
ser.write(b'ATID\r')
x=ser.readline().strip()
print("PANID:",x)
ser.write(b'ATSH\r')
x=ser.readline().strip()
print("Source MAC ID - Higher:",x)
ser.write(b'ATSL\r')
x=ser.readline().strip()
print("Source MAC ID - Lower:",x)
ser.write(b'ATDH\r')
x=ser.readline().strip()
print("Destination MAC ID - Lower:",x)
ser.write(b'ATDL\r')
x=ser.readline().strip()
print("Destination MAC ID - Lower:",x)
ser.write(b'ATWR\r')
x=ser.readline().strip()
print("Writen to configuration:",x)
command = input ("Are you want to modify (y/n): ")
if (command == 'y' or command == 'Y'):
    while True:
        command = input ("Enter the Command: ")
        if (command == "EXIT" or command == "exit"):
            break
        else:
            ser.write(b'+++')
            x=ser.readline().strip()
            print("Attention Response:",x)
            ser.write(str.encode(command + '\r'))
            x=ser.readline().strip()
            print("Command Response:",x)

ser.write(b'+++')
x=ser.readline().strip()
ser.write(b'ATWR\r')
x=ser.readline().strip()
print("Writen to configuration:",x)
print ("Configuration Saved")
print ("Exiting the Program")


