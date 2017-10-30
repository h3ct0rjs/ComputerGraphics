import pygame
from math import pi, cos, sin

'''
Forked from andbet
ToDo:
- Implement default var in the initializer
- Add basic validations
- Repair Docstrings according to pep008 and pep246
- set vars to english
- Understand math equations for translations,rotations, centering.
- Understand pygame methods for draw lines.
- Draw basic figures square, triangle, isometrics.

Homework:
- Scale a figure using a center as reference. x= cx + px
- take a line and rotate that line according to the keboard arrows.
- scale a figure using the keys.
- Ecuacion de la recta
- Encuentre el circuncentro medianas, mediatrix. 


'''

COLOR = {
    'ROJO':(255,0,0),
    'BLANCO':(255,255,255),
    'VERDE':(0,255,0),
    'AZUL':(0,0,255)

    }

class Plano(object):
    """docstring for Plano."""
    def __init__(self, ancho, alto, centro, pantalla):
        '''Constructor
        ancho: ancho de la pantalla
        alto:  alto de la pantalla
        centro: centro de la pantalla
        pantalla: pantalla en la que se dibujara
        '''
        self.centro = centro
        self.ALTO = alto
        self.ANCHO = ancho
        self.pantalla = pantalla
        self.ejes()

    def set_centro(self, centro):
        self.centro = centro

    def set_ancho(self, ancho):
        self.ancho = ancho

    def set_alto(self, alto):
        self.alto = alto

    def ejes(self):
        '''ejes(p,c) recibe la pantalla (p) y el centro (c)'''
        cx, cy = self.centro
        pygame.draw.line(self.pantalla, COLOR['AZUL'], [0, cy], [self.ANCHO, cy])
        pygame.draw.line(self.pantalla, COLOR['AZUL'], [cx, 0], [cx, self.ALTO])

    def Cart(self, pto, escala, rotacion):
        '''Pasar a cartesiano un punto en pantalla'''
        sx, sy = escala
        cx, cy = self.centro
        px, py = pto
        ## escalando
        px = px*sx
        py = py*sy
        ## rotando
        if rotacion != 0:
            rad = (rotacion*pi)/180
            npx = (px*cos(rad)) - (py*sin(rad))
            npy = (px*sin(rad)) + (py*cos(rad))
        else:
            npx = px
            npy = py
        ## tranladando
        nx = cx + int(npx)
        ny = cy - int(npy)
        return [nx, ny]

    def Punto(self, pos, escala=[1,1], rotacion=0):
        '''
        Dibujar un punto en pantalla
        '''
        npos = self.Cart(pos, escala, rotacion)
        pygame.draw.circle(self.pantalla, COLOR['ROJO'], npos, 2)

    def Linea(self, pti, ptf, escala=[1,1], rotacion=0):
        pi = self.Cart(pti, escala, rotacion)
        pf = self.Cart(ptf, escala, rotacion)
        pygame.draw.line(self.pantalla, COLOR['ROJO'], pi, pf)

    def Triangulo(self, lsp, escala=[1,1], rotacion=0):
        ## El ultimo parametro indica el grosor de la linea
        for p in lsp:
            self.Punto(p, escala, rotacion)
        p1, p2, p3 = lsp
        np1 = self.Cart(p1, escala, rotacion)
        np2 = self.Cart(p2, escala, rotacion)
        np3 = self.Cart(p3, escala, rotacion)
        nlsp = [np1, np2, np3]
        pygame.draw.polygon(self.pantalla, COLOR['ROJO'], nlsp, 1)
    

## ejemplo
ANCHO = 600
ALTO = 400
if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(COLOR['BLANCO'])
    centro = [100, 300]

    pl = Plano(ANCHO, ALTO, centro, pantalla)

    pl.ejes()
    ## pl.Punto([20, -30])

    lsp = [[20, 10], [50, 10], [50, 30]]
    pl.Triangulo(lsp) ## triangulo rotacion 0° y escala normal
    pl.Triangulo(lsp, escala=[2,2]) ## sin rotacion escalado a 2
    pl.Triangulo(lsp, rotacion=90) ## triangulo rotado 90° sin escala
    pl.Triangulo(lsp, escala=[2,2], rotacion=90) ## escalado a 2 y rotado 90°

    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
