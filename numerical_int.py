import matplotlib.pyplot as plt
import numpy as np


logging.basicConfig(filename='test.log', level=logging.DEBUG)

def integrate(f, interval, init_condition=0):
	''' Numerically integrate the function f
	along the interval [a,b], where it is 
	defined'''
	l=len(interval)  #figure out how many points are in the interval
	F=np.zeros(l) #F will be our solution, initialize to zero
	F[0]=init_condition
	for i in range(1,l):
		F[i]=F[i-1]+ f[i-1]*(interval[i]-interval[i-1])
	
	return F


def function_values(f, interval):
	''' given a function f like f(x)=x^3
	we return the list of f evaluated at points
	of the interval'''
	return [f(i) for i in interval]

def plot_soln(interval, F, style, axis):  #n is the number of iterations
	n=len(interval)
	axis.plot(interval, F, style, label=f'numerical approx {n} points')

if __name__=='__main__':
	
	fig1=plt.figure('Figure 1')
	ax=fig1.add_axes([-1,-1,2,2])

	for n,c in [(5,'r'), (30,'g'), (60,'c') ]:
		interval=np.linspace(0,5,n)
		f=[i for i in interval]
		plot_soln(interval, integrate(f, interval, 0), f'{c}'+'--', ax)
	
	#ax2.plot(interval, F, 'r--', label=f'numerical approx {n} points')
	
	ax.plot(interval, function_values(lambda x: x**2/2, interval), linewidth=5, label='Exact solution')
	fig1.legend(loc='lower right')
	plt.grid()
	fig1.show()
	