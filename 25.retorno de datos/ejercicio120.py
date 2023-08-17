"""Confeccionar una función que le enviemos como
 parámetro el valor del lado de un cuadrado y nos retorne su superficie."""

def retornar_superficie(lado):
    sup=lado*lado
    return sup

#main
va=int(input("Ingrese el lado del cuadrado :"))
superficie=retornar_superficie(va)
print("El cuadradod de lado ",va,"cm","tiene por superficie ",superficie)