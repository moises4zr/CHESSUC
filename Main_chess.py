
from Piezas import *
from Rey import *
from Reina import *
from Caballo import *
from Alfil import *
from Torre import *
from Peon import *


def main():
    
    """Peon = peon("negro", (2,'B'))
    print(f"La pieza 'peon' ahora está en la posición: {Peon.posicion}")
    
    movimiento = input("Ingrese el movimiento (por ejemplo, B3): ")
    nueva_columna, nueva_fila = movimiento[0], int(movimiento[1])
    Peon.movimiento((nueva_fila, nueva_columna))"""
    
    mi_torre = torre("blanco", (1, 'A'))
    
    movimiento = input("Ingrese el movimiento (por ejemplo, A3): ")
    nueva_columna, nueva_fila = movimiento[0], int(movimiento[1])
    mi_torre.movimiento((nueva_fila, nueva_columna))
    
if __name__ == "__main__":
    main()
