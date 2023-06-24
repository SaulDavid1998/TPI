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
                print("Ese dia esta ocupado, ingrese otro...")
            case 3:
                print("No hay reservas realizadas.")
            case 4:
                print("Esa reserva no esta disponible para señar.")
            case 5:
                print("Esa reserva no esta disponible para cancelar.")
        self.draw_continue()

    #=======================
    #======   ENTER   ======
    #=======================
    
    def draw_enter_fecha(self):
        return int(input("Ingrese el dia en el que reservar: "))
    
    def draw_enter_servicios(self):
        return int(input("Ingrese el ID del servicio a reservar: "))

    def draw_enter_cliente(self):
        return int(input("Ingrese el ID del cliente a cargo de la reserva: "))
    
    def draw_enter_seniar(self):
        return int(input("Ingrese el ID de la reserva a señar: "))
    
    def draw_enter_cancelar(self):
        return int(input("Ingrese el ID de la reserva a cancelar: "))
    
    #==========================
    #======   PREGUNTA   ======
    #==========================
    
    def draw_pregunta_servicios(self):
        print("¿Desea agregar un servicio a su reserva?")
        print("Escriba <si> para aceptar, en caso contrario, ingrese cualquier otro comando/mensaje...")
        return str(input())

    def draw_pregunta_seniar(self):
        print("¿Desea señar esta reserva?")
        print("Escriba <si> para aceptar, en caso contrario, ingrese cualquier otro comando/mensaje...")
        return str(input())

    def draw_pregunta_cancelar(self):
        print("¿Desea cancelar esta reserva?")
        print("Escriba <si> para aceptar, en caso contrario, ingrese cualquier otro comando/mensaje...")
        return str(input())
    
    #==========================
    #======   COMPLETE   ======
    #==========================

    def draw_reserva_terminada(self):
        print("¡Reserva completada!")
    
    def draw_cancelar_terminado(self):
        print("¡Cancelamiento completado!")
    
    def draw_seniar_terminado(self):
        print("¡Seña registrada!")