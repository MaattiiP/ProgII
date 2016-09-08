def meses(mes, bisiesto = False):
	if mes in (1,3,5,7,8,10,12):
		return 31
	elif mes in (4,6,9,11):
		return 30
	elif mes == 2 and bisiesto:
		return 29
	else:
		return 28

def rest_dias():
	dia = int(input("Ingresar día:"))
	mes = int(input("Ingresar mes:"))
	año = int(input("Ingresar año:"))
	print ("Faltan "+str(meses(mes) - dia)+ " día/s para fin de mes")
	

def rest_dias_anio():
	dia = int(input("Ingresar dia: "))
	mes = int(input("Ingresar mes: "))
	anio = int(input("Ingrear año: "))
	diasRest = meses(mes) - dia
	suma = 0
	for x in range (mes+1, 13):
		suma = suma + meses(x) 
	print ("Faltan ",suma + diasRest, " dias para fin de año")
	
rest_dias_anio()
	
def dias_restantes():
	dia = int(input("Ingresar dia: "))
	mes = int(input("Ingresar mes: "))
	diasAño = 0
	for x in range(1,mes):
		diasAño += meses(x)
	rest = (365 - diasAño) - dia
	print(rest)

#dias_restantes()

def dias_transcurridos():
	dia = int(input("Ingresar dia: "))
	mes = int(input("Ingresar mes: "))
	diasAño = 0
	for x in range(1,mes):
		diasAño += meses(x)
	suma = diasAño+dia
	print(suma)

dias_transcurridos()


