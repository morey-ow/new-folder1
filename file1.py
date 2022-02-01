import matplotlib.pyplot as plt
import numpy as np

def integrate(f, interval, init_condition=0):
	''' Numerically integrate the function f
	along the interval [a,b], where it is 
	defined'''
	l=len(interval)
	F=np.zeros(l)
	F[0]=init_condition
	for i in range(1,l):
		F[i]=F[i-1]+ f[i-1]*(interval[i]-interval[i-1])
	return F

def graph(x, y):
	fig, ax = plt.subplots()
	ax.plot(x,y)
	fig.show()

def function_chopped(f, interval):
	''' given a function f like f(x)=x^3
	we return the list f(interval)'''
	return [f(i) for i in interval]

if __name__=='__main__':
	interval=range(0,5,1)
	f=[1, 2, 3, 4, 5, 6]
	F=integrate(f, interval, 0)
	fig, ax = plt.subplots()
	ax.plot(interval,F, 'r' )
	fig.show()
	interval=np.linspace(0,5,600)
	f=[i+1 for i in interval]
	F=integrate(f, interval )
	ax.plot(interval, F)
	ax.plot(interval, function_to_interval(lambda x: x**2/2, interval))
