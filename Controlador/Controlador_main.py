from Vista.Vista import Vista
from Modelo.Cliente import Cliente
from Modelo.Fechas import Fecha
from Controlador.Controlador_reserva import Controlador_reserva

vs = Vista()
cnt_r = Controlador_reserva()
ar_cliente = []
ar_fecha = []

class Controlador:
    def __init__(self):
        self.scr_create_cliente()
        self.scr_create_fecha()

    def scr_create_cliente(self):
        with open("Clientes.txt","r+") as file:
            for lineas in file:
                aux = lineas.strip().split(",")
                ar_cliente.append(Cliente(str(aux[0]),int(aux[1]),int(aux[2]),int(aux[3])))

    def scr_create_fecha(self):
        for i in range(31):
            ar_fecha.append(Fecha(i,False))

    def scr_menu(self):
        try:
            return int(vs.draw_menu())
        except Exception:
            vs.draw_error(1)
        
    def scr_show_clientes(self):
        vs.draw_bar()
        for i,j in enumerate(ar_cliente):
            vs.draw(ar_cliente[i].__str__())
        vs.draw_bar()
        vs.draw_continue()
    
    def scr_show_fechas(self):
        vs.draw_bar()
        for i,j in enumerate(ar_fecha):
            vs.draw(ar_fecha[i].__str__())
        vs.draw_bar()
        vs.draw_continue()
    
    def scr_create_reserva():
        cnt_r.scr_create_reserva()