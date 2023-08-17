"""Cargar una cadena de caracteres por teclado.
 Mostrar la cadena del final al principio utilizando subíndices negativos."""

cadena=input("Cargue la palabra :")
indice=-1
for i in range(len(cadena)):
    print(cadena[indice],end="")
    indice-=1
print()