import yfinance as yf

# Define the stock symbol
symbol = 'AAPL'

# Create a Ticker object for the stock
ticker = yf.Ticker(symbol)

# Retrieve the real-time market data for the stock
data = ticker.info['regularMarketOpen']

# Print the real-time market data
print(data)
