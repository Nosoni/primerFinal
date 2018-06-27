# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from Clases.Equipo import *
import Datos.Bd as bd
from Controlador.Util import encontrar_valor
from Controlador.VistaUtil import del_datos


class AddEquipo(PanedWindow):
    """Panel que contien los campos para introducir los datos de un repuesto"""

    nro_entry = None
    tipo_entry = None
    marca_entry = None
    modelo_entry = None
    detalle_entry = None
    detalle_problema_entry = None
    repuesto_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.repuestoArray = []
        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Nro equipo*: ", ).grid(row=2, column=1)
        Label(self, text="Seleccione tipo de Equipo*: ").grid(
            row=3, column=1)
        Label(self, text="Marca*: ").grid(row=4, column=1)
        Label(self, text="Modelo*: ").grid(row=5, column=1)
        Label(self, text="Detalle*: ", ).grid(row=6, column=1)
        Label(self, text="Detalle físico del equipo.", ).grid(row=6, column=3)
        Label(self, text="Detalle del problema*: ").grid(row=7, column=1)
        Label(self, text="Repuesto: ").grid(row=8, column=1)
        Button(self, text="Agregar Repuesto", command=self.a_rep).grid(row=8, column=3)
        Button(self, text="GUARDAR", command=self.a_equi).grid(row=9, column=1)

        self.get_nro_entry()
        self.get_tipo_entry()
        self.get_marca_entry()
        self.get_modelo_entry()
        self.get_detalle_entry()
        self.get_detalle_problema_entry()
        self.get_repuesto_entry()

    def get_nro_entry(self):
        if not self.nro_entry:
            self.nro_entry = Entry(master=self, width=15)
            self.nro_entry.grid(row=2, column=2)
        return self.nro_entry

    def get_tipo_entry(self):
        if not self.tipo_entry:
            self.tipo = StringVar()
            self.tipo_entry = Radiobutton(self, text="Notebook",
                value="notebook", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=2)
            self.tipo_entry = Radiobutton(self, text="Computadora",
                value="computadora", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=3)
            self.tipo_entry = Radiobutton(self, text="Impresora",
                value="impresora", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=4)
            self.tipo_entry = Radiobutton(self, text="Monitor",
                value="monitor", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=5)
            self.tipo_entry = Radiobutton(self, text="Otro",
                value="otro", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=6)
        return self.tipo

    def get_marca_entry(self):
        if not self.marca_entry:
            self.marca_entry = Entry(master=self, width=15)
            self.marca_entry.grid(row=4, column=2)
        return self.marca_entry

    def get_modelo_entry(self):
        if not self.modelo_entry:
            self.modelo_entry = Entry(master=self, width=15)
            self.modelo_entry.grid(row=5, column=2)
        return self.modelo_entry

    def get_detalle_entry(self):
        if not self.detalle_entry:
            self.detalle_entry = Entry(master=self, width=15)
            self.detalle_entry.grid(row=6, column=2)
        return self.detalle_entry

    def get_detalle_problema_entry(self):
        if not self.detalle_problema_entry:
            self.detalle_problema_entry = Entry(master=self, width=15)
            self.detalle_problema_entry.grid(row=7, column=2)
        return self.detalle_problema_entry

    def get_repuesto_entry(self):
        if not self.repuesto_entry:
            self.repuesto_entry = Entry(master=self, width=15)
            self.repuesto_entry.grid(row=8, column=2)
        return self.repuesto_entry

    def a_equi(self):
        try:
            nro = self.get_nro_entry().get()
            tipo = self.get_tipo_entry().get()
            mar = self.get_marca_entry().get()
            mod = self.get_modelo_entry().get()
            det = self.get_detalle_entry().get()
            det_pro = self.get_detalle_problema_entry().get()

            if self.val_equi(nro, tipo, mar, mod, det_pro):
                bd.equipos.append(Equipo(nro, tipo, mar, mod, det, det_pro, self.repuestoArray))
                messagebox.showinfo("Informacion", "Equipo agregado.")
                self.destroy()
        except Exception as e:
                messagebox.showerror("Error", e)

    def val_equi(self, nro, tipo, mar, mod, det_pro):
        val = False
        if (nro != "" or nro.isdigit()) and mar != "" and mod != "" and det_pro != "":
            if tipo != "":
                val = True
            else:
                messagebox.showinfo("", "Ingrese dato correspondiente al repuesto.")
                val = False
        else:
            messagebox.showinfo("", "Ingrese datos necesarios del repuesto.")
        return val

    def a_rep(self):
        try:
            if self.get_repuesto_entry().get() != "":
                if messagebox.askyesno("Editar", "Desea agregar el repuesto?"):
                    val = encontrar_valor(bd.repuestos, "cod", self.get_repuesto_entry().get())
                    if val is not None:
                        self.repuestoArray.append(val)
                        messagebox.showinfo("Agregado", "Agregado con éxito.")
                    else:
                        messagebox.showwarning("Atención", "No existe repuesto.")
            else:
                messagebox.showwarning("Atención", "Ingrese el código del repuesto.")
        except Exception as e:
            messagebox.showerror("Error", e)


class DelEquipo(PanedWindow):
    """Panel que contien los campos para eliminar un repuesto"""
    nro_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Ingrese número de equipo*: ").grid(row=2, column=1)
        Button(self, text="Eliminar", command=self.eliminar).grid(
            row=3, column=1)

        self.get_nro_entry()

    def get_nro_entry(self):
        if not self.nro_entry:
            self.nro_entry = Entry(master=self, width=15)
            self.nro_entry.grid(row=2, column=2)
        return self.nro_entry

    def eliminar(self):
        try:
            if self.get_nro_entry().get() != "":
                if messagebox.askyesno("Eliminar", "Eliminar equipo?"):
                    val = encontrar_valor(bd.equipos, "nro_equipo", self.get_nro_entry().get())
                    if val is not None:
                        if del_datos(bd.equipos, val):
                            messagebox.showinfo("Eliminado", "Equipo eliminado.")
                            self.destroy()
                        else:
                            messagebox.showinfo("Atención", "Ocurrió un error al eliminar dato.")
                            self.destroy()
                    else:
                        messagebox.showwarning("Atención", "No existe dicho Equipo.")
            else:
                messagebox.showwarning("Atención", "Seleccione el nro de equipo.")
        except:
            messagebox.showerror("Error", "Ocurrió un error inesperado al elimnar el equipo.")
