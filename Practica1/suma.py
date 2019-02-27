###Escribe un programa corto que imprima los primeros N numeros y la suma de los mismo N usando un bucle for. Luego escribe un programaequivalente que imprima los numeros del 1 al 10 usando un bucle while.

sum=0

Num=int(input("Ingrese número"))
for i in range(1, Num+1):
	sum=sum+i
print(sum)

print(range(0,Num))

i=1
while i <=10:
	print(i)
	i=i+1
