from datetime import *
"""Importamos datetime, para utilizar el formato de fechas"""

class Reserva:
    """
    Representa una reserva, que posteriormente se relaciona con la clase de habitación
    ya que una reserva necesita una habitacion, y la habitacion puede tener varias reservas.
    """

    def __init__(self, cliente, cedula, fecha_inicio, fecha_fin):
        """

        Crea una nueva instancia de reserva

        :param cliente: nombre del cliente (str --> str)
        :param cedula: id del cliente (int --> int)
        :param fecha_inicio: La fecha inicial de la reserva (int --> date)
        :param fecha_fin: Fecha final de reserva (int --> date)
        :return: la reserva realizada
        :ValueError: Si la fecha inicial es anterior a la actual, si la fecha inicial es mayor a la final.
        """
        if fecha_inicio > datetime.now().date() and \
                fecha_inicio < fecha_fin:
            self.cliente = cliente
            self.cedula = cedula
            self.fecha_inicio = fecha_inicio
            self.fecha_fin = fecha_fin
        else:
            raise ValueError('La fecha reserva debe ser mayor a '
                             'hoy y la fecha inicial mayor a la '
                             'fecha final')

    def coliciona(self, other):
        """
        :param other: valida si hay otra fecha que coliciona
        :return: verificar la fecha
        :ValueError: Si la fecha ya esta reservada, si esta mal ingresada.
        """
        if isinstance(other, Reserva):
            return (other.fecha_inicio >= self.fecha_inicio and \
                   other.fecha_inicio <=self.fecha_fin) or \
                   (other.fecha_fin >= self.fecha_inicio and \
                   other.fecha_fin <=self.fecha_fin)
        raise ValueError('No puedo comprar reservas con '
                         +type(other).__name__)

    def __repr__(self):
        """representamos nuestra clase reserva"""
        
        return 'Reserva de '+self.cliente\
               +' cedula '+self.cedula+ \
               ' desde '+str(self.fecha_inicio)+ \
               ' hasta '+ str(self.fecha_fin)
