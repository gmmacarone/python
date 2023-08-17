"""Escribir un programa que pida ingresar coordenadas (x,y) 
que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, 
Escribir un programa que pida ingresar coordenadas (x,y) que representan 
puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto 
cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a 
procesar."""

cuad1=0
cuad2=0
cuad3=0
cuad4=0
cant=int(input(" Cuantos puntos procesara ?"))
for f in range (cant):
    x=int(input("Ingrese coordenada X :"))
    y=int(input("Ingrese coordenada Y :"))
    if x>0 and y >0:
        print("1er CUADRANTE")
        cuad1=cuad1+1
    else:
        if x<0 and y>0:
            print("2do CUADRANTE")
            cuad2=cuad2+1
        else:
            if x<0 and y<0:
                print("3do CUADRANTE")
                cuad3=cuad3+1
            else:
                print("4to CUADRANTE")
                cuad4=cuad4+1
print("Coord em 1erC:",cuad1,"Coord en 2doC:",cuad2,"Coord en 3erC:",cuad3,"Coord en 4toC:",cuad4)
        
