from openai import OpenAI

api_key = "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"

client = OpenAI(api_key=api_key)

resposta = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[
        {
            "role": "system",
            "content": "Gere nomes de produtos fictícios sem descrição de acordo com a requisição do usuário."
        },
        {
            "role": "user",
            "content": "Gere 5 produtos"
        }
    ]
)

print(resposta.choices[0].message.content)
