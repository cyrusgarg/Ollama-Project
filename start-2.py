import ollama

response = ollama.list()

print("Available models:")
for model in response["models"]:
    print(model['model'])

res= ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ],
    
)

print(res['message']['content'])

res= ollama.generate(
    model="llama3.2",      
    prompt="What is the capital of France?",
    stream=True
)

# print(ollama.show('llama3.2'))


modelfile = """\
from llama3.2
system "You are a very smart assistant who answers questions in a concise and accurate manner."
parameter temperature 0.3
"""
