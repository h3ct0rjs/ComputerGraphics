'''Task:
Given three input points from the mouse input, build a triangle. 
Show the len of each side and then  the perimeter.
Original Excerpt

    1) Seleccionar tres puntos en la pantalla con el raton, y construir un triangulo.
    2) Mostrar la longitud de cada lado y el perimetro del triangulo'''
import pygame
from libraryq import *
ALTO, ANCHO = 400, 600
DIMENSION = (ANCHO, ALTO)

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode(DIMENSION)
    pygame.display.set_caption( 'Triangulito Hector F. Jimenez, El render Fallo :(')
    pantalla.fill(BLANCO)
    centro = [int(ANCHO / 2), int(ALTO / 2)]
    plano = Plano(ANCHO, ALTO, centro, pantalla)
    pygame.display.flip()
    fin = False
    done = False
    ptos = []                                               # We hold three points
    while not fin:
        counter = 1
        while counter <= 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin = True                              # ends outer while
                    counter = 4                             # quits the  inner while
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if len(ptos) == 3:
                        counter = 10000
                        break                               # quits the  inner while
                    tmp = pygame.mouse.get_pos()
                    ptos.append(tmp)
                    counter += 1
                    print('Puntos Capturados: {}'.format(ptos))  # debug
        if not done :
            if len(ptos) == 3:
                print('\n')
                plano.triangulo(ptos)
            print('\n[Ok]Done')
            pygame.display.flip()
            done = True
        else:
            pass

