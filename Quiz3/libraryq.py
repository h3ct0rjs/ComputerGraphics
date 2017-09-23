import pygame
from math import cos, sin, radians, sqrt
import copy
from sys import exit
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


class Plano(object):
    def __init__(self, an, al, cn, pn):
        self.ancho = an
        self.alto = al
        self.centro = cn
        self.p = pn
        self.ejes()

    def ejes(self):
        cx = self.centro[0]
        cy = self.centro[1]
        pygame.draw.line(self.p, AZUL, [0, cy], [self.ancho, cy])
        pygame.draw.line(self.p, AZUL, [cx, 0], [cx, self.alto])


    def punto(self, pos):
        pygame.draw.circle(self.p, ROJO, pos, 2)

    def linea(self, pini, pfin):
        pygame.draw.line(self.p, NEGRO, pini, pfin)

    def distance(self, pto1, pto2):
        return sqrt(((pto2[0]-pto1[0])*(pto2[0]-pto1[0]))+ ((pto2[1]-pto1[1])*(pto2[1]-pto1[1])))

    def triangulo(self, lst):
        for i in lst:
            self.punto(i)

        self.linea(lst[0], lst[1])
        self.linea(lst[1], lst[2])
        self.linea(lst[2], lst[0])
        ladoA = self.distance(lst[0],lst[1])
        ladoB = self.distance(lst[1],lst[2])
        ladoC = self.distance(lst[2],lst[0])
        perimetro =ladoA +ladoB+ ladoC        
        print('El perimetro del Triangulo es: {}\n Coordenadas Puntos A:{} B:{} C:{} \nLongitudes: {} {} {}'.format(
            round(perimetro,2), lst[0], lst[1], lst[2], round(ladoA,2), round(ladoB,2), round(ladoC,2)))