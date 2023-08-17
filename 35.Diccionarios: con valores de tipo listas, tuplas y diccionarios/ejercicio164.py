"""Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha. 
Permitir almacenar distintas actividades para la misma fecha (se ingresa la 
hora y la actividad)
Implementar las siguientes funciones:
1) Carga de datos en la agenda.
2) Listado completo de la agenda.
3) Consulta de una fecha."""

def carga():
    agenda={}
    continuar="s"
    while continuar=="s":
        fecha=input("ingrese en formato xx/xx/xx :")
        lista=[]
        continuar2="s"
        while continuar2=="s":
            hora=input("ingrese formato  HORA xx:xx :")
            actividad=input("ingrese la actividad :")
            lista.append((hora,actividad))
            agenda[fecha]=lista
            continuar2=input("Mas actividades para la misma fecha s/n :")
        continuar=input("Desea continuar con otra fecha s/n :")
    print(agenda)
    return agenda

def listar(agenda):
    print("****************************************")
    for fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(fecha,hora,actividad)

            
def consulta(agenda):
    fecha=input("ingrese en formato PARA BUSCAR xx/xx/xx :")
    if fecha in agenda:
        print("LO PROGRAMADO")
        for hora,actividad in agenda[fecha]:
            print(fecha,hora,actividad)

#main
#agenda={'12/12/20': [('11:00', 'Almuerzo'), ('15:00', 'Futbol')], '13/01/23': [('11:00', 'Desayuno')]}
agenda=carga()
listar(agenda)
consulta(agenda)