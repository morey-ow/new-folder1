import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2) # an empty line def 

def init(): # Initialize with a blank plot
	line.set_data([], []) # line is a global variable
	return line,
def animate(i): # Plot a moving sine wave
	x = np.linspace(0, 2, 1000)
	y = np.sin(2 * np.pi * (x - 0.01 * i)) 
	line.set_data(x, y)
	return line,
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
anim.save('a.gif')
plt.show()