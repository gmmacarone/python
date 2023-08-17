"""Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa."""

class Alumnos():
    def __init__(self):
        self.nombres = []
        self.notas = []
    
    def menu(self):
        print("Bienvenido")
        op=0
        while op!=4:
            
            print("1-Cargar alumnos")
            print("2-Listar alumnos")
            print("3-Mostrar alumnos con notas >=7")
            print("4-Salir")
            op = int(input("¿Qué desea hacer? :"))
            if (op==1):
                self.carga()
            elif (op==2):
                self.listado()
            elif (op==3):
                self.mostrar_alumno_nota()
    
    def carga(self):
        nombre=input('Ingrese el nombre del estudiante:')
        nota=float(input('Ingrese la primera nota:'))
        self.nombres.append(nombre)
        self.notas.append(nota)

    def listado(self):
        for i in range (len(self.nombres)):
            print("Nombre :",self.nombres[i])
            print ("Nota:",self.notas[i],"\n\n")
    
    def mostrar_alumno_nota(self):
        print("Los que tienes nota >= 7")
        for i in range (len(self.nombres)):
            if self.notas[i]>= 7 :
                print("Nombre :",self.nombres[i])
                print ("Nota:",self.notas[i],"\n\n")

#main
alumno=Alumnos()
alumno.menu()
        

                    
            
                       
