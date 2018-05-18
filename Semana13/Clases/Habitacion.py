from Semana13.Clases.Reserva import Reserva
""" Importamos nuestra clase de reserva, la cual nos permite:
Validar las reservas que sean posibles,
Conocer las caracteristicas de las habitaciones.
"""

class Habitacion:
    """ Representa la clase de una habitacion, y su relacion con las reservas"""

    reservas = []

    def __init__(self, numero, tipo):
        """
        Crea una nueva instancia de Habitaciones
        
        :param numero: El numero de la habitacion
        :param tipo: La caracteristica de la habitacion   
        """
        self.numero = numero
        self.tipo = tipo


    def reservar(self, nueva_reserva):
       """
        Crea una nueva instancia para reserva, y valida las reservas de la habitacion
        
        :param nueva_reserva: Recibe una reserva y valida si esta es viable.
        :return: Validacion de la reserva.
        :ValueError: Si la reserva no se encuentra disponible o esta mal ingresada.
        """        
        for reserva in self.reservas:
            if(reserva.coliciona(nueva_reserva)):
                raise ValueError('La habitación no se'
                                 ' encuentra disponible '
                                 'para esa fecha')
        self.reservas.append(nueva_reserva)


    def __repr__(self):
        """ Representamos nuestra clase """
        
        return 'Habitación # '+self.numero\
               + ' de tipo '+self.tipo+' Tiene '\
               + str(len(self.reservas))+ ' reservas'
