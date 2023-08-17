"""Implementaremos una clase llamada Persona que tendrá como atributo (variable) 
su nombre y dos métodos (funciones), uno de dichos métodos inicializará el atributo 
nombre y el siguiente método mostrará en la pantalla el contenido del mismo."""


class Persona():

    def inicializar(self,nombre):
        self.nombre = nombre
    
    def imprimir(self):
        print("Mi nombre es:", self.nombre)

#main
persona1=Persona()
#instanciamos un objeto persona con su constructor vacío
persona1.inicializar("Jorge")
#llamando al metodo "inicializar" para asignarle valor a sus variables
persona1.imprimir()
