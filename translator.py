import argostranslate.translate
from deep_translator import GoogleTranslator

installed_languages = argostranslate.translate.get_installed_languages()

#  Check internet
def is_online():
    import socket
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except:
        return False

#  Offline translation (Argos)
def translate_offline(text, from_code, to_code):
    try:
        from_lang = next(l for l in installed_languages if l.code == from_code)
        to_lang = next(l for l in installed_languages if l.code == to_code)
        return from_lang.get_translation(to_lang).translate(text)
    except:
        return text

#  Online translation (Google)
def translate_online(text, from_code, to_code):
    try:
        return GoogleTranslator(source=from_code, target=to_code).translate(text)
    except:
        return text

#  MAIN FUNCTION
def to_english(text, lang):

    if lang == "en":
        return text.lower()

    if is_online():
        print(" Using ONLINE translation")
        translated = translate_online(text, lang, "en")
    else:
        print(" Using OFFLINE translation")
        translated = translate_offline(text, lang, "en")

    if not translated or translated.strip() == text.strip():
        print(" Translation failed")
        return text.lower()

    return translated.lower()


def to_original(text, lang):

    if lang == "en":
        return text

    if is_online():
        return translate_online(text, "en", lang)

    # fallback offline (only Hindi supported properly)
    return translate_offline(text, "en", lang)