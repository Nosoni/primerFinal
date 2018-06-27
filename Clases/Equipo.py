# -*- coding: utf-8 -*-
from Controlador.Util import *
import Datos.Bd as bd1


class Equipo():
    """Clase que permite crear a los equipos a reparar de una solicitud"""

    def __init__(self, nro_equipo, tipo, marca, modelo, detalle=None,
        detalle_problema=None, repuesto=None):
        """nro_equipo servirá para la búsqueda por identificador, y no por objeto
        evitamos que el usuario tipee todos los datos de la clase"""
        self.nro_equipo = nro_equipo
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.detalle = detalle  # hace referencia al/los detalles físicos del equipo
        self.detalle_problema = detalle_problema
        self.repuestos = []
        self.repuestos.append(repuesto)

    def add_repuesto(self):
        """Comprueba si el repuesto que se quiere anhadir es instancia de la
        clase repuesto"""
        try:
            self.repuestos.append(encontrar_valor(bd1.repuestos, input_alpha_r("Ingrese Cód. del equipo: ")))
        except:
            print("Error inesperado.")
        else:
            print("Repuesto agregado.")

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict(
            nro_equipo=input_entero_r("Ingrese nro de equipo"),
            tipo=input_opcion("Tipo", ("notebook", "pc mesa", "impresora", "monitor", "otro")),
            marca=input_alpha("Marca"),
            modelo=input_alpha("Modelo"),
            detalle=input_alpha("Detalle fisico"),
            detalle_problema=input_alpha_r("Detalle problema"))

    prompt_init = staticmethod(prompt_init)
