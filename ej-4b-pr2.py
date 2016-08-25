# -*- encoding: utf-8 -*-

def amigos():
    """ amigos no recibe argumentos de entrada y no produce valores de salida.
imprime en pantalla un saludo para  5 personas"""
    input ("piense en sus 5 mejores amigos! presione una tecla cuando este listo")

    amigo1 = input("ingrese el nombre de su mejor amigo!")
    amigo2 = input("ingrese el nombre de su mejor amigo!")
    amigo3 = input("ingrese el nombre de su mejor amigo!")
    amigo4 = input("ingrese el nombre de su mejor amigo!")
    amigo5 = input("ingrese el nombre de su mejor amigo!")
    print ("\n")

    for x in [amigo1, amigo2, amigo3, amigo4, amigo5]:
        print ("hola, como andas?", x)

amigos()

    
