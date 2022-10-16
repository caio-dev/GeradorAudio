from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'

sp = gTTS(
    text=input('Insira aqui o texto que será convertido: '),
    lang='pt-br'
)

sp.save(audio)
playsound(audio)
