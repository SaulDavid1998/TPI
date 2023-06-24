#Importamos los archivos externos que usemos
from Vista.Vista_main import Vista_main
from Modelo.Cliente import Cliente
from Modelo.Fechas import Fecha
from Modelo.Reserva import Reserva
from Modelo.Servicio import Servicio

vs = Vista_main() #Creamos el objeto vs, desde el cual llamaremos los metodos de Vista_main
ar_cliente = [] #Creamos un array vacia para los clientes
ar_fecha = [] #Creamos un array vacia para las fechas
ar_servicio = [] #Creamos un array vacia para los clientes
ar_reserva = [] #Creamos un array vacia para los clientes

class Controlador:
    def __init__(self): #El controlador comenzara leyendo los archivos y guardando sus datos en arrays.
        self.scr_create_cliente()
        self.scr_create_fecha()
        self.scr_create_servicio()
        self.scr_leer_reserva()
    
    #===============================
    #======   LEER ARCHIVOS   ======
    #===============================

    def scr_leer_reserva(self):
        with open("Reserva.txt","r+") as file: #Abrimos el archivo
            int_number = -1
            for lineas in file: #Leemos cada renglon individualmente
                int_number += 1
                aux = lineas.strip().split(",") #Separamos los atributos del renglon que estamos leyendo
                ar_reserva.append(Reserva(float(aux[2]))) #Creamos la reserva, junto a el monto guardado en el archivo.
                ar_reserva[int_number].set_cliente(int(aux[0])) #Asignamos el ID del cliente.
                ar_reserva[int_number].set_fecha(int(aux[1])) #Asignamos el dia.
                ar_fecha[int(aux[1])].SetEstado(True) # Asignamos el dia como True.
                ar_reserva[int_number].set_status(str(aux[3])) #Asignamos el estado.
                #===CARGAR SERVICIOS===
                for i in range(4,len(aux),1):
                    ar_reserva[int_number].add_servicio_nomonto(int(aux[i]))

    #CREATE _ CLIENTE: Leemos el archivo de Clientes y hacemos append al array...
    #Esto con el fin de manipularlos libremente, sin tener que leer el archivo todo el rato.
    def scr_create_cliente(self):
        with open("Clientes.txt","r+") as file: #Abrimos el archivo
            for lineas in file: #Leemos cada renglon individualmente
                aux = lineas.strip().split(",") #Separamos los atributos del renglon que estamos leyendo
                ar_cliente.append(Cliente(str(aux[0]),int(aux[1]),int(aux[2]),int(aux[3]))) #Creamos el cliente

    #CREATE _ FECHA: Asignamos al array fecha, 31 objetos Fecha, los cuales vienen en False por defecto.
    #False = Dia libre || True = Ya hay una reserva en esa fecha.
    def scr_create_fecha(self):
        for i in range(31):
            ar_fecha.append(Fecha(i,False)) #Creamos el dia
    
    #CREATE _ SERVICIO: Leemos el archivo de Servicios y hacemos append al array...
    #Esto con el fin de manipularlos libremente, sin tener que leer el archivo todo el rato.
    def scr_create_servicio(self):
        with open("Servicios.txt","r+") as file: #Abrimos el archivo
            for lineas in file: #Leemos cada renglon individualmente
                aux = lineas.strip().split(",") #Separamos los atributos del renglon que estamos leyendo
                ar_servicio.append(Servicio(str(aux[0]),int(aux[1]))) #Creamos el cliente

    #MENU: Vista muestra en pantalla el menu y devuelve lo escrito.
    def scr_menu(self):
        try:
            return int(vs.draw_menu())
        except Exception:
            vs.draw_error(1) # Error 1 = Debe ingresar un digito numerico.

    #==============================================
    #======   MOSTRAR ARRAYS - NO CONTINUE   ======
    #==============================================
    
    #SCRIPT _ MOSTRAR _ RESERVA _ SMALL: Muestra la reserva seleccionada sin detalles.
    def scr_show_reserva_small(self,id):
        for i in range(5):
            vs.draw(ar_reserva[id].__str__(i))

    #SCRIP _ MOSTRAR _ RESERVA: Muestra las reservas y NO pide pulsar Enter para continuar...
    def scr_show_reservas(self):
        for i,j in enumerate(ar_reserva): #Enumerate = Se ejecutara en cada uno de los valores del array, osea, cada cliente.
            vs.draw_bar()
            vs.draw(ar_reserva[i].__str_id__(int(i))) #str_id muestra especificamente la linea de ID.
            self.scr_show_reserva_small(i)

    #SCRIPT _ MOSTRAR _ CLIENTES: Muestra los clientes y NO pide pulsar Enter para continuar..
    def scr_show_clientes(self):
        vs.draw_bar()
        for i,j in enumerate(ar_cliente): #Enumerate = Se ejecutara en cada uno de los valores del array, osea, cada cliente.
            vs.draw(ar_cliente[i].__str__(i)) #__str__ muestra de forma bonita y detallada el objeto.
        vs.draw_bar()

    #SCRIPT _ MOSTRAR _ SERVICIOS: Muestra los servicios y NO pide pulsar Enter para continuar.
    def scr_show_servicios(self):
        vs.draw_bar()
        for i,j in enumerate(ar_servicio): #Enumerate = Se ejecutara en cada uno de los valores del array, osea, cada servicio.
            vs.draw(ar_servicio[i].__str__(i)) #__str__ muestra de forma bonita y detallada el objeto.
        vs.draw_bar()

    #SCRIPT _ MOSTRAR _ FECHAS: Muestra las fechas y NO pide pulsar Enter para continuar.
    def scr_show_fechas(self):
        vs.draw_bar()
        for i,j in enumerate(ar_fecha): #Enumerate = Se ejecutara en cada uno de los valores del array, osea, cada fecha.
            vs.draw(ar_fecha[i].__str__()) #__str__ muestra de forma bonita y detallada el objeto.
        vs.draw_bar()

    #==============================================
    #======   MOSTRAR ARRAYS - SI CONTINUE   ======
    #==============================================

    #SCRIPT _ MOSTRAR _ FECHAS _ CONTINUE: Muestra las fechas y pide pulsar Enter para continuar.
    def scr_show_fechas_cont(self):
        self.scr_show_fechas()
        vs.draw_continue()

    #SCRIPT _ MOSTRAR _ SERVICIOS _ CONTINUE: Muestra los servicios y pide pulsar Enter para continuar.
    def scr_show_servicios_cont(self):
        self.scr_show_servicios()
        vs.draw_continue()

    #SCRIPT _ MOSTRAR _ CLIENTES _ CONTINUE: Muestra los clientes y pide pulsar Enter para continuar..
    def scr_show_clientes_cont(self):
        self.scr_show_clientes()
        vs.draw_continue()

    #SCRIPT _ MOSTRAR _ RESERVA _ CONTINUE: Muestra las reservas y pide pulsar Enter para continuar..
    def scr_show_reservas_cont(self):
        if len(ar_reserva) == 0:
            vs.draw_error(3)
        else:
            for i,j in enumerate(ar_reserva): #Enumerate = Se ejecutara en cada uno de los valores del array, osea, cada cliente.
                vs.draw_bar()
                vs.draw(ar_reserva[i].__str_id__(int(i))) #__str_id__ muestra especificamente la linea de ID.
                self.scr_show_reserva_small(i)
            vs.draw_bar()
            vs.draw_continue()
    
    #===============================
    #======   CREAR RESERVA   ======
    #===============================
    #Van a ver que uso "len(ar_reserva) - 1"
    #Len me dice la cantidad de valores que tiene un array.
    #Entonces al crear la primera reserva, Len daria 1, porque hay una sola reserva.
    #Pero como sabemos, los arrays comienzan a leerse desde el 0.
    #Asi que le restamos 1 para manipular especificamente la ultima reserva creada.
    #Si saben alguna forma mas corta de hacerlo, me avisan B)
    def scr_create_reserva(self):
        ar_reserva.append(Reserva()) #Creamos la reserva
        #======Seleccionar Cliente======
        self.scr_show_clientes() #Mostramos al usuario los clientes.
        self.int_idcliente = vs.draw_enter_cliente() #Pedimos al usuario ingrese la ID del cliente.
        ar_reserva[(len(ar_reserva) - 1)].set_cliente(self.int_idcliente)
        #======Seleccionar Dia======
        self.scr_show_fechas() #Mostramos al usuario los dias y si estan disponibles o no.
        self.int_fecha = vs.draw_enter_fecha() #Pedimos al usuario ingresar el dia.
        while ar_fecha[self.int_fecha].GetEstado() == True: #Aca leemos el array fecha segun el dia ingresado, en caso de ser True, el dia esta ocupado.
            vs.draw_error(2) # Error 1 = Dia ocupado.
            self.int_fecha = vs.draw_enter_fecha() #Pedimos al usuario ingresar otra vez el dia.
        ar_reserva[(len(ar_reserva) - 1)].set_fecha(self.int_fecha)
        ar_fecha[self.int_fecha].SetEstado(True)
        #======Seleccionar Servicios======
        while vs.draw_pregunta_servicios() == "si":
            self.scr_show_servicios() #Mostramos al usuario los servicios.
            int_idservice = vs.draw_enter_servicios() #int_idservice sera el numero ingresado.
            if int_idservice > -1 and int_idservice < len(ar_servicio): #Verificamos que el numero ingresado este entre 0 y el maximo de servicios (Estos incluidos).
                ar_reserva[(len(ar_reserva) - 1)].add_servicio(int_idservice,ar_servicio[int_idservice].GetPrecio()) #Extendemos la array de servicios, dandole la ID y el monto del servicio.
        #Si dejamos la casilla vacia o escribimos algo random, se termina la parte de servicios y pasamos con la siguiente.
        #======Finalizar======
        #Esto de aca abajo se encarga de mostrar los distintos montos a sumar.
        #Para mas información revisar: Reserva -> STR -> __str_price__
        vs.draw_bar()
        vs.draw_reserva_terminada()
        for i in range(3):
            vs.draw(ar_reserva[(len(ar_reserva) - 1)].__str_price__(i))
        ar_reserva[(len(ar_reserva) - 1)].calcular_iva()
        for i in range(3,5,1):
            vs.draw(ar_reserva[(len(ar_reserva) - 1)].__str_price__(i))
        vs.draw_bar()
        vs.draw_continue()

    #================================
    #======   CAMBIAR STATUS   ======
    #================================
    def scr_seniar(self):
        self.scr_show_reservas() #Mostramos las reservas.
        vs.draw_bar()
        int_seniar = vs.draw_enter_seniar() #Pedimos al usuario que escriba la ID de la reserva a señar.
        if ar_reserva[int_seniar].get_status() == "En Cola...": #Preguntamos si la reserva esta En Cola, para no señar una reserva cancelada o ya señada.
            vs.draw(ar_reserva[int_seniar].__str_senia__()) #En caso de que este En Cola, le mostramos al usuario cuanto costaria.
            if vs.draw_pregunta_seniar() == "si": #Pedimos al usuario que escriba si para confirmar.
                ar_reserva[int_seniar].set_status("Señado") #Cambiamos el estado de la reserva a Señado.
            vs.draw_seniar_terminado() #Printeamos que el señado fue terminado.
            vs.draw_continue()
        else:
            vs.draw_error(4) #En caso de que no este En Cola, se le avisara al usuario.

    def scr_cancelar(self):
        self.scr_show_reservas() #Mostramos las reservas.
        vs.draw_bar()
        int_cancel = vs.draw_enter_cancelar() #Pedimos al usuario que escriba la ID de la reserva a cancelar.
        if ar_reserva[int_cancel].get_status() == "En Cola..." or ar_reserva[int_cancel].get_status() == "Señado": #Preguntamos si la reserva no esta cancelada.
            vs.draw(ar_reserva[int_cancel].__str_cancelar__()) #En caso de que no este cancelado, le mostramos al usuario cuanto dinero se devolveria.
            if vs.draw_pregunta_cancelar() == "si": #Pedimos al usuario que escriba si para confirmar.
                ar_reserva[int_cancel].set_status("Cancelado") #Cambiamos el estado de la reserva a Cancelado.
            vs.draw_cancelar_terminado() #Printeamos que el cancelamiento fue terminado.
            vs.draw_continue()
        else:
            vs.draw_error(5) #En caso de que no este En Cola o Señado, se le avisara al usuario.