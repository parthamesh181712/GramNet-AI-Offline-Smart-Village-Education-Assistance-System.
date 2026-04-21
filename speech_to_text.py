import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            text = r.recognize_google(audio, language="en-IN")  #  FORCE ENGLISH

            print("Recognized:", text)
            return text.lower()

        except sr.WaitTimeoutError:
            print(" Listening timeout")
            return ""

        except sr.UnknownValueError:
            print(" Could not understand audio")
            return ""

        except sr.RequestError:
            print(" Internet error (Speech API)")
            return ""