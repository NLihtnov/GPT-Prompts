from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

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

