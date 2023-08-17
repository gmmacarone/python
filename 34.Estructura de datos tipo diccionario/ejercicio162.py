"""Crear un diccionario en Python que defina como clave el número de documento 
de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento."""

def carga():
    personas={}
    for i in range(3):
        dni=int(input("Ingrese el DNI :"))
        nombre=input("Ingrese Nombre :")
        personas[dni]=nombre
    return personas

def listar(personas):
    for item in personas:
        print("**********")
        print("DNI:",item," NOMBRE :",personas[item])
        print()

def consultar(personas):
    du=int(input("Ingrese DU :"))
    if du in personas:
        print("El DU ",du," corresponde a  ",personas[du])

#main
personas=carga()
listar(personas)
consultar(personas)