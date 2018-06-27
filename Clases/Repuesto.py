# -*- coding: utf-8 -*-
from Controlador.Util import *
from abc import ABCMeta, abstractmethod


class Repuesto(metaclass=ABCMeta):
    """Clase que contiene el detalle de los repuestos para las reparaciones
    de los equipos"""

    cant_repuesto = 0

    def __init__(self, cod, marca, modelo, precio=0):
        self.cod = cod
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.__class__.cant_repuesto += 1

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict(cod=input_alpha("Código"),
                    marca=input_alpha_r("Marca"),
                    modelo=input_alpha("Modelo"),
                    precio=input_entero_r("Precio"))

    prompt_init = staticmethod(prompt_init)


class Disco(Repuesto):
    """Contiene los detalles de los discos"""

    cant_disco = 0

    def __init__(self, cod, marca, modelo, precio=0, capacidad=0):
        super().__init__(cod, marca, modelo, precio)
        self.capacidad = capacidad
        self.__class__.cant_disco += 1

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        parent_init = Repuesto.prompt_init()
        capacidad = input_entero_r("Ingrese capacidad de disco (GB)")
        parent_init.update({
            "capacidad": capacidad})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Cartucho(Repuesto):
    """Contiene un dato que indica si la tinta es de color o no"""
    # es_color = ("si", "no")

    cant_cartucho = 0

    def __init__(self, cod, marca, modelo, precio=0, color=""):
        super().__init__(cod, marca, modelo, precio)
        self.color = color
        self.__class__.cant_cartucho += 1

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        parent_init = Repuesto.prompt_init()
        color = input_opcion("Cartucho es de color", ("si", "no"))
        parent_init.update({
            "color": color})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Memoria(Repuesto):
    """Contiene la capacidad de la memoria"""

    cant_memoria = 0

    def __init__(self, cod, marca, modelo, precio=0, capacidad=0):
        super().__init__(cod, marca, modelo, precio)
        self.capacidad = capacidad
        self.__class__.cant_memoria += 1

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        parent_init = Repuesto.prompt_init()
        capacidad = input_entero_r("Capacidad de memoria (GB)")
        parent_init.update({
            "capacidad": capacidad})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Otro(Repuesto):
    """Contiene el tipo de repuesto y los datos basicos"""

    cant_otro = 0

    def __init__(self, cod, marca, modelo, precio=0, tipo=""):
        super().__init__(cod, marca, modelo, precio)
        self.tipo = tipo
        self.cant_otro += 1

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        tipo = input_alpha_r("Tipo de repuesto")
        parent_init = Repuesto.prompt_init()
        parent_init.update({
            "tipo": tipo})
        return parent_init

    prompt_init = staticmethod(prompt_init)
