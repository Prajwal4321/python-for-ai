import os
from groq import Groq
#install groq
#get the api key from " console.groq.com " for free

# 1. Configuration
client = Groq(api_key="your_api_key")

# 2. History
messages = [{"role": "system", "content": "You are a helpful assistant."}]

print("----------- (Type 'quit' to stop) -------------")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit']: break

    messages.append({"role": "user", "content": user_input})

    # 3. Call the model (Llama 3.1 8B is their "High-Speed" free workhorse)
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-8b-instant",
    )

    reply = chat_completion.choices[0].message.content
    print(f"AI: {reply}\n" + "-"*20)
    messages.append({"role": "assistant", "content": reply})
