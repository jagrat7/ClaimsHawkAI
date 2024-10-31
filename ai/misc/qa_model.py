from transformers import pipeline
import csv
import pandas as pd

model_name = "deepset/roberta-base-squad2"

# Initialize the question-answering pipeline
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

# Function to process a single sentence
def process_sentence(sentence):
    QA_input = {
        'question': 'What claim was made by the politician in this sentence?',
        'context': sentence
    }
    return nlp(QA_input)

# Read the CSV file
df = pd.read_csv('data/President_Bidens_State_of_the_Union_Address_2024-03-08T034913Z.csv')

# Process each sentence in the 'context' column
results = []
for sentence in df['context']:
    if isinstance(sentence, str) and sentence.strip():  # Check if the sentence is not empty
        result = process_sentence(sentence)
        results.append((sentence, result))

# Save the results to a new CSV file
with open('processed_biden_speech.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Original Sentence', 'Extracted Claim', 'Confidence Score'])
    for sentence, result in results:
        writer.writerow([sentence, result['answer'], result['score']])

print(f"Processing complete. Results saved to 'processed_biden_speech.csv'")
