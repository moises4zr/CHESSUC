from Piezas import piezas

class torre(piezas):
    def __init__(self, color, posicion, capturada=False):
        super().__init__(color, posicion, capturada)
      
    def movimiento(self, nueva_posicion):
        fila_actual, columna_actual = self.posicion
        nueva_fila, nueva_columna = nueva_posicion
        
        if columna_actual == nueva_columna or nueva_fila == fila_actual:
            self.posicion = nueva_posicion
            print(f"La pieza 'torre' ahora está en la posición: {self.posicion}")
        else:
            print("Movimiento Incorrecto, la pieza no se ha movido")
