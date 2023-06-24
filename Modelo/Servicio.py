class Servicio:
    def __init__(self,servicio,precio):
        self.servicio = servicio
        self.precio = precio

    def GetServicio(self):
        return self.servicio
    
    def GetPrecio(self):
        return self.precio

    def SetPrecio(self,precio):
        self.precio=precio

    def SetServicio(self,servicio):
        self.servicio=servicio

    #def devolver_servicio(self):
        #return self.aux[str(self.GetServicio(),self.GetPrecio())]
    
    def __str__(self,par):
        return "|| ID: " + str(par) + " - Servicio: " + str(self.servicio) + " - Costo: " + str(self.precio) + " ||"