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
        self.equipos = []
        self.equipos.append(equipo)
        self.presupuesto = presupuesto
        self.estado = estado

    def add_equipo(self, equipo):
        self.equipos.append(equipo)

    def calc(self):
        money = 0
        if self.equipos:
            for equipo in self.equipos:
                for repuesto in equipo.repuestos:
                    money += repuesto.precio
        return money

    def cambiar_estado(self):
        self.estado = "concluido"

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto.
        La solicitud ingresa en estado pendiente por default"""
        print("La fecha se setea automaticamente!")
        f = datetime.now()
        return dict(solicitud_numero=input_entero_r("Ingrese nro. de Solicitud: "),
                    fecha=f,
                    cliente=encontrar_valor(bd1.clientes, input_alpha_r("Ingrese Cédula del cliente")),
                    empleado=encontrar_valor(bd1.empleados, input_alpha_r("Ingrese Cédula del empleado")),
                    equipo=encontrar_valor(bd1.equipos, input_alpha_r("Ingrese Cód. del equipo")),
                    presupuesto=input_entero_r("Ingrese presupuesto3"),
                    estado="pendiente")

    prompt_init = staticmethod(prompt_init)
