from ollama import chat

messages = [
  {
    'role': 'user',
    'content': 'Explain about abha card',
  },
]

response = chat('llama3.2', messages=messages)
print(response['message']['content'])