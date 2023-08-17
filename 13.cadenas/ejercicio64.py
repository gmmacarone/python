"""Ingresar un mail por teclado.
Verificar si el string ingresado contiene solo un caracter "@" """


cant=0
mail=input(" Ingrese el mail completo :")
for x in range (len(mail)):
    if mail[x]=="@":
        cant=cant+1
print("El mail tiene ",cant," @")