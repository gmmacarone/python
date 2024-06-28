class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        ultimo_nodo = self.cabeza
        while ultimo_nodo.siguiente:
            ultimo_nodo = ultimo_nodo.siguiente
        ultimo_nodo.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = ___.siguiente
