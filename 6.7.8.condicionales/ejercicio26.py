#De un operario sabemos sueldo y antiguedad.
#Si el sueldo es inferior a $500 y antiguedad >=10años aumentar un 20% y mostrar el real
#Si el sueldo es inferior a $500 y antiguedad <10años aumentar un 5% y mostrar el real
#Si el sueldo es MAYOR O IGUAL a $500 y sin antiguedad y mostrar el real


sueldo=int(input("Ingrese el SUELDO :$"))
ant=int(input("Ingrese antigüedad :"))

if sueldo>=500:
    print("EL operario cobra:",sueldo,"sin AUMENTO")
else:    
    if sueldo<=500 and ant>=10:
        ajuste_sueldo=sueldo*1.20
        print("EL operario pasara a cobrar:",ajuste_sueldo,"20% AUMENTO")
    else:
        ajuste_sueldo=sueldo*1.05
        print("EL operario pasara a cobrar:",ajuste_sueldo,"10% AUMENTO")
    