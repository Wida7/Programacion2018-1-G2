from Semana13.Clases.Habitacion import Habitacion
"""Importamos nuestra clase de habitacion la cual nos permite:
relacionarl los hoteles con las habitaciones.
"""

class Hotel:
    """Representa nuestro hotel"""

    habitaciones = []
    """Crea la lista de habitaciones, para relacionar con cada hotel"""

    def __init__(self, nombre, estrellas, servicios):
        """
        Crea una nueva instancia de hotel
        :param nombre: nombre del hotel
        :param estrellas: estrellas del hotel
        :param servicios: prestacion de servicios de la habitacion
        :return: representacion del hotel
        """
        self.nombre = nombre
        self.estrellas = estrellas
        self.servicios = servicios

    def __repr__(self):
        """Representamos la clase del hotel"""
        
        return 'Hotel '+ self.nombre +' de '+ \
               self.estrellas + ' presta los servicios de '\
               + str(self.servicios)
