import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

fig, ax = plt.subplots()

def init_func():
	ax.clear()	

def draw_frame(i):
	ax.clear()
	ax.set_xlim([0,10])
	ax.set_ylim([-2,2])
	ax.scatter(i,np.sin(i), s=i)
	t=np.linspace(0,10*i, 100)
	ax.plot(t,np.sin(t))

anim=FuncAnimation(fig,draw_frame,np.arange(11), init_func=init_func)

anim.save('myfig.gif', dpi=150,
writer=PillowWriter(fps=24))
