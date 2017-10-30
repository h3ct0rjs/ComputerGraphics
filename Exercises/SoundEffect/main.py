import pygame

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

    def update(self):
        self.rect.x += self.var_x
        self.rect.y += self.var_y

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption("Juego basico")

    # Grupos
    general = pygame.sprite.Group()

    jp = Jugador()
    general.add(jp)
    s = pygame.mixer.Sound('static/disparo.ogg')
    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jp.var_x = -5
                    jp.var_y = 0
                if event.key == pygame.K_RIGHT:
                    jp.var_x = 5
                    jp.var_y = 0
                if event.key == pygame.K_UP:
                    jp.var_x = 0
                    jp.var_y = -5
                if event.key == pygame.K_DOWN:
                    jp.var_x = 0
                    jp.var_y = 5
                    s.play()

        general.update()

        pantalla.fill(NEGRO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
