"""Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)

Definir dos objetos de la clase Alumno."""

class Alumno():

    def inizializar(self,nombre,nota):
        self.nombre = nombre
        """Atributo del objeto (variable) con el valor "nombre" pasado por parámetro
        al constructor (__init__)
        y se guarda en un atributo llamado
        'nombre'.
        El mismo procedimiento es aplicable para definir otros atributos
        que puedan ser necesarios como: edad, dirección..."""
        self.nota = nota

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def mostrar_estado(self):
        if 0 <= self.nota < 4 : #si está reprobado
            print("REPROBADO")
        else:
            print("APROBADO")


#main
alumno1=Alumno()
alumno1.inizializar("pedro",6)
alumno1.mostrar()
alumno1.mostrar_estado()

