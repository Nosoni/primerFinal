# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from Clases.Persona import Cliente, Empleado
from Clases.Repuesto import Disco, Memoria, Cartucho, Otro
from Clases.Equipo import Equipo
from Clases.Contacto import Contacto
from Clases.Solicitud import Solicitud
import Datos.Bd as bd

bgC = "black"
fgC = "black"
bgBC = "white"
p_sal_pri = "700x400+150+100"
p_sal_sec = "500x300+250+180"


def list_datos(datos):
    """Genera una ventana que muestra los datos de una lista con scrollbar"""
    ventana = Tk()
    ventana.title("Lista")
    ventana.resizable(0, 0)
    ventana.geometry(p_sal_sec)

    Label(ventana, text="Detalle de los datos", ).pack()

    def colocar_scrollbar(listbox, scrollbar):
        scrollbar.config(command=listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox.pack(side=LEFT, fill=Y)

    frame1 = Frame(ventana, bd=5, height=600, width=350)
    frame1.pack()
    #700x400+150+100
    scroll1 = Scrollbar(frame1)
    list1 = Listbox(frame1, width=70, height=20)
    list1.pack()
    colocar_scrollbar(list1, scroll1)

    def cargarlistbox(lista, listbox):
        ind, largo = 0, len(lista)
        while ind < largo:
            listbox.insert(END, lista[ind])
            ind += 1

    #ventana.focus_set()
    #ventana.grab_set()
    #OBS: trate de crear un focus permanente en esta ventana para tener que
    #cerrarla para seguir usando el programa pero no logre hacerlo
    ventana.overrideredirect(1)

    cargarlistbox(datos, list1)
    ventana.mainloop()


def list_soli(soli=bd.solicitudes):
    """Genera una lista con los datos de las solicitudes"""
    datos = ['------======DETALLE SOLICITUDES======------']
    bucle = 1
    ep = "                  "
    ep1 = "                                      "
    for sol in soli:
        datos.append("{}- Cliente: {}".format(bucle, sol.cliente))
        datos.append("     Empleado: {}".format(sol.empleado))
        datos.append("     Equipos: ")
        bucle2 = 1
        for equi in sol.equipo:
            datos.append("{}-{}- Tipo: {}".format(ep, bucle2, equi.tipo))
            datos.append("{}-Marca: {}".format(ep, equi.marca))
            datos.append("{}-Modelo: {}".format(ep, equi.modelo))
            datos.append("{}-Detalle: {}".format(ep, equi.detalle))
            datos.append("{}-Problema: {}".format(ep,
                equi.detalle_problema))
            datos.append("{}-Costo: {}".format(ep, equi.costo_m))
            datos.append("{}-Estado: {}".format(ep, equi.estado))
            datos.append("{}-Repuestos:".format(ep))
            bucle1 = 1
            if equi.repuestos:
                for rep in equi.repuestos:
                    datos.append("{}={}- Marca: {}".format(ep1, bucle1,
                        rep.marca))
                    datos.append("{}=Modelo: {}".format(ep1, rep.modelo))
                    datos.append("{}=Costo: {}".format(ep1, rep.costo))
                    datos.append("")
                    bucle1 += 1
            datos.append("")
            bucle2 += 1

        datos.append("")

        bucle += 1
    list_datos(datos)


def list_bajas():
    """Genera una lista con los datos de las solicitudes procesadas"""
    list_soli(bd.solicitudes_baja)


def list_cliente():
    """Genera una lista con los datos de los clientes"""
    datos = ['------======DETALLE CLIENTES======------']
    bucle = 1
    for cli in bd.clientes:
        datos.append("{}- Cedula: {}".format(bucle, cli.cedula))
        datos.append("     Nombre: {}".format(cli.nombre))
        datos.append("     Apellido: {}".format(cli.apellido))
        datos.append("     Direccion: {}".format(cli.direccion))
        datos.append("     Contactos: ")
        if cli.contactos:
            datos.append("     -----Tel: {}".format(cli.contactos.tel))
            datos.append("     -----Cel: {}".format(cli.contactos.cel))
            datos.append("     -----Email: {}".format(cli.contactos.emails))
        datos.append("     Ruc: {}".format(cli.ruc))
        datos.append("")
        datos.append("")
        bucle += 1
    list_datos(datos)


def list_empleado():
    """Genera una lista con los datos de los empleados"""
    datos = ['------======DETALLE EMPLEADOS======------']
    bucle = 1
    for emp in bd.empleados:
        datos.append("{}- Cedula: {}".format(bucle, emp.cedula))
        datos.append("     Nombre: {}".format(emp.nombre))
        datos.append("     Apellido: {}".format(emp.apellido))
        datos.append("     Direccion: {}".format(emp.direccion))
        datos.append("     Contactos: ")
        if emp.contactos:
            datos.append("     -----Tel: {}".format(emp.contactos.tel))
            datos.append("     -----Cel: {}".format(emp.contactos.cel))
            datos.append("     -----Email: {}".format(emp.contactos.emails))
        datos.append("     Tecnico: {}".format(emp.tecnico))
        datos.append("     Fecha Inicio: {}".format(emp.fecha_ini))
        datos.append("     Sueldo: {}".format(emp.sueldo))
        datos.append("")
        datos.append("")
        bucle += 1
    list_datos(datos)


def list_repuesto():
    """Genera una lista con los datos de los repuestos"""
    datos = ['------======DETALLE REPUESTOS======------']
    bucle = 1
    for rep in bd.repuestos:
        datos.append("{}- Marca: {}".format(bucle, rep.marca))
        datos.append("     Modelo: {}".format(rep.modelo))
        datos.append("     Costo: {}".format(rep.costo))
        if type(rep) is Disco:
            datos.append("     Capacidad: {}".format(rep.capacidad))
            datos.append("     ==Disco==")
        elif type(rep) is Memoria:
            datos.append("     Tamanho: {}".format(rep.capacidad))
            datos.append("     ==Memoria==")
        elif type(rep) is Cartucho:
            datos.append("     Color: {}".format(rep.color))
            datos.append("     ==Cartucho==")
        else:
            datos.append("     Otro: {}".format(rep.tipo))
            datos.append("     ==Otro==")
        datos.append("")
        datos.append("")
        bucle += 1
    list_datos(datos)
