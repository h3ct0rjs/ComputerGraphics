from src.util import *
from src.core import *

def main():
    logic()
if __name__ == '__main__':
    banner()
    print('\n{}Iniciando Simulacion Grafica'.format(ok))
    try :
        main()
        print('{}Game Over, Simulacion Terminada'.format(ok))
    except:
        print('{}No pudo Cargar la Funcion Principal'.format(warning))
    print('{}GOD BYE!'.format(ok))