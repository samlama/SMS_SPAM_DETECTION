from textblob import TextBlob

def analyze_sentiment(comment):
    analysis = TextBlob(comment)

    if analysis.sentiment.polarity > 0:
        return "Positive Sentiment"
    elif analysis.sentiment.polarity == 0:
        return "Neutral Sentiment"
    else:
        return "Negative Sentiment"

sample_input = "This product exceeded my expectations. Highly recommended!"

# Analyze the sentiment
sentiment_output = analyze_sentiment(sample_input)

print(sentiment_output)
