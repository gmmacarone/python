"""Confeccionar una clase que administre una agenda personal.
 Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa."""

class Agenda():

    def __init__(self):
        self.lista={}
    
    def carga(self):
        nombre=input("Ingrese el nombre :")
        telefono=int(input("Ingrese el telefono :"))
        mail=input("Ingrese mail :")
        self.lista[nombre]=(telefono,mail)
    
    def consulta_nombre(self):
        nom=input("Ingrese nombre a consulta :")
        if nom in self.lista:
            print(self.lista[nom],self.lista[nom][0],self.lista[nom][1])
        print("---------------------------------------------------------")
    
    def lista_completa(self):
        print("-------------------------------------------")
        print("LISTA COMPLETA")
        for nombre in self.lista:
            print(nombre,self.lista[nombre][0],self.lista[nombre][1])
    
    def modificar(self):
        print("")
        nom=input("Ingrese nombre a consulta :")
        if nom in self.lista:
            tel=int(input(" Nuevo TELEFONO :"))
            correo=input(" Nuevo CORREO :")
            self.lista[nom]=(tel,correo)
        else:
            print(" SIN ESE CONTACTO EN AGENDA!!!!")

    def menu(self):
        op=0
        while op!=5:
            print("1- Carga de un contacto en la agenda.")
            print("2- Listado completo de la agenda.")
            print("3- Consulta ingresando el nombre de la persona.")
            print("4- Modificación de su teléfono y mail.")
            print("5- Finalizar programa.")
            op=int(input("Opcion :"))
            if op==1:
                self.carga()
            elif op==2:
                self.lista_completa()  
            elif op==3:
                self.consulta_nombre()
            elif op==4:
                self.modificar()
            
#main
anotacion=Agenda()
anotacion.menu()
                
            
