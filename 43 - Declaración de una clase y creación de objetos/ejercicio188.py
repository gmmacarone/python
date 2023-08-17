"""Confeccionar una clase que permita carga el nombre y la edad de una persona.
 Mostrar los datos cargados. 
Imprimir un mensaje si es mayor de edad (edad>=18)"""


class Persona:
    def inicializar(self,nom,anios):
        self.nombre=nom
        self.edad=anios

    def mostrar(self):
        print("La persona es ",self.nombre," y tiene :",self.edad," años")

    def mayor(self):
        if self.edad>=18:
            print(self.nombre , "es mayor de edad")
        else:
            print("ES MENOR!")

#main
persona1=Persona()
persona1.inicializar("Pedro",22)
persona1.mostrar()
persona1.mayor()

persona2=Persona()
persona2.inicializar("Anita",2)
persona2.mostrar()
persona2.mayor()

