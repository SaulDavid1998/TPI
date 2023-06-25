class Servicio:
    def __init__(self,servicio,precio):
        self.__servicio = servicio
        self.__precio = precio

    def GetServicio(self):
        return self.__servicio
    
    def GetPrecio(self):
        return self.__precio

    def SetPrecio(self,precio):
        self.__precio=precio

    def SetServicio(self,servicio):
        self.__servicio=servicio

    def __str__(self,par):
        return "|| ID: " + str(par) + " - Servicio: " + str(self.GetServicio()) + " - Costo: " + str(self.GetPrecio()) + " ||"