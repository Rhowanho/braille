from pygame import mixer
from gtts import gTTS

def TTS(String):
    FileName = str(String) + ".mp3"
    tts = gTTS(text=String, lang='ko')
    tts.save('C:/Users/tjaud/Documents/motor/Flask/Speech/' + FileName)

def Playing(str):
    mixer.init()
    mixer.music.load('C:/Users/tjaud/Documents/motor/Flask/Speech/' + str +".mp3")
    mixer.music.play()