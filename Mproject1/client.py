from openai import OpenAI
client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

print(completion.choices[0].message.content)