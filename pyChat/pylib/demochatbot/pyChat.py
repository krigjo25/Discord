import os
import transformers
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
        os.system('start res.mp3')
        os.remove('res.mp3')
        print(f'AI :> {text}')

        return

    @staticmethod
    def AiDate():

        now = datetime.now().date().strftime('%d. %b, %Y')

        return f' Today\'s date {now}'

    @staticmethod
    def AiTime():

        now = datetime.now().time().strftime('%H:%M')

        return f'It\'s {now} a Clock.'

    def SpeechToText(self):

        reconizer = sr.Recognizer()

        with sr.Microphone() as mic:
            print('Listening to your voice...')
            audio = reconizer.listen(mic)

        try:
            self.text = reconizer.recognize_google(audio)
            print(f'me -> {self.text}')

        except:
            print('I\'m sorry Something went south')

        return 

    def WakePyChatUp(self, text):
        return True if self.name in text else False

if __name__ == '__main__':

    ex = True
    ai = PyChat(name = 'Jake')
    npl = transformers.pipelines('conversational', model='microsoft/DialoGPT-medium')
    os.environ['TOKENIZERS_PARALLELISM'] = True

    while ex:

        ai.SpeechToText()

        if ai.WakePyChatUp(ai.text) is True:res = 'Hello, I\'m PyChat, What can i do for you?'
        elif 'time' in ai.text:res = ai.AiTime()
        elif 'date' in ai.text:res = ai.AiDate()
        elif any(i in ai.text for i in ['exit', 'close']): 
            res = np.random.choice(['Tata', 'Bye'])
            ex = False
        
        ai.TextSpeech(res)
    print('--- PyChat left the voice chat ---')