#Se ingresan un conjunto de n alturas de personas por teclado. 
#Mostrar la altura promedio de las personas
suma_altura=0
x=1
cant_personas=int(input("De cuantas personas se cargara su altura :"))
while x<=cant_personas:
    print("La altura de la persona ",x)
    altura=float(input("Ingrese la altura :"))
    suma_altura=suma_altura+altura
    prom=suma_altura/cant_personas
    x=x+1
print ("La altura promedio es ",prom)