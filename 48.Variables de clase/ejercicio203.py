"""Definir una clase Cliente que almacene un código de cliente y un nombre.
En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que tienen suspendidas sus cuentas corrientes.
Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta corriente."""

class Cliente():
    suspendidos=[]
    def __init__(self, codigo_cliente,nombre):
        self.__codigo = codigo_cliente #Atributo privado para almacenar el valor del cliente
        self._nombre=nombre

    def impresion(self):
        print("Codigo: ",self.__codigo,"Nombre:",self._nombre)
        self.estado()

    def suspender(self):
        Cliente.suspendidos.append(self.__codigo)
    
    def estado(self):
        if (self.__codigo in Cliente.suspendidos)==True :
            print ("Cliente Suspendido")
        else:
            print ("Cliente Activo")
#main
c1=Cliente('098765432','Gus')
print("\nDatos del primer cliente:")
c1.impresion()
c2=Cliente("00554443","Lore")
print("\nDatos del segundo cliente:")
c2.impresion()
c2.suspender()
print("Nuevo estado")
c2.impresion()
