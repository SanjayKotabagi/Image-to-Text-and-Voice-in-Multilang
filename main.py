from asyncio.windows_events import NULL
from fnmatch import translate
import img2text as i2t
import lang2lang as l2l
import text2voice as t2v
import voice2text as v2t
import streamlit as st

service = st.radio(
     "What service do you want ?",
     ('Get text from Image with Voice', 'Voice to Text','Text to Voice'))


if service == 'Get text from Image with Voice':
    itype = st.radio(
     "How you want to upload files ?",
     ('Locally', 'Camera'))
    if itype == "Locally":
        picture = st.file_uploader("Choose a file")
    if itype == "Camera":
        picture = st.camera_input("Take a picture")
        if picture:
            with open ('image.jpg','wb') as file:
                file.write(picture.getbuffer())
        picture = 'image.jpg'

    try:
        textres = i2t.get_text(picture)
        st.write(textres)
        aud = t2v.convert2speech(textres,'en')
        audio_file = open(aud, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg')
        tres = ''
        if st.button("Kannada"):
            tres = l2l.convert2lang('en','kn',textres)
        if st.button("Hindi"):
            tres = l2l.convert2lang('en','hi',textres)
        st.write(tres)
    except:
        pass 

if service == "Voice to Text":
    try:
        st.write('Talk (Timeout 4 sec)')
        voiceres = v2t.get_res()
        st.write(voiceres)
        st.write('Press Record')
        tres = ''
        translang = st.radio("Choose Languge to Translate",('Kannada', 'Hindi'))
        if translang == 'Kannada':
            tres = l2l.convert2lang('en','kn',voiceres)
        if translang == 'Hindi':
            tres = l2l.convert2lang('en','hi',voiceres)
        st.write(tres)
    except:
        pass

if service == "Text to Voice":
    textres = st.text_input('Text You want to Convert')
    try:
        aud = t2v.convert2speech(textres,'en')
        audio_file = open(aud, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg')
        tres = ''
        translang = st.radio("Choose Languge to Translate",('Kannada', 'Hindi'))
        if translang == 'Kannada':
            tres = l2l.convert2lang('en','kn',textres)
        if translang == 'Hindi':
            tres = l2l.convert2lang('en','hi',textres)
        st.write(tres)
    except:
        pass
