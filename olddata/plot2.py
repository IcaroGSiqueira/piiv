import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial

ser = serial.Serial('/dev/ttyACM0/',9600)

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [])
data = 1

def init():
	ax.set_xlim(0, 25)
	ax.set_ylim(0,1)
	return ln,

def update(frame):
	xdata.append(frame)
	data = np.sin(data)
	ydata.append(data)
	ln.set_data(xdata, ydata)
	return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 128),init_func=init, blit=True)
plt.show()
