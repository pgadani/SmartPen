import serial

port = '/dev/ttyACM0'
baud = 112500

if __name__ == '__main__':
	s = serial.Serial(port=port, baudrate=baud)
	s.write('h')
	while(True):
		if s.readable():
			print(s.readline())