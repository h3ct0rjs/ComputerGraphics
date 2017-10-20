import pygame
#from libreriacls import*
import random
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

ANCHO = 600
ALTO = 400


class Proyectil(pygame.sprite.Sprite):
    '''
    Enemy Class:
        Implements all the methods over the enemy's 
    '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15, 50])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.var_y = -5

    def update(self):
      # print('Varianza : ({}, {}) Poscion:({},{})'.format
        self.rect.y += self.var_y

class Jugador(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(BLANCO)
        self.rect=self.image.get_rect()
        self.var_x=0
        #self.var_y=0

    def update(self):
        self.rect.x+=self.var_x
        if (self.rect.x <= 0):
            self.var_x ==0

class Rival(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.ancho=an
        self.alto=al
        self.image=pygame.Surface([an,al])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.y=-30
        self.var_x=0
        self.var_y=5
        self.temporizador=random.randrange(100)

    def update(self):
        if (self.temporizador > 0):
            self.temporizador-=1
        else:
            self.rect.y+=self.var_y
        if (self.rect.y > 430):
            self.remove(rivales)
            self.remove(general)




if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    jugador=Jugador(50,70)
    general=pygame.sprite.Group()
    balas = pygame.sprite.Group()
    general.add(jugador)
    jugador.rect.x=310
    jugador.rect.y=360

    rivales=pygame.sprite.Group()
    n=10
    for i in range(n):
        r=Rival(20,20)
        r.rect.x=random.randrange(10,ANCHO-20)
        #r.rect.y=random.randrange(-10,ALTO-20)
        rivales.add(r)
        general.add(r)

    fuente=pygame.font.Font(None,52)
    ptos=0
    fin_juego=False
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.var_x=5
                    #jugador.var_y=0
            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_UP:
            #        jugador.var_y=-5
            #        jugador.var_x=0
            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_DOWN:
            #        jugador.var_y=5
            #        jugador.var_x=0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jugador.var_x=-5
                    #jugador.var_y=0
                
                if event.key == pygame.K_SPACE:
                    b = Proyectil()
                    b.rect.x = jugador.rect.x
                    b.rect.y = jugador.rect.y
                    balas.add(b)
                    general.add(b)

            if event.type == pygame.KEYUP:
                #jugador.var_y=0
                jugador.var_x=0
            if event.type == pygame.QUIT:
                fin=True



        #Gestion de colision
        ls_col=pygame.sprite.spritecollide(jugador, rivales, True)
        for elemento in ls_col:
            ptos+=1
            #print ptos
            general.update()
        if ptos>0:
            fin_juego=True

        #Actualizacion pantalla
        #if not fin_juego:
        general.update()
        pantalla.fill(AZUL)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
    #else:
         #   texto=fuente.render("JUEGO TERMINADO",True,BLANCO)
         #   pantalla.fill(NEGRO)
         #   pantalla.blit(texto,[150,220])
         #   pygame.display.flip()

        '''
        Mover IZQ DER jugador
        Rv cayendo
        Condicion derrota: Choque -1 vida
        '''
