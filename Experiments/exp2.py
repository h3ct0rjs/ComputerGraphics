#!/usr/bin/env python
# Basic Window Creation, Display Properties
# this experiment add code to learn more about window events
import pygame
DIMENSION = (350, 400)
# scr = pygame.display.set_mode(DIMENSION)  #Default Dimension is the same
# as my main XWindow
d = pygame.display
screen = d.set_mode(DIMENSION)
caption = d.set_caption('Josh the man')

running = True  # Flag to keep the while loop runing

while running:
    event = pygame.event.poll()
    # If you want to close it using the close icon, a trigger inside the
    # pygame
    if event.type == pygame.QUIT:
        running = False
        print('Good Bye')    
