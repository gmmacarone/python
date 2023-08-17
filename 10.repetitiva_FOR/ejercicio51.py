"""Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: 
equilátero (tres lados iguales), isósceles (dos lados iguales), 
o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo."""
equi=0
iso=0
esca=0
n=int(input("cuantos triangulos desea leer :"))

for x in range (n):
    l1=int(input("Ingrese un lado :"))
    l2=int(input("Ingrese otro lado :"))
    l3=int(input("Ingrese el tercer lado :"))
    if l1==l2 and l1==l3:
        print ("TRIANGULO EQUILATERO")
        equi=equi+1
    else:
        if l1==l3 or l2==l3 or l1==l21:
            print("TRIANGULO ISOSCELES")
            iso=iso+1
        else:
            print("TRIANGULO ESCALENO")
            esca=esca+1
print("Triangulo equilateros :",equi," Triangulo isosceles :",iso," Triangulo escaleno :",esca)