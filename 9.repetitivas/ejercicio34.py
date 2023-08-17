#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
#realizar un programa que lea los sueldos que cobra cada empleado e 
#informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
# Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
mas=0
menos=0
gasto=0
x=1
cant_empleados=int(input("Ingrese la cantidad de empleados a cargar : "))
while x<=cant_empleados:
    print("El empleado número :",x)
    monto=float(input("Cobra :$"))
    gasto=gasto+monto
    if monto>=100 and monto<=300:
        menos=menos+1
    else:
        mas=mas+1
    x=x+1
print("Del total de ",x," Empleados.La Empresa pago $",gasto)
print(menos," Cobran entre $100 y $300")
print(mas," Cobran mas de $300")            