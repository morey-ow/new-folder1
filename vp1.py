#%%
from time import sleep
from matplotlib.pyplot import arrow
import vpython as vp

ball=vp.sphere(color=vp.color.red)
#sleep(5)
ball.color=vp.color.green

#myBox=vp.box(color=vp.color.yellow)
myTube=vp.cylinder(pos=vp.vector(0,-5,0), color=vp.color.red, width=3, height=3,length=5)
myTube2=vp.cylinder(pos=vp.vector(0,5,0), axis=vp.vector(1,1,1), color=vp.color.white, width=3, height=3,length=5)
vp.arrow(lenth=10)
xpos=0
deltax=0.1
while True:
	vp.rate(10)
	xpos+=deltax
	ball.pos=vp.vector(xpos,0,0)

