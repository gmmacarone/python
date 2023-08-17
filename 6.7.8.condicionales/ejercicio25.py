#Se ingresa un valor para X y otro para Y . 
#Determinar en que cuadrante se encuentra de un eje cartesiano

x=int(input("Ingrese la coordenada X:"))
y=int(input("Ingrese la coordenada Y:"))
if x>0 and y>0:
    print ("Corresponde PRIMER cuadrante")
else:
    if x>0 and y<0:
        print ("Corresponde CUARTO cuadrante")
    else:
        if x<0 and y>0:
            print ("Corresponde SEGUNDO cuadrante")
        else:
            if x<0 and y<0:
                print ("Corresponde TERCER cuadrante")
            else:
                print ("Corresponde EJE cuadrante")