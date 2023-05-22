import yfinance as yf

# Get the list of all tickers available on Yahoo Finance
all_tickers = yf.Tickers()

# Extract the ticker symbols
ticker_symbols = all_tickers.tickers.keys()

# Print the ticker symbols
for symbol in ticker_symbols:
    print(symbol)
