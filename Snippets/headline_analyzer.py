# After 'pip install nltk', you may need to run these commands on the python shell for the package to be ready to use:
# import nltk
# nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

# Define the input text
input_text = "Apples Are Good For You - Here's Why."

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Analyze the sentiment of the input text
sentiment_scores = sia.polarity_scores(input_text)

# 'compound' is most likely what you should look at from the output of the above command.

# Print the sentiment scores
print(sentiment_scores)
