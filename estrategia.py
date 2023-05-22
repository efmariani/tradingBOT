from Indicadores import media_movil
from data import Tikers_Cargados
import pandas as pd
import os

folder_path = os.path.join(os.getcwd(), "TickersData")


# Imprimir la lista de nombres de archivos
Tickers= Tikers_Cargados()

def verificar_cruce_medias_moviles(datos, periodo_ma1, periodo_ma2):
    ma1 = media_movil(datos,periodo_ma1)
    ma2 = media_movil(datos,periodo_ma2)
    
    if ma1[-2] > ma2[-2] and ma1[-1] < ma2[-1]:
        print('Cierra '+i)
        return 
    elif ma1[-2] < ma2[-2] and ma1[-1] > ma2[-1]:
        print('Abre '+i)
        return
    else:

        return
        


for i in Tickers:

# Cargar archivo CSV
    data = pd.read_csv(folder_path+'/'+i)
    datos_cierre= data['Close']
    try:
        verificar_cruce_medias_moviles(datos_cierre,50,100)
    except:
        pass