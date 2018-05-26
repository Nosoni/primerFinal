from Clases.Persona import *
from Clases.Solicitud import *
from Clases.Repuesto import *
from Clases.Equipo import *
from pickle import dump


def inicializar_datos():
    """Funcion que sirve para cargar algunos datos en el sistema"""

    path = "/home/franco/PycharmProjects/1erFinal/Datos/"

    # Clientes
    bd.clientes.append(Cliente(1, "Ariel", "Curtido", "Asunción"))
    bd.clientes.append(Cliente(2, "César", "Rolon", "Capiatá"))
    bd.clientes.append(Cliente(3, "Tamara", "Ocampos", "Fdo. de la Mora", None, "111111111-1"))
    bd.clientes.append(Cliente(4, "Arnaldo", "Perez", "Asunción", None, "222222222-2"))
    bd.clientes.append(Cliente(5, "Adrian", "Recalde", "Villa Elisa"))
    f = abrir(path + "clientes", "wb")
    dump(bd.clientes, f)
    f.close()

    # Empleados
    bd.empleados.append(Empleado(1, "Lucio", "Fernandez", "Asuncion", None, 2000000))
    bd.empleados.append(Empleado(2, "Juan", "Aguero", "San Lorenzo", None, 1000000))
    bd.empleados.append(Empleado(3, "Tito", "Ibarrola", "San Lorenzo, casa: 90", None, 3000000))
    bd.empleados.append(Empleado(4, "Daniel", "Sanchez", "San Lorenzo"))
    bd.empleados.append(Empleado(5, "Uriel", "Yael", "Lambaré", None))
    bd.empleados.append(Jefe(100, "Francisco", "Recalde", "Roberto L. Pettit", None, 2500000))
    f = abrir(path + "empleados", "wb")
    dump(bd.empleados, f)
    f.close()

    # Repuestos
    bd.repuestos.append(Disco(1, "Samsung", "RJ80", 500000, 10000))
    bd.repuestos.append(Disco(2, "Samsung", "RJ30", 330000, 500))
    bd.repuestos.append(Cartucho(3, "HP", "DeskJet", 67000, "no"))
    bd.repuestos.append(Cartucho(4, "HP", "DeskJet", 70000, "si"))
    bd.repuestos.append(Memoria(5, "SanDisk", "DDR2", 220000, 4))
    bd.repuestos.append(Memoria(6, "SanDisk", "DDR5", 320000, 4))
    bd.repuestos.append(Otro(7, "HP", "Confort", 300000, "Teclado"))
    bd.repuestos.append(Otro(8, "HP", "Confort", 110000, "Mouse"))
    f = abrir(path + "repuestos", "wb")
    dump(bd.repuestos, f)
    f.close()

    # Equipos
    bd.equipos.append(Equipo(1, "notebook", "Acer", "Aspire", "Color gris", "No enciende",
                             Memoria(5, "SanDisk", "DDR2", 220000, 4)))
    bd.equipos.append(Equipo(2, "otro", "HP", "TonerTJ", "Color negro", "Recarga",
                             Cartucho(4, "HP", "DeskJet", 70000, "si")))
    bd.equipos.append(Equipo(3, "computadora", "Satellite", "SobreMesa", "Color negro", "Mantenimiento"))
    bd.equipos.append(Equipo(4, "impresora", "HP", "DeskJet400", "Color blanco", "No estira hoja"))
    bd.equipos.append(Equipo(5, "monitor", "Acer", "16``","LCD", "No enciende"))
    bd.equipos.append(Equipo(6, "notebook", "Acer", "Aspire", "Color negro", "Problema teclado",
                             Otro(7, "HP", "Confort", 300000, "Teclado")))
    f = abrir(path + "equipos", "wb")
    dump(bd.equipos, f)
    f.close()

    # Solicitudes
    bd.solicitudes.append(Solicitud(1, datetime.now(), Cliente(1, "Ariel", "Curtido", "Asunción"),
                                    Empleado(1, "Lucio", "Fernandez", "Asuncion", None, 2000000),
                                    Equipo(3, "computadora", "Satellite", "SobreMesa", "Color negro", "Mantenimiento"),
                                           20000, "pendiente"))
    bd.solicitudes.append(Solicitud(2, datetime.now(), Cliente(2, "César", "Rolon", "Capiatá"),
                                    Empleado(4, "Daniel", "Sanchez", "San Lorenzo"),
                                    Equipo(5, "monitor", "Acer", "16``", "LCD", "No enciende"), 15000, "concluido"))
    f = abrir(path + "solicitudes", "wb")
    dump(bd.solicitudes, f)
    f.close()
