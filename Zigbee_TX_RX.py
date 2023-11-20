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
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1             
 )
counter=0       

if __name__ == "__main__":
    try:
        while True:
            ser.write(str.encode('Write counter: %d \n'%(counter)))
            time.sleep(1)
            counter += 1
            x=ser.readline().strip()
            if len(x) != 0 :
                print(x)
    except KeyboardInterrupt:
        ser.close()
        print ('Exiting Program')
            