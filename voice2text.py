import speech_recognition as sr


r = sr.Recognizer()
def get_res():    
    with sr.Microphone(0) as source:
        audio_text = r.listen(source,timeout=2)
        
        try:
            return ("Text: "+r.recognize_google(audio_text))
        except:
            return ("Sorry, I did not get that")
