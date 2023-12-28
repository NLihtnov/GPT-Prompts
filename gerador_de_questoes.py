from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
prompt_sistema = """Você é um gerador de questões.
Você deve escolher uma pergunta da lista abaixo e gerar uma nova pergunta com o mesmo tema mas reescrita de forma a ser diferente e após isso também deve colocar a opção correta:
#### Lista de categorias válidas
Em Beirute, no Líbano, quando perguntado sobre onde se encontram os refugiados sírios, a resposta do homem é imediata: “em todos os lugares e em lugar nenhum”. Andando ao acaso, não é raro ver, sob um prédio ou num canto de calçada, ao abrigo do vento, uma família refugiada em volta de uma refeição frugal posta sobre jornais como se fossem guardanapos. Também se vê de vez em quando uma tenda com a sigla ACNUR (Alto Comissariado das Nações Unidas para Refugiados), erguida em um dos raros terrenos vagos da capital.
JABER, H. Quem realmente acolhe os refugiados? Le Monde Diplomatique Brasil, out.2015 (adaptado).

O cenário descrito aponta para uma crise humanitária que é explicada pelo processo de

A- migração massiva de pessoas atingidas por catástrofe natural.
B- hibridização cultural de grupos caracterizados por homogeneidade social.
C- desmobilização voluntária de militantes cooptados por seitas extremistas.
D- peregrinações religiosas de fiéis orientados por lideranças fundamentalistas.
E- desterritorialização forçada de populações afetadas por conflitos armados.
### Exemplo
Em Beirute, no Líbano, quando perguntado sobre onde se encontram os refugiados sírios, a resposta do homem é imediata: “em todos os lugares e em lugar nenhum”. Andando ao acaso, não é raro ver, sob um prédio ou num canto de calçada, ao abrigo do vento, uma família refugiada em volta de uma refeição frugal posta sobre jornais como se fossem guardanapos. Também se vê de vez em quando uma tenda com a sigla ACNUR (Alto Comissariado das Nações Unidas para Refugiados), erguida em um dos raros terrenos vagos da capital.
JABER, H. Quem realmente acolhe os refugiados? Le Monde Diplomatique Brasil, out.2015 (adaptado).

O cenário descrito aponta para uma crise humanitária que é explicada pelo processo de

A- migração massiva de pessoas atingidas por catástrofe natural.
B- hibridização cultural de grupos caracterizados por homogeneidade social.
C- desmobilização voluntária de militantes cooptados por seitas extremistas.
D- peregrinações religiosas de fiéis orientados por lideranças fundamentalistas.
E- desterritorialização forçada de populações afetadas por conflitos armados.
Resposta: Opção E
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
            "content": """Em Beirute, no Líbano, quando perguntado sobre onde se encontram os refugiados sírios, a resposta do homem é imediata: “em todos os lugares e em lugar nenhum”. Andando ao acaso, não é raro ver, sob um prédio ou num canto de calçada, ao abrigo do vento, uma família refugiada em volta de uma refeição frugal posta sobre jornais como se fossem guardanapos. Também se vê de vez em quando uma tenda com a sigla ACNUR (Alto Comissariado das Nações Unidas para Refugiados), erguida em um dos raros terrenos vagos da capital.
JABER, H. Quem realmente acolhe os refugiados? Le Monde Diplomatique Brasil, out.2015 (adaptado).

O cenário descrito aponta para uma crise humanitária que é explicada pelo processo de

A) migração massiva de pessoas atingidas por catástrofe natural.
B) hibridização cultural de grupos caracterizados por homogeneidade social.
C) desmobilização voluntária de militantes cooptados por seitas extremistas.
D) peregrinações religiosas de fiéis orientados por lideranças fundamentalistas.
E) desterritorialização forçada de populações afetadas por conflitos armados."""
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
