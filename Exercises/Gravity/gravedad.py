import pygame
from random import randrange

# Contantes globales

# Colores
NEGRO = (0,   0,   0)
BLANCO = (255, 255, 255)
AZUL = (0,   0, 255)
ROJO = (255,   0,   0)
VERDE = (0, 255,   0)

# Dimensiones pantalla
ANCHO = 800
ALTO = 600


class Block(pygame.sprite.Sprite):

    def __init__(self, a, al):
        pygame.sprite.Sprite.__init__(self)
        ancho = 40
        alto = 60
        self.image = pygame.Surface([a, al])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()


class Jugador(pygame.sprite.Sprite):

    var_x = 0
    var_y = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ancho = 40
        alto = 60
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()

    def gravity(self):
        if self.rect.y >= ALTO - self.rect[3]:
            self.var_y = 0
        else:
            if self.var_y == 0:
                self.var_y = 1
            else:
                self.var_y += 0.35

    def update(self):
        self.gravity()
        self.rect.x += self.var_x
        self.rect.y += self.var_y

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption('Gravity Wizard                                                 \
                    @c1b3r')

    # Grupos
    general = pygame.sprite.Group()

    jugador = Jugador()
    bloques = pygame.sprite.Group()
    general.add(jugador)
    for i in range(4):
        b = Block(50, 15)
        b.rect.x = randrange(0, ANCHO)
        b.rect.y = randrange(300, ALTO - 30)
        bloques.add(b)
        general.add(b)

    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jugador.var_x = -5

                if event.key == pygame.K_RIGHT:
                    jugador.var_x = 5

                if event.key == pygame.K_SPACE:
                    jugador.rect.y = ALTO - jugador.rect.height - 1
                    jugador.var_y = -10

            if event.type == pygame.KEYUP:
                jugador.var_x = 0
        ls_col = pygame.sprite.spritecollide(jugador, bloques, False)
        print(ls_col)
        general.update()
        pantalla.fill(NEGRO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)
