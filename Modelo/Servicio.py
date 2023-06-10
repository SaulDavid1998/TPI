class Servicio:
    def init(self,servicio="",precio=0.0):
        self.__servicio=servicio
        self.__precio=precio

    def GetServicio(self):
        return self.__servicio
    def GetPrecio(self):
        return self.__precio

    def SetPrecio(self,precio):
        self.__precio=precio
    def SetServicio(self,servicio):
        self.__servicio=servicio