from pygame import mixer
from gtts import gTTS

def TTS(String):
    FileName = str(String) + ".mp3"
    tts = gTTS(text=String, lang='ko')
    tts.save('./Speech/' + FileName)

def Playing(str):
    mixer.init()
    mixer.music.load('./Speech/' + str +".mp3")
    mixer.music.play()
