class Fechas:
    def __init__(self,fecha=0,estado=True):
        self.__fecha=fecha
        self.__estado=estado

    def GetFecha(self):
        return self.__fecha
    def GetEstado(self):
        return self.__estado

    def SetEstado(self,estado):
        self.__estado=estado
    def SetFecha(self,fecha):
        self.__fecha=fecha

    def Verificar(self):
        pass
        #aca iria codigo para ver si esta la fecha
        #libre el en txt. Parecido a lo hecho en el
        #primer parcial


