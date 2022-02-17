#%%
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
print(2+2)
#%%
fig=plt.figure()
#plt.axes(projection='3d')



ax=plt.axes(xlim=(0,3), ylim=(-1,1))
myline, = ax.plot([], []) # <----plot returns a list 
#reasonable convention because plot allows many ways for its parameters. E.g. plot(x1, y1, 'g^', x2, y2, 'g-') will return a list with two Line2D elements. For consistency, also when there is only one Line2D element a list will be returned. – 
#%%



def init(): # Initialize with a blank plot
	myline.set_data([], []) # line is a global variable
	return [myline]

def my_animate(i):
	x=np.linspace(0,2,100)
	y=np.sin(x-0.01*i)
	myline.set_data(x, y)
	return [myline]  #<--- we need to return a list containing  

myanim = animation.FuncAnimation(fig, my_animate, init_func=init, frames=200, interval=200, blit=True)

#myanim = animation.FuncAnimation(fig, my_animate, init_func=init, frames=200, interval=20, blit=True)
myanim.save('a200.gif')
plt.show()
# %%
