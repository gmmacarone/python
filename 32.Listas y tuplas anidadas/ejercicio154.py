"""Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en la primer componente el nombre del candidato y en la segunda componente 
cargar una lista con componentes de tipo tupla con el nombre de la provincia 
y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado, pero si se cargaran por asignación 
tendría una estructura similar a esta:

candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55)]) , ("luis", [("buenos aires",20)]) ]

1) Función para cargar todos los candidatos, 
sus nombres y las provincias con los votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos 
en todas las provincias.


"""



def carga():
    candidatos=[]
    
    for j in range(2): 
        nombre=input("Ingrese el nombre :")
        provincia=[]
        for i in range(2):
            prov=input("Ingrese la Provincia :")
            votos=int(input("Ingrese votos :"))
            provincia.append((prov,votos))
        candidatos.append((nombre,provincia))
        
    return(candidatos)


def imprimir(candidatos):
    for i in range(2):
        print("****************")
        print("----- candidato -----")
        print(candidatos[i][0])
        print("__________votos_______________")
        for j in range(2):
            print(candidatos[i][1][j])
       
def sumar_imprimir(candidatos):
    sum=0
    for j in range(2):
        for i in range(2):
            #print("ACA")
            sum+=(candidatos[j][1][i][1]) #0 1 0 1 : 100
                                              #0 1 0 1 : 200
        print("----- candidato -----")
        print(candidatos[j][0])
        print("__________votos_______________")
        print(sum)
        sum=0

#main
"""
candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55),("buenos aires",20)]) ]

print(candidatos[0][0])    #juan
print(candidatos[0][1][0]) #cordoba 100
    print(candidatos[0][1][0][1])#100
print(candidatos[0][1][1]) #buenos aires 200
    print(candidatos[0][1][1][1])#200

print(candidatos[1][0]) #ana
print(candidatos[1][1][0]) #cordoba 55
    print(candidatos[1][1][0][1])  #55
print(candidatos[1][1][1]) #buenos aires 20
    print(candidatos[1][1][1][1])  #20

"""

candidatos=carga()
imprimir(candidatos)
sumar_imprimir(candidatos)