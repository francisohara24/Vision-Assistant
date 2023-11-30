# Code I wrote to test serial communication on the Raspberry Pi
import serial

# connect to serial port ttyAMA0
ser = serial.Serial("/dev/ttyAMA0")

# read first 100 characters sent over port
data = ser.read(100)
print(data)

# close the serial connection
ser.close()