#-*- encoding: utf-8 -*-

def factorial():
	"""
	
	Pide un numero natural n y calcula su factorial.
	No recibe argumentos de entrada y no posee valores de salida.

	"""
	print ("================BIENVENIDO A NUESTRO PROGRAMA!================ \nCon él, podrás saber el factorial de cualquier número natural! \n")
	
	n = int(input ("Ingrese un número natural por favor: "))
	fact = 1 #determinamos el valor de inicialización en 1
	
	for x in range (1 , n +1):
		fact = fact * x
	print fact
		
factorial()
