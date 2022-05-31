import os
import numpy as np
import speech_recognition as sr

from datetime import datetime
from gtts import gTTS

class PyChat():

    def __init__(self, name):
        self.name = name
        print(f'--- Starting up {name} ---')
        return
    @staticmethod

    def TextSpeech(text):

        speaker = gTTS(text=text, lang='en', slow=False)
        speaker.save('res.mp3')
        os.system("start res.mp3")
        os.remove('res.mp3')
        print('{self.name} : {text}')

        return

    def WakePyChatUp(self, text):
        return True if self.name in text.lower() else False

    @staticmethod
    def AiClock(text):

        now = datetime.now().time().strftime('%H:%M')
        return f'It\'s {now} a Clock'
    
    def AiDate(self):

        date = datetime.date().strftime('%d/%a-%y')
        return f'Today\'s date : {date}'
        
    def SpeechToText(self):

        reconizer = sr.Recognizer()

        with sr.Microphone() as mic:
            print('Listening to your voice')
            audio = reconizer.listen(mic)

        try:
            self.text = reconizer.recognize_google(audio)
            print(f'me > {self.text}')

        except:
            print('me got an error')

        return 
    
if __name__ == '__main__':

    ai = PyChat(name = 'Julie')

    while True:

        ai.SpeechToText()

        if ai.WakePyChatUp(ai.text) is True:
            
            res = 'Hello, I\'m PyChat, What can i do for you?'
            ai.TextSpeech(res)

            #   Action to be done
        elif "time" in ai.text:
            res= ai.AiClock()
        else:
            res = 'I\'m sorry, Come again?'
            ai.TextSpeech(res)

    print(f'---  Closing down {self.name}')