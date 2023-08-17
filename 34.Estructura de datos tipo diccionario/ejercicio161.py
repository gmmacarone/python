"""Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano.
 La clave es la palabra en ingles y el valor es la palabra en castellano.
Crear las siguientes funciones:
1) Cargar el diccionario.
2) Listado completo del diccionario.
3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar 
su traducción.

"""

def carga():
    diccionario={}
    for item in range(3):
        ingles=input("Palabra en Ingles :")
        espaniol=input("Palabra en Español :")
        diccionario[ingles]=espaniol
    return diccionario

def listar(diccionario):
    for item in diccionario:
        print(item , ":" ,diccionario[item])

def traduccion(diccionario,word):
    if word in diccionario:
            print("**********")
            print("TRADUCCION")
            print(word," :",diccionario[word])
            
    else:
        print("NO TENEMOS ESA TRADUCCION!")
        
#main
diccionario=carga()
listar(diccionario)
word=input("Introduzca una palabra :")
traduccion(diccionario,word)

