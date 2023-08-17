#ingresar DIA MES y AÑO y ferificar si es Navidad

dia=int(input(" Ingrese el DIA :"))
mes=int(input("Ingrese el MES :"))
anio=int(input("Ingrese el año :"))
print ("Estamos en ",dia, mes , anio)
if dia==25 and mes==12:
    print ("Corresponde NAVIDAD")
else:
    print("ESPERA")