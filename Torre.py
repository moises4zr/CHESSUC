from Piezas import piezas

class torre(piezas): 
      def __init__(self, color, estado = 'no movida', capturada = False, posiciones = None):
        super().__init__(color, estado,  capturada, posiciones)