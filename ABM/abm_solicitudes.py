# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.Solicitud import Solicitud
from Clases.Equipo import Equipo
from datetime import timedelta, datetime
from Clases.Repuesto import Disco, Memoria, Cartucho, Otro
from functools import reduce
dias_garantia = 30

class AddSoli(PanedWindow):
    "Panel que contiene los campos para introducir los datos de la solicitud"

    cliente_entry = None
    empleado_entry = None
    tipo_entry = None
    marca_entry = None
    modelo_entry = None
    detalle_fisico_entry = None
    detalle_problema_entry = None
    costo_entry = None
    estado_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.equipArray = []
        Label(self, text="Ingrese datos de la solicitud", ).grid(
            row=1, column=2)
        Label(self, text="Cliente*: ").grid(row=2, column=1)
        Label(self, text="Empleado*: ").grid(row=3, column=1)
        Label(self, text="Agregar equipo: ").grid(row=4, column=1)
        Button(self, text="GUARDAR SOLI", command=self.a_cli).grid(
            row=12, column=1)

        Label(self, text="Tipo*: ").grid(row=5, column=1)
        Label(self, text="Marca*: ").grid(row=6, column=1)
        Label(self, text="Modelo*: ").grid(row=7, column=1)
        Label(self, text="Detalle Fisico: ").grid(row=8, column=1)
        Label(self, text="Problema: ").grid(row=9, column=1)
        Label(self, text="Costo Mantenimiento: ").grid(row=10, column=1)
        Label(self, text="Estado*: ").grid(row=11, column=1)
        Button(self, text="Add Equi", command=self.a_equi).grid(
            row=4, column=2)

        self.get_cliente_entry()
        self.get_empleado_entry()
        self.get_tipo_entry()
        self.get_marca_entry()
        self.get_modelo_entry()
        self.get_detalle_fisico_entry()
        self.get_detalle_problema_entry()
        self.get_costo_entry()
        self.get_estado_entry()

    def get_cliente_entry(self):
        if not self.cliente_entry:
            self.cliente_entry = Entry(master=self, width=20)
            self.cliente_entry.grid(row=2, column=2)
        return self.cliente_entry

    def get_empleado_entry(self):
        if not self.empleado_entry:
            self.empleado_entry = Entry(master=self, width=20)
            self.empleado_entry.grid(row=3, column=2)
        return self.empleado_entry

    def get_tipo_entry(self):
        if not self.tipo_entry:
            self.tipo = StringVar()
            self.tipo_entry = Radiobutton(self, text="Notebook",
                value="notebook", variable=self.tipo)
            self.tipo_entry.grid(row=5, column=2)
            self.tipo_entry = Radiobutton(self, text="Computadora",
                value="computadora", variable=self.tipo)
            self.tipo_entry.grid(row=5, column=3)
            self.tipo_entry = Radiobutton(self, text="Impresora",
                value="impresora", variable=self.tipo)
            self.tipo_entry.grid(row=5, column=4)
            self.tipo_entry = Radiobutton(self, text="Monitor",
                value="monitor", variable=self.tipo)
            self.tipo_entry.grid(row=5, column=5)
            self.tipo_entry = Radiobutton(self, text="Otro",
                value="otro", variable=self.tipo)
            self.tipo_entry.grid(row=5, column=6)
        return self.tipo

    def get_marca_entry(self):
        if not self.marca_entry:
            self.marca_entry = Entry(master=self, width=20)
            self.marca_entry.grid(row=6, column=2)
        return self.marca_entry

    def get_modelo_entry(self):
        if not self.modelo_entry:
            self.modelo_entry = Entry(master=self, width=20)
            self.modelo_entry.grid(row=7, column=2)
        return self.modelo_entry

    def get_detalle_fisico_entry(self):
        if not self.detalle_fisico_entry:
            self.detalle_fisico_entry = Entry(master=self, width=20)
            self.detalle_fisico_entry.grid(row=8, column=2)
        return self.detalle_fisico_entry

    def get_detalle_problema_entry(self):
        if not self.detalle_problema_entry:
            self.detalle_problema_entry = Entry(master=self, width=20)
            self.detalle_problema_entry.grid(row=9, column=2)
        return self.detalle_problema_entry

    def get_costo_entry(self):
        if not self.costo_entry:
            self.costo_entry = Entry(master=self, width=20)
            self.costo_entry.grid(row=10, column=2)
        return self.costo_entry

    def get_estado_entry(self):
        if not self.estado_entry:
            self.estado = StringVar()
            self.estado_entry = Radiobutton(self, text="Pendiente",
                value="pendiente", variable=self.estado)
            self.estado_entry.grid(row=11, column=2)
            self.estado_entry = Radiobutton(self, text="Concluido",
                value="concluido", variable=self.estado)
            self.estado_entry.grid(row=11, column=3)
        return self.estado

    def val_soli(self, c, e):
        val = False
        if c.isalpha() and e.isalpha():
            val = True
        else:
            messagebox.showinfo("", "Ingrese nombre y empleado")
        return val

    def a_cli(self):
            # Anhade la solicitud a la bd
            if self.equipArray:
                try:
                    cli = self.get_cliente_entry().get()
                    emp = self.get_empleado_entry().get()
                    if self.val_soli(cli, emp):
                        solicitud = Solicitud(**{"fecha": datetime.now(),
                        "cliente": cli, "empleado": emp})
                        solicitud.equipo = self.equipArray
                        bd.solicitudes.append(solicitud)
                        #print("final de ingreso de datos")
                        messagebox.showinfo("Informacion", "Solicitud agregada")
                        self.destroy()
                except Exception as e:
                    messagebox.showerror('Error', e)
            else:
                messagebox.showinfo("Informacion", "Debe ingresar equipo")

    def val_equi(self, tip, mar, mod, det, det_p, cos, est):
        val = False
        if tip != "" and mar != "" and est != "" and (cos.isdigit() or
        cos == "") and mod != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese correctamente los datos del " +
                "equipo")
        return val

    def a_equi(self):
            try:
                tip = self.get_tipo_entry().get()
                mar = self.get_marca_entry().get()
                mod = self.get_modelo_entry().get()
                det = self.get_detalle_fisico_entry().get()
                det_p = self.get_detalle_problema_entry().get()
                cos = self.get_costo_entry().get()
                est = self.get_estado_entry().get()
                if self.val_equi(tip, mar, mod, det, det_p, cos, est):
                    equipo = Equipo(**{"tipo": tip, "marca": mar,
                    "modelo": mod, "detalle": det, "detalle_problema": det_p,
                    "costo_m": cos, "repuesto": None, "estado": est})
                    self.equipArray.append(equipo)
                    messagebox.showinfo("Informacion", "Equipo agregado")
            except Exception as e:
                messagebox.showerror('Error', e)


class ActSoli(PanedWindow):
    """Panel que contiene los campos para agregar un repuesto a una solicitud"""

    soli_entry = None
    equipo_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.repuesto = Disco("Samsung", "RJ80", 500000, 10000)

        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Ingrese numero de solicitud*: ").grid(row=2, column=1)
        Label(self, text="Ingrese numero de equipo*: ").grid(row=3, column=1)
        Button(self, text="Agregar Repuesto (DISCO)", command=self.add).grid(
            row=6, column=1)

        self.get_soli_entry()
        self.get_equipo_entry()

    def get_soli_entry(self):
        if not self.soli_entry:
            self.soli_entry = Entry(master=self, width=20)
            self.soli_entry.grid(row=2, column=2)
        return self.soli_entry

    def get_equipo_entry(self):
        if not self.equipo_entry:
            self.equipo_entry = Entry(master=self, width=20)
            self.equipo_entry.grid(row=3, column=2)
        return self.equipo_entry

    def add(self):
        # Anhade un repuesto a la solicitud deseada
        try:
            sol = int(self.get_soli_entry().get())
            eqi = int(self.get_equipo_entry().get())
            if bd.solicitudes[sol - 1].equipo[eqi - 1]:
                bd.solicitudes[sol - 1].equipo[eqi - 1].repuestos.append(
                    self.repuesto)
                messagebox.showinfo("Informacion", "Agregado")
                self.destroy()
        except:
            messagebox.showinfo("Infor", "No existe equipo o solicitud")


class DelSoli(PanedWindow):
    """Panel que contien los campos para eliminar una solicitud"""
    soli_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Ingrese num de solicitud*: ").grid(row=2, column=1)
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
            if(messagebox.askyesno("Eliminar", "Eliminar solicitud?")):
                bd.solicitudes.pop(pos - 1)
                messagebox.showinfo("Eliminado", "Solicitud eliminada")
                self.destroy()
        except:
            messagebox.showerror("Infor", "No existe solicitud")


class BajaSoli(PanedWindow):
    """Panel que contien los campos para procesar una solicitud"""
    soli_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Ingrese numero de solicituda a procesar*: ").grid(
            row=2, column=1)
        Button(self, text="Procesar", command=self.procesar).grid(
            row=3, column=1)

        self.get_soli_entry()

    def get_soli_entry(self):
        if not self.soli_entry:
            self.soli_entry = Entry(master=self, width=20)
            self.soli_entry.grid(row=2, column=2)
        return self.soli_entry

    def procesar(self):
        try:
            pos = int(self.get_soli_entry().get())
            if(messagebox.askyesno("Procesar", "Procesar solicitud?")):
                dato = bd.solicitudes.pop(pos - 1)
                bd.solicitudes_baja.append(dato)
                messagebox.showinfo("Informacion", "Solicitud procesada")
                self.calc(dato)
        except:
            messagebox.showerror("Infor", "No existe solicitud")

    #Funcion que calcula los valores para procesar una solicitud
    def calc(self, dato):
            if dato.fecha is not None:
                self.fech = (dato.fecha + timedelta(days=dias_garantia))
            montos = self.generador(dato)
            money = self.calc_monto(montos)
            messagebox.showinfo("Resultado", "Cliente: " + dato.cliente +
            "\nEmpleado: " + dato.empleado + "\nMonto total: " + str(money) +
            "\nGarantia hasta: " + str(self.fech))
            self.destroy()

    # Utilizamos la funcion reduce para sumar todos los elementos de una lista
    # -------------Parte que equivale a la programacion funcional--------------
    def calc_monto(self, lista):
        return reduce(self.sumar, lista)

    def generador(self, dato):
        # Retornamos los valores de los montos para calcular el total
        # Esta funcion trabaja con el concepto de generador
        if dato.equipo:
            for equi in dato.equipo:
                yield equi.costo_m
                if equi.repuestos:
                    for rep in equi.repuestos:
                        yield rep.costo

    def sumar(self, x, y):
        return x + y