# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.Repuesto import Disco, Memoria, Cartucho, Otro
from Controlador.Util import encontrar_valor
from Controlador.VistaUtil import del_datos


class AddRepuesto(PanedWindow):
    """Panel que contien los campos para introducir los datos de un repuesto"""

    tipo_entry = None
    codigo_entry = None
    marca_entry = None
    modelo_entry = None
    precio_entry = None
    capacidad_entry = None
    tamanho_entry = None
    detalle_entry = None
    color_entry = None
    tipoNom_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Seleccione tipo de repuesto*: ").grid(
            row=2, column=1)
        Label(self, text="Código*: ", ).grid(row=4, column=1)
        Label(self, text="Marca*: ", ).grid(row=5, column=1)
        Label(self, text="Modelo*: ").grid(row=6, column=1)
        Label(self, text="Precio*: ").grid(row=7, column=1)
        Label(self, text="(Disco) Capacidad: ", ).grid(row=8, column=2)
        Label(self, text="(Memoria) Tamaño: ").grid(row=9, column=2)
        Label(self, text="(Otro) Detalle: ").grid(row=10, column=2)
        Label(self, text="(Cartucho) Color: ").grid(row=11, column=2)
        Button(self, text="GUARDAR", command=self.a_rep).grid(row=9, column=1)

        self.get_tipo_entry()
        self.get_codigo_entry()
        self.get_marca_entry()
        self.get_modelo_entry()
        self.get_precio_entry()
        self.get_capacidad_entry()
        self.get_tamanho_entry()
        self.get_detalle_entry()
        self.get_color_entry()

    def get_tipo_entry(self):
        if not self.tipo_entry:
            self.tipo = StringVar()
            self.tipo_entry = Radiobutton(self, text="Disco",
                value="disco", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=1)
            self.tipo_entry = Radiobutton(self, text="Memoria",
                value="memoria", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=2)
            self.tipo_entry = Radiobutton(self, text="Cartucho",
                value="cartucho", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=3)
            self.tipo_entry = Radiobutton(self, text="Otro",
                value="otro", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=4)
        return self.tipo

    def get_codigo_entry(self):
        if not self.codigo_entry:
            self.codigo_entry = Entry(master=self, width=15)
            self.codigo_entry.grid(row=4, column=2)
        return self.codigo_entry

    def get_marca_entry(self):
        if not self.marca_entry:
            self.marca_entry = Entry(master=self, width=15)
            self.marca_entry.grid(row=5, column=2)
        return self.marca_entry

    def get_modelo_entry(self):
        if not self.modelo_entry:
            self.modelo_entry = Entry(master=self, width=15)
            self.modelo_entry.grid(row=6, column=2)
        return self.modelo_entry

    def get_precio_entry(self):
        if not self.precio_entry:
            self.precio_entry = Entry(master=self, width=15)
            self.precio_entry.grid(row=7, column=2)
        return self.precio_entry

    def get_capacidad_entry(self):
        if not self.capacidad_entry:
            self.capacidad_entry = Entry(master=self, width=15)
            self.capacidad_entry.grid(row=8, column=3)
        return self.capacidad_entry

    def get_tamanho_entry(self):
        if not self.tamanho_entry:
            self.tamanho_entry = Entry(master=self, width=15)
            self.tamanho_entry.grid(row=9, column=3)
        return self.tamanho_entry

    def get_detalle_entry(self):
        if not self.detalle_entry:
            self.detalle_entry = Entry(master=self, width=15)
            self.detalle_entry.grid(row=10, column=3)
        return self.detalle_entry

    def get_color_entry(self):
        if not self.color_entry:
            self.color = StringVar()
            self.color_entry = Radiobutton(self, text="Si", value="si",
                variable=self.color)
            self.color_entry.grid(row=11, column=3)
            self.color_entry = Radiobutton(self, text="No", value="no",
                variable=self.color)
            self.color_entry.grid(row=11, column=4)
        return self.color

    def val_rep(self, tip, cod, mar, mod, pre, cap, tam, det, col):
        val = False
        if cod != "" and mar != "" and mod != "" and pre.isdigit():
            if tip == "disco" and cap.isdigit():
                val = True
            elif tip == "memoria" and tam.isdigit():
                val = True
            elif tip == "cartucho" and col != "":
                val = True
            elif tip == "otro" and det != "":
                val = True
            else:
                messagebox.showinfo("", "Ingrese dato correspondiente al repuesto")
                val = False
        else:
            messagebox.showinfo("", "Ingrese datos necesarios del repuesto")
        return val

    def a_rep(self):
        try:
            tip = self.get_tipo_entry().get()
            cod = self.get_codigo_entry().get()
            mar = self.get_marca_entry().get()
            mod = self.get_modelo_entry().get()
            pre = self.get_precio_entry().get()
            cap = self.get_capacidad_entry().get()
            tam = self.get_tamanho_entry().get()
            det = self.get_detalle_entry().get()
            col = self.get_color_entry().get()

            if self.val_rep(tip, cod, mar, mod, pre, cap, tam, det, col):
                if (tip == "disco"):
                    bd.repuestos.append(Disco(**{"cod": cod,
                        "marca": mar, "modelo": mod, "precio": pre,
                        "capacidad": cap}))
                    messagebox.showinfo("Informacion", "Disco agregado")
                elif (tip == "memoria"):
                    bd.repuestos.append(Memoria(**{"cod": cod,
                        "marca": mar, "modelo": mod, "precio": pre,
                        "capacidad": tam}))
                    messagebox.showinfo("Informacion", "Memoria agregada")
                elif (tip == "cartucho"):
                    bd.repuestos.append(Cartucho(**{"cod": cod,
                        "marca": mar, "modelo": mod, "precio": pre,
                        "color": col}))
                    messagebox.showinfo("Informacion", "Cartucho agregado")
                elif (tip == "otro"):
                    bd.repuestos.append(Otro(**{"cod": cod,
                        "marca": mar, "modelo": mod, "precio": pre,
                        "tipo": det}))
                    messagebox.showinfo("Informacion", "Otro agregado")
                self.destroy()
        except Exception as e:
                messagebox.showerror('Error', e)


class DelRepuesto(PanedWindow):
    """Panel que contien los campos para eliminar un repuesto"""
    cod_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Ingrese num de repuesto*: ").grid(row=2, column=1)
        Button(self, text="Eliminar", command=self.eliminar).grid(
            row=3, column=1)

        self.get_cod_entry()

    def get_cod_entry(self):
        if not self.cod_entry:
            self.cod_entry = Entry(master=self, width=15)
            self.cod_entry.grid(row=2, column=2)
        return self.cod_entry

    def eliminar(self):
        try:
            if messagebox.askyesno("Eliminar", "Eliminar repuesto?"):
                val = encontrar_valor(bd.repuestos, "cod", self.get_cod_entry().get())
                if val is not None:
                    if del_datos(bd.repuestos, val):
                        messagebox.showinfo("Eliminado", "Repuesto eliminado")
                        self.destroy()
                    else:
                        messagebox.showinfo("Atención", "Ocurrió un error al eliminar dato.")
                        self.destroy()
                else:
                    messagebox.showwarning("Atención", "No existe dicho Repuesto.")
        except:
            messagebox.showerror("Error", "Ocurrió un error inesperado al elimnar el repuesto.")
