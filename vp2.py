import vpython as vp
import numpy as np

xpos=0
ypos=1
zpos=0
ball=vp.sphere(make_trail=True, pos=vp.vector(xpos,ypos,zpos), color=vp.color.red, radius=0.5)
ground=vp.box(length=200, height=1, width=100, color=vp.color.green, opacity=0.5)
vp.arrow(axis=vp.vector(1,0,0), label='X')

dt=0.01
vx=5
vy=10
ay=-9.8
t=0
while ypos>0:
	vp.rate(10)
	t=t+dt
	xpos=xpos+vx*t
	ypos=ypos + vy*t+ ay*(t**2)
	ball.pos=vp.vector(xpos, ypos, zpos)
	print(f'{xpos, ypos, zpos}')

while True:
	pass
	