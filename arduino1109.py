import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

contador = 0

while (contador < 300):
	value = ser.read()
	print(value)
#	print(contador)
	contador = contador + 1
arquivo.close()
