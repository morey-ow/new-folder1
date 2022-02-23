from math import log, floor

while True:
	x=input('Enter decimal to convert binary: ')
	x=float(x)
#x = 10  #base 10, want to express in base 2
	if x==0:
		print(0)
		break
	elif x<0: #if x is negative, print negative sign and make it positive
		print('-', end='')
		x=-x
	base2=[] #this will collect the digits
	n=floor(log(x)/log(2))
	if n<0: base2=['0']
	while n>=0:
		if x>=2**n:
			base2.append(1)
			x=x-2**n
		else:
			base2.append(0)
		n=n-1
	for d in base2:
		print(d, end='')
	# done with the integer part of input
	# now deal with fractional part
	if x==0: #not fractional part
		base2=[]
		pass
	else:
		base2=['.']	
		for _ in range(50):
			if x==0.0:
				break
			elif x< 0.5:
				x=2*x
				base2.append(0)
			else:
				x=2*x-1
				base2.append(1)
	for d in base2:
		print(d, end='')
	
	print('\n')
	#print(f' x 2^{floor(n)}')