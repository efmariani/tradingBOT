import yfinance as yf
import pandas as pd
import mplfinance as mpf
from datetime import datetime
import os


#Parametros
ticker = "AAPL"
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



tikerData = importData (ticker, start_date, end_date)

mpf.plot(tikerData, type='candle', mav=(100,200), volume=True, title='Apple Stock')





