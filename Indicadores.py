import numpy as np


#Media Movil, recibe los datos y el periodo, lo saca por medio de la convolucion siendo el valor final un promedio sin ponderar de los valores anteriores.
def media_movil(datos, periodo):
    ma = np.convolve(datos, np.ones(periodo) / periodo, mode='valid')
    return ma

