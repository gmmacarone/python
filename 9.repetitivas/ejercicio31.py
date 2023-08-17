#Una planta que fabrica perfiles de hierro posee un lote de n piezas.
#Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar
# y luego ingrese la longitud de cada perfil; 
#sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas.
# Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.
x=0
aptas=0
cant=int(input("Cuantas piezas procesa :"))
while x<cant:
    long=float(input("Ingrese long de la pieza :"))
    
    if long>=1.20 and long<=1.3:
        aptas=aptas+1
    x=x+1
    
print ("Existen ",aptas,"piezas en condiciones entre 1.2 / 1.3")
