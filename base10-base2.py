from math import log, floor

while True:
	x=input('Enter decimal to convert binary')
	x=float(x)
#x = 10  #base 10, want to express in base 2
	if x==0:
		print(0)
		break
	elif x<0: #if x is negative, print negative sign and make it positive
		print('-', end='')
		x=-x

	n=floor(log(x)/log(2))
	x=x/2**(n)-1
	print('1.', end='')
	for _ in range(50):
		if x==0:
			break
		elif x< 0.5:
			x=2*x
			print(0, end='')
		else:
			x=2*x-1
			print(1, end='')
	print(f' x 2^{floor(n)}')