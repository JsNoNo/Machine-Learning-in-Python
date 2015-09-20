import matplotlib
import matplotlib.pyplot as plt
from numpy import array


def plotFigure(data, label):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	label = [i+1 for i in label]
	ax.scatter(array(data)[:,0],array(data)[:,1],15.0*array(label),15.0*array(label))
	plt.show()




