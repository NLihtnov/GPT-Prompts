from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
prompt_sistema = """Você é um gerador de questões.
Você deve escolher uma pergunta da lista abaixo e gerar uma nova pergunta com o mesmo tema mas reescrita de forma a ser diferente:
#### Lista de categorias válidas
Beleza
Entretenimento
Esportes
Outros
### Exemplo
bola de tenis
Esportes
"""
client = OpenAI(api_key=api_key)

resposta = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": prompt_sistema
        },
        {
            "role": "user",
            "content": "bola de ping pong"
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    n=5
)
for i in range(0,5):
    print(resposta.choices[i].message.content)
    print("---------------------------------")
