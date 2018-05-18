from Semana13.Clases.Habitacion import Habitacion
"""Importamos nuestra clase de habitacion"""

class Hotel:
    """Representa nuestro hotel"""

    habitaciones = []

    def __init__(self, nombre, estrellas, servicios):
        """
        Crea una nueva instancia de hotel
        :param nombre: nombre del hotel
        :param estrellas: estrellas del hotel
        :param servicios: prestacion de servicios del hotel
        """
        self.nombre = nombre
        self.estrellas = estrellas
        self.servicios = servicios

    def __repr__(self):
        return 'Hotel '+ self.nombre +' de '+ \
               self.estrellas + ' presta los servicios de '\
               + str(self.servicios)
