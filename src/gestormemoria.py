from gestor.Fichero import Fichero
from gestor.Memoria import Memoria
from gestor.Programa import Programa
if __name__ == '__main__':
    fichero = Fichero()
    memoria = Memoria(2000, fichero.leerFichero('particiones.txt'))
    menu = Programa(memoria)
    menu.start()
