"""Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el banco requiere que al final del día calcule la cantidad de dinero que hay depositado.

Lo primero que hacemos es identificar las clases:

Podemos identificar la clase Cliente y la clase Banco.

Luego debemos definir los atributos y los métodos de cada clase:

Cliente		
    atributos
        nombre
        monto
    métodos
        __init__
        depositar
        extraer
        retornar_monto

Banco
    atributos
        3 Cliente (3 objetos de la clase Cliente)
    métodos
        __init__
        operar
        depositos_totales
"""

class Cliente():
    def __init__(self,nombre):
        #constructor con el parámetro "nombre" para inicializar un cliente nuevo
        self.nombre = nombre
        self.monto=0
    def depositar(self,monto):
        self.monto += monto
    def extraer(self,monto):
        self.monto -= monto
    def retornar_monto(self):
        return self.monto
    
    #Clase banco tiene 2 clientes como miembros por lo tanto se
    #declaran en su constructor
    #dos instancias del objeto Cliente
    #1-clienteA - Alfredo
    #2-clienteB - Juanito

class Banco():
    def __init__(self):
        self.clienteA=Cliente("Alfredo")
        self.clienteB=Cliente("Juanito")
        self.clienteC=Cliente("Ana")
    def operar(self):
        print ("Deposito a cuenta A:$5000")
        self.clienteA.depositar(5000)
        print ("Monto actual:",self.clienteA.retornar_monto())
        print ()
        print("Deposito desde cuenta C:$7000")
        self.clienteC.depositar(7000)
        print ("Retiro desde cuenta C:-$4000")
        self.clienteC.extraer(4000)
        print ("Monto actual:",self.clienteC.retornar_monto())
        print()
        print("Deposito desde cuenta B:$8000")
        self.clienteB.depositar(8000)
        print ("Monto actual:",self.clienteB.retornar_monto())
        print()
    def depositos_totales(self):
        total=(self.clienteA.retornar_monto()+self.clienteB.retornar_monto()+self.clienteC.retornar_monto())
        return total
 #main
banco_santander=Banco()
banco_santander.operar()
print("\nTotal de Depósitos: ", banco_santander.depositos_totales())

            

