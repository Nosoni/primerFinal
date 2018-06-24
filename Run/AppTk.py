# -*- coding: utf-8 -*-

import tkinter as tk
from Vistas.Vistas import PanelPrincipal
from InicializarDatos.ScriptCargaDatos import inicializar_datos

inicializar_datos()
root = tk.Tk()
vista_principal = PanelPrincipal(root)
root.mainloop()
root.destroy()
