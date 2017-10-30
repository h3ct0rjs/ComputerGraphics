import pygame
import random
from src.libreria2 import *

class Player(pygame.sprite.Sprite):

    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.__an = an
        self.__al = al
        self.image = pygame.Surface([an, al])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.var_x = 0
        self.var_y = 0

    def update(self):
        if self.rect.x < 0:
            self.var_x = 5
        elif self.rect.x > ANCHO - self.image.get_rect()[2]:
            self.var_x = -5
        self.rect.x += self.var_x


class Enemigo(pygame.sprite.Sprite):
    '''
    Enemy Class:
        Implements all the methods over the enemy's 
    '''

    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an, al])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.y = -30
        self.var_x = 0
        self.var_y = 2
        self.timer = random.randrange(100)

    def update(self, lista, general):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.rect.y += self.var_y
        if (self.rect.y > (ALTO - 60)):
            self.remove(lista)
            self.remove(general)
        # print('Varianza : ({}, {}) Poscion:({},{})'.format(
        # self.var_x, self.var_y, self.rect.x, self.rect.y))


def main():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(BLANCO)
    pygame.display.set_caption('Square Invaders')
    jugador = Player(50, 70)
    general = pygame.sprite.Group()
    general.add(jugador)
    rivales = pygame.sprite.Group()
    for i in range(20):
        r = Enemigo(15, 15)
        r.rect.x = random.randrange(10, ANCHO - 20)
        #r.rect.y = random.randrange(10, ALTO - 20)
        rivales.add(r)
        general.add(r)
    jugador.rect.x = 50
    jugador.rect.y = (ALTO - 60 * 2)
    reloj = pygame.time.Clock()
    general.draw(pantalla)
    ptos = 0
    fuente = pygame.font.Font(None, 36)
    fin = False
    fin_juego = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.var_x = 5
                    jugador.var_y = 0

                elif event.key == pygame.K_LEFT:
                    jugador.var_x = -5
                    jugador.var_y = 0

            if event.type == pygame.QUIT:
                fin = True
        # gestion de colision
        ls_col = pygame.sprite.spritecollide(jugador, rivales, True)
        for i in ls_col:
            ptos += 1
        if ptos < 0:
            fin_juego = True

        if(fin_juego):
            pantalla.fill(NEGRO)

        jugador.update()
        rivales.update(rivales, general)
        pantalla.fill(BLANCO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)

        if len(rivales) < 20:
            for i in range(20):
                r = Enemigo(15, 15)
                r.rect.x = random.randrange(10, ANCHO - 20)
                #r.rect.y = random.randrange(10, ALTO - 20)
                rivales.add(r)
                general.add(r)

if __name__ == '__main__':
    main()
