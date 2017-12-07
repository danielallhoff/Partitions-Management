class Proceso:
    def __init__(self,nombre, llegada, memoria, tiempo_ejecucion):
        self.nombre = nombre
        self.llegada = llegada
        self.memoria = memoria
        self.tiempo_ejecucion = tiempo_ejecucion

    def getNombre(self):
        return self.nombre

    def getLlegada(self):
        return self.llegada

    def getMemoria(self):
        return self.memoria

    def getTiempo(self):
        return self.tiempo_ejecucion

    def __str__(self):
        return ('%s %s' % (self.memoria, self.nombre))


