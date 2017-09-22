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
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
        print('Game Over')
    elif event.type == pygame.MOUSEMOTION:
        print('Mouse in pos: {} at: {}'.format(type(event.pos), event.pos))
        x, y = event.pos
# print(pygame.event.pump())     #This is a event queue handle by the
# pygame handler
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 12), (330, 21))
    d.flip()
    #clock.tick(7)               # refresh display 
