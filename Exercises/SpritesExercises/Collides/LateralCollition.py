import pygame
import random
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

ANCHO = 600
ALTO = 400

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
        if self.rect.x  < 0 :
            self.var_x = 5 
        elif self.rect.x>ANCHO-self.image.get_rect()[2]:
            self.var_x = -5 
        self.rect.x += self.var_x

        self.rect.y += self.var_y


class Enemigo(pygame.sprite.Sprite):

    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an, al])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.var_x = -5
        self.var_y = 0

    def update(self):
        if self.rect.x  < 0 :
            self.var_x = 5 
        elif self.rect.x>ANCHO-self.image.get_rect()[2]:
            self.var_x = -5 
        self.rect.x += self.var_x

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(BLANCO)
    pygame.display.set_caption('Sprite')

    jugador = Player(50, 70)
    general = pygame.sprite.Group()
    general.add(jugador)
    rivales = pygame.sprite.Group()
    for i in range(20):
        r = Enemigo(15, 15)
        r.rect.x = random.randrange(10, ANCHO - 20)
        r.rect.y = random.randrange(10, ALTO - 20)
        rivales.add(r)
        general.add(r)
    jugador.rect.x = 50
    jugador.rect.y = 50
    reloj = pygame.time.Clock()
    general.draw(pantalla)
    ptos = 0
    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.var_x = 5
                    jugador.var_y = 0

                elif event.key == pygame.K_LEFT:
                    jugador.var_x = -5
                    jugador.var_y = 0

                elif event.key == pygame.K_UP:
                    jugador.var_y = -5
                    jugador.var_x = 0

                elif event.key == pygame.K_DOWN:
                    jugador.var_y = 5
                    jugador.var_x = 0

            if event.type == pygame.KEYUP:
                jugador.var_y = 0
                jugador.var_x = 0

            if event.type == pygame.QUIT:
                fin = True

            ls_col = pygame.sprite.spritecollide(jugador, rivales, True)
            for i in ls_col:
                ptos += 1
                print('{}'.format(ptos))

        jugador.update()
        rivales.update()
        pantalla.fill(BLANCO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
