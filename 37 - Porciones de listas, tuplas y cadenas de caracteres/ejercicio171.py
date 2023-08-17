"""Confeccionar una función que le enviemos un número de mes como parámetro y 
nos retorne una tupla con todos 
los nombres de meses que faltan hasta fin de año."""

def meses_faltantes(mes):
    meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre")
    return meses[mes:]
#main
mes=int(input("Ingrese el número de mes a buscar para enviar los faltantes :"))
faltantes=meses_faltantes(mes)
print("Los faltantes al mes : ",mes , " son :",faltantes)