"""Elaborar una función que muestre la tabla de multiplicar del valor que le 
enviemos como parámetro. Definir un segundo parámetro llamado termino que por 
defecto almacene el valor 10. Se deben mostrar tantos términos de la tabla de 
multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa
 con argumentos nombrados."""

def tabla_multiplicar(valor,termino=10):
    resultado=[]
    for i in range(termino):
        res=valor*i
        resultado.append(res)
    return resultado

def imprimir(resultado):
    print(resultado)

#main
imprimir(tabla_multiplicar(2))
imprimir(tabla_multiplicar(2,termino=5))