#!/usr/bin/env python
# Drawing lines
import pygame

DIMENSION = (350, 400)
#pygame.draw.line and pygame.draw.aaline
# Arguments
# screen,Color,point1,point2, wideline

d = pygame.display
screen = d.set_mode(DIMENSION)
caption = d.set_caption('Draw Lines')

running = True  # Flag to keep the while loop runing

while running:
    supdate = d.flip()
    event = pygame.event.poll()
    # If you want to close it using the close icon, a trigger inside the
    # pygame
    if event.type == pygame.QUIT:
        running = False
        print('Game Over')
    blue = 0, 0, 255
    point1 = (350,0)
    for i in range(0,400,10):
        point2 = (0,i)
        pygame.draw.line(screen, blue, point1, point2, 1)