#!/usr/bin/env python
# Draw a color bar
import pygame

width = 800
height = 600
DIMENSION = (width, height)
#pygame.draw.line and pygame.draw.aaline
# Arguments
# screen,Color,point1,point2, wideline
barheight = 124

d = pygame.display
screen = d.set_mode(DIMENSION)
caption = d.set_caption('Draw Lines:Animation 1 ')
y = 0
dir = 1
bgcolor = 56, 200, 32
barcolor =[]
for i in range(1, 63):
    barcolor.append((3,0,i*3))

for i in range(1, 63):
    barcolor.append((0,0,255-i*4))

running = True  # Flag to keep the while loop runing

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
        print('Game Over')
    screen.fill(bgcolor)
    for i in range(0, barheight):
        pygame.draw.aaline(screen, barcolor[i], (0,y+i), (799,y+i))
    
    y+=dir
    if y + barheight>599 or y <0:
        dir *=-1
    d.flip()