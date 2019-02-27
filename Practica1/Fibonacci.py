###Escriba un programa que calcule los primeros N terminos de la serie de FibonacciII
a=0
b=1
print (a)
print (b)
i=0
n=100
while i<n:
	s=a+b
	a=b
	b=s
	print (s)
	i+=1
