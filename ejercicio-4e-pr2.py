def saludarAmigos ():
    """saludarAmigos: No recibe argumentos --> No devuelve valores
    Pregunta la cantidad de amigos a saludar
    Pide el nombre de sus amigo y lo saluda
    Lo repite la cantidad de veces ingresada
    """
    cantidad = int (input ("Ingrese la cantidad de amigos a saludar: "))
    for x in range (1, cantidad + 1):
        amigo = input ("Ingrese el nombre de su amigo: ")
        print ("Hola, todo bien? " + amigo, end = "\n")

saludarAmigos()
