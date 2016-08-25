#a)
def perimetro(base, altura):
    return (base * 2) + (altura * 2)

#print ("el perimetro del rectangulo es: ", perimetro(2, 4), "cm")

#b)
def area_rec(base, altura):
    return (base * altura)

#print ("el area del rectangulo es: ", area_rec (2, 4), "cm²")

#c)
def rectangulo(x1, x2, y1, y2):
    h = y2 - y1
    b = x2 - x1


    print ('Perimetro: ', perimetro(b, h),
           'Area: ',area_rec(b, h))


rectangulo(5, 6, 7 , 9)
     
#D)
def circulo(radio):
    pi=3.141592
    print ("el perimetro de un circulo de radio: ", radio, "es: ", pi * radio * 2 )

circulo(4)

def per 
