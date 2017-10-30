'''
Utilities for Computer Graphics, Howework 2
'''
from random import randint
import pygame
# CONSTANT VALUES
# SCREEN CONFIG
ALTO = 500
ANCHO = 500

# COLOR SET
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
VERDE = (10, 255, 10)
AMARILLO = (100, 255, 100)

# Set of colors in order to check status in the terminal
reset = '\x1b[0m'    # reset all colors to white on black
bold = '\x1b[1m'     # enable bold text
uline = '\x1b[4m'    # enable underlined text
nobold = '\x1b[22m'  # disable bold text
nouline = '\x1b[24m'  # disable underlined text
red = '\x1b[31m'     # red text
green = '\x1b[32m'   # green text
blue = '\x1b[34m'    # blue text
cyan = '\x1b[36m'    # cyan text
white = '\x1b[37m'   # white text (use reset unless it's only temporary)
yellow = '\x1b[33m'

# Indicators
warning = '{}[✘✘✘]{}'.format(red, reset)
info = '{}[!!!]{}'.format(yellow, reset)
ok = '{}[OK✓]{}'.format(cyan, reset)

# Basic Version Info.
version__ = '{}0.3v{}'.format(cyan, reset)
authors = '{}{}\tHéctor F. Jimenez S'.format(bold, red, reset)
emails = '{}hfjimenez@utp.edu.co{}'.format(white, reset)
topic = '{}{}\n\t\tUTP:Compugrafica 2017-2{}'.format(uline, white, reset)
# Banners
l_art = [
    """{}
         ▌ ▐·▄▄▄ . ▐ ▄       • ▌ ▄ ·. 
        ▪█·█▌▀▄.▀·•█▌▐█▪     ·██ ▐███▪{}
        ▐█▐█•▐▀▀▪▄▐█▐▐▌ ▄█▀▄ ▐█ ▌▐▌▐█·{}
         ███ ▐█▄▄▌██▐█▌▐█▌.▐▌██ ██▌▐█▌
        . ▀   ▀▀▀ ▀▀ █▪ ▀█▄▀▪▀▀  █▪▀▀
    {}""".format(yellow, blue, red, reset),
    """{}      ||   / /                                      
      ||  / /  ___       __      ___      _   __    
      || / / //___) ) //   ) ) //   ) ) // ) )  ) ) {}
      ||/ / //       //   / / //   / / // / /  / /  {}
      |  / ((____   //   / / ((___/ / // / /  / / {} {}""".format(yellow, blue, red, version__ , reset),

]


def banner():
    art = l_art[randint(0, len(l_art) - 1)]
    print('{}\n{}, {}{}'.format(art, authors, emails, topic))


# Extra Functions
def Cut(fileimg,spritefilas,spritecols):
    imagen = pygame.image.load(fileimg).convert_alpha()
    ancho_img, alto_img = imagen.get_size()
    sp_fil = spritefilas
    sp_col = spritecols
    an_corte = ancho_img / sp_col
    al_corte = alto_img / sp_fil
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
