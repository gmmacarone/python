"""Confeccionar una función que reciba el nombre de un operario, 
el pago por hora y la cantidad de horas trabajadas. Debe mostrar su sueldo y el nombre. 
Hacer la llamada de la función mediante argumentos nombrados."""

def calculo_sueldo(nombre,pago_hora,cant_hora):
    sueldo=pago_hora*cant_hora
    print("El operario :",nombre," trabajo hs:",cant_hora," y cobra :$",sueldo)

#main

calculo_sueldo("Pepe",2000,8)
calculo_sueldo(pago_hora=7000,)