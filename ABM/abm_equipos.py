from tkinter import *
from tkinter import messagebox
import Datos.Bd as bd
from Clases.Persona import Empleado
from Clases.Contacto import Contacto


class PanelLogin(PanedWindow):
    """Panel de login"""
    user = None
    password = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()
        self.grab_set()  # deshabilita las otras ventanas hasta que esta se destruya

    def inicializar(self):
        self.__panel_master.title("MENU Login")
        self.__panel_master.protocol("WM_DELETE_WINDOW", "onexit")
        self.__panel_master.resizable(0, 0)
        Label(self, text="Usuario").grid(row=1, column=1)
        Label(self, text="Usuario").grid(row=1, column=1)
        Label(self, text="Contraseña: ").grid(row=2, column=1)
        Button(self, text="Login", command=self.login).grid(row=3, column=2)

        self.get_user()
        self.get_password()

    def get_user(self):
        if not self.user:
            self.user = Entry(master=self, textvariable=StringVar())
            self.user.grid(row=1, column=2)
            return self.user

    def get_password(self):
        if not self.password:
            self.password = Entry(master=self, textvariable=StringVar(), show="•")
            self.password.grid(row=2, column=2)
        return self.password