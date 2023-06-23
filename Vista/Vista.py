class Vista:
    def draw_bar(self):
        print("====================================")

    def draw_continue(self):
        print("Pulse Enter para continuar...")
        input()
    
    def draw(self,thing_to_draw):
        print(thing_to_draw)
    
    def draw_menu(self):
        self.draw_bar()
        print("Sistema de asesoramiento de Eventos - SocialEvent S.A.")
        print("")
        print("1 - Mostrar Clientes")
        print("2 - Mostrar Fechas.")
        print("3 - Mostrar Reservas.")
        print("4 - Reservar Fecha.")
        print("5 - Pagar Seña Inicial.")
        print("6 - Cancelar Reserva.") # 7 - Calcular dinero a devolver
        return input()

    def draw_error(self,n_error):
        self.draw_bar()
        match n_error:
            case 1:
                print("Debe ingresar un digito numerico.")
        self.draw_continue()