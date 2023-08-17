"""Confeccionar una aplicacions que muestre un mensaje que se pasa por parametro y 
muestre la suma de dos numeros cargados desde la funcion y muestre la despedida"""

def mostrar_mensaje(mensaje):
    print("*****************")
    print(mensaje)
    print("*****************")

def carga_suma():
    valor1=int(input("Carga el valor :"))
    valor2=int(input("Carga el otro valor :"))
    suma=valor1+valor2
    print("La suma es :",suma)

#main
mostrar_mensaje("La suma de los numeros")
carga_suma()
mostrar_mensaje("Fin")