from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken

codificador = tiktoken.encoding_for_model("gpt-3.5-turbo-16k")

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")
        
prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega("./lista_de_compras_100_clientes.csv")

lista_de_tokens = codificador.encode(prompt_sistema + prompt_usuario)
numero_de_tokens= len(lista_de_tokens)
print(f"Número de tokens na entrada: {numero_de_tokens}")
modelo = "gpt-3.5-turbo"
tamanho_esperado_saida = 2048 
if numero_de_tokens >= 4096 - tamanho_esperado_saida:
    modelo = "gpt-3.5-turbo-16k"
print(f"Modelo escolhido: {modelo}")

client = OpenAI(api_key=api_key)
resposta = client.chat.completions.create(
  model=modelo,
  messages=[
    {
      "role": "system",
      "content": prompt_sistema
    },
    {
      "role": "user",
      "content": prompt_usuario
    }
  ],
  temperature=1,
  max_tokens=tamanho_esperado_saida,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(resposta.choices[0].message.content)
