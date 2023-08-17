"""Plantear una clase llamada Jugador.
Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__, imprimir y pasar_tiempo (que debe reducir en uno la variable de clase).
Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta para el fin de juego (iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
Reducir dicha variable hasta llegar a cero."""

class Jugador():
    tiempo=30
    def __init__(self, nombre , puntaje):
        self.__nombre = nombre
        self.__puntaje = puntaje

    def imprimir(self):
        print("Nombre: ", self._Jugador__nombre)
        print("Puntaje:", self._Jugador__puntaje )
    
    def pasar_tiempo(self):
        Jugador.tiempo -=1
        if (Jugador.tiempo == 0 ):
            print("tiempo alcanzado!!!")
            
#main
jugador1=Jugador("Pepe",100)
jugador2=Jugador("Ana",40)
print("\n")
while Jugador.tiempo>0:
    jugador1.pasar_tiempo()
    
    print("spend the time....")

jugador1.imprimir()
jugador2.imprimir()



