import pygame
from math import cos, sin, radians
import copy

ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


class Plano(object):
    '''Plane 2d Class:
    Supported Methods:
    *ejes()
    *cart(pto)
    *punto((x,y))
    *linea(point1,point2), where point1 is the start point and point2 is the stop point
    Auxiliar Methods:
    *rotate
    '''
    ancho = 0
    alto = 0
    centro = []

    def __init__(self, an, al, cn, pn):
        '''Constructor
        an: ancho de pantalla
        al: alto de pantalla
        cn: centro
        pn: pantalla
        '''
        self.ancho = an
        self.alto = al
        self.centro = cn
        self.p = pn

    def ejes(self):
        cx = self.centro[0]
        cy = self.centro[1]
        pygame.draw.line(self.p, ROJO, [0, cy], [self.ancho, cy])
        pygame.draw.line(self.p, ROJO, [cx, 0], [cx, self.alto])

    def cart(self, pto):
        cx = self.centro[0]
        cy = self.centro[1]
        px = pto[0]
        py = pto[1]
        xp = int(cx + px)
        yp = int(cy - py)
        return [xp, yp]

    def punto(self, pos):
        pygame.draw.circle(self.p, ROJO, self.cart(pos), 2)

    def linea(self, pini, pfin):
        pygame.draw.line(self.p, NEGRO, self.cart(pini), self.cart(pfin))


def escalar(pto, s):
    x = pto[0] * s[0]
    y = pto[1] * s[1]
    return [x, y]


def rotar(pto, an):
    anr = radians(an)
    x = (pto[0] * cos(anr)) - (pto[1] * sin(anr))
    y = (pto[0] * sin(anr)) + (pto[1] * cos(anr))
    return [x, y]


def escalarPoligono(pto_list, s):
    ''' 
    Escala un poligono segun el primer punto de las lista que lo conforma
    '''
    pfijo = pto_list[0]
    pto_list2 = copy.deepcopy(pto_list)

    for i, j in enumerate(pto_list2):
        print(pfijo)
        pto_list2[i][0] = j[0] - pfijo[0]
        pto_list2[i][1] = j[1] - pfijo[1]
        pto_list2[i] = escalar(pto_list2[i], s)

    for i, j in enumerate(pto_list2):
        pto_list2[i][0] = j[0] + pfijo[0]
        pto_list2[i][1] = j[1] + pfijo[1]

    return pto_list2


def rotarPoligono(pto_list, an):
    pfijo = pto_list[0]
    pto_list2 = copy.deepcopy(pto_list)
    for i, j in enumerate(pto_list2):
        print(pfijo)
        pto_list2[i][0] = j[0] - pfijo[0]
        pto_list2[i][1] = j[1] - pfijo[1]
        pto_list2[i] = rotar(pto_list2[i], an)
    for i, j in enumerate(pto_list2):
        pto_list2[i][0] = j[0] + pfijo[0]
        pto_list2[i][1] = j[1] + pfijo[1]
    return pto_list2


class Polar(Plano):

    def Polar(self, r, angulo):
        angulor = radians(angulo)
        y = r * sin(angulor)
        x = r * cos(angulor)
        return (int(x), int(y))

    def Punto(self, r, an):
        """
        Sobre Escritura de Metodo
        """
        np = self.Polar(r, an)
        pygame.draw.circle(self.p, ROJO, self.Cart(np), 2)

    def Puntor(self, r, an):
        """
        Sobre Escritura de Metodo
        """
        np = self.Polar(r, an)
        pygame.draw.circle(self.p, ROJO, self.Cart(np), 2)

    def Recta(self, r, ang):
        np = self.Polar(r, ang)
        self.linea([0, 0], np)

    def Rose(self, a, k):
        '''Create a rose draw'''
        angle = 0.5
        for i in range(3600):
            self.Punto(a * cos(k * radians(i)), angle)
            angle += 1
        print('Done')
