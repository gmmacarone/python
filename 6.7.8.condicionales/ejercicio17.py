#Confeccionar un programa que permita cargar un numero entero positivo de hasta tres cifras.Que
#muestre un mensaje si tiene 1, 2 o 3 cifras . Mostrar ERROR si el numero tiene mas de tres cifras 

num=int(input("ingrese un numero POSITIVO de hasta TRES cifras :"))
if num<1000:
    if num<100:
        if num<10:
            print (" El ",num,"tiene 1 cifra")
        else:
            print (" El ",num,"tiene 2 cifra")
    else:
        print (" El ",num,"tiene 3 cifra")
else:
    print (" El ",num,"tiene mas de TRES cifra")