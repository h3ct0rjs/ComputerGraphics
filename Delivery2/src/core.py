import pygame
from random import randrange
from src.util import *


class Jugador(pygame.sprite.Sprite):
    """
    Player Class
    """

    def __init__(self, m):
        """
        Initializer
        """
        pygame.sprite.Sprite.__init__(self)
        self.m = m
        self.dir = 0
        self.image = self.m[0][self.dir]
        self.rect = self.image.get_rect()
        self.x = 0
        self.var_x = 0
        self.var_y = 0


    def update(self, collidable):
        """
        Update the relative position for the player
        Set limits to stay in the same screen size in x position
        """
        
        # Lateral Limits
        if self.rect.x < 0:
            self.var_x = 5
        elif self.rect.x > ANCHO - self.image.get_rect()[2]:
            self.var_x = -5

        # Vertical Limits
        if self.rect.y < 0:
            self.var_y = 5
        if self.rect.y > ALTO - 40:
            self.var_y = -5

        self.gravity()
        self.rect.x += self.var_x

        self.rect.y += self.var_y

        if self.x < 2:
            self.x += 1
        else:
            self.x = 0

        self.image = self.m[self.x][self.dir]
        
    def gravity(self):
        if self.rect.y >= ALTO - self.rect[3]:
            self.var_y = 0
        else:
            if self.var_y == 0:
                self.var_y = 1
            else:
                self.var_y += 0.4 #  If this value goes up the jump is lower.


class Blocks(pygame.sprite.Sprite):
    """
    Building Blocks Class
    """

    def __init__(self, an, al):
        """
        Initializer for creating the blocks
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an, al])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.y = ALTO - self.rect.height
        self.var_x = 0
        self.var_y = 0


class Rival(pygame.sprite.Sprite):
    """
    Enemy Initializer
        it will create a delay to simulate randomness, 
        it will appear in different times 
    """

    def __init__(self, an, al):
        __CRANDOM = (randrange(255), randrange(255), randrange(255))
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an, al])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()   # a 4 tuple sizex,sizey, posx, posy
        self.var_x = 0
        self.var_y = 1  # control the enemy speed
        self.actual_state = []
        self.past_state = []
        self.temporizador = randrange(1000)
        self.level = 1          # by default we start with a low speed

    def update(self):
        if self.temporizador > 0:
            self.temporizador -= 1
        else:
            self.rect.y += self.var_y

    def level(self, level):
        """
        Normally it will  return a None datatype
        """
        self.level = level


class Proyectil(pygame.sprite.Sprite):

    def __init__(self):
        """
        Proyectil Initializer
        """
        _CRANDOM = (randrange(255), randrange(255), randrange(255))
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([4, 20])
        self.image.fill(_CRANDOM)
        self.rect = self.image.get_rect()
        self.var_y = -5

    def update(self):
        """
        Update the relative position for Proyectil
        """
        self.rect.y += self.var_y
