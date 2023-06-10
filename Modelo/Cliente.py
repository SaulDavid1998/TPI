class Cliente:
    def __init__(self,nombre="",dni=0,telefono=""):
        self.__nombre=nombre
        self.__dni=dni
        self.__telefono=telefono
        self.__edad=0
        self.__formaDePago=""

    def GetNombre(self):
        return self.__nombre
    def GetDni(self):
        return self.__dni
    def GetTelefono(self):
        return self.__telefono
    def GetEdad(self):
        return self.__edad
    def GetMetodoPago(self):
        return self.__formaDePago

    def SetNombre(self,nombre):
        self.__nombre=nombre
    def SetDni(self,dni):
        self.__dni=dni
    def SetTelefono(self,telefono):
        self.__telefono=telefono
    def SetFormaDePago(self,fdp):
        self.__formaDePago=fdp
    def SetEdad(self,edad):
        self.__edad=edad
