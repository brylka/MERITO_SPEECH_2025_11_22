from openai import OpenAI
from dotenv import load_dotenv
import os

# Pobranie klucza OpenAI
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY_2')

# Inicjalizacja klienta OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Model do użycia
model = "gpt-3.5-turbo"

print("ChatGPT API - prosty interfejs")
print("Wpisz 'exit' aby zakończyć")
print("-" * 50)

# Główna pętla
while True:
    # Pobierz pytanie od użytkownika
    user_prompt = input("\nTwoje pytanie: ")

    # Zakończ jeśli wpisano 'exit'
    if user_prompt.lower() == 'exit':
        print("Do widzenia!")
        break

    try:
        # Wysłanie zapytania do ChatGPT
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": user_prompt}],
            temperature=0.7
        )

        # Wyświetl odpowiedź
        print(response)
        print("\nOdpowiedź ChatGPT:")
        print(response.choices[0].message.content)

        # Statystyki
        print(f"\nZużyte tokeny: {response.usage.total_tokens}")
        print("-" * 50)

    except Exception as e:
        print(f"\nBłąd: {str(e)}")
