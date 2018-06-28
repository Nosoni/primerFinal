# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.Solicitud import Solicitud
from datetime import timedelta, datetime
from functools import reduce
from Controlador.Util import encontrar_valor
from Controlador.VistaUtil import del_datos

dias_garantia = 30


class AddSoli(PanedWindow):
    """Panel que contiene los campos para introducir los datos de la solicitud"""

    sol_nro_entry = None
    cliente_entry = None
    equi_entry = None
    empleado_entry = None
    presupuesto_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.equipArray = []
        Label(self, text="Ingrese datos de la solicitud", ).grid(
            row=1, column=2)
        Label(self, text="Nro. de Solicitud*: ").grid(row=2, column=1)
        Label(self, text="Cédula Cliente*: ").grid(row=3, column=1)
        Label(self, text="Cédula Empleado*: ").grid(row=4, column=1)
        Label(self, text="Agregar equipo*: ").grid(row=5, column=1)
        Label(self, text="Presupuesto:* ").grid(row=6, column=1)
        Button(self, text="Add Equi", command=self.a_equi).grid(
            row=5, column=3)
        Button(self, text="GUARDAR", command=self.a_sol).grid(
            row=7, column=2)

        self.get_sol_nro_entry()
        self.get_cliente_entry()
        self.get_empleado_entry()
        self.get_presupuesto_entry()

    def get_sol_nro_entry(self):
        if not self.sol_nro_entry:
            self.sol_nro_entry = Entry(master=self, width=20)
            self.sol_nro_entry.grid(row=2, column=2)
        return self.sol_nro_entry

    def get_cliente_entry(self):
        if not self.cliente_entry:
            self.cliente_entry = Entry(master=self, width=20)
            self.cliente_entry.grid(row=3, column=2)
        return self.cliente_entry

    def get_empleado_entry(self):
        if not self.empleado_entry:
            self.empleado_entry = Entry(master=self, width=20)
            self.empleado_entry.grid(row=4, column=2)
        return self.empleado_entry

    def get_equi_entry(self):
        if not self.equi_entry:
            self.equi_entry = Entry(master=self, width=20)
            self.equi_entry.grid(row=5, column=2)
        return self.equi_entry

    def get_presupuesto_entry(self):
        if not self.presupuesto_entry:
            self.presupuesto_entry = Entry(master=self, width=20)
            self.presupuesto_entry.grid(row=6, column=2)
        return self.presupuesto_entry

    def a_sol(self):
        try:
            sol = self.get_sol_nro_entry().get()
            cli = encontrar_valor(bd.clientes, "cedula", self.get_cliente_entry().get())
            emp = encontrar_valor(bd.empleados, "cedula", self.get_empleado_entry().get())
            pre = self.get_presupuesto_entry().get()

            solicitud = Solicitud(sol, datetime.now(), cli, emp, self.equipArray, pre, "Pendiente")
            bd.solicitudes.append(solicitud)
            messagebox.showinfo("Informacion", "Solicitud agregada")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", e)

    def val_soli(self, nro_soli, cliente, emp, pre):
        val = False
        if nro_soli != "":
            val = True
        else:
            messagebox.showwarning("Atención", "Ingrese nro. de Solicitud.")
        if cliente != "":
            encontrar = encontrar_valor(bd.clientes, "cedula", cliente)
            if encontrar is not None:
                val = True
            else:
                messagebox.showwarning("Atención", "No se encuentra el cliente.")
        else:
            messagebox.showwarning("Atencipon", "Ingrese un cliente.")
        if emp != "":
            encontrar = encontrar_valor(bd.empleados, "cedula", emp)
            if encontrar is not None:
                val = True
            else:
                messagebox.showwarning("Atención", "No se encuentra el empleado.")
        else:
            messagebox.showwarning("Atencipon", "Ingrese un empleado.")
        if pre != "" and pre.isdigit():
            val = True
        else:
            messagebox.showwarning("Atencipon", "Ingrese el presupuesto.")
        return val

    def a_equi(self):
        try:
            if self.get_equi_entry().get() != "":
                if messagebox.askyesno("Editar", "Desea agregar el equipo?"):
                    val = encontrar_valor(bd.equipos, "nro_equipo", self.get_equi_entry().get())
                    if val is not None:
                        self.equipArray.append(val)
                        messagebox.showinfo("Agregado", "Agregado con éxito.")
                    else:
                        messagebox.showwarning("Atención", "No existe repuesto.")
            else:
                messagebox.showwarning("Atención", "Ingrese el nro. del equipo.")
        except Exception as e:
            messagebox.showerror("Error", e)


class ActSoli(PanedWindow):
    """Panel que contiene los campos para agregar un repuesto a una solicitud"""

    soli_entry = None
    presupuesto_entry = None
    equipo_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.equipArray = []
        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Ingrese numero de solicitud*: ").grid(row=2, column=1)
        Label(self, text="Actualizar Presupuesto: ").grid(row=3, column=1)
        Label(self, text="Agregar equipo: ").grid(row=4, column=1)
        Button(self, text="Add Equi", command=self.a_equi).grid(
            row=4, column=3)
        Button(self, text="GUARDAR", command=self.a_sol).grid(
            row=7, column=2)

        self.get_soli_entry()
        self.get_presupuesto_entry()
        self.get_equipo_entry()

    def get_soli_entry(self):
        if not self.soli_entry:
            self.soli_entry = Entry(master=self, width=20)
            self.soli_entry.grid(row=2, column=2)
        return self.soli_entry

    def get_presupuesto_entry(self):
        if not self.presupuesto_entry:
            self.presupuesto_entry = Entry(master=self, width=20)
            self.presupuesto_entry.grid(row=3, column=2)
        return self.presupuesto_entry

    def get_equipo_entry(self):
        if not self.equipo_entry:
            self.equipo_entry = Entry(master=self, width=20)
            self.equipo_entry.grid(row=4, column=2)
        return self.equipo_entry

    def a_equi(self):
        try:
            if self.get_equipo_entry().get() != "":
                if messagebox.askyesno("Editar", "Desea agregar el equipo?"):
                    val = encontrar_valor(bd.equipos, "nro_equipo", self.get_equipo_entry().get())
                    self.equipArray.append(val)
                    messagebox.showinfo("Agregado", "Agregado con éxito.")
            else:
                messagebox.showwarning("Atención", "Ingrese el nro. del equipo.")
        except Exception as e:
            messagebox.showerror("Error", e)

    def a_sol(self):
        try:
            sol = self.get_soli_entry().get()
            if sol != "":
                solicitud = encontrar_valor(bd.solicitudes, "solicitud_numero", sol)
                if solicitud is not None:
                    if self.get_presupuesto_entry().get() != "":
                        solicitud.presupuesto = self.get_presupuesto_entry().get()
                    if len(self.equipArray) > 0:
                        for equi in self.equipArray:
                            solicitud.equipos.append(equi)
                    messagebox.showinfo("Informacion", "Solicitud actualizado.")
                    self.destroy()
                else:
                    messagebox.showinfo("Informacion", "Solicitud no encontrada.")
            else:
                messagebox.showinfo("Atención", "Ingrese el nro de Solicitud.")
        except Exception as e:
            messagebox.showerror("Error", e)


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
            if self.get_soli_entry().get() != "":
                if messagebox.askyesno("Eliminar", "Eliminar solicitud?"):
                    val = encontrar_valor(bd.solicitudes, "solicitud_numero", self.get_soli_entry().get())
                    if val is not None:
                        if del_datos(bd.solicitudes, val):
                            messagebox.showinfo("Eliminado", "Solicitud eliminada.")
                            self.destroy()
                        else:
                            messagebox.showinfo("Atención", "Ocurrió un error al eliminar dato.")
                            self.destroy()
                    else:
                        messagebox.showwarning("Atención", "No existe solicitud.")
            else:
                messagebox.showwarning("Atención", "Ingrese Nro. de solicitud.")
        except:
            messagebox.showerror("Error", "Ocurrió un error inesperado al elimnar la solicitud.")


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
        Label(self, text="Ingrese número de solicitud a procesar*: ").grid(
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
            if self.get_soli_entry().get() != "":
                if messagebox.askyesno("Procesar", "Procesar solicitud?"):
                    val = encontrar_valor(bd.solicitudes, "solicitud_numero", self.get_soli_entry().get())
                    if val is not None:
                        val.cambiar_estado()
                        self.calc(val)
                        if del_datos(bd.solicitudes, val):
                            bd.solicitudes_baja.append(val)
                            messagebox.showinfo("Procesada", "Solicitud dada de baja.")
                        else:
                            messagebox.showinfo("Atención", "Ocurrió un error al eliminar dato.")
            else:
                messagebox.showinfo("Atención", "Ingrese nro. de solicitud.")
        except:
            messagebox.showerror("Infor", "No existe solicitud")

    # Funcion que calcula los valores para procesar una solicitud
    def calc(self, dato):
        if dato.fecha is not None:
            self.fech = (dato.fecha + timedelta(days=dias_garantia))
        montos = self.generador(dato)
        money = self.calc_monto(montos)
        messagebox.showinfo("Resultado", "Cliente: " + dato.cliente.Nombre + " " + dato.cliente.apellido +
                            "\nEmpleado: " + dato.empleado.nombre + " " + dato.empleado.apellido + "\nMonto total: " + str(money) +
                            "\nGarantia hasta: " + str(self.fech))
        self.destroy()

    # Utilizamos la funcion reduce para sumar todos los elementos de una lista
    # --------------Parte equivalente a programacion funcional----------------
    def calc_monto(self, lista):
        return reduce(self.sumar, lista)

    def generador(self, dato):
        # Retornamos los valores de los montos para calcular el total
        # Esta funcion trabaja con el concepto de generador
        if dato.equipos:
            for equi in dato.equipos:
                if equi.repuestos:
                    for rep in equi.repuestos:
                        if rep is not None:
                            if rep.precio:
                                yield rep.precio

    def sumar(self, x, y):
        return x + y
