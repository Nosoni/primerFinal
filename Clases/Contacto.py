# -*- coding: utf-8 -*-
from Controlador.Util import *


class Contacto:
    """Clase que contiene los contactos de las personas"""

    def __init__(self, celular=None, email=None, red_social=None):
        self.celular = celular
        self.email = email
        self.red_social = red_social

    def get_celular(self):
        return self.celular

    def get_email(self):
        return self.email

    def get_red_social(self):
        return self.red_social

    def set_celular(self, celular):
        self.celular = celular

    def set_email(self, email):
        self.email = email

    def set_red_social(self, red_social):
        self.red_social = red_social

    def mostrar_datos(self):
        # Muestra los datos de Contacto
        print("\nDetalles del Contacto\n")
        print("Celular: " + str(self.celular))
        print("Email: " + str(self.email))
        print("Red Social: " + str(self.red_social))

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict({
            "celular": input_alpha("Celular: "),
            "email": input_alpha("Email: "),
            "red_social": input_alpha("Red Social.")})

    prompt_init = staticmethod(prompt_init)
