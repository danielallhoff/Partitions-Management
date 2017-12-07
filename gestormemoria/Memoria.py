class Memoria:
    def __init__(self, instante, max, algoritmo, procesos):
        self.instante = instante
        self.max = max
        self.algoritmo = algoritmo
        self.procesos = procesos
    def getInstante(self):
        return self.instante
    def __str__(self):
        str = '%s ' % (self.instante)

        return str