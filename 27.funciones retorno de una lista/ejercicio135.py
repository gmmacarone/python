"""En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio."""


def carga():
    sueldos=[]
    for i in range (10):
        plata=int(input("Ingrese el sueldo :$"))
        sueldos.append(plata)
    return sueldos


def impresion(sueldos):
    for i in range (10):
        print("Impresion de sueldo :",sueldos[i])
        print("____________________________________")

def superior(sueldos):
    cont=0
    for i in range(10):
        if sueldos[i]>4000:
            cont+=1
    print("Sueldos superiores a $4000 :",cont)

def promedio(sueldos):
    sum=0
    for i in range (10):
        sum=sum+sueldos[i]
    prom=sum//10

    return prom

def debajo_prom(sueldos,prom):
    for i in range(10):
        if sueldos[i]<prom:
            print("Sueldos debajo del PROMEDIO :",sueldos[i])
            print("**********************")


#main
sueldos=carga()
impresion(sueldos)
superior(sueldos)
prom=promedio(sueldos)
print("EL PROMEDIO ES :",prom)
debajo_prom(sueldos,prom)
