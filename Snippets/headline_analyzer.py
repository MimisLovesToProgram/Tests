# After 'pip install nltk', you will need to run these commands on the python shell for the package to be ready to use:
# import nltk
# nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

# Defining a dictionary of 'safe' companies and their Ticker Symbols:
safe_company_tickers = {"Berkshire Hathaway": "BRK.B",
                        "The Walt Disney Company": "DIS",
                        "Vanguard High-Dividend Yield ETF": "VYM",
                        "Procter & Gamble": "PG",
                        "Vanguard Real Estate Index Fund": "VNQ",
                        "Starbucks": "SBUX",
                        "Apple": "AAPL",
                        "Quest Diagnostics": "DGX",
                        "Microsoft": "MSFT"}

# Define the input text
input_text = "Apple Announces Record-Braking Profits for 2024."

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Analyze the sentiment of the input text
sentiment_scores = sia.polarity_scores(input_text)

# 'compound' is most likely what you should look at from the output of the above command.

# Print the sentiment scores
print(sentiment_scores)

company = ""
for word in input_text.split():
    if word in safe_company_tickers:
        company = word

print(f"Company's Ticker: {safe_company_tickers[company]}")
