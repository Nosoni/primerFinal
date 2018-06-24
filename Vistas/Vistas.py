# -*- coding: utf-8 -*-
from tkinter import *
from Controlador.VistaUtil import *
from Controlador.Util import *
bgC = "black"
p_pri = "700x400+150+100"
p_sec = "500x300+250+180"

#______________________________________________________________________________
#________________________________Panel Principal_______________________________


class PanelPrincipal(Frame):
    """Panel principal que contiene el menu con las llamadas a las funciones
    del programa"""
    __vista_actual = None

    def __init__(self, panel_master):
        Frame.__init__(self, panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.__panel_master.geometry(p_pri)
        self.__panel_master.title("MENU PRINCIPAL")
        self.__panel_master.protocol("WM_DELETE_WINDOW", "onexit")
        self.__panel_master.resizable(0, 0)
        self.__panel_master.config(bg=bgC)
        menubar = Menu(self.__panel_master)
        self.__panel_master.config(menu=menubar)

        #Menú Cliente
        menu_cliente = Menu(menubar, tearoff=0)
        menu_cliente.add_command(label="Agregar cliente", command=self.add_cliente)
        menu_cliente.add_command(label="Eliminar cliente", command=self.del_cliente)
        menu_cliente.add_command(label="Listar clientes", command=self.list_cliente)
        menu_cliente.add_command(label="Listar clientes detallado", command=self.list_cliente_det)
        menubar.add_cascade(label="Clientes", menu=menu_cliente)

        #Menú Empleado
        menu_empleado = Menu(menubar, tearoff=0)
        menu_empleado.add_command(label="Agregar empleado", command=self.add_empleado)
        menu_empleado.add_command(label="Eliminar empleado", command=self.del_empleado)
        menu_empleado.add_command(label="Listar empleado", command=self.list_empleado)
        menu_empleado.add_command(label="Editar salario", command=self.edit_salario)
        menubar.add_cascade(label="Empleados", menu=menu_empleado)

        #Menú Repuestos
        menu_repuesto = Menu(menubar, tearoff=0)
        menu_repuesto.add_command(label="Agregar repuesto", command=self.add_repuesto)
        menu_repuesto.add_command(label="Eliminar repuesto", command=self.del_repuesto)
        menu_repuesto.add_command(label="Listar repuesto", command=self.list_repuesto)
        menubar.add_cascade(label="Repuestos", menu=menu_repuesto)

        # Menú Equipos
        menu_equipos = Menu(menubar, tearoff=0)
        menu_equipos.add_command(label="Agregar repuesto", command=self.add_equipo)
        menu_equipos.add_command(label="Eliminar repuesto", command=self.del_equipo)
        menu_equipos.add_command(label="Listar repuesto", command=self.list_equipo)
        menubar.add_cascade(label="Repuestos", menu=menu_equipos)

        #Menú Solicitud
        menu_soli = Menu(menubar, tearoff=0)
        menu_soli.add_command(label="Agregar Solicitud", command=self.add_soli)
        menu_soli.add_command(label="Actualizar Solicitud", command=self.act_soli)
        menu_soli.add_command(label="Eliminar solicitud", command=self.del_soli)
        menu_soli.add_command(label="Listar solicitudes", command=self.list_soli)
        menu_soli.add_separator()
        menu_soli.add_command(label="Dar de baja solicitud", command=self.baja_soli)
        menu_soli.add_command(label="Lista de bajas", command=self.list_bajas)
        menubar.add_cascade(label="Solicitud", menu=menu_soli)

        #Menú Ayuda
        menu_ayuda = Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Cargar Datos", command=self.script_cagar_datos)
        menu_ayuda.add_command(label="Acerca del sistema", command=self.info)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

        #Salir
        menubar.add_command(label="Salir", command=self.salir)

    def fin(self):
        guardar_datos()
        exit()
