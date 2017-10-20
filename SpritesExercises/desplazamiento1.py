import pygame

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

ANCHO = 600
ALTO = 400


class Bloque(pygame.sprite.Sprite):

    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an, al])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(BLANCO)
    pygame.display.set_caption('Sprite')

    block = Bloque(50, 70)
    general = pygame.sprite.Group()
    general.add(block)

    block.rect.x = 100
    block.rect.y = 100
    reloj = pygame.time.Clock()
    general.draw(pantalla)

    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        block.rect.x += 5
        pantalla.fill(BLANCO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)

