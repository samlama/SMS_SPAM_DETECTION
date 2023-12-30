from sklearn.feature_extraction.text import CountVectorizer
def create_bow_vector(query):
    vectorizer = CountVectorizer()
    bow_vector = vectorizer.fit_transform([query])

    feature_names = vectorizer.get_feature_names_out()
    counts = bow_vector.toarray().flatten()

    bow_dict = {feature: count for feature, count in zip(feature_names, counts)}

    return bow_dict

sample_input = "How to learn NLP and Perform the preprocessing?"

bow_vector = create_bow_vector(sample_input)

print(bow_vector)
