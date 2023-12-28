from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")



def categorizaProduto(nome_do_produto, categorias_validas):
    prompt_sistema = f"""Você é um gerador de questões.
    Você deve escolher uma pergunta da lista abaixo e gerar uma nova pergunta com o mesmo tema mas reescrita de forma a ser diferente:
    Se você receber uma categoria invalida, responda com "Não posso ajudar com isso". 
    #### Lista de categorias válidas
    {categorias_validas}
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
                "content": nome_do_produto
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=5
    )
    print(resposta.choices[0].message.content)

print("Digite as categorias validas:")
categorias_validas = input()

while True:
    print("Digite o nome do produto:")
    nome_do_produto = input()
    categorizaProduto(nome_do_produto, categorias_validas)