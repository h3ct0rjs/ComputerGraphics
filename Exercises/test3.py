import pygame
from libreria2 import *

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ANCHO = 600
ALTO = 400


def triangulo(plano, ptos):
    for p in ptos:
        plano.punto(p)

    plano.linea(ptos[0],ptos[1])
    plano.linea(ptos[1],ptos[2])
    plano.linea(ptos[2],ptos[0])


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption('Hector F', 'Spine Runtime')
    pantalla.fill(BLANCO)
    centro = [200,250]

    pl = Plano(ANCHO, ALTO, centro, pantalla)
    pl.ejes()

    tript = [[20,20],[100,20],[100,100]]
    triEs = escalarPoligono(tript, [2,2])
    triangulo(pl, triEs)
    triRot = rotarPoligono(triEs, 90)
    triangulo(pl, triRot)

    pygame.display.flip()
    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
