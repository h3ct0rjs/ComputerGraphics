import pygame
from random import randrange
from src.core import *
if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    m = Recortar('img/sabanasprite.png')
    jp = Jugador(m)
    general = pygame.sprite.Group()
    general.add(jp)
    jp.rect.x = randrange(1, 300)
    jp.rect.y = randrange(1, 500)
    reloj = pygame.time.Clock()
    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.var_x = 5
                    jp.var_y = 0
                    jp.dir = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jp.var_y = -5
                    jp.var_x = 0
                    jp.dir = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    jp.var_y = 5
                    jp.var_x = 0
                    jp.dir = 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jp.var_x = -5
                    jp.var_y = 0
                    jp.dir = 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jp.var_y = 0
                    jp.var_x = 0
            if event.type == pygame.KEYUP:
                jp.var_y = 0
                jp.var_x = 0
            if event.type == pygame.QUIT:
                fin = True

        # Actualizacion pantalla
        general.update()
        pantalla.fill(NEGRO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
