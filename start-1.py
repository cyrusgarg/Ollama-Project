import requests
import json

url="http://localhost:11434/api/generate"

data={
    "model": "llama3.2",
    "prompt": "What is the capital of France?",
}

response=requests.post(url, json=data,stream=True)

#check if the request was successful
if response.status_code==200:
    print("Request successful. Streaming response")
    for line in response.iter_lines():
        if line:
            decoded_line=line.decode('utf-8')
            result=json.loads(decoded_line)
            generated_text=result.get("response", "")
            print(generated_text, end='', flush=True)

else:
    print(f"Request failed with status code {response.status_code}")