# -*- encoding: utf-8 -*-
def pantalla ():
    """ la funcion pantalla imprime en pantalla los numero del diez al veinte.
no recibe argumentos de entrada y no devuelve ningun argumento """
    print("Imprime los números del 10 al 20")
    for x in range (10, 21):
        print(str(x), sep = "\n")

pantalla()
