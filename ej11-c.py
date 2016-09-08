def fecha():
	dia = int(input("Ingrese un día:"))
	mes = int(input("Ingrese un mes:"))
	año = int(input("Ingrese un año:"))
	
	if dia > 31 or mes > 12:
		print("Fecha no válida")
	elif mes == 2 and dia > 29:
		print("Fecha no valida")
	else:
		print("Fecha válida:"+str(dia)+"/"+str(mes)+"/"+str(año))

fecha()

