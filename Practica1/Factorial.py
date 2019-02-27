### Escriba un programa que calcule el factorial de un número N
def factorial():
	num= int(input("Ingresa numero"))
	factorial= 1
	for i in range(num):
		factorial= factorial*num
		num= num-1
	print(factorial)
factorial()
