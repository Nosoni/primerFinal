# -*- coding: utf-8 -*-
import os
from pickle import load


# ________________________________FRAMEWORK__________________________________________
# Validadores para distintos casos y necesidades
def cls():
    """Permite limpiar la consola de python para que sea mas comodo usarla"""
    os.system("clear")


def cls_():
    """Permite limpiar la consola de python para que sea mas comodo usarla
       Muestra un mensaje"""
    cls()
    print("\n\n--==Ingrese datos (Campos con * son obligatorios)==--\n")


def input_range(text, men, may):
    """ Solicita un valor entero dentro de un rango y se devuelve
        Se introduce el texto a mostrar y el rango de valor minimo y maximo"""
    while True:
        valor = input("{} ({}-{}) *: ".format(text, men, may))
        try:
            valor = int(valor)
            if valor <= may and valor >= men:
                return valor
            else:
                raise ValueError
        except ValueError:
            pass


def input_opcion(text, opciones):
    """ Solicita un valor que debe estar presente en la lista opciones"""
    text += " ({})*: ".format(", ".join(opciones))
    val = input(text)
    while val.lower() not in opciones:
        val = input(text)
    return val.lower()


def input_entero(text):
    """ Solicita un valor entero y lo devuelve.
        Si se introduce una cadena vuelve a solicitarlo
        Si no se introduce nada devuelve 0 """
    while True:
        valor = input("{}: ".format(text))
        try:
            valor = int(valor)
            return valor
        except ValueError:
            if valor is "":
                return None


def input_entero_r(text):
    """ Solicita un valor entero y lo devuelve. (es requerido)
        Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
    while True:
        valor = input("{} *: ".format(text))
        try:
            valor = int(valor)
            return valor
        except ValueError:
            pass


def input_alpha(text):
    """ Solicita una cadena"""
    while True:
        valor = input("{}: ".format(text))
        try:
            return valor
        except ValueError:
            pass


def input_alpha_r(text):
    """ Solicita una cadena (requerido)"""
    while True:
        valor = input("{} *: ".format(text))
        try:
            if valor is not "":
                return valor
            else:
                raise ValueError
        except ValueError:
            pass


def abrir(path, modo):
    """Recibe una direccion y modo de apertura de archivo/fichero
    y retorna el archivo"""
    try:
        f = open(path, modo)
        return f
    except:
        print("Verifique, no se pudo encontrar el archivo " + path)
    else:
        return f


def cargar(f):
    """Recibe un fichero con un objeto serializado, retorna el objeto"""
    try:
        obj = load(f)
    except:
        return []
    else:
        return obj


def encontrar_valor(lista, text):
    for val in lista:
        if str(val.cedula) == text:
            return val
