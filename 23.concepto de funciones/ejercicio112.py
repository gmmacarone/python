"""Confeccionar una aplicación que muestre una presentación 
en pantalla del programa. Solicite la carga de dos valores y
nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.
Implementar estas actividades en tres funciones."""


def presentacion():
    print("Este programa carga dos calores por teclado!")
    print("Efectua la sumam de los mismos")
    print("Muestra el resultado!")

def carga_suma():
    valor1=int(input("Carga el valor :"))
    valor2=int(input("Carga el otro valor :"))
    suma=valor1+valor2
    print("La suma es :",suma)

def final():
    print("Gracias por usar!!!!")

#programa principal

presentacion()
carga_suma()
final()
