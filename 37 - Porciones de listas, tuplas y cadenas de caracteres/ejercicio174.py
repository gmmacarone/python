"""Cargar una cadena por teclado luego:
1) Imprimir los dos primeros caracteres.
2) Imprimir los dos últimos
3) Imprimir todos menos el primero y el último caracter."""

def carga():
    
    palabra=input("Ingrese la palabra :")
    
    return palabra

def imprime_dos_primeros(cadena):
    lista_dos_primeros=cadena[:2]
    print("Lista completa : ",cadena)
    print("Los dos primeros :",lista_dos_primeros)

def imprime_dos_ultimos(cadena):
    print()
    tamanio=len(cadena)
    print("DESDE LA FUNCION TAMANIO ES ",tamanio)
    lista=cadena[tamanio-2:]
    lista_dos_ultimos=lista
    print("Lista completa : ",cadena)
    print("Los dos ultimos :",lista_dos_ultimos)

def imprime_menos_primero_y_ultimo(cadena):
    print()
    tamanio=len(cadena)
    lista=cadena[1:tamanio]
    print("Lista completa : ",cadena)
    print("Imprimo menos primero y ultimo :",lista)

#main
cadena=carga()
imprime_dos_primeros(cadena)
imprime_dos_ultimos(cadena)
imprime_menos_primero_y_ultimo(cadena)

