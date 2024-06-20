class piezas():
    def __init__(self, color, estado = 'no movida', capturada = False, posiciones = None ): 
        self.color = color 
        self.estado = estado
        self.capturada = capturada
        self.posiciones = posiciones
        
        
class Rey(piezas): 
    def __init__(self, color, estado = 'no movida', capturada = False, posiciones = None ): 
        super().__init__(color, estado,  capturada, posiciones)

class Reina(piezas): 
    def __init__(self, color, estado, capturada, posiciones):
        super().__init__(color, estado,  capturada, posiciones)
        
class Caballo(piezas): 
      def __init__(self, color, estado, capturada, posiciones):
        super().__init__(color, estado,  capturada, posiciones)
        
class Alfil(piezas): 
      def __init__(self, color, estado, capturada, posiciones):
        super().__init__(color, estado,  capturada, posiciones)
        
class Torre(piezas): 
      def __init__(self, color, estado, capturada, posiciones):
        super().__init__(color, estado,  capturada, posiciones)
        
class Peon(piezas): 
      def __init__(self, color, estado, capturada, posiciones, promocion):
        super().__init__(color, estado,  capturada, posiciones)
        self.promocion = promocion 
    
    