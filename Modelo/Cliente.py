class Cliente:
    def __init__(self,nombre="",dni=0,telefono=0,edad=0):
        self.__nombre=nombre
        self.__dni=dni
        self.__telefono=telefono
        self.__edad=edad

    def GetNombre(self):
        return self.__nombre
    
    def GetDni(self):
        return self.__dni
    
    def GetTelefono(self):
        return self.__telefono
    
    def GetEdad(self):
        return self.__edad

    def SetNombre(self,nombre):
        self.__nombre=nombre

    def SetDni(self,dni):
        self.__dni=dni

    def SetTelefono(self,telefono):
        self.__telefono=telefono

    def SetEdad(self,edad):
        self.__edad=edad

    def __str__(self):
        return "|| Nombre: " + str(self.__nombre) + " - DNI: " + str(self.__dni) + " - Telefono: " + str(self.__telefono) + " - Edad: " + str(self.__edad) + " ||"