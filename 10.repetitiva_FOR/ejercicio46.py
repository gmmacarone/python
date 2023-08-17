#Codificar un programa que lea n números enteros y calcule 
#la cantidad de valores mayores o iguales a 1000 (n se carga por teclado)
#Este tipo de problemas también se puede resolver empleando la estructura repetitiva for. 
#Lo primero que se hace es cargar una variable que indique 
#la cantidad de valores a ingresar. 
#Dicha variable se carga antes de entrar a la estructura repetitiva for.
cant=0
n=int(input("Cuantos valores desea ingresar :"))
for x in range (n):
    num=int(input("Ingrese el numero :"))
    if num>=1000:
        cant=cant+1
print ("Se cargaron ",n,"numeros.Solo ",cant," mayor a 1000")