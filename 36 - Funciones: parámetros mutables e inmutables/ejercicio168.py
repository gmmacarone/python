"""Confeccionar un programa que almacene en un diccionario como clave 
el nombre de un contacto y como valor su número telefónico:
1) Carga de contactos y su número telefónico.
2) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto 
para su búsqueda.
3) Imprimir la lista completa de contactos con sus números telefónicos."""

def carga():
    agenda={}
    for i in range(3):
        nombre=input("Ingrese el nombre :")
        numero=int(input("Ingrese el numero :"))
        agenda[nombre]=numero
    return agenda

def modifica_num(agenda):
    nombre=input("Ingrese el nombre a buscar :")
    if nombre in agenda:
        numero=int(input("El nuevo numero es :"))
        agenda[nombre]=numero
    else:
        print("Nombre no encontrado!")

def imprimir(agenda):
    print("_________________")
    print("LISTA")
    for nombre in agenda:
        print(nombre," = ",agenda[nombre])
#main
agenda=carga()
modifica_num(agenda)
imprimir(agenda)
