class Vista_reserva:
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