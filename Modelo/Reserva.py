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
    
    def add_monto(self,par_monto): #Suma dinero al monto final de la reserva.
        self.monto += par_monto #Esto es usado al agregar un servicio.
    
    def add_servicio(self,id,cost): #Agrega un servicio.
        self.obj_servicios.append(id) #Primero registra su id, ya que no se guarda un array como tal.
        self.add_monto(cost) #Luego con add_monto se suma al monto final.

    def add_servicio_nomonto(self,id): #Al leer las reservas que estan en el archivo, no necesitamos sumar el monto.
        self.obj_servicios.append(id) #Entonces con esta función solo agregamos la ID de los servicios.

    #=====================
    #=====   _STR_   =====
    #=====================

    #Complejos

    def __str__(self,type):
        match type:
            case 0: return "|| Cliente: " + str(self.get_cliente()) + " ||" #Mostramos el nombre del cliente. # REEMPLAZADA POR __str_cliente__
            case 1: return "|| Dia: " + str(self.get_fecha()) + " ||"   #Mostramos el dia del evento.
            case 2: return "|| ID Servicios: " + str(self.get_servicios()) + " ||" #Mostramos el ID de los servicios.
            case 3: return "|| $ " + str(self.get_monto()) + " ||" #Mostramos el monto total.
            case 4: return "|| Estado: " + str(self.get_status()) + " ||" #Mostramos el estado.
    
    def __str_price__(self,type):
        match type:
            case 0: return "Precio de la reserva: $" + str(self.get_monto()) #Mostramos el precio de la reserva + servicios.
            case 1: return "Gastos administrativos: $100" #Mostramos el gasto administrativo.
            case 2: return "IVA: " + str((self.get_monto() * 1.21) - self.get_monto()) + "%" #Mostramos lo que se suma debido al IVA.
            case 3: return "En total, el evento costara: $" + str(self.get_monto()) #Mostramos el precio final.
            case 4: return "La seña a realizar es de: $" + str(self.get_monto() * 0.3) #Mostramos el precio a señar.

    #Simples

    def __str_id__(self,id):
        return "|| ID: " + str(id) + " ||"
    
    def __str_senia__(self):
        return "La seña a realizar es de: $" + str(self.get_monto() * 0.3)
    
    def __str_cancelar__(self):
        if self.get_status() == "Señado": #Si la reserva esta señada, se devolvera parte de la seña, en caso contrario, no.
            return "El dinero a devolver es: $" + str((self.get_monto() * 0.3) * 0.2)
        else:
            return "No hay que devolver dinero."
    
    def __str_cliente__(self,name):
        return "|| Cliente: " + str(name) + " ||"