from Semana13.Clases.Habitacion import Habitacion
"""Importamos nuestra clase de habitacion la cual nos permite
relacionar nuestra clase de hotel con habitaciones
"""

class Hotel:
    """Representa nuestro hotel"""

    habitaciones = []

    def __init__(self, nombre, estrellas, servicios):
        """
        Crea una nueva instancia de hotel
        :param nombre: nombre del hotel
        :param estrellas: estrellas del hotel
        :param servicios: prestacion de servicios de la habitacion
        :return: representacion de las habitaciones
        """
        self.nombre = nombre
        self.estrellas = estrellas
        self.servicios = servicios

    def __repr__(self):
        """Representamos la clase del hotel"""
        
        return 'Hotel '+ self.nombre +' de '+ \
               self.estrellas + ' presta los servicios de '\
               + str(self.servicios)
