from transformers import pipeline
import csv

model_name = "deepset/roberta-base-squad2"

# Initialize the question-answering pipeline
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

# Function to process a single sentence
def process_sentence(sentence):
    QA_input = {
        'question': 'Was there a claim made by the politician in this sentence? If Yes, what was it?',
        'context': sentence
    }
    return nlp(QA_input)

# Read sentences from CSV and process each one
results = []
with open('sentences.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row:  # Check if the row is not empty
            sentence = row[0]
            result = process_sentence(sentence)
            results.append((sentence, result))

# # Print results
# for sentence, result in results:
#     print(f"Sentence: {sentence}")
#     print(f"Answer: {result['answer']}")
#     print(f"Score: {result['score']}")
#     print("-" * 50)

# Optionally, you can save the results to a new CSV file
with open('processed_sentences.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Sentence', 'Answer', 'Score'])
    for sentence, result in results:
        writer.writerow([sentence, result['answer'], result['score']])


# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
