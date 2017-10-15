import serial
import numpy as np

port = '/dev/ttyACM0'
baud = 112500

if __name__ == '__main__':
	s = serial.Serial(port=port, baudrate=baud)
	while(True):
		if s.readable():
			# msg = [ord(c) for c in s.read(12)]
			# a = [(128-msg[0]) * 256 + msg[1], (128-msg[2]) * 256 + msg[3], (128-msg[4]) * 256 + msg[5]]
			# print('ax: ', a[0], 'ay', a[1], 'az', a[2])
			msg = s.readline() # read 6 values, 2 bytes each
			s.flush()
			if len(msg) < 28: 
				# print(len(msg))
				continue
			# print('BYTES ',', '.join([str(c) for c in msg]))
			gyro = []
			accel = []
			for a in range(0, 16, 4):
				gyro.append(int.from_bytes(msg[a:a+2], byteorder='big', signed=True) / 16384.0)
			for a in range(16, 28, 4):
				accel.append(int.from_bytes(msg[a:a+2], byteorder='big', signed=True))
			# print("Gyro: ", gyro)
			print("Accel: ", int(np.linalg.norm(np.array(accel))))