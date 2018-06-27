# -*- coding: utf-8 -*-
from tkinter import *
from Controlador.VistaUtil import *
from Controlador.Util import *
from ABM.abm_clientes import *
from ABM.abm_empleados import *
from ABM.abm_repuestos import *
from ABM.abm_solicitudes import *
from ABM.abm_contactos import *
from Controlador.Util import encontrar_valor
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
        self.__vista_actual = PanelLogin(panel_master)
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
        menu_cliente.add_command(label="Editar cliente", command=self.edit_cliente)
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
        menu_ayuda.add_command(label="Acerca del sistema", command=self.info)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

        #Salir
        menu_opciones = Menu(menubar, tearoff=0)
        menu_opciones.add_command(label="Cerrar Sesión", command=self.cerrar_sesion)
        menu_opciones.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Opciones", menu=menu_opciones)

    def cerrar_sesion(self):
        self.limpiar()
        self.__vista_actual = PanelLogin(self.__panel_master)

    def salir(self):
        guardar_datos()
        exit()

    def limpiar(self):
        if self.__vista_actual:
            self.__vista_actual.destroy()

    def accion(self):
        messagebox.showinfo("Info", "No implementado")

    def info(self):
        messagebox.showinfo("Informacion", "Versión del sistema 0.1")

    def add_cliente(self):
        self.limpiar()
        form = AddCliente(self.__panel_master)
        self.__vista_actual = form

    def del_cliente(self):
        self.limpiar()
        form = DelCliente(self.__panel_master)
        self.__vista_actual = form

    def list_cliente(self):
        pass

    def list_cliente_det(self):
        pass

    def edit_cliente(self):
        self.limpiar()
        form = AddContacto(self.__panel_master)
        self.__vista_actual = form

    def add_empleado(self):
        self.limpiar()
        form = AddEmpleado(self.__panel_master)
        self.__vista_actual = form

    def del_empleado(self):
        self.limpiar()
        form = DelEmpleado(self.__panel_master)
        self.__vista_actual = form

    def list_empleado(self):
        pass

    def edit_salario(self):
        pass

    def add_repuesto(self):
        self.limpiar()
        form = AddRepuesto(self.__panel_master)
        self.__vista_actual = form

    def del_repuesto(self):
        self.limpiar()
        form = DelRepuesto(self.__panel_master)
        self.__vista_actual = form

    def list_repuesto(self):
        pass

    def add_equipo(self):
        self.limpiar()
        #form = AddEquipo(self.__panel_master)
        #self.__vista_actual = form

    def del_equipo(self):
        self.limpiar()
        #form = DelEquipo(self.__panel_master)
        #self.__vista_actual = form

    def list_equipo(self):
        pass

    def add_soli(self):
        self.limpiar()
        form = AddSoli(self.__panel_master)
        self.__vista_actual = form

    def act_soli(self):
        self.limpiar()
        form = ActSoli(self.__panel_master)
        self.__vista_actual = form

    def del_soli(self):
        self.limpiar()
        form = DelSoli(self.__panel_master)
        self.__vista_actual = form

    def list_soli(self):
        pass

    def baja_soli(self):
        self.limpiar()
        form = BajaSoli(self.__panel_master)
        self.__vista_actual = form

    def list_bajas(self):
        pass


class PanelLogin(PanedWindow):
    """Panel de login"""
    user = None
    password = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()
        self.grab_set()  # deshabilita las otras ventanas hasta que esta se destruya

    def inicializar(self):
        self.__panel_master.geometry(p_pri)
        self.__panel_master.title("MENU Login")
        self.__panel_master.protocol("WM_DELETE_WINDOW", "onexit")
        self.__panel_master.resizable(0, 0)
        self.__panel_master.config(bg=bgC)
        Label(self, text="Usuario").grid(row=1, column=1)
        Label(self, text="Contraseña: ").grid(row=2, column=1)
        Button(self, text="Login", command=self.login).grid(row=3, column=2)

        self.get_user()
        self.get_password()

    def get_user(self):
        if not self.user:
            self.user = Entry(master=self, textvariable=StringVar())
            self.user.grid(row=1, column=2)
            return self.user

    def get_password(self):
        if not self.password:
            self.password = Entry(master=self, textvariable=StringVar(), show="•")
            self.password.grid(row=2, column=2)
        return self.password

    def login(self):
        val = encontrar_valor(bd.usuarios, "user", self.user.get())
        if val is not None:
            if val.activo:
                if val.password is not None:
                    if val.password == self.password.get():
                        messagebox.showinfo("", "Login exitoso.")
                        self.destroy()
                    else:
                        messagebox.showwarning("Atención", "Datos incorrectos")
                else:
                    messagebox.showwarning("Atención", "No es posible verificar usuario")
            else:
                messagebox.showwarning("Atención", "Usuario Inactivo")
        else:
            messagebox.showwarning("Atención", "No existe usuario")
