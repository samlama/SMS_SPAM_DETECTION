import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

def tokenize_subject_line(subject_line):
    tokens = word_tokenize(subject_line.lower())

    tokens = [token for token in tokens if token.isalnum()]

    return tokens

sample_input = "Important Update: Action Required"

tokenized_output = tokenize_subject_line(sample_input)

print(tokenized_output)
