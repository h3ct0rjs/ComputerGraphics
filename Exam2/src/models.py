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

class Enemy(pygame.sprite.Sprite):
    pass 