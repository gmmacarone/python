"""Declarar una clase llamada Familia. Definir como atributos el nombre del padre, madre y una lista con los nombres de los hijos.
Definir el método especial __str__ que retorne un string con el nombre del padre, la madre y de todos sus hijos.

"""

class Familia:
    def __init__(self, nomPadre , nomMadre , nomHijo=[]):
        self.nomPadre = nomPadre
        self.nomMadre= nomMadre
        self.nomHijo  = nomHijo
    #Método para imprimir los datos de la familia
    def __str__(self):
        cadena= "La familia es "+ self.nomPadre +", "+ self.nomMadre
        for i in self.nomHijo:
            cadena += ", "+i
        return cadena
    
#main
familia_Blas=Familia("Ramiro Blas","Ofelia Correa",["Omarsito Blas","Junior Blas"])
print(familia_Blas)
familia_Blanco=Familia("Humberto Blanco","Rita Graso")
print (familia_Blanco )
familia_Negri=Familia("Juan Negri","Rina Flores")
print (familia_Negri)

