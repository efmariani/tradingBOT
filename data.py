import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# Abrir el archivo de texto en modo lectura
with open('Tikers.txt', 'r') as archivo:
    # Leer el contenido del archivo
    contenido = archivo.read() 
# Dividir el contenido en una lista utilizando el salto de línea como separador
valores = contenido.split('\n')



#Parametros de tiempo
start_date = "2010-01-01"
end_date = datetime.now().strftime('%Y-%m-%d')

#Funcion de obtener datos
def importData (ticker, start_date, end_date):

    #Obtiene la direccion de la carpeta TickersData
    subfolder_path = os.path.join(os.getcwd(), "TickersData")

    #Si no existe la carpeta TickerData la crea
    if not os.path.exists(subfolder_path):
        os.mkdir(subfolder_path)

    #Importa los datos del Ticket desde la fecha start hasta la fecha end
    #tickers = "SPY AAPL" list of tickers
    #period = "1y",          # time period
    #interval = "1d",        # trading interval
    #prepost = False,        # download pre/post market hours data?
    #repair = True           # repair obvious price errors e.g. 100x?
    try:
        tikerDataUpdate = yf.download(ticker, start=start_date, end=end_date, interval = "1d", prepost = False) 
    except:
        print('Error de conexion a base de datos.')
        return

    

    return tikerDataUpdate



def refresh_Data():
    for i in valores:
        ticker=i
        tikerData = importData (ticker, start_date, end_date)
        tikerData.to_csv('TickersData/'+ticker+'.csv', index=False)


def Tikers_Cargados():
# Ruta de la carpeta
    folder_path = os.path.join(os.getcwd(), "TickersData")
# Obtener la lista de nombres de archivos en la carpeta
    nombres_archivos = os.listdir(folder_path)
    return nombres_archivos

