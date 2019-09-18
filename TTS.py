from pygame import mixer
from gtts import gTTS

def TTS(String):
    FileName = str(String) + ".mp3"
    tts = gTTS(text=String, lang='ko')
    tts.save('/home/ubuntu/braille/Speech/' + FileName)

def Playing(str):
    mixer.init()
    mixer.music.load('/home/ubuntu/braille/Speech/' + str +".mp3")
    mixer.music.play()
