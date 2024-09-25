import spacy

# Load the SpaCy model
nlp = spacy.load('en_core_web_sm')

def parse_user_description(description):
    """Extracts keywords from the user description."""
    doc = nlp(description)
    # Extract relevant adjectives and nouns for the wallpaper style
    keywords = [token.text for token in doc if token.pos_ in ('NOUN', 'ADJ')]
    return keywords

# Example usage:
# keywords = parse_user_description("I want a minimalistic blue wallpaper")
# print(keywords)
