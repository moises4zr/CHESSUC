from Piezas import piezas

class peon(piezas):
    def __init__(self, color, posicion, capturada=False):
        super().__init__(color, posicion, capturada)

    def movimiento(self, nueva_posicion):
        fila_actual, columna_actual = self.posicion
        nueva_fila, nueva_columna = nueva_posicion

        # Lógica de movimiento para el peón: mover una casilla hacia adelante en la misma columna
        if columna_actual == nueva_columna and (nueva_fila == fila_actual + 1):
            self.posicion = nueva_posicion
            print(f"La pieza 'peon' ahora está en la posición: {self.posicion}")
        else:
            print("Movimiento Incorrecto, la pieza no se ha movido")

  