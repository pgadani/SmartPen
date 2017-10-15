import numpy as np

H = np.array([0, 0, 1])
R = 0
Q = .01

def getA(t):
	return np.array([[1, t, 0], [0, 1, t], [0, 0, 1]])

def getQ(t):
	return np.array([[1/20 * t**5, 1/8 * t**4, 1/6 * t**3], [1/8 * t**4, 1/3 * d**3, 1/2 * t**2], [1/6 * t**3, 1/2 * t**2, t]])

def timeUpdate(x, p, t=0):
	A = getA(t)
	xn = np.dot(A, x)
	pn = np.dot(np.dot(A, p), np.transpose(A)) + getQ(t)
	return xn, pn

def measUpdate(x, p, z):
	y = z - np.dot(H, x)
	s = R + np.dot(np.dot(H, p), np.transpose(H))
	K = np.dot(np.dot(p, np.transpose(H)), s**-1)
	xn = x + np.dot(K, y)
	pn = np.dot(np.eye(3) - np.dot(K, H), p)
	return xn, pn