import re
import string
def clean_text(text):
    # Remove punctuation, special characters, and numbers
    text = re.sub(r'[^\w\s]', '', text)
    # Convert the text to lowercase___
    text = text.lower()
    return text
def process_dataset(dataset):
    cleaned_reviews = []
    for review in dataset:
        cleaned_review = clean_text(review)
        words = cleaned_review.split()
        cleaned_reviews.append(words)
    return cleaned_reviews
# Sample input dataset
sample_input = [
    "Dow Jones hits record high amid strong corporate earnings.",
    "Terrible experience! The service was slow and the food was cold.",
    "I love this product. It exceeded my expectations!",
    "I enjoy a lot. This can be best in my career and I love the gestures"
]
cleaned_dataset = process_dataset(sample_input)
print(cleaned_dataset)