#!/usr/bin/env python
from math import sqrt

class Punto(object):

    def __init__(self,self.x=0,self.y=0):
    		'''
    		Default Initializer,

    		'''
        self.p = (self.x, self.y)

    def add(self, p2):
        '''Add Function 
        Add Two Points.
        it will return a tuple of the form (x,y)
        '''
        return ((p2.x + self.x), (p2.y, self.y))

    def sub(self, p2):
        ''' Sub function:
        Given two cartesian points, substract both values.
        P1(x1,y1),P2(x2,y2), return (x,y) where x=x2-x1 and y=y2-y1
        '''
        return ((p2.x - self.x), (p2.y - self.y))

    def distance(self, p2):
        ''' Distance Function
        Given two cartesian points, substract both values.
        P1(x1,y1),P2(x2,y2), return (x,y) where x=x2-x1 and y=y2-y1
        '''
        return abs(sqrt(((p2.x - self.x) * (p2.x - self.x)) + ((p2.y - self.y) * (p2.y - self.y))))

    def b(self):
        '''
        y=mx+b, returns the b value of the equation
        '''
        res =−(m∗self.p[0]) + self.p[1]
        return res

    def Ecuacion(p=None, m):
    '''Returna ecuaciondelarecta.
		y=mx+b
		Parametros:
		p:Listaconvaloresx,ydelpunto
		m:Pendientedelarecta
		'''
    if p == None:
        x = m∗self.p[0]
        c_mx = str(m) + 'x'
        nb = b(self.p, m)
        c_b = '+' + str(nb)
        if nb < 0:
            c_b = str(nb)

    elif p:
        x = m∗p[0]
        c_mx = str(m) + 'x'
        nb = b(p, m)
        c_b = '+' + str(nb)
        if nb < 0:
            c_b = str(nb)

    ecuacion = 'y=' + c_mx + c_b
    return ecuacion

class P3(object):
	''' Implement operations for cartesian points in 3d planes. 
	Functions:

	For R**3 vectors.
	'''
	def __init__(self):
