"""Crear una clase Persona que tenga como atributo el nombre y la edad.
El operador == retornará verdadero si las dos personas tienen la misma edad, el operador > retornará True si la edad del objeto de la izquierda tiene una edad mayor a la edad del objeto de la derecha del operador >, y así sucesivamente

"""

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad",self.edad,"\n")
    
    def __eq__(self,objeto2):
        if self.edad==objeto2.edad:
            return True
        else:
            return False
    """
    def __gt__(self,objeto2):
        if self.edad>objeto2.edad:
            return True
    
    def __ne__(self,objeto2):
        if self.edad != objeto2.edad:
            return True
"""
#main
persona1=Persona("Claudia",44)
persona2=Persona("Ana",4)
if persona1==persona2:
    print ("Son iguales")
else:
    print('No son iguales')