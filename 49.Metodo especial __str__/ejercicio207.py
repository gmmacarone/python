"""Desarrollar un programa que implemente una clase llamada Jugador.
Definir como atributos su nombre y puntaje.
Codificar el método especial __str__ que retorne el nombre y si es principiante (menos de 1000 puntos) o experto (1000 o más puntos)"""

class Jugador:
    def __init__(self,nombre,puntaje):
        self.__nombre = nombre #Atributo privado
        self._puntaje= puntaje
    
    def __str__(self):
        #Metodo para imprimir los datos del objeto jugador
        if self._puntaje<1000:
            return f"PRINCIPIANTE - Nombre:{self.__nombre} Puntaje:{self._puntaje}"
        else:
            return f"EXPERTO- Nombre:{self.__nombre} Puntaje:{self._puntaje}"

#MAIN
jugador1=Jugador("Pedro",3000000)
jugador2=Jugador("Ana",30)
print(jugador1)#Imprime el valor de la variable jugador
print(jugador2)