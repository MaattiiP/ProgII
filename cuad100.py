#! /usr/bin/python3.4

#def cuadrado(n):
 #   return n*n

#def suma_cuad(n):
 #   suma=0
  #  for x in range(1, n+1):
   #     suma = suma + cuadrado (x)
    #return suma

#print ("la suma de los primeros 100 cuadrados es: ", suma_cuad(100)) 

def hola (nombre) :
    return "Hola " + nombre + "¡"

def saludar ():

    nombre = input ("Por favor ingrese su nombre: ")
    saludo = hola (nombre)
    print (saludo)


    
saludar ()

def imprimir_cuadrados ():
    print ("Se calcularan cuadrados ingresados entre dos nùmeros ingresdos")


    n1 = int (input ("Ingrese un número entero: "))
    n2 = int (input ("Ingrese otro número entero: "))

    for x in range (n1, n2 + 1):
        print (x*x)

    print ("Es todo por ahora")

imprimir_cuadrados()
