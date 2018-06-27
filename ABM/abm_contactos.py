from tkinter import *
from Clases.Contacto import *
from Controlador.Util import encontrar_valor
from tkinter import messagebox


class AddContacto(PanedWindow):
    """Panel de AddContacto"""

    cedula_entry = None
    tel_entry = None
    email_entry = None
    red_social_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese dato requiero del Cliente a editar", ).grid(row=1, column=2)
        Label(self, text="Cédula*: ", ).grid(row=2, column=1)
        Label(self, text="Teléfono:").grid(row=3, column=1)
        Label(self, text="Email: ").grid(row=4, column=1)
        Label(self, text="Red social: ").grid(row=5, column=1)
        Button(self, text="Guardar", command=self.crear_contacto).grid(row=6, column=2)

        self.get_cedula_entry()
        self.get_tel_entry()
        self.get_email_entry()
        self.get_red_social_entry()

    def get_cedula_entry(self):
        if not self.cedula_entry:
            self.cedula_entry = Entry(master=self, width=20)
            self.cedula_entry.grid(row=2, column=2)
        return self.cedula_entry

    def get_tel_entry(self):
        if not self.tel_entry:
            self.tel_entry = Entry(master=self, width=20)
            self.tel_entry.grid(row=3, column=2)
        return self.tel_entry

    def get_email_entry(self):
        if not self.email_entry:
            self.email_entry = Entry(master=self, width=20)
            self.email_entry.grid(row=4, column=2)
        return self.email_entry

    def get_red_social_entry(self):
        if not self.red_social_entry:
            self.red_social_entry = Entry(master=self, width=20)
            self.red_social_entry.grid(row=5, column=2)
        return self.red_social_entry

    def crear_contacto(self):
        try:
            if messagebox.askyesno("Editar", "Desea editar dicho Cliente?"):
                val = encontrar_valor(bd.clientes, "cedula", self.get_cedula_entry().get())
                if val is not None:
                    red_social = self.get_red_social_entry().get()
                    cel = self.get_tel_entry().get()
                    mail = self.get_email_entry().get()
                    a = Contacto(cel, mail, red_social)
                    val.contactos.append(a)
                    messagebox.showinfo("Editado", "Editado con éxito.")
                    self.destroy()
                else:
                    messagebox.showwarning("Atención", "No existe Cliente.")
                    self.destroy()
        except:
            messagebox.showerror("Error", "Ocurrió un error inesperado al elimnar el cliente.")
