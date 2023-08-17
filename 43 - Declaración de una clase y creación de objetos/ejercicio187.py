"""Implementar una clase llamada Alumno que tenga como atributos su nombre
 y su nota. Definir los métodos para inicializar sus atributos, imprimirlos y 
mostrar un mensaje si está regular (nota mayor o igual a 4)"""

class Alumno:
    def inicializar(self,nom,calificacion):
        self.nombre=nom
        self.nota=calificacion

    def imprimir(self):
        print("Nombre :",self.nombre)
        print("Calificacion :",self.nota)
    
    def regular(self):
        if self.nota>=4:
            print("El alumno :",self.nombre," esta REGULAR")
        else:
            print("El alumno :",self.nombre," esta IRREGULAR")

#main
alumno1=Alumno()
alumno1.inicializar("Pedro",6)
alumno1.imprimir()
alumno1.regular()

alumno1=Alumno()
alumno1.inicializar("Ana",2)
alumno1.imprimir()
alumno1.regular()

