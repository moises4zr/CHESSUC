from Piezas import piezas

class peon(piezas): 
      def __init__(self, color, promocion, estado = 'no movida', capturada = False, posiciones = None):
        super().__init__(color, estado,  capturada, posiciones)
        self.promocion = promocion