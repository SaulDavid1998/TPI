class Vista_main:
    #=======================
    #======   EXTRA   ======
    #=======================
    def draw_bar(self):
        print("====================================")

    def draw_continue(self):
        print("Pulse Enter para continuar...")
        input()
    
    def draw(self,thing_to_draw):
        print(thing_to_draw)

    #======================
    #======   MENU   ======
    #======================
    
    def draw_menu(self):
        self.draw_bar()
        print("Sistema de asesoramiento de Eventos - SocialEvent S.A.")
        print("")
        print("1 - Mostrar Clientes.")
        print("2 - Mostrar Fechas.")
        print("3 - Mostrar Reservas.")
        print("4 - Mostrar Servicio")
        print("5 - Reservar Fecha.")
        print("6 - Pagar Seña Inicial.")
        print("7 - Cancelar Reserva.")
        print("8 - Cerrar Programa")
        return input()
    
    #============================
    #======   DRAW ERROR   ======
    #============================

    def draw_error(self,n_error):
        self.draw_bar()
        match n_error:
            case 1:
                print("Debe ingresar un digito numerico.")
            case 2:
                print("Ese dia esta ocupado, ingrese otro...") #Este error fue reemplazado por draw_error_dia_ocupado.
            case 3:
                print("No hay reservas realizadas.")
            case 4:
                print("Esa reserva no esta disponible para señar.")
            case 5:
                print("Esa reserva no esta disponible para cancelar.")
            case 6:
                print("No hay ningun dia disponible luego del ingresado...")
            case 7:
                print("El valor ingresado causo un error, intente de nuevo...")
            case 8:
                print("El valor ingresado se sale del rango estipulado.")
        self.draw_continue()