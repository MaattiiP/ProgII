def cuadrados():
    print ("Se calcularan los cuadrados entre dos numeros ingresados")

    n1 = int(input("ingrese un numero entero: "))
    n2 = int(input ("ingrese otro numero entero: "))

    for x in range (n1, n2):
        print ("el cuadrado de ",x, "es", (x * x))

    print ("es todo por ahora")

cuadrados()
