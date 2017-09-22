import pygame
from libreria import *

if __name__== '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    pantalla.fill(BLANCO)

    #centro=[300,250]
    centro=[200,250]
    ejes(pantalla,centro)
    Punto(pantalla,cart([10,10],centro))#Devuelve un valor en pantalla respecto al centro
    pygame.display.flip()


    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               fin=True
