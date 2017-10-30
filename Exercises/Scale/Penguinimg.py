import pygame
from librerias.libreria2 import *

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ANCHO = 600
ALTO = 400

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption('Hector F', 'Spine Runtime')
    pantalla.fill(BLANCO)
    tux = pygame.image.load('img/tux.png')
    pantalla.blit(tux, [100, 100])
    pygame.display.flip()

    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
