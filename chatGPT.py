import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write for me how to feel good "}])
print(completion.choices[0].message.content)
