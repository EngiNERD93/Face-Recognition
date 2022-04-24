#This code is for Serial Communication
#pip install pyserial
#pip install windows-curses

import serial

port = "COM5"

ser = serial.Serial(port, 115200, timeout = 0)

while True:
    data = ser.write(str.encode('AUTH'))
    print("serial comm active")

