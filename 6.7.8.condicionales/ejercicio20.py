#se carga una fecha con tres datos separados, DIA , MES y AÑO .
# Determinar si corresponde al primer trimestre del año

dia=int(input(" Ingrese el DIA :"))
mes=int(input("Ingrese el MES :"))
anio=int(input("Ingrese el año :"))

if mes==1 or mes==2 or mes==3:
    print ("Corresponde al primer trimestre")
else:
    print("NO ES DEL PRIMER TRIMESTRE")
