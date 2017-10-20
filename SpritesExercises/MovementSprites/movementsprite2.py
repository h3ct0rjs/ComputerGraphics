#TAREA Bresenham , DDA
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
    # print(m)
    jp = Jugador(m)
    general = pygame.sprite.Group()
    general.add(jp)
    jp.rect.x = randrange(50, 300)
    jp.rect.y = randrange(50, 500)
    reloj = pygame.time.Clock()
    fin = False
    ptos = []                                               # We hold three points
    while not fin:
        counter = 0
        while counter < 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin = True                              # ends outer while
                    counter = 3                             # quits the  inner while
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if len(ptos) == 2:
                        counter = 10000
                        break                               # quits the  inner while
                    tmp = pygame.mouse.get_pos()
                    ptos.append(tmp)
                    counter += 1
                    print('Puntos Capturados: {}'.format(ptos[0][0]))  # debug
        print(ptos)
        x=[(x,y),(x2, y2)]
        x[0][1]



        # Actualizacion pantalla
        general.update()
        pantalla.fill(NEGRO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
