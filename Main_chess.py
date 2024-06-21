from Piezas import *
from Rey import *


def main():
    rey1 = rey('Negro', 'no movida') 
    print(rey1.color, rey1.estado, rey1.capturada, rey1.posiciones)  


if __name__ == "__main__":
    main()
