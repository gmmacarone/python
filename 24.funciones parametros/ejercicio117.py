"""Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. 
La carga de los valores hacerlo por teclado."""



def cargar():
    n1=int(input("Ingrese un num :"))
    n2=int(input("Ingrese otro num :"))
    n3=int(input("Ingrese el ultimo num :"))
    mayor(n1,n2,n3)

def mayor(n1,n2,n3):
    if n1>n2 and n1>n3:
        print("El MAYOR",n1)
    else:
        if n2>n3:
            print("EL MAYOR",n2)
        else:
            print("EL MAYOR",n3)


#main
cargar()

