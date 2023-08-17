"""Cargar una oración por teclado.
 Mostrar luego cuantos espacios en blanco se ingresaron.
   Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es """""
cant=0
oracion=input(" Cargue una oracion :")
for x in range (len(oracion)):
    if oracion[x]==" ":
        cant=cant+1
print(" Tiene ",cant," espacios")