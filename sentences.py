import re
import csv

# Open the text file and read its contents
with open('./data/biden7mar2024.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove text within parentheses
text = re.sub(r'\(.*?\)', '', text)

# Replace newlines with spaces to join multi-line sentences
text = re.sub(r'\n+', ' ', text)

# New regex pattern for sentence splitting
sentence_pattern = r'(?<=[.!?])\s+(?=[A-Z])|(?<=[.!?]")(?:\s+(?=[A-Z][a-z])|$)'

# Split the text into sentences
sentences = re.split(sentence_pattern, text)

# Clean and filter sentences
cleaned_sentences = [
    ' '.join(sentence.split())  # Remove extra whitespace within sentences
    for sentence in sentences
    if sentence.strip() and len(sentence.split()) > 3  # Require at least 4 words
]

# Save the sentences to a CSV file
with open('sentences.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for sentence in cleaned_sentences:
        writer.writerow([sentence])