import openai

# Din API-nyckel (byt ut nedan)
openai.api_key = "YOUR_API_KEY_HERE"

def nero_prompt():
    print("Välkommen till NERO OS 🧠\n")
    while True:
        user_input = input("🗣️ Du: ")

        if user_input.lower() in ["avsluta", "exit", "sluta"]:
            print("👋 Hejdå! Nero loggar ut.")
            break

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Du är en varm, hjälpsam, rolig och klok AI-assistent kallad NERO OS."},
                    {"role": "user", "content": user_input}
                ]
            )

            reply = response['choices'][0]['message']['content']
            print(f"🤖 NERO: {reply}\n")

        except Exception as e:
            print(f"⚠️ Fel: {e}")

if __name__ == "__main__":
    nero_prompt()
