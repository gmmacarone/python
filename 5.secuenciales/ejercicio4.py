#Realizar un calculo de un producto ingresando el precio y la cantidad del mismo . Se muestra el valor total a pagar
precio=int(input("Ingrese el precio , sin centavos, del producto :"))
cantidad=int(input("Ingrese la cantidad a adquirir de ese producto :"))
total=precio*cantidad
print("Lo que Ud va a pagar es :$",total)