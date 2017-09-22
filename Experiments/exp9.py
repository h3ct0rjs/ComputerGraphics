#!/usr/bin/env python
# Mouse Motion Events
import pygame
pygame.init()

clock = pygame.time.Clock()
width = 400
height = 300

# Definir algunos colores
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)

DIMENSION = (width, height)
#pygame.draw.line and pygame.draw.aaline
# Arguments
# screen,Color,point1,point2, wideline
d = pygame.display
screen = d.set_mode(DIMENSION)
caption = d.set_caption('Mouse Events ')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print('Game Over, Quiting...')
        elif event.type == pygame.KEYDOWN:
            print('Tecla Abajo')
        else:
            d.flip()