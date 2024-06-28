Class Cliente:
 def__init__(self, nombre, saldo_inicial=0):
 self.nombre = nombre
 self.saldo = saldo_inicial
def depositar(self, monto):
  self.saldo += monto
  print(f"{self.nombre} ha depositado ${monto}. Saldo actual: ${self.saldo}")
def extraer(self, monto):
  if monto > self.saldo:
    print(f"{self.nombre} no tiene suficiente saldo para extraer ${monto}. Saldo actual: ${self.saldo}")
  else:
    self.saldo -= monto
    print(f"{self.nombre} ha extraido ${monto}. Saldo actual: ${self.saldo}")
class Banco:
  def __init__(self):
  self.clientes=[]
  def agregar_clientes(self, cliente):
    self.clientes-append(cliente)
  def calcular_total_depositado(self):
    total=0
    for cliente in self.clientes:
      total += cliente.saldo
    return total
  def mostrar_menu():
    print("n--- Menú de Operaciones ---")}
    print("1. Depositar dinero")
    print("2. Extraer dinero")
    print("3. Calcular total depositado")
    print("4. Salir)
    opcion = int(input("Seleccione una opción: "))
    return opcion
  def buscar_cliente(nombre, banco):
    for cliente in banco.clientes:
     if clientes.nombre == nombre:
       return cliente
    return None
 def main():
    # Crear banco
    banco = banco
    # Crear clientes y agregarlos al banco
    lautaro = Cliente("Lautaro", 1000)
    lorena = Cliente("Lorena", 1500)
    marr = Cliente("Marr, 2000)
    banco.agregar_cliente(lautaro)
    banco.agregar_cliente(lorena)
    banco.agregar_cliente(marr)
    while True:
     opcion = mostrar_menu()
    if opcion == 1:
    nombre = input("Ingrese el nombre del cliente:  ")
    monto = float(input("Ingrese el monto a depositar: "))
    cliente = buscar_cliente(nombre, banco)
    if cliente:
    cliente.depositar(monto)
    else:
    print("Cliente no encontrado.")
  elif oncion == 2
    nombre = input("Ingrese el nombre del cliente:  ")
    monto = float(input("Ingrese el monto a extraer: "))
    cliente = buscar_cliente(nombre, banco)
    if cliente:
    cliente.extraer(monto)
    else: print("Cliente no encontrado.")
  elif opcion == 3
    total = banco. calcular_total_depositado()
    print(f"El total depositado en el banco es: ${total}")
  elif opcion == 4:
    print("Saliendo del programa.")
    break
  else:print("Opcion no valida. Intente de nuevo.")
if __name__ == "__main__":
    main()