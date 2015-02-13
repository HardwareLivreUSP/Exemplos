import serial 
import sys

ser = serial.Serial(sys.argv[1], 9600)
ser.write(sys.argv[2])
