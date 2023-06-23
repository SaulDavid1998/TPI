from Controlador.Controlador_main import Controlador

cnt = Controlador()

while True:
    int_option = cnt.scr_menu()
    match int_option:
        case 1:
            cnt.scr_show_clientes()
        case 2:
            cnt.scr_show_fechas()
        case 4:
            cnt.scr_create_reserva()