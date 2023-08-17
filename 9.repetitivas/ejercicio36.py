#Mostrar los múltiplos de 8 hasta el valor 500. 
#Debe aparecer en pantalla 8 - 16 - 24, etc
elemento=0
terminos=1
print("ACA",terminos)
while elemento<496:
    elemento=8*terminos
    print(elemento)
    terminos=terminos+1
