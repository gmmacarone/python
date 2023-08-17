"""Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)"""

class Persona():

    def inizializar(self,nombre,edad):
        self.nombre=nombre
        self.edad = edad
        #Metodo para imprimir los datos de la persona
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad:",self.edad)

    def mayor(self):
        if (self.edad > 18 ):
            return "ES MAYOR"
        else:
            return "NO ES MAYOR DE EDAD"
#main
persona1=Persona()
persona1.inizializar("Pedro",12)
print("\nDatos del primer usuario:")
persona1.mostrar()
print(persona1.mayor())