#Se ingresa un numero positivo de uno o dos digitos (1.....99).Mostrar un mensaje 
#indicando si el numero tiene uno o dos digitos

print("Yo te indico si tu numero tiene un o dos digitos!")
num=int(input("Ingrese un mumero entre 1....99 :"))
if num<=9:
    print("El numro tiene un solo digito!")
else:
    print("El numro tiene dos digitos!")
