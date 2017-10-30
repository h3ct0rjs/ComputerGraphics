import pygame
from librerias.libreria2 import *
# Move an image using pygame
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ANCHO = 480
ALTO = 640

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ALTO, ANCHO])
    pygame.display.set_caption('Hector F', 'Spine Runtime')
    pantalla.fill(BLANCO)
    tux = pygame.image.load('librerias/img/tux.png')
    pp = tux.get_rect()
    backgroundimg = pygame.image.load('librerias/img/bg.jpg')
    pantalla.blit(tux, [200, 100])
    pygame.display.flip()
    fin = False
    y = 0
    flag = None
    reloj = pygame.time.Clock()
    posy, posx = 0, 0
    varx, vary = 0, 0

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    varx -= 3
                elif event.key == pygame.K_RIGHT:
                    varx += 3
                elif event.key == pygame.K_UP:
                    vary -= 3
                elif event.key == pygame.K_DOWN:
                    vary += 3
        posy += vary
        posx += varx
        pantalla.blit(backgroundimg, [0, 0])
        pantalla.blit(tux, [posx, posy])
        pygame.display.flip()

        reloj.tick(20)
