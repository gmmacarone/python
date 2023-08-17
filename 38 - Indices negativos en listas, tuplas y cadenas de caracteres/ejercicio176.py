"""Confeccionar una función que reciba una palabra y verifique si es capicúa 
(es decir que se lee igual de izquierda a derecha que de derecha a izquierda)"""

def capicua(palabra):
    indice=-1
    cont=0
    for i in range(0,len(palabra)//2):
        if palabra[i]==palabra[indice]:
            cont+=1
        indice-=1
    print(palabra)
    if cont==(len(palabra)//2):
    
        print("CAPICUA!!!!")
    else:
        print("NO ES capicua")
#main
capicua("neuquen")
capicua("casa")