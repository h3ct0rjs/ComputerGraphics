import pygame
from src.core import *
from src.util import *


def logic():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    # Font
    fuente = pygame.font.Font('static/fonts/pizza.ttf', 52)
    fuente2 = pygame.font.Font('static/fonts/pizza.ttf', 30)
    pygame.display.set_caption(
        'Gravity Wizard                                         @c1b3r')
    backgroundimg = pygame.image.load('static/img/backgrounds/background.gif')

    m = Cut('static/img/characters/ken.png', 10, 7)
    player = Jugador(m)
    player.rect.y = int(ALTO)
    # Move the Player piece to the pos x, pos y
    player.rect.x = 60
    player.rect.y = int((ALTO - 10) / 1.2)

    #Creates a Block s
    block = Blocks(80, 20)    
    # Move the block piece to the pos x, pos y
    block.rect.x = int((ANCHO - 20) / 2)
    block.rect.y = int((ALTO) / 1.2)

    # Groups : Actions, Creations
    general = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    blocks.add(block)

    general.add(player)
    # Settings Default values
    pointst = int(0)  # debug
    salud = int(500)
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
                    player.var_y = 0
                    player.dir = 1  # Matriz image direction

                if event.key == pygame.K_LEFT:
                    player.var_x = -5
                    player.var_y = 0
                    player.dir = 3

                if event.key == pygame.K_UP:
                    player.var_y = -5
                    player.var_x = 0
                    player.dir = 2

                if event.key == pygame.K_DOWN:
                    player.var_y = 5
                    player.var_x = 0
                    player.dir = 7

                if event.key == pygame.K_SPACE:  # Jump
                    player.rect.y = ALTO - player.rect.height - 1
                    player.var_y = -15
            if event.type == pygame.QUIT:
                fin = True

        if not fin_juego:
            pantalla.fill(NEGRO)
            pantalla.blit(backgroundimg, [0, 0])
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
            blocks.draw(pantalla)
            player.update()
            general.draw(pantalla)
    
            pygame.display.flip()
        else:
            pantalla.fill(NEGRO)
            texto3 = fuente.render("Game Over", True, BLANCO)
            pantalla.blit(texto3, [200, 220])
            pygame.display.flip()

        reloj.tick(10)
