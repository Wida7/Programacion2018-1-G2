from Semana13.Clases.Hotel import Hotel
from Semana13.Clases.Habitacion import Habitacion
from Semana13.Clases.Reserva import Reserva
"""importamos nuestras clases para las relaciones"""
from datetime import *
"""importamos para utilizar formatos de date"""

def cargar_hoteles(file):
    """
    Creamos una base de datos en un ducumento txt conforme al objeto de hoteles
    
    :param file: hoteles (str --> str)
    :return: abrir base de datos(txt) de hoteles
    """
    hoteles_resultante = []
    with open(file) as bd_Hoteles:
        """abrimos nuestro archivo para agregar los datos de hoteles"""
        
        lineas = bd_Hoteles.readlines()
        for linea in lineas:
            """damos formato a la base de datos, con posiciones y separadores"""
            
            variables = linea.strip().split(',')
            hoteles_resultante.append(Hotel(variables[0],
                                 variables[1],
                                 variables[2:]))
        bd_Hoteles.close()
    return hoteles_resultante


def cargar_habitaciones(file):
    """
    Creamos una base de datos en un ducumento txt conforme al objeto de habitaciones
    
    :param file: habitaciones (str --> str)
    :return: abrir base de datos(txt) de habitaciones
    """
    habitaciones_resultantes = []
    with open(file) as bd_Habitcion:
        """abrimos nuestro archivo para agregar los datos de habitaciones"""
        
        lineas = bd_Habitcion.readlines()
        for linea in lineas:
            """damos formato a la base de datos"""
            
            variables = linea.strip().split(',')
            habitaciones_resultantes.append(Habitacion(variables[0],
                                                       variables[1]))
        bd_Habitcion.close()
    return habitaciones_resultantes

def cargar_reservas(file):
    """
    Creamos una base de datos en un ducumento txt conforme al objeto de reservas
    
    :param file: reservas (str --> str)
    :return: abrir base de datos(txt) de habitaciones
    """
    
    reservas_resultantes = []
    with open(file) as bd_reservas:
        """abrimos nuestro documentos txt para guardar los datos"""
        lineas = bd_reservas.readlines()
        """relacionamos nuestros datos de (bd_reservas) para guardarlos"""
        
        for linea in lineas:
            """damos formato a la base de datos"""
            
            variables = linea.strip().split(',')
            fecha_inicio = datetime.strptime(
                variables[2],'%Y-%m-%d').date()
            fecha_fin = datetime.strptime(
                variables[3], '%Y-%m-%d').date()
            reservas_resultantes.append(Reserva(
                variables[0],
                variables[1],
                fecha_inicio,
                fecha_fin
            ))
        bd_reservas.close()
    return reservas_resultantes


def guardar_reserva(hotel, habitacion, reserva):
    """
    Funcion para guardar la reserva en la base de datos
    :param hotel: nombre hotel
    :param habitacion: nombre habitacion
    :param reserva: datos de reserva
    :return: guardar la reserva en una base de datos
    """
    f = open('bd/reservas/' +
             hotel.nombre +
             habitacion.numero +
             '.txt', 'a')
    f.write(reserva.cliente + ','
            + reserva.cedula + ',' +
            str(reserva.fecha_inicio) + ','
            + str(reserva.fecha_fin) + '\n')
    f.close()
