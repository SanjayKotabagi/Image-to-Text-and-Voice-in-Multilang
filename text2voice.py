from gtts import gTTS
import os

from sqlalchemy import false, true

def convert2speech(text='',lang='en'):
    try:
        myobj = gTTS(text=text, lang=lang, slow=False)
        myobj.save("audio.ogg")
        return "audio.ogg"
    except:
        pass

