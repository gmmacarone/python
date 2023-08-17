"""Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: inicializar los valores de x e y que llegan como parámetros, imprimir en que cuadrante se encuentra dicho punto (concepto matemático, primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)"""

class Punto():
    def __init__(self, x, y):
        self.x = x   # Coordenada X del punto en el pl
        self.y = y  #coordenada y
    def cuadrante(self):
        if self.x>0 and self.y>0:
            print("PRIMER")
        elif self.x<0 and self.y>0:
            print("SEGUNDO")
        elif self.x<0 and self.y<0:
            print("TERCER")
        elif self.x>0 and self.y<0:
            print("CUARTO")
        else:
            print("EJE")
#main
p1=Punto(0,0)    #(X,Y)
p1.cuadrante()
        