import yfinance as yf
import pandas as pd
import mplfinance as mpf


ticker = "AAPL"
start_date = "2020-01-01"
end_date = "2023-05-01"

data = yf.download(ticker, start=start_date, end=end_date)
print(data.head())


mpf.plot(data, type='candle', mav=(20,50), volume=True, title='Apple Stock')





