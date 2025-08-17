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