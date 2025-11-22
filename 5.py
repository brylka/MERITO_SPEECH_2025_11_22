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

# Historia konwersacji
conversation_history = []

print("ChatGPT API - konwersacja z historią")
print("Wpisz 'exit' aby zakończyć, 'reset' aby wyczyścić historię")
print("-" * 50)

# Główna pętla
while True:
    # Pobierz pytanie od użytkownika
    user_prompt = input("\nTy: ")

    # Zakończ jeśli wpisano 'exit'
    if user_prompt.lower() == 'exit':
        print("Do widzenia!")
        break

    # Reset historii
    if user_prompt.lower() == 'reset':
        conversation_history = []
        print("Historia konwersacji wyczyszczona")
        continue

    # Dodaj wiadomość użytkownika do historii
    conversation_history.append({"role": "user", "content": user_prompt})

    try:
        # Wysłanie zapytania do ChatGPT z całą historią
        response = client.chat.completions.create(
            model=model,
            messages=conversation_history,
            temperature=0.7
        )

        # Pobierz odpowiedź
        assistant_message = response.choices[0].message.content

        # Dodaj odpowiedź do historii
        conversation_history.append({"role": "assistant", "content": assistant_message})

        # Wyświetl odpowiedź
        print(f"\nChatGPT: {assistant_message}")

        # Statystyki
        print(f"\nZużyte tokeny: {response.usage.total_tokens}")
        print(f"Wiadomości w historii: {len(conversation_history)}")
        print("-" * 50)

    except Exception as e:
        print(f"\nBłąd: {str(e)}")
        # Usuń ostatnią wiadomość użytkownika w razie błędu
        conversation_history.pop()
