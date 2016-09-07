#-*- coding: utf-8 -*-
"""
Analisis:

Espececificar la solución:
    No recibe argumentos --> No devuelve valores
La función debe reciber un número N introcucido por el usuario
Y debe imprimir en pantalla los numeros triangulares de 1 hasta N.

Diseño de la solución:
Se introduce un número N
Aplica la firmula para todos los numeros de 1 hasta N
Imprime en pantalla los números triangulares junto con su indice

Ejemplos:
1 - 1
2 - 3
3 - 6
4 - 10
5 - 15
"""

def triFormula ():
    print ("Muestra en pantalla los números triangulares de 1" , "hasta el número ingresado", end = "\n")
    numeroIn = int (input("Ingrese un número: "))
    print ("Números triangulares: ", end = "\n")
    for x in range (1, numeroIn + 1):
        numeroTri = int((x * (x + 1)) / 2)
        print (str(x) + " - " + str(numeroTri), end = "\n")

triFormula()

def triangular ():
    print ("Muestra en pantalla los números triangulares de 1" , "hasta el número ingresado", end = "\n")
    numeroIn = int (input("Ingrese un número: "))
    print ("Números triangulares: ", end = "\n")
    numeroTri = 0
    for x in range (1, numeroIn + 1):
        numeroTri = numeroTri + x
        print (str(x) + " - " + str(numeroTri), end = "\n")

triangular()
