def tablas():
	n = int(input("ingrese un numero por favor: "))
	mult = 1 
	for x in range (1 , 11):
		mult = n * x 
		print (str(n) + " por " + str(x) + " = " + str(mult))

tablas()
