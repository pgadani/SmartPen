import serial

port = '/dev/ttyACM0'
baud = 112500

if __name__ == '__main__':
	s = serial.Serial(port=port, baudrate=baud)
	while(True):
		if s.readable():
			# msg = [ord(c) for c in s.read(12)]
			# a = [(128-msg[0]) * 256 + msg[1], (128-msg[2]) * 256 + msg[3], (128-msg[4]) * 256 + msg[5]]
			# print('ax: ', a[0], 'ay', a[1], 'az', a[2])
			msg = s.read(12) # read 6 values, 2 bytes each
			gyro = []
			accel = []
			for a in range(0, 6, 2):
				gyro.append(int.from_bytes(msg[a:a+2], byteorder='big'))
				accel.append(int.from_bytes(msg[a+6:a+8], byteorder='big'))
			print("Gyro: ", gyro)
			print("Accel: ", accel)