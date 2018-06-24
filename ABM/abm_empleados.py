# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.Persona import Empleado
from Clases.Contacto import Contacto
from datetime import datetime


class AddEmpleado(PanedWindow):
    """Panel que contien los campos para introducir los datos de un empleado"""

    cedula_entry = None
    nombre_entry = None
    apellido_entry = None
    direccion_entry = None
    tel_entry = None
    cel_entry = None
    email_entry = None
    tecnico_entry = None
    sueldo_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos de la solicitud", ).grid(
            row=1, column=2)
        Label(self, text="Cedula*: ").grid(row=2, column=1)
        Label(self, text="Nombre*: ").grid(row=3, column=1)
        Label(self, text="Apellido*: ").grid(row=4, column=1)
        Label(self, text="Direccion: ").grid(row=5, column=1)
        Label(self, text="Contactos*: ").grid(row=7, column=1)
        Label(self, text="tel.: ").grid(row=6, column=2)
        Label(self, text="cel.: ").grid(row=7, column=2)
        Label(self, text="email: ").grid(row=8, column=2)
        Label(self, text="Tecnico*: ").grid(row=9, column=1)
        Label(self, text="Sueldo: ").grid(row=10, column=1)
        Button(self, text="GUARDAR", command=self.a_emp).grid(row=11, column=3)

        self.get_cedula_entry()
        self.get_nombre_entry()
        self.get_apellido_entry()
        self.get_direccion_entry()
        self.get_tel_entry()
        self.get_cel_entry()
        self.get_email_entry()
        self.get_tecnico_entry()
        self.get_sueldo_entry()

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

    def get_tel_entry(self):
        if not self.tel_entry:
            self.tel_entry = Entry(master=self, width=20)
            self.tel_entry.grid(row=6, column=3)
        return self.tel_entry

    def get_cel_entry(self):
        if not self.cel_entry:
            self.cel_entry = Entry(master=self, width=20)
            self.cel_entry.grid(row=7, column=3)
        return self.cel_entry

    def get_email_entry(self):
        if not self.email_entry:
            self.email_entry = Entry(master=self, width=20)
            self.email_entry.grid(row=8, column=3)
        return self.email_entry

    def get_tecnico_entry(self):
        if not self.tecnico_entry:
            self.tecnico = StringVar()
            self.tecnico_entry = Radiobutton(self, text="Si", value="si",
                variable=self.tecnico)
            self.tecnico_entry.grid(row=9, column=2)
            self.tecnico_entry = Radiobutton(self, text="No", value="no",
                variable=self.tecnico)
            self.tecnico_entry.grid(row=9, column=3)
        return self.tecnico

    def get_sueldo_entry(self):
        if not self.sueldo_entry:
            self.sueldo_entry = Entry(master=self, width=20)
            self.sueldo_entry.grid(row=10, column=2)
        return self.sueldo_entry

    def val_emp(self, tec, sue, ced, nom, ape, dre):
        val = False
        if (tec != "" and (sue.isdigit() or sue == "") and ced.isdigit() and
        nom != "" and ape != ""):
            val = True
        else:
            messagebox.showinfo("", "Ingrese correctamente los datos del " +
                "empleado")
        return val

    def val_cont(self, tel, cel, mail):
        val = False
        if tel != "" or cel != "" or mail != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese por lo menos 1 contacto")
        return val

    def a_emp(self):
        try:
            tel = self.get_tel_entry().get()
            cel = self.get_cel_entry().get()
            mail = self.get_email_entry().get()
            tec = self.get_tecnico_entry().get()
            sue = self.get_sueldo_entry().get()
            ced = self.get_cedula_entry().get()
            nom = self.get_nombre_entry().get()
            ape = self.get_apellido_entry().get()
            dre = self.get_direccion_entry().get()

            if (self.val_emp(tec, sue, ced, nom, ape, dre) and
            self.val_cont(tel, cel, mail)):
                self.contacto = Contacto(tel, cel, mail)
                bd.empleados.append(Empleado(**{
                    "tecnico": tec, "fecha_ini": datetime.now(),
                    "sueldo": sue, "cedula": ced, "nombre": nom,
                    "apellido": ape, "direccion": dre,
                    "contacto": self.contacto}))
                messagebox.showinfo("Informacion", "Empleado agregado")
                self.destroy()
        except Exception as e:
            messagebox.showerror('Error', e)


class DelEmpleado(PanedWindow):
    """Panel que contien los campos para eliminar un empleado"""
    soli_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Ingrese numero de empleado*: ").grid(row=2, column=1)
        Button(self, text="Eliminar", command=self.eliminar).grid(
            row=3, column=1)

        self.get_soli_entry()

    def get_soli_entry(self):
        if not self.soli_entry:
            self.soli_entry = Entry(master=self, width=20)
            self.soli_entry.grid(row=2, column=2)
        return self.soli_entry

    def eliminar(self):
        try:
            pos = int(self.get_soli_entry().get())
            if(messagebox.askyesno("Eliminar", "Eliminar empleado?")):
                bd.empleados.pop(pos - 1)
                messagebox.showinfo("Eliminado", "Empleado eliminado")
                self.destroy()
        except:
            messagebox.showerror("Infor", "No existe empleado")