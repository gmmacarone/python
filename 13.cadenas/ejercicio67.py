"""Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas.
 Contar la cantidad de vocales. 
 Crear un segundo string con toda la oración en minúsculas para que 
 sea más fácil disponer la condición que verifica que es una vocal."""
cant=0
oracion=input(" Ingrese oracion :")
oracion2=oracion.lower()
for x in range (len(oracion2)):
    if oracion2[x]=="a" or oracion2[x]=="e" or oracion2[x]=="i" or oracion2[x]=="o" or oracion2[x]=="u":
        cant=cant+1
print(cant," vocales")