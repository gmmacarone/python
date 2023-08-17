"""Desarrollar una función que solicite la carga del dia, mes y año y almacene
 dichos datos en una tupla que luego debe retornar. La segunda función a 
 implementar debe recibir una tupla con la fecha y mostrarla por pantalla."""


def cargar_fecha():
    dia=int(input("Ingrese dia :"))
    mes=int(input("Ingrese mes :"))
    anio=int(input("Ingrese año :"))
    return (dia,mes,anio)

def imprimir(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

#main
fecha=cargar_fecha()
imprimir(fecha)