from core.speech_to_text import listen
from core.translator import to_english, to_original
from core.tutor import tutor_response
from core.text_to_speech import speak
from core.search_engine import load_index
from langdetect import detect
import socket
#  INTERNET CHECK
def is_online():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except:
        return False

# Load FAISS
print(" Loading FAISS index...")
index, chunks = load_index()
print(" AI Tutor Ready ")

while True:

    print("\n1. Text\n2. Voice")
    choice = input("Choose: ")

    # INPUT
    if choice == "1":
        user_input = input("You: ")
    else:
        user_input = listen()

    if not user_input or len(user_input.strip()) < 3:
        print(" Try again")
        continue

    # LANGUAGE DETECT
    try:
        lang = detect(user_input)
    except:
        lang = "en"

    print("Language:", lang)

    #  ONLINE / OFFLINE MODE
    online = is_online()

    if online:
        print(" Using ONLINE translation")
    else:
        print(" Using OFFLINE mode")

    # TRANSLATE TO ENGLISH
    query_en = to_english(user_input, lang)

    if query_en.strip() == user_input.strip():
        print(" Translation fallback used")

    print("Translated:", query_en)

    # AI RESPONSE
    answer_en = tutor_response(query_en, chunks, index)

    # BACK TRANSLATION
    final_answer = to_original(answer_en, lang)

    print("Tutor:", final_answer)

    # 🔊 SPEAK EVERY TIME
    speak(final_answer, lang)
import gc
gc.collect()