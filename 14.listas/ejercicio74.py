#Definir una lista que almacene por asignación los nombres de 5 personas. 
#Contar cuantos de esos nombres tienen 5 o más caracteres.

nombres=["Jorge","Camilo","Jony","Ana","Lore"]
cont=0
for x in range(len(nombres)):
    if len(nombres[x])>=5:
        cont=cont+1
print(" La lista es ",nombres)
print("Mas o de 5 letras ",cont)