import yfinance as yf
import pandas as pd
import mplfinance as mpf
from datetime import datetime
import os



ticker = "AAPL"
start_date = "2020-01-01"
end_date = datetime.now().strftime('%Y-%m-%d')

tikerDataUpdate = yf.download(ticker, start=start_date, end=end_date, interval = "1d", prepost = False)  

print(tikerDataUpdate.head())

tikerDataUpdate = tikerDataUpdate.reset_index()

print(tikerDataUpdate.head())