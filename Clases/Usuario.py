class Usuario:
    """ Esta clase representa al Usuario, el cual le permite acceder al sistema """

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.activo = True

    def cambia_pass(self, password):
        self.password = password

    def inactivar(self):
        self.activo = False
