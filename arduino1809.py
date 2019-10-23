import serial

serial = serial.Serial("/dev/ttyACM0",9600)
while 1:
	out1 = input("Saída 1: \n")
	out2 = input("Saída 2: \n")
	serial.write(out1)
	serial.write(out2)
