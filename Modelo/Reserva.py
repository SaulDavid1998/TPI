class Reserva:
    def __init__(self,monto = float(750)):
        self.str_status = "En Cola..."
        self.monto = monto
        self.obj_cliente = -1 #Asignamos la ID a cliente, segun la ID del cliente que contrate el servicio.
        self.obj_fecha = -1 #Asignamos el dia en que se realizara el evento.
        self.obj_servicios = [] #Servicio es un array donde guardaremos las id's del servicio, NO EL NOMBRE, NI EL MONTO.
        
    def calcular_iva(self):
        self.monto = (self.monto * 1.21) + 100

    #=====================
    #======   SET   ======
    #=====================

    def set_cliente(self,par_cliente):
        self.obj_cliente = par_cliente

    def set_fecha(self,par_fecha):
        self.obj_fecha = par_fecha
    
    def set_status(self,par_status):
        self.str_status = par_status

    #=====================
    #======   GET   ======
    #=====================

    def get_status(self):
        return self.str_status
    
    def get_cliente(self):
        return self.obj_cliente

    def get_fecha(self):
        return self.obj_fecha
    
    def get_servicios(self):
        return self.obj_servicios
    
    def get_monto(self):
        return self.monto

    #=====================
    #======   ADD   ======
    #=====================
    
    def add_monto(self,par_monto):
        self.monto += par_monto
    
    def add_servicio(self,id,cost):
        self.obj_servicios.append(id)
        self.add_monto(cost)

    def add_servicio_nomonto(self,id):
        self.obj_servicios.append(id)

    #=====================
    #=====   _STR_   =====
    #=====================

    def __str__(self,type):
        match type:
            case 0: return "|| Cliente: " + str(self.get_cliente()) + " ||"
            case 1: return "|| Dia: " + str(self.get_fecha()) + " ||"
            case 2: return "|| ID Servicios: " + str(self.get_servicios()) + " ||"
            case 3: return "|| $ " + str(self.get_monto()) + " ||"
            case 4: return "|| Estado: " + str(self.get_status()) + " ||"
    
    def __str_id__(self,id):
        return "|| ID: " + str(id) + " ||"
    
    def __str_price__(self):
        print("Precio de la reserva: " + str(self.get_monto()))
        print("Gastos administrativos: $100")
        print("IVA: " + str((self.get_monto() * 1.21) - self.get_monto()))
        self.calcular_iva()
        print("Precio final: " + str(self.get_monto()))
        return "En total, el evento costara: $ " + str(self.get_monto())