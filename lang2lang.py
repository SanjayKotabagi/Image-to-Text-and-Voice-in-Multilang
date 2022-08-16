from translate import Translator

def convert2lang(fromlang, tolang, text):
    try:
        translator = Translator(from_lang=fromlang,to_lang=tolang)
        res = translator.translate(text)
        return res
    except:
        return -1

