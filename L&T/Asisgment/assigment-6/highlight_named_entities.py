import spacy
def highlight_named_entities(description):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(description)
    highlighted_description = ""
    for token in doc:
        if token.ent_type_:
            highlighted_description += f"[{token.ent_type_}] {token.text} "
        else:
            highlighted_description += token.text + " "

    return highlighted_description.strip()

sample_input = "The iPhone 13 features a stunning Super Retina XDR display."
highlighted_output = highlight_named_entities(sample_input)
print(highlighted_output)
