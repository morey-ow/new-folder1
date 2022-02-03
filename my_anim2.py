from matplotlib import animation
from matplotlib.pyplot import savefig
from numpy import linspace
from numerical_int import *
from my_anim import *

t=np.linspace(0,10,101)
x=np.vectorize(lambda t: t**2)
y=np.vectorize(lambda t: 2*np.cos(t)**2)
z=np.vectorize(lambda t: np.sin(t))

fig=plt.figure(figsize=(15,15))
ax=fig.add_subplot(projection='3d')
ax.plot(x(t), y(t), z(t))

fig.savefig('any.png')

def draw_frame2(i):
	ax.scatter(x(i), y(i), z(i), color='red')

anim=FuncAnimation(fig, draw_frame2, t)
anim.save('myfig2.gif', dpi=150,
writer=PillowWriter(fps=24))