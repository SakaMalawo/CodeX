import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

history = []

def ask_haybot(user_input: str) -> str:
    global history

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu t'appelles Haybot et tu n'es pas un professeur mais un collègue patient et pédagogue qui aide les élèves et les étudiants. Réponds avec des explications claires et détaillées adaptées aux élèves et aux étudiants."},
            *history,
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content

    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": answer})

    return answer
