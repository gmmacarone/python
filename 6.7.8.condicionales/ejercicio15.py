#se carga tres numeros distintos mostrar el mayor
#https://youtu.be/Kg1H-bECRzA

nota1=int(input("Ingrese nota 1° :"))
nota2=int(input("Ingrese nota 2° :"))
nota3=int(input("Ingrese nota 3° :"))

if(nota1>nota2):
 
    if(nota1>nota3 ):
        print("El MAYOR ES ",nota1)
    else:
        print("El MAYOR ES ",nota3)

else:
    if(nota2>nota3 ):
        print("El MAYOR ES ",nota2)
    else:
        print("El MAYOR ES ",nota3)