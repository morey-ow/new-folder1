#In this file, we implememnt forward euler for vector valued function u, with du/dt = f(u,t)`
#so f is vector valued to

#%%
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym  #symbolic python
from scipy.integrate import solve_ivp


#see https://stackoverflow.com/questions/37970424/what-is-the-difference-between-drawing-plots-using-plot-axes-or-figure-in-matpl/56629063
# https://www.skytowner.com/explore/getting_started_with_matplotlib
# to understand object oriented matplotlib
# I used some ideas from Greg Winther's implementation of
# forward_euler at https://youtu.be/CIERyk_36lk


def forward_euler(f, interval, init_condition): #here f(u,t):R^d X R \to R^d  is a vector valued function
	''' Numerically integrate the function f
	along the interval [a,b], where it is 
	defined'''
	#f=lambda u,t: np.asarray(f(u,t))
	l=len(interval)  #figure out how many points are in the time interval
	d=len(init_condition) #the number of equations
	F=np.zeros((d,l)) #F will be our solution, initialize to zero
	F[:,0]=np.asarray([init_condition])
	for i in range(1,l):
		F[:,i]=F[:,i-1]+ f(F[:,i-1], interval[i-1])*(interval[i]-interval[i-1])
	
	return F



#def plot_soln(interval, F, style, axis):  #n is the number of iterations
#	n=len(interval)
#	d, n = F.shape
#	for i in range(d):
#		axis.plot(interval, F[i,:], style, label=f'numerical approx {n} points')

if __name__=='__main__':
	a,b=(0,50)

	# we solve equation the second order diff eq y'' + y = 0, so let u=(y, y') and 
	# so du/dt=(y',y'')=(y', -y) since y''=-y for our particular equation.

	def f(u, t):
		return np.asarray([u[1], -u[0]])


	fig1=plt.figure('Figure 1', figsize=(8,10))
	ax=plt.axes()
	
	for n,c in [(6000,'r'), (1000, 'g') ]:
		interval=np.linspace(a,b,n)
		F=forward_euler(f, interval, [0,1])
		#plot_soln(interval, F , f'{c}'+'--', ax)
		ax.plot(interval, F[0,:], f'{c}'+'--', label=f'numerical approx {n} points')

	# We know y''+y=0 has y=sin(t) as a solution

	def F0(t):
		return np.sin(t)  #our solution to the diff eq u'' + u = 0 is u=sin(t)

	interval=np.arange(a,b,0.1)
	ax.plot(interval, [F0(i) for i in interval], linewidth=2, label='Exact solution')
	ax.set_xlim(a,b)
	ax.set_title('Numerical integration via forward Euler')
	plt.legend(loc='lower right')
	plt.grid()

	plt.xlabel('t')
	plt.ylabel('F(t)')
	
	#%%

	#comparison with scipy's initial value problems solver solve_ivp
	def f_switch(t,u):  #switch the u,t order to conform to solve_ivp
		return f(u,t)
	sol=solve_ivp(f_switch, [a,b], [0,1])
	ax.plot(sol.t, sol.y[0], 'r', linewidth=2, label='scipy solve_ivp solution')
	plt.show()
	
	fig1.savefig('graph.png')
	
# %%
