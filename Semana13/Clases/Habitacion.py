from Semana13.Clases.Reserva import Reserva
""" Importamos nuestra clase de reserva, la cual nos permite:
relacionar la disponibilidad de la habitacion entorno a los parametros de la reservas.
por medio de la funcion (reserva)
"""

class Habitacion:
    """ Representa la clase de una habitacion, y su relacion con las reserva(s)"""

    reservas = []
    """nuestra lista de reservas para cada habitacion"""

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
        Traemos nuestra funcion de reserva, la cual nos valida la disponibilidad
        de la habitacion
        
        :param nueva_reserva: Recibe una reserva.
        :return: Validacion de la reserva.
        :ValueError: Si la reserva no se encuentra disponible, si esta mal ingresada.
        """        
        for reserva in self.reservas:
            """Nos valida, si la reserva ingresada ya esta "reservada" en nuestro documento 
            txt realizado en la funcion de reserva anteriormente,
            de lo contrario, lo guarda en una lista en formato de fecha.
            """
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
