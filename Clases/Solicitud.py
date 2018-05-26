# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from Controlador.Util import *
import Datos.Bd as bd1


class Solicitud:
    """Clase donde se guardan los datos de la solicitud de reparacion
        ---Se almacenan los datos de los equipos"""

    def __init__(self, solicitud_numero, fecha, cliente, empleado, equipo, presupuesto=0, estado=None):
        self.solicitud_numero = solicitud_numero
        self.fecha = fecha
        self.cliente = cliente
        self.empleado = empleado
        self.equipo = []
        self.equipo.append(equipo)
        self.presupuesto = presupuesto
        self.estado = estado

    def mostrar_datos(self):
        print("\nDetalles de la solicitud\n")
        print(("Nro. Solicitud: {}" + str(self.solicitud_numero)))
        print(("Fecha: {}" + str(self.fecha)))
        print(("Cliente: {}" + str(self.cliente.nombre + " " + self.cliente.apellido)))
        print(("Empleado: {}" + str(self.empleado.nombre + " " + self.empleado.apellido)))
        if self.equipo:
            for equi in self.equipo:
                if equi is not None:
                    equi.mostrar_datos()
        else:
            print("--Sin equipos--")
        print(("Presupuesto: {}" + str(self.presupuesto)))
        print(("Estado: {}" + str(self.estado)))

    def add_equipo(self, equipo):
        self.equipo.append(equipo)

    def calc(self, dias_garantia):
        print("\n----Detalles----")
        print(("Fecha: {}".format(self.fecha)))
        if self.fecha is not None:
            print(("Garantia hasta: {}".format(self.fecha + timedelta(days =dias_garantia))))
        print(("Cliente: {}".format(self.cliente.nombre + " " + self.cliente.apellido)))
        print(("Empleado: {}".format(self.empleado.nombre + " " + self.empleado.apellido)))
        """por cada equipo se consulta por los repuestos utilizados, y el monto de los mismos"""
        money = 0
        if self.equipo:
            for equi in self.equipo:
                for repuesto in equi.repuestos:
                    money += repuesto.precio
        print(("El costo total es de: Gs {}".format(money)))
        print("")

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        print("La fecha se setea automaticamente!")
        f = datetime.now()
        return dict(solicitud_numero=input_entero_r("Ingrese nro. de Solicitud: "),
                    fecha=f,
                    cliente=encontrar_valor(bd1.clientes, input_alpha_r("Ingrese Cédula del cliente: ")),
                    empleado=encontrar_valor(bd1.empleados, input_alpha_r("Ingrese Cédula del empleado: ")),
                    equipo=encontrar_valor(bd1.equipos, input_alpha_r("Ingrese Cód. del equipo: ")),
                    presupuesto=input_entero_r("Ingrese presupuesto: "),
                    estado=(input_opcion("Estado", ("concluido", "pendiente")).lower()))

    prompt_init = staticmethod(prompt_init)
