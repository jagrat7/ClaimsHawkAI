from transformers import GPT2Tokenizer, TFGPT2LMHeadModel

# Load the pre-trained GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = TFGPT2LMHeadModel.from_pretrained('gpt2')

# Define the input prompt
prompt = "Get the fruits from this list [brick,dog,apple,carrot,kiwi,plum,cat,pig] "

# Encode the input prompt
encoded_input = tokenizer(prompt, return_tensors='tf')

# Generate text using the model
output = model.generate(
    input_ids=encoded_input['input_ids'],  # Input prompt
    max_length=50,                       # Maximum length of the generated text
    num_return_sequences=10,               # Number of sequences to generate
    no_repeat_ngram_size=2,               # Prevent repeating n-grams
    top_k=50,                             # Top-K sampling
    top_p=0.95,                           # Top-p (nucleus) sampling
    temperature=0.7,                      # Sampling temperature
    do_sample=True                        # Enable sampling
)

# Decode the generated text
for o in output:
    decoded_text = tokenizer.decode(o, skip_special_tokens=True)
    print('***output: ',decoded_text) 

