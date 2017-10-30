
import pygame
# CONSTANT VALUES
ALTO = 480
ANCHO = 640
NEGRO = (0, 0, 0)


class Jugador(pygame.sprite.Sprite):

    def __init__(self, m):
        pygame.sprite.Sprite.__init__(self)
        self.m = m
        self.dir = 0
        self.image = self.m[0][self.dir]
        self.rect = self.image.get_rect()
        self.x = 0
        self.var_x = 0
        self.var_y = 0

    def update(self):
        if self.x < 2:
            self.x += 1
        else:
            self.x = 0
        self.image = self.m[self.x][self.dir]
        self.rect.x += self.var_x
        self.rect.y += self.var_y


def Recortar(archivo):
    imagen = pygame.image.load(archivo).convert_alpha()
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
