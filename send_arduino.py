import serial
import time

ser = serial.Serial('/dev/cu.usbmodemFA131', 9600)
time.sleep(3)

ser.write('1'.encode())

time.sleep(3)
ser.write('0'.encode())

time.sleep(1)
ser.close()
