import pygame
from gtts import gTTS

freq = 24000
bitsize = -16
channels = 2
buffer = 512

def TTS(String):
    FileName = str(String) + ".mp3"
    tts = gTTS(text=String, lang='ko')
    tts.save('/home/ubuntu/braille/Speech/' + FileName)

def Playing(str):
    pygame.init()
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.load('/home/ubuntu/braille/Speech/' + str +".mp3")
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(30)
    pygame.mixer.music.stop()
