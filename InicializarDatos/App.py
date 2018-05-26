# -*- coding: utf-8 -*-
from Clases.Negocio import Negocio
from InicializarDatos.ScriptCargaDatos import cargar_datos

if __name__ == "__main__":
    cargar_datos()
    app = Negocio()
    app.menu()
