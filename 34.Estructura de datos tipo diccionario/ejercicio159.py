"""En el bloque principal del programa definir un diccionario que
 almacene los nombres de paises como clave y como valor la cantidad de habitantes. 
Implementar una función para mostrar cada clave y valor."""


def imprimir(paises):
    for claves in paises:
        print (claves,paises[claves])


#main
paises={"Argentina":4000000,"Chile":230000,"Peru":120000}
imprimir(paises)
