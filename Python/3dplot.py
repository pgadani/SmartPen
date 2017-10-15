from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def getRotMatrix(q):
	n = np.linalg.norm(q)
	q = [r/n for r in q]
	return np.array([
		[1 - 2*q[2]**2 - 2*q[3]**2, 2*q[1]*q[2] - 2*q[3]*q[0], 2*q[1]*q[3] + 2*q[2]*q[0]], 
		[2*q[1]*q[2] + 2*q[3]*q[0], 1 - 2*q[1]**2 - 2*q[3]**2, 2*q[2]*q[3] - 2*q[1]*q[0]], 
		[2*q[1]*q[3] - 2*q[2]*q[0], 2*q[2]*q[3] + 2*q[1]*q[0], 1 - 2*q[1]**2 - 2*q[2]**2]])

def showPen(ax, p):
	print(p)
	ax.plot([0, p[0]], [0, p[1]], [0, p[2]])
	ax.set_xlim(-1.2, 1.2)
	ax.set_ylim(-1.2, 1.2)
	ax.set_zlim(-1.2, 1.2)

if __name__ == '__main__':
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	q = np.array([1, 1, 1, 1])
	rot = getRotMatrix(q)
	p = np.array([0, 1, 0])
	showPen(ax, np.dot(rot, p))
	plt.show()