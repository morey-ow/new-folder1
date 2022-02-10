import matplotlib.pyplot as plt
import numpy as np
import sympy as sym  #symbolic python

#see https://stackoverflow.com/questions/37970424/what-is-the-difference-between-drawing-plots-using-plot-axes-or-figure-in-matpl/56629063
# https://www.skytowner.com/explore/getting_started_with_matplotlib
# to understand object oriented matplotlib

def integrate(fv, interval, init_condition=0):
	''' Numerically integrate the function f
	along the interval [a,b], where it is 
	defined'''
	l=len(interval)  #figure out how many points are in the interval
	F=np.zeros(l) #F will be our solution, initialize to zero
	F[0]=init_condition
	for i in range(1,l):
		F[i]=F[i-1]+ fv[i-1]*(interval[i]-interval[i-1])
	
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
	a,b=(-5,5)

	def f(x):
		return np.sin(x)  #f(x)=sin x
	
	fig1=plt.figure('Figure 1', figsize=(8,10))
	ax=fig1.add_subplot()
	
	for n,c in [(6,'c'), (30,'g'), (60,'r') ]:
		interval=np.linspace(a,b,n)
		fv=function_values(f, interval)   #f(x)=sin x
		plot_soln(interval, integrate(fv, interval, 0), f'{c}'+'--', ax)
	
	#ax2.plot(interval, F, 'r--', label=f'numerical approx {n} points')
	X=sym.symbols('X')
	def F(x):
		symbolicF=sym.integrate(sym.sin(X), X) #symbolic integral of f(X) is F(X)
		return symbolicF.subs(X,x) - symbolicF.subs('X', a) # return F(x) - a number - instead of F(X)
	
	interval=np.arange(a,b,0.1)
	ax.plot(interval, function_values(F, interval), linewidth=5, label='Exact solution')
	ax.set_xlim(a,b)
	ax.set_title('Numerical integration via forward Euler')
	plt.legend(loc='lower right')
	plt.grid()

	plt.xlabel('t')
	plt.ylabel('F(t)')
	plt.show()
	fig1.savefig('graph.png')
	