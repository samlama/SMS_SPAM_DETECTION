import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
def tokenize_headline(headline):
    tokens = word_tokenize(headline)
    return tokens
def tokenize_headlines(headlines):
    tokenized_headlines = []
    for headline in headlines:
        tokens = tokenize_headline(headline)
        tokenized_headlines.append(tokens)
    return tokenized_headlines
# Sample input headlines
sample_input = [
    "Dow Jones hits record high amid strong corporate earnings.",
    "The marginal product of the company is higher than the last year",
    "Tech stocks surge as companies report better-than-expected profits.",
    "Federal Reserve announces interest rate hike."
]
tokenized_output = tokenize_headlines(sample_input)
print(tokenized_output)
