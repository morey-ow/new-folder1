import vpython as vp
import numpy as np

xpos=0
ypos=3
zpos=0
ball=vp.sphere(make_trail=True, pos=vp.vector(xpos,ypos,zpos), color=vp.color.red, radius=0.5)
ground=vp.box(length=1200, height=2, width=100, color=vp.color.green, opacity=0.5)
vp.arrow(axis=vp.vector(1,0,0), label='X')

dt=0.01
vx=7
vy=24
ay=-9.8
t=0
while ypos>0:
	vp.rate(10)
	t=t+dt
	xpos=xpos+vx*t
	ypos=ypos + vy*t+ ay*(t**2)
	ball.pos=vp.vector(xpos, ypos, zpos)
	print(f'{xpos, ypos, zpos, t}')

while True:
	pass
	