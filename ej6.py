def factorial():
	"""
	Pide un numero natural n y calcula su factorial!

	"""
	n = int(input ("ingrese un numero natural por favor: "))
	fact = 1 #determinamos el valor de inicializacion en 1
	
	for x in range (1 , n +1):
		fact = fact * x
	print fact
		
factorial()
