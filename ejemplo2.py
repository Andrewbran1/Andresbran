'''
base=0
altura=0
base=input("Ingrese la altura del rectángulo: ")
base=float(base)
altura=input("Ingrese la base del rectangulo: ")
altura=float(altura)
area=base*altura
perimetro=2*base+2*altura

print("El área del rectangulo es: ")
print(area)
print("El perimetro del rectangulo es: ")
print(perimetro)
'''
'''
radio=0
pi=3.14
radio=input("Ingrese el radio del circulo")
radio=float(radio)
area=pi*radio**2
perimetro=2*pi*radio
print("el área del circulo es: ")
print(area)
print("El perimetro del circulo es: ")
print(perimetro)
'''
'''
cateto1=0
cateto2=0
cateto1=float(input("ingrese el valor del cateto 1: "))
cateto2=float(input("Ingrese el valor del cateto 2: "))
hipotenusa=(cateto1**2+cateto2**2)**(1/2)
print("la hipotenusa es: ", hipotenusa)
'''
'''
nombre=0
año=0
nombre=input("Ingrese su nombre: ")
año=int(input("ingrese su edad: "))
nacimiento=(2024-año)
print("Su nombre es: ",nombre)
print("Su año de nacimiento es: ",nacimiento)
'''

anionaci=int(input("Ingrese el año de nacimiento: "))
edad=2024-anionaci
if edad>=18:
    print("Es mayor de edad")
else:
    print("ES menor de edad, ya que tiene",edad,"años")