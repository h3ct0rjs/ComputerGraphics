import pygame
from libreriaobj import *
ALTO=400
ANCHO=600
if __name__== '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    #centro=[300,250]
    centro=[200,250]
    #Esto es un objeto una instancia de la clase, con valores definidos
    plano=Polar(ANCHO,ALTO,centro,pantalla)
    plano.Punto(50,45)
    plano.Recta(50,45)
    #s=[[80,20],[30,-40],[-40,50]]
    #Triangulo(pl,ls)#Le mando mi plano y una lista de puntos
    #ejes no necesita parametro porque solo tiene self
    #   pl.ejes()
    plano.Rose(150,5)

    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               fin=True
