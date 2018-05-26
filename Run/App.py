# -*- coding: utf-8 -*-
from Clases.Negocio import Negocio
from InicializarDatos.ScriptCargaDatos import inicializar_datos

if __name__ == "__main__":
    inicializar_datos()
    app = Negocio()
    app.menu()
