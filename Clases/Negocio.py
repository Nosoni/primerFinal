# -*- coding: utf-8 -*-

from abc import ABCMeta
from Clases.Persona import Cliente, Empleado
from Clases.Solicitud import *
from Clases.Equipo import *
from Clases.Repuesto import Disco, Cartucho, Memoria, Otro
from Controlador.Util import *
import Datos.Bd as bd

dias_garantia = 30


class Empresa(metaclass=ABCMeta):
    def __init__(self):
        pass


class Negocio(Empresa):
    """Clase que contiene todos los menus y las funciones para modificar
    los datos del negocio"""

    tipo_rep = {"disco": Disco,
                "memoria": Memoria,
                "cartucho": Cartucho,
                "otro": Otro}

    def __init__(self):
        super().__init__()
        cargar_datos()

    # ________________________________Menu___Empleados______________________________
    def add_empleado(self):
        cls_()
        bd.empleados.append(Empleado(**Empleado.prompt_init()))

    def del_empleado(self):
        dato = encontrar_valor(bd.empleados, "cedula", input_alpha_r("Ingrese nro de documento: "))
        if dato:
            self.del_datos(bd.empleados, dato)
        else:
            print("No se encontró el dato a eliminar.")

    def listar_empleado(self):
        self.listar_datos(bd.empleados)

    def listar_empleado_det(self):
        self.listar_datos_det(bd.empleados)

    def edit_salario(self):
        pass

    # ________________________________Menu___Cliente________________________________
    def add_cliente(self):
        cls_()
        bd.clientes.append(Cliente(**Cliente.prompt_init()))

    def del_cliente(self):
        dato = encontrar_valor(bd.clientes, "cedula", input_alpha_r("Ingrese nro de documento: "))
        if dato:
            self.del_datos(bd.clientes, dato)
        else:
            print("No se encontró el dato a eliminar.")

    def listar_cliente(self):
        self.listar_datos(bd.clientes)

    def listar_cliente_det(self):
        self.listar_datos_det(bd.clientes)

    # ________________________________Menu___Solicitud______________________________
    def add_solicitud(self):
        """Permite crear una solicitud con todas sus partes
        Primero se ingresan los datos de la solicitud, luego se anhade un
        equipo o mas y cada equipo puede tener  repuestos"""
        cls_()
        solicitud = Solicitud(Solicitud.prompt_init())
        bd.solicitudes.append(solicitud)

    def act_solicitud(self):
        """Permite agregar repuestos a las computadoras de solicitudes
        creadas anteriormente"""
        if not bd.solicitudes:
            print("\nSin datos.")
            return input("Presione enter para volver al menu..")
        """retornará la solicitud que desea actualizar"""
        soli = encontrar_valor(bd.solicitudes, "solicitud_numero", input_alpha_r("Ingrese nro de Solicitud: "))
        try:
            print()
            #soli.mostrar_datos()
            print_objeto(soli)
            resp_add = input_opcion("Desea ingresar un nuevo equipo?", ("si", "no"))
            """si no existe el equipo que desea add a la solicitud, le permitira add"""
            while resp_add == "si":
                resp_add_nuevo = input_opcion("Existe el equipo?", ("si", "no"))
                if resp_add_nuevo == "si":
                    equi = encontrar_valor(bd.equipos, "cod", input_alpha_r("Ingrese nro de Equipo: "))
                else:
                    equi = Equipo(**Equipo.prompt_init())
                soli.add_equipo(equi)
                resp_add = input_opcion("Desea ingresar otro equipo?", ("si", "no"))
        except:
            print("Invalido")
        input("Presiona enter para volver al menu..")

    def baja_solicitud(self):
        """Elimina una solicitud que se desea retirar, pero calcula el valor
        total para repasar a facturacion"""
        soli = encontrar_valor(bd.solicitudes, "solicitud_numero", input_alpha_r("Ingrese nro de Solicitud: "))
        #soli.mostrar_datos()
        print_objeto(soli)
        resp = input_opcion("Desea dar de baja la solicitud?", ("si", "no"))
        if resp == "si":
            print("\n----Detalles----")
            print(("Fecha: {}".format(soli.fecha)))
            if soli.fecha is not None:
                print(("Garantia hasta: {}".format(soli.fecha + timedelta(days=dias_garantia))))
            print(("Cliente: {}".format(soli.cliente.nombre + " " + soli.cliente.apellido)))
            print(("Empleado: {}".format(soli.empleado.nombre + " " + soli.empleado.apellido)))
            money = soli.calc()
            soli.cambiar_estado()
            bd.solicitudes.remove(soli)
            bd.solicitudes_baja.append(soli)
            print(("El costo total es de: Gs {}".format(money)))
        else:
            print("Cancelado.")

    def del_solicitud(self):
        dato = encontrar_valor(bd.solicitudes, "solicitud_numero", input_alpha_r("Ingrese nro de solicitud: "))
        if dato:
            self.del_datos(bd.solicitudes, dato)
        else:
            print("No se encontró el dato a eliminar.")

    def list_solicitudes(self):
        self.listar_datos(bd.solicitudes)

    def list_solicitudes_baja(self):
        self.listar_datos(bd.solicitudes_baja)

    # ________________________________Menu___Equipos_______________________________
    def add_equipo(self):
        cls_()
        bd.equipos.append(Equipo(**Equipo.prompt_init()))

    def del_equipo(self):
        dato = encontrar_valor(bd.equipos, "cod", input_alpha_r("Ingrese código del equipo: "))
        if dato:
            self.del_datos(bd.equipos, dato)
        else:
            print("No se encontró el dato a eliminar.")

    def list_equipo(self):
        self.listar_datos(bd.equipos)

    # ________________________________Menu___Repuesto_______________________________
    def add_repuesto(self):
        """Permite anhadir uno de los tipos de repuestos"""
        cls_()
        opcion = input_opcion("Tipo Repuesto", ("disco", "memoria", "tarjeta",
                                                "cartucho", "otro"))
        print()
        datos = self.tipo_rep[opcion].prompt_init()
        bd.repuestos.append(self.tipo_rep[opcion](**datos))

    def del_repuesto(self):
        dato = encontrar_valor(bd.repuestos, "cod", input_alpha_r("Ingrese código del equipo: "))
        if dato:
            self.del_datos(bd.repuestos, dato)
        else:
            print("No se encontró el dato a eliminar.")

    def list_repuesto(self):
        self.listar_datos(bd.repuestos)

    # ______________________________Funciones_______________________________________
    def del_datos(self, lista, dato):
        """Permite eliminar un objeto"""
        if lista:
            resp = input_opcion("Desea eliminar el dato?", ("si", "no"))
            if resp == "si":
                lista.remove(dato)
                print("Eliminado.")
            else:
                print("Cancelado.")
        else:
            print("\nSin datos.")

    def listar_datos(self, lista, p=True):
        """Permite listar los datos contenidos en en los distintos vectores
           El valor p = False sirve para imprimir sin pausas"""
        if lista:
            print()
            cont = 1
            for val in lista:
                print(("-----------------=={}==-----------------".format(cont)))
                #val.mostrar_datos()
                print_objeto(val)
                print()
                if (cont % 5) is 0:
                    if p:
                        input("Presione enter para continuar...")
                cont += 1
            if p:
                input("Presione enter para volver al menu...")
        else:
            input("\nSin datos. \nPresione enter para continuar...")

    def listar_datos_det(self, lista, p=True):
        """Permite listar los datos contenidos en en los distintos vectores
           El valor p = False sirve para imprimir sin pausas"""
        if lista:
            print()
            cont = 1
            for val in lista:
                print(("-----------------=={}==-----------------".format(cont)))
                #val.mostrar_datos_det()
                print_objeto(val)
                print()
                if (cont % 5) is 0:
                    if p:
                        input("Presione enter para continuar...")
                cont += 1
            if p:
                input("Presone enter para volver al menú...")
        else:
            input("\nSin datos. \nPresione enter para continuar...")

    def fin(self):
        guardar_datos()
        exit()

    # ______________________________====MENUS====__________________________________
    def menu(self):
        """Menu principal del programa"""
        while True:
            cls()
            print("-----------------------------------------------------------")
            print("--------------------MENU--PRINCIPAL------------------------")
            print()
            for key in list(self.o_principal.keys()):
                print(("{} - {}".format(key, self.o_principal[key]["t"])))
            print()
            opcion = input_range("Ingrese una opción", 1, self.o_principal.__len__())
            self.o_principal[int(opcion)]["f"](self)

    def menu_list(self, text, dic):
        """Presenta el menu con las o_principal"""
        while True:
            cls()
            print(("\n------------------{}--------------------------\n".
                   format("MENÚ --" + text)))
            for key in list(dic.keys()):
                print(("{} - {}".format(key, dic[key]["t"])))
            print()
            opcion = input_range("Ingrese una opción", 1, dic.__len__())
            dic[int(opcion)]["f"](self)

    def menu_clientes(self):
        self.menu_list("CLIENTES", self.o_clientes)

    def menu_empleados(self):
        self.menu_list("EMPLEADOS", self.o_empleados)

    def menu_solicitud(self):
        self.menu_list("SOLICITUDES", self.o_solicitudes)

    def menu_equipos(self):
        self.menu_list("EQUIPOS", self.o_equipos)

    def menu_repuestos(self):
        self.menu_list("REPUESTOS", self.o_repuestos)

    o_clientes = {}
    o_clientes[1] = {"t": "Agregar cliente", "f": add_cliente}
    o_clientes[2] = {"t": "Eliminar cliente", "f": del_cliente}
    o_clientes[3] = {"t": "Listar clientes", "f": listar_cliente}
    o_clientes[4] = {"t": "Listar clientes detallado", "f": listar_cliente_det}
    o_clientes[5] = {"t": "Volver", "f": menu}

    o_empleados = {}
    o_empleados[1] = {"t": "Agregar empleado", "f": add_empleado}
    o_empleados[2] = {"t": "Eliminar empleado", "f": del_empleado}
    o_empleados[3] = {"t": "Listar empledos", "f": listar_empleado}
    o_empleados[4] = {"t": "Listar empledos detallado", "f": listar_empleado_det}
    o_empleados[5] = {"t": "Editar Salario", "f": edit_salario}
    o_empleados[6] = {"t": "Volver", "f": menu}

    o_solicitudes = {}
    o_solicitudes[1] = {"t": "Agregar Solicitud", "f": add_solicitud}
    o_solicitudes[2] = {"t": "Actualizar Solicitud", "f": act_solicitud}
    o_solicitudes[3] = {"t": "Dar de baja Solicitud", "f": baja_solicitud}
    o_solicitudes[4] = {"t": "Eliminar Solicitud", "f": del_solicitud}
    o_solicitudes[5] = {"t": "Listar Solicitues", "f": list_solicitudes}
    o_solicitudes[6] = {"t": "Listar Solicitues Baja", "f": list_solicitudes_baja}
    o_solicitudes[7] = {"t": "Volver", "f": menu}

    o_equipos = {}
    o_equipos[1] = {"t": "Agregar equipo", "f": add_equipo}
    o_equipos[2] = {"t": "Eliminar equipo", "f": del_equipo}
    o_equipos[3] = {"t": "Listar equipos", "f": list_equipo}
    o_equipos[4] = {"t": "Volver", "f": menu}

    o_repuestos = {}
    o_repuestos[1] = {"t": "Agregar repuesto", "f": add_repuesto}
    o_repuestos[2] = {"t": "Eliminar repuesto", "f": del_repuesto}
    o_repuestos[3] = {"t": "Listar repuestos", "f": list_repuesto}
    o_repuestos[4] = {"t": "Volver", "f": menu}

    o_principal = {}
    o_principal[1] = {"t": "Menú de Clientes", "f": menu_clientes}
    o_principal[2] = {"t": "Menú de Empleados", "f": menu_empleados}
    o_principal[3] = {"t": "Menú de Solicitudes", "f": menu_solicitud}
    o_principal[4] = {"t": "Menú de Equipos", "f": menu_equipos}
    o_principal[5] = {"t": "Menú de Repuestos", "f": menu_repuestos}
    o_principal[6] = {"t": "Terminar ejecución", "f": fin}
