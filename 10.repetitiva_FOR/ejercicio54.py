"""Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los 
tres turnos tiene un promedio de edades mayor."""

ac_man=0
ac_tar=0
ac_noc=0
prom_man=0
prom_tar=0
prom_noc=0


for m in range (5):
    edad_man=int(input(" Edad del alumno de la mañana :"))
    ac_man=ac_man+edad_man
    prom_man=ac_man/5
for t in range (6):
    edad_tar=int(input(" Edad del alumno de la tarde :"))
    ac_tar=ac_tar+edad_tar
    prom_tar=ac_tar/6
for n in range (11):
    edad_noc=int(input(" Edad del alumno de la noche :"))
    ac_noc=ac_noc+edad_noc
    prom_noc=ac_noc/11
print("Promedio edades :")
print("Mañana :",prom_man," Tarde :",prom_tar," Noche :",prom_noc)
if prom_man>prom_tar and prom_man>prom_noc:
    print("Mayor promedio de edades a la mañana ")
else:
    if prom_tar>prom_noc:
        print("Mayor promedio de edades a la tarde ")
    else:
        print("Mayor promedio de edades a la noche ")

