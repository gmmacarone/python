"""Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. 
Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa."""

class Administre():
    
    def __init__(self):
        self.alumnos=[]
        self.notas=[]
        self.menu()
    
    def carga(self):
        for i in range(3):
            self.nom=input("Ingrese el nombre :")
            self.calif=int(input("Ingrese la nota :"))
            self.alumnos.append(self.nom)
            self.notas.append(self.calif)

    def listar(self):
        for i in range(3):
            print("-------------------------------------------")
            print("ALUMNO :",self.alumnos[i]," NOTA :",self.notas[i])
            print("-------------------------------------------")
    
    def mayor_siete(self):
        for i in range(3):
            if self.notas[i]>7:
                print("ALUMNO :",self.alumnos[i]," NOTA :",self.notas[i])
    
    def menu(self):
        op=0
        while op!=4:
            print("1- Cargar alumnos.")
            print("2- Listar alumnos.")
            print("3- Mostrar alumnos con notas mayores o iguales a 7.")
            print("4- Finalizar programa.")
            op=int(input("Ingrese op = "))
            if op==1:
                self.carga()
            elif op==2:
                self.listar()
            elif op==3:
                self.mayor_siete()
            elif op==4:
                op=4
#main
alumno1=Administre()

            