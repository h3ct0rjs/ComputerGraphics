import configparser as ConfigParser
from src.utils import *
from pprint import pprint


def main():
    interprete = ConfigParser.ConfigParser()
    interprete.read('mapa.map')
    d = dict()
    for s in interprete.sections():
        descripcion = dict(interprete.items(s))
        d[s] = descripcion

    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    matrix = Cut(d['nivel1']['origen'], 12, 32)
    print(list(d['nivel1']['mapa']))
    nl = []
    for i in list(d['nivel1']['mapa']):
        if i is '.':
            nl.append(matrix[16][0])
        elif i is '\n':
            nl.append('\n')
        elif i is '$':
            nl.append(matrix[31][0])
    
    #d['nivel1']['mapa'] = nl
    print('------------------')
    pprint(d['nivel1'])  # debug
    for i in d['nivel1']['mapa']:
        for j in i:
            print(i)
            pantalla.blit(nl[i], [i * 32, j * 32])

    """for i in range(int(ANCHO / 32)):
        for j in range(int(ALTO / 32)):
            pantalla.blit(matrix[16][0], [i * 32, j * 32])
    """

    pygame.display.flip()
    input()


if __name__ == '__main__':
    main()
    