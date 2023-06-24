from Controlador.Controlador_main import Controlador

cnt = Controlador()

while True:
    int_option = cnt.scr_menu() #Vista muestra en pantalla el menu y define a int_option segun lo escrito.
    match int_option: #Match = Depende que valor tome int_option, realizara cosas diferentes.
        #Mostrar Clientes.
        case 1:
            cnt.scr_show_clientes_cont() #Llama la respectiva función.
        #Mostrar Fechas.
        case 2:
            cnt.scr_show_fechas_cont() #Llama la respectiva función.
        #Mostrar Reservas.
        case 3:
            cnt.scr_show_reservas_cont() #Llama la respectiva función.
        #Mostrar Servicio.
        case 4:
            cnt.scr_show_servicios_cont() #Llama la respectiva función.
        #Reservar Fecha.
        case 5:
            cnt.scr_create_reserva() #Llama la respectiva función.