#Un postulante a un empleo realiza un test
#Se tiene CANTIDAD DE PREGUNTAS y CANTIDAD DE REPUESTAS CORRECTAS
#NIVEL MAXIMO si el % > =90
#NIVEL MEDIO si el % >= 75 y 90
#NIVEL REGULAR si 50 y 75
#NIVEL FUERA =<50

cant_preg=int(input("Ingrese la cantidad de preguntas realizadas :"))
cant_correctas=int(input("Ingrese las correctas :"))
nivel=(cant_correctas*100)/cant_preg
print ("NIVEL :",nivel,"%")
if nivel>=90:
    print ("Aprobo con un ",nivel,"% . MAXIMO")
else:
    if nivel>=75:
        print ("Aprobo con un ",nivel,"% . MEDIO")
    else:
        if nivel>=50:
            print ("Aprobo con un ",nivel,"% . REGULAR")
        else:
            print ("Aprobo con un ",nivel,"% . FUERA!")