"""Desarrollar una clase que represente un punto en el plano y tenga 
los siguientes métodos: inicializar los valores de x e y que llegan como parámetros,
imprimir en que cuadrante se encuentra dicho punto (concepto matemático, 
primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)"""

class Plano():

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def cuadrante(self):
        if self.x>0 and self.y>0:
            print("PRIMER CUADRANTE")
        else:
            if self.x<0 and self.y>0:
                print("SEGUNDO CUADRANTE")
            else:
                if self.x<0 and self.y<0:
                    print("TERCER CUADRANTE")
                else:
                    print("CUARTO CUADRANTE")
#main
plano1=Plano(-3,3)
plano1.cuadrante() 