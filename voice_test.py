from core.speech_to_text import listen
from core.text_to_speech import speak
from core.tutor import tutor_response

while True:
    print("\n🎤 Speak now (or say 'exit'):")

    user_input = listen()

    print("You said:", user_input)

    if user_input.lower() == "exit":
        break

    response = tutor_response(user_input)

    print("Bot:", response)

    speak(response)