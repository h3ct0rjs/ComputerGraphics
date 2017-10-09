import pygame
from random import randrange
from copy import deepcopy

ALTO = 500
ANCHO = 500

ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
VERDE = (10, 255, 10)
AMARILLO = (100, 255, 100)


class Jugador(pygame.sprite.Sprite):

    def __init__(self, an, al):
        """
        Initializer
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an, al])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.y = ALTO - self.rect.height
        self.var_x = 0

    def update(self):
        """
        Update the relative position for the player
        Set limits to stay in the same screen size in x position
        """
        if self.rect.x < 0:
            self.var_x = 5
        elif self.rect.x > ANCHO - self.image.get_rect()[2]:
            self.var_x = -5
        self.rect.x += self.var_x


class Rival(pygame.sprite.Sprite):
    """
    Proyectil Initializer
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

        # emulate a timeless functions, this will simulate different times
        # from top to down

        self.temporizador = randrange(1000)

        self.level = 1          # by default we start with a low speed
        self

    def update(self):
        if self.temporizador > 0:
            self.temporizador -= 1
        # State Machine
        # Update Present Enemy State,  Changes
        #self.actual_state = deepcopy(lista)

        
        #past_state =deepcopy(self.actual_state)
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
    

def logic():
    pygame.init()
    #pygame.mixer.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(NEGRO)
    pygame.display.set_caption('Chromium Clone                                                 \
        @c1b3r')
    player = Jugador(50, 15)

    # Move the Player piece to the pos x, pos y
    player.rect.x = int((ANCHO - 70) / 2)
    player.rect.y = int((ALTO - 20) / 1.2)

    # Groups : Actions, Creations
    general = pygame.sprite.Group()
    rivales = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    general.add(player)

    # Bullets Group
    ls_col = pygame.sprite.Group()

    # Font
    fuente = pygame.font.Font('static/fonts/pizza.ttf', 52)
    fuente2 = pygame.font.Font('static/fonts/pizza.ttf', 30)

    # Settings Default values
    points = 0
    pointst = int(0)  # debug
    salud = int(500)

    # Create a list of enemies
    for i in range(10):
        r = Rival(20, 20)
        r.rect.x = randrange(0, ANCHO - 15)
        r.rect.y = -20
        rivales.add(r)
        general.add(r)

    # Clock and display refresh
    reloj = pygame.time.Clock()
    pygame.display.flip()

    # flag for end of Game
    fin = False
    fin_juego = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.var_x = 5
                    player.var_y

                if event.key == pygame.K_LEFT:
                    player.var_x = -5

                if event.key == pygame.K_SPACE:
                    b = Proyectil()
                    b.rect.x = player.rect.x + \
                        int(player.rect.width / 2) - int(b.rect.width / 2)
                    b.rect.y = player.rect.y
                    balas.add(b)
                    general.add(b)

            if event.type == pygame.KEYUP:
                player.var_y = 0
                player.var_x = 0

            if event.type == pygame.QUIT:
                fin = True

        if not fin_juego:
            for b in balas:
                ls_col = pygame.sprite.spritecollide(b, rivales, True)
                for e in ls_col:
                    points += 1
                    rivales.remove(e)
                    pointst += 5
                    balas.remove(b)
                    general.remove(b)

            if len(rivales) < 16:
                for i in range(40):
                    r = Rival(20, 20)
                    r.rect.x = randrange(0, ANCHO - 15)
                    r.rect.y = -20
                    rivales.add(r)
                    general.add(r)

            pantalla.fill(NEGRO)
            # Text Data
            if salud is 0:
                fin_juego = True
                texto2 = fuente2.render("Salud :" + str(salud), True, ROJO)
            elif salud >= 5 and salud <= 10:
                texto2 = fuente2.render("Salud :" + str(salud), True, AMARILLO)
            else:
                texto2 = fuente2.render("Salud :" + str(salud), True, VERDE)
            texto = fuente2.render("Puntos:" + str(pointst), True, ROJO)
            pantalla.blit(texto, [20, 450])
            pantalla.blit(texto2, [(ANCHO - 20 * 4.2), 450])

            general.update()
            #print('Cantidad Rivales Actual {}'.format(len(rivales)))  # debug
            rivales.update()

            general.draw(pantalla)
            pygame.display.flip()

            for r in rivales:
                #print(r.rect.y)
                if r.rect.y - 5 > player.rect.y:
                    salud -= 10
                    rivales.remove(r)
                    general.remove(r)
        else:
            pantalla.fill(NEGRO)
            texto3 = fuente.render("Game Over", True, BLANCO)
            pantalla.blit(texto3, [200, 220])
            pygame.display.flip()

        reloj.tick(60)
