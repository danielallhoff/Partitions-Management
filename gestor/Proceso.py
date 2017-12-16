class Proceso:
    def __init__(self,nombre, llegada, memoria, tiempo_ejecucion):
        self.__nombre = nombre
        self.__llegada = llegada
        self.__memoria = memoria
        self.__tiempo_ejecucion = tiempo_ejecucion
        self.__asignado = False


    def isAsignado(self):
        return self.__asignado
    def gastoTiempo(self):
        self.__tiempo_ejecucion = self.__tiempo_ejecucion - 1
    def setAsignado(self,asignado):
        self.__asignado = asignado
    def setMemoria(self,memoria):
        self.__memoria = memoria
    def getNombre(self):
        return self.__nombre
    def getLlegada(self):
        return self.__llegada
    def getMemoria(self):
        return self.__memoria
    def getTiempo(self):
        return self.__tiempo_ejecucion
    def __str__(self):
        return ('%s %s' % (self.__nombre, self.__memoria))


