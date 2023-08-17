"""Plantear un programa que permita jugar a los dados. Las reglas de juego son:
se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino "perdió".

Lo primero que hacemos es identificar las clases:

Podemos identificar la clase Dado y la clase JuegoDeDados.

Luego los atributos y los métodos de cada clase:

Dado		
    atributos
        valor
    métodos
        tirar
        imprimir
        retornar_valor

JuegoDeDados
    atributos
        3 Dado (3 objetos de la clase Dado)
    métodos
        __init__
        jugar
        
"""
import random

class Dado():
    def __init__(self):
        self.dado=0
                
    def tirar(self):
        self.dado=random.randint(1,6)
    
    def imprimir(self):
        print("Valor :",self.dado)
    
    def retornar_valor(self):
        return (self.dado)
    
class JuegoDeDados():
    def __init__(self):
        self.dado1=Dado()
        self.dado2=Dado()
        self.dado3=Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado2.tirar()
        self.dado3.tirar()
        self.dado1.imprimir()
        self.dado2.imprimir()
        self.dado3.imprimir()
        if self.dado1.retornar_valor()==self.dado2.retornar_valor()==self.dado3.retornar_valor():
            print ("Ganaste!")
        else:
            print ("Perdiste")

#main
juego1=JuegoDeDados()
juego1.jugar()

