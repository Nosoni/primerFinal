# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.Persona import Cliente
from Clases.Contacto import Contacto
from Controlador.Util import encontrar_valor
from Controlador.VistaUtil import del_datos


class AddCliente(PanedWindow):
    """Panel que contien los campos para introducir los datos de un cliente"""

    cedula_entry = None
    nombre_entry = None
    apellido_entry = None
    direccion_entry = None
    cel_entry = None
    email_entry = None
    red_social_entry = None
    ruc_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos del Cliente").grid(row=1, column=2)
        Label(self, text="Cédula*: ").grid(row=2, column=1)
        Label(self, text="Nombre*: ").grid(row=3, column=1)
        Label(self, text="Apellido*: ").grid(row=4, column=1)
        Label(self, text="Dirección: ").grid(row=5, column=1)
        Label(self, text="Contactos: ").grid(row=7, column=1)
        Label(self, text="Celular: ").grid(row=6, column=2)
        Label(self, text="Email: ").grid(row=7, column=2)
        Label(self, text="Red Social: ").grid(row=8, column=2)
        Label(self, text="Ruc: ").grid(row=9, column=1)
        Button(self, text="GUARDAR", command=self.a_cli).grid(row=10, column=3)

        self.get_cedula_entry()
        self.get_nombre_entry()
        self.get_apellido_entry()
        self.get_direccion_entry()
        self.get_cel_entry()
        self.get_email_entry()
        self.get_red_social_entry()
        self.get_ruc_entry()

    def get_cedula_entry(self):
        if not self.cedula_entry:
            self.cedula_entry = Entry(master=self, width=20)
            self.cedula_entry.grid(row=2, column=2)
        return self.cedula_entry

    def get_nombre_entry(self):
        if not self.nombre_entry:
            self.nombre_entry = Entry(master=self, width=20)
            self.nombre_entry.grid(row=3, column=2)
        return self.nombre_entry

    def get_apellido_entry(self):
        if not self.apellido_entry:
            self.apellido_entry = Entry(master=self, width=20)
            self.apellido_entry.grid(row=4, column=2)
        return self.apellido_entry

    def get_direccion_entry(self):
        if not self.direccion_entry:
            self.direccion_entry = Entry(master=self, width=20)
            self.direccion_entry.grid(row=5, column=2)
        return self.direccion_entry

    def get_cel_entry(self):
        if not self.cel_entry:
            self.cel_entry = Entry(master=self, width=20)
            self.cel_entry.grid(row=6, column=3)
        return self.cel_entry

    def get_email_entry(self):
        if not self.email_entry:
            self.email_entry = Entry(master=self, width=20)
            self.email_entry.grid(row=7, column=3)
        return self.email_entry

    def get_red_social_entry(self):
        if not self.red_social_entry:
            self.red_social_entry = Entry(master=self, width=20)
            self.red_social_entry.grid(row=8, column=3)
        return self.red_social_entry

    def get_ruc_entry(self):
        if not self.ruc_entry:
            self.ruc_entry = Entry(master=self, width=20)
            self.ruc_entry.grid(row=9, column=2)
        return self.ruc_entry

    """def a_cont(self):
        form = AddContacto(self.__panel_master)
        self.__vista_actual = form"""

    def a_cli(self):
        try:
            cel = self.get_cel_entry().get()
            mail = self.get_email_entry().get()
            red_social = self.get_red_social_entry().get()
            ced = self.get_cedula_entry().get()
            nom = self.get_nombre_entry().get()
            ape = self.get_apellido_entry().get()
            dre = self.get_direccion_entry().get()

            if (self.val_cli(ced, nom, ape) and
            self.val_cont(cel, mail, red_social)):
                self.contacto = Contacto(cel, mail, red_social)
                bd.clientes.append(Cliente(**{"ruc": self.get_ruc_entry().get(),
                "cedula": ced, "nombre": nom, "apellido": ape, "direccion": dre,
                "contacto": self.contacto}))
                messagebox.showinfo("Informacion", "Cliente agregado")
                self.destroy()
        except Exception as e:
            messagebox.showerror("Error", e)

    def val_cli(self, ced, nom, ape):
        val = False
        if ced.isdigit() and nom != "" and ape != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese correctamente los datos del cliente")
        return val

    def val_cont(self, cel, mail, red_social):
        val = False
        if red_social != "" or cel != "" or mail != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese por lo menos 1 contacto")
        return val


class DelCliente(PanedWindow):
    """Panel que contien los campos para eliminar un cliente"""
    cedula_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Ingrese numero de cliente*: ").grid(row=2, column=1)
        Button(self, text="Eliminar", command=self.eliminar).grid(
            row=3, column=1)

        self.get_cedula_entry()

    def get_cedula_entry(self):
        if not self.cedula_entry:
            self.cedula_entry = Entry(master=self, width=20)
            self.cedula_entry.grid(row=2, column=2)
        return self.cedula_entry

    def eliminar(self):
        try:
            if messagebox.askyesno("Eliminar", "Eliminar cliente?"):
                val = encontrar_valor(bd.clientes, "cedula", self.get_cedula_entry().get())
                if val is not None:
                    if del_datos(bd.clientes, val):
                        messagebox.showinfo("Eliminado", "Cliente eliminado")
                        self.destroy()
                    else:
                        messagebox.showinfo("Atención", "Ocurrió un error al eliminar dato.")
                        self.destroy()
                else:
                    messagebox.showwarning("Atención", "No existe Cliente.")
        except:
            messagebox.showerror("Error", "Ocurrió un error inesperado al elimnar el cliente.")
