import vpython as vp
from scipy.integrate import solve_ivp
from astropy.time import Time
from astroquery.jplhorizons import Horizons


#from Rhett Allain https://www.youtube.com/watch?v=froU7lSU7IU
# and 

vp.scene.width=600
vp.scene.height=600

G=6.67e-11 #Gravitational constant
Re=6.378e6 #radius of earth in meters
Me=5.972e24  #mass of earth kg
Mm=7.348e22 
Rm=1.7371e6 # radius of moon in meter
Rem=384.4e6 # distance to moon in meters


moon=vp.sphere(make_trail=True, pos=vp.vector(10*Re,0,0), radius=Rm, color=vp.color.white)
earth=vp.sphere(pos=vp.vector(0,0,0), radius=Re)

moon.x=5

while True:
	vp.rate(10)
	moon.pos=vp.vector(2, 2, 2)
