# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.Repuesto import Disco, Memoria, Cartucho, Otro


class AddRepuesto(PanedWindow):
    """Panel que contien los campos para introducir los datos de un repuesto"""

    tipo_entry = None
    marca_entry = None
    modelo_entry = None
    costo_entry = None
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
        Label(self, text="Marca*: ", ).grid(row=4, column=1)
        Label(self, text="Modelo*: ").grid(row=5, column=1)
        Label(self, text="Costo*: ").grid(row=6, column=1)
        Label(self, text="(Disco) Cacidad: ", ).grid(row=7, column=2)
        Label(self, text="(Memoria) Tamanho: ").grid(row=8, column=2)
        Label(self, text="(Tarjeta) TipoNom: ").grid(row=9, column=2)
        Label(self, text="(Cartucho) Color: ").grid(row=10, column=2)
        Label(self, text="(Otro) Detalle: ").grid(row=11, column=2)
        Button(self, text="GUARDAR", command=self.a_rep).grid(row=9, column=1)

        self.get_tipo_entry()
        self.get_marca_entry()
        self.get_modelo_entry()
        self.get_costo_entry()
        self.get_capacidad_entry()
        self.get_tamanho_entry()
        self.get_detalle_entry()
        self.get_color_entry()
        self.get_tipoNom_entry()

    def get_tipo_entry(self):
        if not self.tipo_entry:
            self.tipo = StringVar()
            self.tipo_entry = Radiobutton(self, text="Disco",
                value="disco", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=1)
            self.tipo_entry = Radiobutton(self, text="Memoria",
                value="memoria", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=2)
            self.tipo_entry = Radiobutton(self, text="Tarjeta",
                value="tarjeta", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=3)
            self.tipo_entry = Radiobutton(self, text="Cartucho",
                value="cartucho", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=4)
            self.tipo_entry = Radiobutton(self, text="Otro",
                value="otro", variable=self.tipo)
            self.tipo_entry.grid(row=3, column=5)
        return self.tipo

    def get_marca_entry(self):
        if not self.marca_entry:
            self.marca_entry = Entry(master=self, width=20)
            self.marca_entry.grid(row=4, column=2)
        return self.marca_entry

    def get_modelo_entry(self):
        if not self.modelo_entry:
            self.modelo_entry = Entry(master=self, width=20)
            self.modelo_entry.grid(row=5, column=2)
        return self.modelo_entry

    def get_costo_entry(self):
        if not self.costo_entry:
            self.costo_entry = Entry(master=self, width=20)
            self.costo_entry.grid(row=6, column=2)
        return self.costo_entry

    def get_capacidad_entry(self):
        if not self.capacidad_entry:
            self.capacidad_entry = Entry(master=self, width=20)
            self.capacidad_entry.grid(row=7, column=3)
        return self.capacidad_entry

    def get_tamanho_entry(self):
        if not self.tamanho_entry:
            self.tamanho_entry = Entry(master=self, width=20)
            self.tamanho_entry.grid(row=8, column=3)
        return self.tamanho_entry

    def get_detalle_entry(self):
        if not self.detalle_entry:
            self.detalle_entry = Entry(master=self, width=20)
            self.detalle_entry.grid(row=9, column=3)
        return self.detalle_entry

    def get_color_entry(self):
        if not self.color_entry:
            self.color = StringVar()
            self.color_entry = Radiobutton(self, text="Si", value="si",
                variable=self.color)
            self.color_entry.grid(row=10, column=3)
            self.color_entry = Radiobutton(self, text="No", value="no",
                variable=self.color)
            self.color_entry.grid(row=10, column=4)
        return self.color

    def get_tipoNom_entry(self):
        if not self.tipoNom_entry:
            self.tipoNom_entry = Entry(master=self, width=20)
            self.tipoNom_entry.grid(row=11, column=3)
        return self.tipoNom_entry

    def val_rep(self, tip, mar, mod, cos, cap, tam, det, col, tpN):
        val = False
        if mar != "" and mod != "" and cos.isdigit():
            val = True

            if tip == "disco" and cap.isdigit():
                val = True
            elif tip == "memoria" and tam.isdigit():
                val = True
            elif tip == "tarjeta" and det != "":
                val = True
            elif tip == "cartucho" and col != "":
                val = True
            elif tip == "otro" and tpN != "":
                val = True
            else:
                messagebox.showinfo("", "Ingrese dato correspondiente al " +
                "repuesto")
                val = False

        else:
            messagebox.showinfo("", "Ingrese datos necesarios del repuesto")

        return val

    def a_rep(self):
        try:
            tip = self.get_tipo_entry().get()
            mar = self.get_marca_entry().get()
            mod = self.get_modelo_entry().get()
            cos = self.get_costo_entry().get()
            cap = self.get_capacidad_entry().get()
            tam = self.get_tamanho_entry().get()
            det = self.get_detalle_entry().get()
            col = self.get_color_entry().get()
            tpN = self.get_tipoNom_entry().get()

            if self.val_rep(tip, mar, mod, cos, cap, tam, det, col, tpN):
                if (tip == "disco"):
                    bd.repuestos.append(Disco(**{
                        "marca": mar, "modelo": mod, "costo": cos,
                        "capacidad": cap}))
                    messagebox.showinfo("Informacion", "Disco agregado")
                elif (tip == "memoria"):
                    bd.repuestos.append(Memoria(**{
                        "marca": mar, "modelo": mod, "costo": cos,
                        "capacidad": tam}))
                    messagebox.showinfo("Informacion", "Memoria agregada")
                elif (tip == "cartucho"):
                    bd.repuestos.append(Cartucho(**{
                        "marca": mar, "modelo": mod, "costo": cos,
                        "color": col}))
                    messagebox.showinfo("Informacion", "Cartucho agregado")
                elif (tip == "otro"):
                    bd.repuestos.append(Otro(**{
                        "marca": mar, "modelo": mod, "costo": cos,
                        "tipo": tpN}))
                    messagebox.showinfo("Informacion", "Otro agregado")
                self.destroy()
        except Exception as e:
                messagebox.showerror('Error', e)


class DelRepuesto(PanedWindow):
    """Panel que contien los campos para eliminar un repuesto"""
    soli_entry = None

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

        self.get_soli_entry()

    def get_soli_entry(self):
        if not self.soli_entry:
            self.soli_entry = Entry(master=self, width=20)
            self.soli_entry.grid(row=2, column=2)
        return self.soli_entry

    def eliminar(self):
        try:
            pos = int(self.get_soli_entry().get())
            if(messagebox.askyesno("Eliminar", "Eliminar Repuesto?")):
                bd.repuestos.pop(pos - 1)
                messagebox.showinfo("Eliminado", "Repuesto eliminado")
        except:
            messagebox.showerror("Infor", "No existe repuesto")