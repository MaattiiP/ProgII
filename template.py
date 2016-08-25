# -*- encoding: utf-8 -*-

# Importación de librerias (si las hubiese) una por línea.

def nombre_de_la_funcion(argumento1, argumento2):
    """
        Pequeño resumen del funcionamiento de la
        función 'nombre_de_la_funcion'.
        Args:
            argumento1: argumento de tipo A que representa B
            argumento2: argumento de tipo X que representa Y
        Returns:
            returns: la función retorna el valor correspondiente a Z
    """
    print('primer linea de código')
    print('segunda linea de código')
    # Comentario dentro del código explicando el funcionamiento
    # de un bloque de código como el siguiente
    for x in range(1,5):
        print(x)

    return 'valor de retorno'


# La siguiente línea indica la acción que se realizará
# al llamar el archivo desde la terminal.
nombre_de_la_funcion(1,2)
