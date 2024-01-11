import yfinance

data = yfinance.download("TSLA", "2024-01-01", "2024-01-12")
print(data["Low"])
