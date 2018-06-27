# -*- coding: utf-8 -*-
from abc import ABCMeta
from Clases.Contacto import *


class Persona(metaclass=ABCMeta):
    """Clase padre que permite crear un objeto de tipo persona"""

    def __init__(self, cedula, nombre, apellido, direccion=None,
                 contacto=None):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.contactos = []
        self.contactos.append(contacto)

    def add_contacto(self, contacto):
        # Agrega contactos a la Persona
        self.contactos.append(contacto)

    def editar_contacto(self, contacto_viejo, contacto_nuevo):
        # Edita un contacto
        self.borrar_contacto(contacto_viejo)
        self.add_contacto(contacto_nuevo)

    def borrar_contacto(self, contacto):
        # Elimina un contacto
        self.contactos.remove(contacto)

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict(cedula=input_entero_r("Ingrese cédula"),
                    nombre=input_alpha_r("Ingrese Nombre").title(),
                    apellido=input_alpha_r("Ingrese Apellido").title(),
                    direccion=input_alpha("Ingrese Dirección"))

    prompt_init = staticmethod(prompt_init)


class Empleado(Persona):
    """Clase extendida de Persona que detalla al Empleado"""

    cant_empleado = 0

    def __init__(self, cedula, nombre, apellido, direccion=None,
                 contacto=None, salario=0):
        super().__init__(cedula, nombre, apellido, direccion, contacto)
        self.salario = salario
        self.__class__.cant_empleado += 1

    def actualizar_salario(self, salario):
        self.salario = salario

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        parent_init = Persona.prompt_init()
        datos = Contacto.prompt_init()
        contacto = Contacto(**datos)
        salario = input_entero_r("Ingrese Salario")
        parent_init.update({"contacto": contacto,
                            "salario": salario})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Jefe(Empleado):
    """Clase extendida de Empleado que permite al empleado cancelar
    solicitud"""

    cant_jefe = 0

    def __init__(self, cedula, nombre, apellido, direccion,
                 contacto=None, salario=0):
        Empleado.__init__(self, cedula, nombre, apellido, direccion,
                          contacto, salario)
        self.__class__.cant_jefe += 1

    def cancelar_solicitud(self):
        # Metodo para cancelar una solicitud
        pass


class Cliente(Persona):
    """Clase extendida de Persona que detalla a un Cliente"""

    cant_cliente = 0

    def __init__(self, cedula, nombre, apellido, direccion,
                 contacto=None, ruc=None):
        super().__init__(cedula, nombre, apellido, direccion,
                         contacto)
        self.ruc = ruc
        self.__class__.cant_cliente += 1

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        parent_init = Persona.prompt_init()
        datos = Contacto.prompt_init()
        contacto = Contacto(**datos)
        ruc = input_alpha("Ingrese Ruc")
        parent_init.update({"contacto": contacto,
                            "ruc": ruc})
        return parent_init

    prompt_init = staticmethod(prompt_init)
