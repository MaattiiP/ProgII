 # -*- encoding: utf-8 -*-
def montoFinal ():
    print("Devuelve el monto (pesos) final a obtener en funcion del interes y los años")
    dinero = float (input ("Ingrese su capital inicial: "))
    interes = float (input ("Ingrese la tasa de interes: "))
    años = int (input ("Ingrese la cantidad de años a depositar: "))
    montoF = dinero * (1 + interes/100)** años
    print ("El monto final a obtener es: $",str(montoF))

montoFinal()

