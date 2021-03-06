# -*- coding: utf-8 -*-
from Controlador.Util import *


class Contacto:
    """Clase que contiene los contactos de las personas"""

    def __init__(self, celular=None, email=None, red_social=None):
        self.celular = celular
        self.email = email
        self.red_social = red_social

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict({
            "celular": input_alpha("Celular"),
            "email": input_alpha("Email"),
            "red_social": input_alpha("Red Social")})

    prompt_init = staticmethod(prompt_init)
