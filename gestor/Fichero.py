from gestor.Proceso import Proceso
class Fichero:
    @staticmethod
    def leerFichero(fichero):

        fich = open(fichero, 'r')

        procesos = []
        if not fich.closed:
            for linea in fich.readlines():
                l = linea.split(' ')
                proceso = Proceso(l[0],int(l[1]),int(l[2]),int(l[3]))
                procesos.append(proceso)
            fich.close()
        else:
            print "Error! No se ha podido abrir el fichero"

        return procesos