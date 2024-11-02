# from transformers import GPT2Tokenizer, TFGPT2LMHeadModel

# # Load the pre-trained GPT-2 tokenizer and model
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = TFGPT2LMHeadModel.from_pretrained('gpt2')

# # Define the input prompt
# prompt = "Get the fruits from this list [brick,dog,apple,carrot,kiwi,plum,cat,pig] "

# # Encode the input prompt
# encoded_input = tokenizer(prompt, return_tensors='tf')

# # Generate text using the model
# output = model.generate(
#     input_ids=encoded_input['input_ids'],  # Input prompt
#     max_length=50,                       # Maximum length of the generated text
#     num_return_sequences=10,               # Number of sequences to generate
#     no_repeat_ngram_size=2,               # Prevent repeating n-grams
#     top_k=50,                             # Top-K sampling
#     top_p=0.95,                           # Top-p (nucleus) sampling
#     temperature=0.7,                      # Sampling temperature
#     do_sample=True                        # Enable sampling
# )

# # Decode the generated text
# for o in output:
#     decoded_text = tokenizer.decode(o, skip_special_tokens=True)
#     print('***output: ',decoded_text) 

# pip install accelerate
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-9b")
model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2-9b",
    device_map="auto",
    torch_dtype=torch.bfloat16,
    offload_folder=None,  # This disables disk offloading
    low_cpu_mem_usage=True,
)

input_text = "Write me a poem about Machine Learning."
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))


# import transformers
# import torch

# model_id = "meta-llama/Meta-Llama-3-8B"

# pipeline = transformers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
# )
# pipeline("Hey how are you doing today?")
