# coding=utf-8
class Programa:
    def __init__(self, memoria):
        self.__memoria = memoria
    def opcStr(self):
        print "============"
        print "----MENÚ----"
        print "============\n"
        print "1.Primer hueco"
        print "2.Mejor hueco"
        print "3.Salir!"
    def start(self):
        opc = '0'
        while(opc != '3'):
            self.opcStr()
            opc = str(input("Opción:"))
            if opc == '1':
                print "Has seleccionado el algoritmo del primer hueco!"
                self.__memoria.primerHueco()
                print self.__memoria
            elif(opc == '2'):
                print "Has seleccionado el algoritmo del mejor hueco!"
                self.__memoria.mejorHueco()
                print self.__memoria
            elif(opc == '3'):
                print "Finalización del programa!"
            else:
                print "Opción Incorrecta!"