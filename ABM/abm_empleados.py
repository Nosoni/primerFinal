# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.Persona import Empleado
from Clases.Contacto import Contacto
from Controlador.Util import encontrar_valor
from Controlador.VistaUtil import del_datos


class AddEmpleado(PanedWindow):
    """Panel que contien los campos para introducir los datos de un empleado"""

    cedula_entry = None
    nombre_entry = None
    apellido_entry = None
    direccion_entry = None
    cel_entry = None
    email_entry = None
    red_social_entry = None
    salario_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos del Empleado").grid(row=1, column=2)
        Label(self, text="Cédula*: ").grid(row=2, column=1)
        Label(self, text="Nombre*: ").grid(row=3, column=1)
        Label(self, text="Apellido*: ").grid(row=4, column=1)
        Label(self, text="Dirección: ").grid(row=5, column=1)
        Label(self, text="Contactos: ").grid(row=7, column=1)
        Label(self, text="Celular: ").grid(row=6, column=2)
        Label(self, text="Email: ").grid(row=7, column=2)
        Label(self, text="Red Social: ").grid(row=8, column=2)
        Label(self, text="Sueldo*: ").grid(row=9, column=1)
        Button(self, text="GUARDAR", command=self.a_emp).grid(row=10, column=3)

        self.get_cedula_entry()
        self.get_nombre_entry()
        self.get_apellido_entry()
        self.get_direccion_entry()
        self.get_cel_entry()
        self.get_email_entry()
        self.get_red_social_entry()
        self.get_salario_entry()

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

    def get_salario_entry(self):
        if not self.salario_entry:
            self.salario_entry = Entry(master=self, width=20)
            self.salario_entry.grid(row=9, column=2)
        return self.salario_entry

    def val_emp(self, ced, nom, ape, salario):
        val = False
        if ((salario.isdigit() or salario != "") and ced != "" and
        nom != "" and ape != ""):
            val = True
        else:
            messagebox.showinfo("", "Ingrese correctamente los datos del " +
                "empleado")
        return val

    def val_cont(self, cel, mail, red):
        val = False
        if cel != "" or mail != "" or red != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese por lo menos 1 contacto")
        return val

    def a_emp(self):
        try:
            cel = self.get_cel_entry().get()
            mail = self.get_email_entry().get()
            red_social = self.get_red_social_entry().get()
            salario = self.get_salario_entry().get()
            ced = self.get_cedula_entry().get()
            nom = self.get_nombre_entry().get()
            ape = self.get_apellido_entry().get()
            dre = self.get_direccion_entry().get()

            if (self.val_emp(ced, nom, ape, salario) and
            self.val_cont(cel, mail, red_social)):
                self.contacto = Contacto(cel, mail, red_social)
                bd.empleados.append(Empleado(**{"cedula": ced, "nombre": nom,
                    "apellido": ape, "direccion": dre,
                    "contacto": self.contacto, "salario": salario}))
                messagebox.showinfo("Informacion", "Empleado agregado")
                self.destroy()
        except Exception as e:
            messagebox.showerror("Error", e)


class DelEmpleado(PanedWindow):
    """Panel que contien los campos para eliminar un empleado"""
    cedula_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Ingrese cédula del empleado*: ").grid(row=2, column=1)
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
            if messagebox.askyesno("Eliminar", "Eliminar empleado?"):
                val = encontrar_valor(bd.empleados, "cedula", self.get_cedula_entry().get())
                if val is not None:
                    if del_datos(bd.empleados, val):
                        messagebox.showinfo("Eliminado", "Empleado eliminado")
                        self.destroy()
                    else:
                        messagebox.showinfo("Atención", "Ocurrió un error al eliminar dato.")
                        self.destroy()
                else:
                    messagebox.showwarning("Atención", "No existe Empleado.")
        except:
            messagebox.showerror("Error", "Ocurrió un error inesperado al elimnar el empleado.")


class EditSalarioEmpleado(PanedWindow):
    """Panel que contien los campos para editar un empleado"""
    cedula_entry = None
    salario_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese dato requiero del Empleado a editar", ).grid(row=1, column=2)
        Label(self, text="Ingrese cédula del empleado*: ").grid(row=2, column=1)
        Label(self, text="Nuevo salario*: ").grid(row=3, column=1)
        Button(self, text="Guardar", command=self.edit_salario).grid(
            row=4, column=2)

        self.get_cedula_entry()
        self.get_salario_entry()

    def get_cedula_entry(self):
        if not self.cedula_entry:
            self.cedula_entry = Entry(master=self, width=20)
            self.cedula_entry.grid(row=2, column=2)
        return self.cedula_entry

    def get_salario_entry(self):
        if not self.salario_entry:
            self.salario_entry = Entry(master=self, width=20)
            self.salario_entry.grid(row=3, column=2)
            self.salario_entry.grid(row=3, column=2)
        return self.salario_entry

    def edit_salario(self):
        try:
            if self.val_cedula(self.get_cedula_entry().get()):
                if messagebox.askyesno("Eliminar", "Eliminar empleado?"):
                    val = encontrar_valor(bd.empleados, "cedula", self.get_cedula_entry().get())
                    if val is not None:
                        if self.val_salario(self.get_salario_entry().get()):
                            val.salario = self.get_salario_entry().get()
                            messagebox.showinfo("Editado", "Editado con éxito.")
                            self.destroy()
                        else:
                            messagebox.showinfo("Editado", "Ingrese el salario.")
                    else:
                        messagebox.showwarning("Atención", "No existe Empleado.")
                        self.destroy()
            else:
                messagebox.showwarning("Atención", "Ingrese nro. de cédula.")
        except:
            messagebox.showerror("Error", "Ocurrió un error inesperado al elimnar el empleado.")

    def val_salario(self, salario):
        val = False
        if salario != "":
            val = True
        return val

    def val_cedula(self, cedula):
        val = False
        if cedula != "":
            val = True
        return val
