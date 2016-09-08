
def meses(mes, bisiesto = False):
	if mes in (1,3,5,7,8,10,12):
		return("El mes posee 31 días")
	elif mes in (4,6,9,11):
		return("El mes posee 30 días")
	elif mes == 2 and bisiesto:
		return("El mes posee 29 días")
	else:
		return("El mes posee 28 días")

meses(12, bisiesto = True)
meses(6)
meses(2)
meses(2, bisiesto = True)
	
def test_meses():
	assert meses(4) == "El mes posee 30 días"
	assert meses(2, bisiesto = True) == "El mes posee 29 días"
	assert meses(12) == "El mes posee 31 días"
	assert meses(2, bisiesto = False) == "El mes posee 28 días"
