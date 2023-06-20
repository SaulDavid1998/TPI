class Fecha:
    def __init__(self,fecha=0,estado=False):
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

    def __str__(self):
        return "|| Dia: " + str(self.__fecha) + " - Estado: " + str(self.__estado) + " ||"

    def Verificar(self):
        pass


