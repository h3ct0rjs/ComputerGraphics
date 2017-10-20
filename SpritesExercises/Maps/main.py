import pygame
from src.core import *
from src.util import *
from math import ceil
ALTO = 600
ANCHO = 600
#Tareas, Bresenham

def main():
    pygame.init()
    print('{} Iniciando Simulacion Grafica'.format(ok))
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(NEGRO)
    imagen = pygame.image.load('fondos/terrenogen.png').convert()
    ancho_img, alto_img = imagen.get_size()
    sp_fila = 12    #altura/n
    sp_col = 32  # ancho/n
    Matrix = [[0 for x in range(sp_col)]
              for y in range(int(sp_fila))]
    
    #print(Matrix[0])       #debug

    print('{}{}MetaInformacion{} Ancho:{}x Alto:{}'.format(
        bold, white, reset, ancho_img, alto_img))
    
    for i in range(sp_fila):
        for j in range(sp_col):
            cuadro = ((j*32),(i*32), int(ancho_img/sp_col), int(alto_img/sp_fila))
            recorte = imagen.subsurface(cuadro)
            dir(recorte)
            Matrix[i][j] = recorte

    #test 
    for i in range(int(ANCHO/32)):
        for j in range(int(ALTO/32)):
            pantalla.blit(Matrix[11][15], [i*32, j*32])

    
    pygame.display.flip()
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

if __name__ == '__main__':
    main()
    print('{} DONE'.format(ok))
        
