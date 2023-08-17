"""Se desea almacenar los datos de 3 alumnos. 
Definir un diccionario cuya clave sea el número de 
documento del alumno. 
Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre 
de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas."""


def carga():
    alumnos={}
    salida1="s"
    while salida1=="s":
        dni=int(input("Ingrese el DNI :"))
        lista=[]
        salida2="s"
        while salida2=="s":
            materia=input("Ingrese la materia :")
            nota=int(input("Ingrese la nota :"))
            lista.append((materia,nota))
            alumnos[dni]=(lista)
            salida2=input("Ingresa otra materia s/n :")
        salida1=input("Carga otro ALUMNO ? s/n :")
    print(alumnos)


def listar (alumnos):
    for dni in alumnos:
        for materia,nota in alumnos[dni]:
            print(dni,materia,nota)

def consulta(alumnos):
    dni=int(input("Ingrese el DNI del alumno :"))
    if dni in alumnos:
        for materia,nota in alumnos[dni]:
            print(dni,materia,nota)
    
#main
alumnos=carga()
#alumnos={222222: [('Geografia', 4), ('Matema', 3)], 666666: [('Lengua', 5)]}
listar(alumnos)
consulta(alumnos)