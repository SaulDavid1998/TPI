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
        self.draw_continue()

    def draw_error_dia_ocupado(self,day):
        print("Ese dia esta ocupado, quizas le interesaria el " + str(day) + "...")

    #=======================
    #======   ENTER   ======
    #=======================
    
    def draw_enter_fecha(self):
        try:
            return int(input("Ingrese el dia en el que reservar: "))
        except Exception:
            self.draw_error(2)
    
    def draw_enter_servicios(self):
        try:
            return int(input("Ingrese el ID del servicio a reservar: "))
        except Exception:
            self.draw_error(2)

    def draw_enter_cliente(self):
        try:
            return int(input("Ingrese el ID del cliente a cargo de la reserva: "))
        except Exception:
            self.draw_error(2)
    
    def draw_enter_seniar(self):
        try:
            return int(input("Ingrese el ID de la reserva a señar: "))
        except Exception:
            self.draw_error(2)
    
    def draw_enter_cancelar(self):
        try:
            return int(input("Ingrese el ID de la reserva a cancelar: "))
        except Exception:
            self.draw_error(2)
    
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