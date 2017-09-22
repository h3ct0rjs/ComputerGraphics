#!/usr/bin/env python
# Drawing lines
import pygame
width = 350
height = 400
DIMENSION = (width, height)
#pygame.draw.line and pygame.draw.aaline
# Arguments
# screen,Color,point1,point2, wideline

d = pygame.display
screen = d.set_mode(DIMENSION)
caption = d.set_caption('Draw Lines:Animation 1 ')
y = 0
dir = 1
linecolor = 255, 0, 0
bgcolor = 0, 0, 23

running = True  # Flag to keep the while loop runing

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
        print('Game Over')
    screen.fill(bgcolor)
    pygame.draw.line(screen, linecolor, (0, y),(width-1, y),2)
    y+=dir
    if y == 0 or y == height-1 : dir *=-1
    d.flip()