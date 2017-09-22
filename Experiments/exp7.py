#!/usr/bin/env python
# Mouse Motion Events
import pygame
width = 400
height = 300
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
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print('Mouse in pos: {} at: {}'.format(type(event.pos),event.pos))
#print(pygame.event.pump())     #This is a event queue handle by the pygame handler
    screen.fill((0,0,0))
    d.flip()