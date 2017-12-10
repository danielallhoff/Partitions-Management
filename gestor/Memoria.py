from gestor.Proceso import  Proceso
class Memoria:
        def __init__(self,  max, procesos):
            self.__instante = 1
            self.__max = max
            self.__procesos = procesos
            self.__procesosAct = []
            self.__maxSpace = max
            for proceso in procesos:
                if(proceso.getLlegada() == 0):
                    if(proceso.getMemoria()<= self.__maxSpace):
                        self.__procesosAct.append(proceso)
                        self.__maxSpace -= proceso.getMemoria()
            if(self.__maxSpace > 0):
                self.__procesosAct.append(Proceso("Hueco",None, self.__maxSpace,None))

        def getInstante(self):
            return self.__instante

        def getProcesoAct(self,i):
            return self.__procesosAct.__getitem__(i)

        def insertarProceso(self,i,proceso):
            tam = self.getProcesoAct(i).getMemoria() - proceso.getMemoria()
            if(tam > 0):
                self.__procesosAct.insert(i+1,Proceso("Hueco",None, tam, None))
            self.__procesosAct[i] = proceso

        def getMax(self):
            return self.__max
        def getProcesosAct(self):
            return self.__procesosAct
        def hayHueco(self,proceso,hueco):
                if(hueco.isAsignado() == False and proceso.getMemoria() <= hueco.getMemoria()):
                    return True
        def primerHueco(self):
            for i,proceso in enumerate(self.__procesos):
                hueco = False
                if(proceso.getLlegada() <= self.getInstante()):
                    for j,hueco in enumerate(self.__procesosAct):
                        if(self.hayHueco(proceso,hueco[j])):
                            self.insertarProceso(j,proceso)
                            self.__procesos.pop(i)
                            i -= 1
                    if hueco == False : print "Por ahora, no hay hueco para el proceso: %s" % (proceso.getNombre())
            for i,proceso in enumerate(self.__procesosAct):
                if(proceso.isAsignado()): self.__procesosAct[i].gastoTiempo()
            self.__instante += 1

        '''def mejorHueco(self):
           for i,proceso in enumerate(self.__procesos):
                hueco = False
                if(proceso.getLlegada() <= self.getInstante()):
                    for j,hueco in enumerate(self.__procesosAct):
                        if(self.hayHueco(proceso,hueco[j])):
                            hueco = True
                            self.insertarProceso(j,proceso)
                            self.__procesos.pop(i)
                            i -= 1
                    if hueco == False : print "Por ahora, no hay hueco para el proceso: %s" % (proceso.getNombre())
            self.__instante += 1
        '''
        def getProcesos(self):
            return self.__procesos
        def __str__(self):
            str = '%s ' % (self.__instante)
            mem = 0
            for proceso in self.getProcesos():
                str += '[%s %s] ' % (mem,proceso.__str__())
                mem += int(proceso.getMemoria())
            str += '\n'
            return str
