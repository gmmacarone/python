"""Confeccionar una función que reciba una cadena de caracteres y nos devuelva 
los tres primeros.
En el bloque principal del programa definir una tupla con los nombres de meses. 
Mostrar por pantalla los primeros tres caracteres de cada mes."""

def devuelve_caracter(cadena):
    return cadena[:3]

#main
meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre")
for mes in meses:
    muestra_tres_primeros=devuelve_caracter(mes)
    print(muestra_tres_primeros)