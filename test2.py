from transformers import pipeline

# Load a pre-trained NER model
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER")

# Example transcript
transcript = """
As your leader, I promise to reduce unemployment rates by 5% within the next year.
We will also increase the budget for healthcare by 20%.
"""

# Extract claims
claims = ner_pipeline(transcript)

# Filter and process claims
extracted_claims = [entity['word'] for entity in claims if entity['entity_group'] == 'CLAIM']

print(claims)
