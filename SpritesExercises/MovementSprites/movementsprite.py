import pygame
from random import randrange
ALTO = 480
ANCHO = 640
NEGRO = (0, 0, 0)


def Recortar(archivo):
    imagen = pygame.image.load('img/sabanasprite.png').convert_alpha()
    ancho_img, alto_img = imagen.get_size()
    sp_fil = 8
    sp_col = 9
    an_corte = ancho_img / sp_col
    al_corte = alto_img / sp_fil
    #print(al_corte, an_corte)
    matriz = []
    for i in range(sp_col):
        # se desplaza en columnas
        fila = []
        for j in range(sp_fil):
            # posicion en x, posdicion en y ,cuadro recorteancho,corte en alto
            cuadro = ((i * an_corte), (j * al_corte), an_corte, al_corte)
            fila.append(imagen.subsurface(cuadro))
        matriz.append(fila)
    return matriz


class Jugador(pygame.sprite.Sprite):

    def __init__(self, m):
        pygame.sprite.Sprite.__init__(self)
        self.m = m
        self.dir = 0
        self.image = m[0][self.dir]
        self.rect = self.image.get_rect()
        self.x = 0
        self.var_x = 0
        self.var_y = 0

    def update(self):
        if self.x < 2:
            self.x += 1
        else:
            self.x = 0
        self.image = m[self.x][self.dir]
        self.rect.x += self.var_x
        self.rect.y += self.var_y


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    m = Recortar('img/sabanasprite.png')
    print(m)
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
