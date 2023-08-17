"""Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares."""
neg=0
pos=0
mul=0
ac_par=0

for n in range (10):
    val=int(input("Ingrese un valor :"))
    if val<0:
        neg=neg+1
    else:
        pos=pos+1
    if val%15==0:
        mul=mul+1
    if val%2==0:
        ac_par=ac_par+val
print("Cant positivos ",pos," Cant negativos ",neg)
print("Multiplos de 15 ",mul)
print("Acumilados pares ",ac_par)