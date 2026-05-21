
import requests
import json
from datetime import datetime
import speech_recognition as sr
from PIL import Image
import pytesseract

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

API_KEY = "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"

# Create recognizer
recognizer = sr.Recognizer()

print("Welcome to PyChat AI!")
print("Type 'exit' to quit.\n")

while True:

    print("\n1. Type Message")
    print("2. Use Microphone")
    print("3. Image To Text + AI Summary")

    choice = input("Choose option: ")

    # TEXT INPUT
    if choice == "1":

        user_input = input("You: ")

    # MICROPHONE INPUT
    elif choice == "2":

        with sr.Microphone() as source:

            print("Listening...")

            audio = recognizer.listen(source)

            user_input = recognizer.recognize_google(audio)

            print("You:", user_input)

    # OCR + AI SUMMARY
    elif choice == "3":

        image_path = input("Enter image path: ").strip('"')

        image = Image.open(image_path)

        extracted_text = pytesseract.image_to_string(image)

        print("\nExtracted Text:\n")
        print(extracted_text)

        # Send extracted text to AI
        user_input = "Summarize this text:\n" + extracted_text

    else:
        print("Invalid Choice")
        continue

    # EXIT CONDITION
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # API REQUEST
    response = requests.post(

        url="https://openrouter.ai/api/v1/chat/completions",

        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },

        json={

            "model": "openai/gpt-3.5-turbo",

            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }
    )

    # Convert response to JSON
    data = response.json()

    # Current Time
    current_time = datetime.now().strftime("%I:%M %p")

    # CHECK RESPONSE
    if "choices" in data:

        bot_reply = data["choices"][0]["message"]["content"]

        # PRINT BOT RESPONSE
        print("\n[" + current_time + "] PyChat AI: " + bot_reply)

        # SAVE CHAT HISTORY
        history = open("chat_history.txt", "a")

        history.write("[" + current_time + "] You: " + user_input + "\n")
        history.write("[" + current_time + "] PyChat AI: " + bot_reply + "\n\n")

        history.close()

    else:
        print("\nError:", data)
                                              



























                                                                                            