from gestor.Proceso import  Proceso
class Memoria:
        def __init__(self,  max, procesos):
            self.__instante = 0
            self.__max = max
            self.__procesos = procesos
            self.__procesosAct = []
            self.__maxSpace = max
            for i,proceso in enumerate(self.__procesos):
                if(proceso.getLlegada()) == 0:
                    if(proceso.getMemoria() <= self.__maxSpace):
                        proceso.setAsignado(True)
                        self.__procesosAct.append(proceso)
                        self.__procesos[i] = None
                        self.__maxSpace -= proceso.getMemoria()
            if(self.__maxSpace > 0):
                self.__procesosAct.append(Proceso("Hueco",None, self.__maxSpace,None))
        def getInstante(self):
            return self.__instante

        def getProcesoAct(self,i):
            return self.__procesosAct.__getitem__(i)

        def insertarProceso(self,i,proceso):
            tam =  (self.__procesosAct[i]).getMemoria() - proceso.getMemoria()
            if(tam > 0):
                self.__procesosAct.insert(i+1,Proceso("Hueco",None, tam, None))
            proceso.setAsignado(True)
            self.__procesosAct[i] = proceso

        def getMax(self):
            return self.__max
        def getProcesosAct(self):
            return self.__procesosAct
        def hayHueco(self,proceso,hueco):
                if(hueco.isAsignado() == False and proceso.getMemoria() <= hueco.getMemoria()):
                    return True
        def procesosTerminados(self):
            for i,proceso in enumerate(self.__procesosAct):
                if proceso.getTiempo() <= 0:
                    self.__procesosAct.pop(i)
                    self.__procesosAct.insert(i,Proceso("Hueco",None,proceso.getMemoria(),None))
        def gastarTiempo(self):
            for i,proceso in enumerate(self.__procesosAct):
                if(proceso.isAsignado()):
                    proceso.gastoTiempo()
                    self.__procesosAct[i] = proceso
            self.__instante += 1
        def juntarHuecos(self):
            init = -1
            fin = -1
            esHueco = False
            huecoNuevo = Proceso("Hueco", None,0, None)
            huecoNuevo.setAsignado(False)
            for i, proceso in enumerate(self.__procesosAct):
                if(proceso.isAsignado() == False):
                    if(esHueco == False):
                        init = i
                        esHueco = True
                    fin = i
                    huecoNuevo.setMemoria(huecoNuevo.getMemoria()+ proceso.getMemoria())
                if(proceso.isAsignado() == True or i == len(self.__procesosAct)-1):
                    if(init >= 0 and fin >= 0):
                        for j in reversed(range(init,fin+1)):
                            self.__procesosAct.pop(j)
                        self.__procesosAct.insert(init, huecoNuevo)
                        esHueco = False
        def manejarFinTiempo(self):
            self.gastarTiempo()
            print self.__str__()
            self.procesosTerminados()
            self.juntarHuecos()

        def primerHueco(self):
            for i,proceso in enumerate(self.__procesos):
                hayHueco = False
                if proceso != None:
                    if proceso.getLlegada() <= self.getInstante():
                        for j,hueco in enumerate(self.__procesosAct):
                            if self.hayHueco(proceso, hueco):
                                hayHueco = True
                                self.insertarProceso(j, proceso)
                                self.__procesos[i] = None
                                break
                        if hayHueco == False : print "Por ahora, no hay hueco para el proceso: %s" % (proceso.getNombre())
            self.manejarFinTiempo()
        def mejorHueco(self):
            for i,proceso in enumerate(self.__procesos):
                hayHueco = False
                if proceso != None:
                    if proceso.getLlegada() <= self.getInstante():
                        for j,hueco in enumerate(self.__procesosAct):
                            if self.hayHueco(proceso, hueco):
                                hayHueco = True
                                self.insertarProceso(j, proceso)
                                self.__procesos[i] = None
                                break
                        if hayHueco == False : print "Por ahora, no hay hueco para el proceso: %s" % (proceso.getNombre())
            self.manejarFinTiempo()
        def getProcesos(self):
            return self.__procesos
        def __str__(self):
            str = '%s ' % (self.__instante)
            mem = 0
            for proceso in self.getProcesosAct():
                str += '[%s %s] ' % (mem,proceso.__str__())
                mem += proceso.getMemoria()
            str += '\n'
            return str
