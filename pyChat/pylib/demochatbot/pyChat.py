import os
import transformers
import numpy as np
import speech_recognition as sr

from time import sleep
from datetime import datetime
from gtts import gTTS

class PyChat():

    def __init__(self, name):

        self.name = name
        print(f'--- Starting up {name} ---')

        return

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

    @staticmethod
    def TextSpeech(text):

        print(f'AI :> {text}')

        # configuring audio input
        speaker = gTTS(text=text, lang='en', slow=False)
        speaker.save('res.mp3')
        statbuff = os.stat('res.mp3')
        mbytes = statbuff.st_size / 1024
        duration = mbytes / 200
        os.system('start res.mp3')
        os.system('close res.mp3')
        sleep(int(50*duration))
        os.remove('res.mp3')

        return

    def WakePyChatUp(self, text):
        return True if self.name in text else False

    @staticmethod
    def AiDate():

        now = datetime.now().date().strftime('%d. %b, %Y')

        return f' Today\'s date {now}'

    @staticmethod
    def AiTime():
        now = datetime.now().time().strftime('%H:%M')

        return f'It\'s {now} a Clock.'

if __name__ == '__main__':

    #   Initializing variables
    ex = True
    ai = PyChat(name = 'Jake')
    nlp = transformers.pipeline('conversational', model='microsoft/DialoGPT-medium')
    os.environ['TOKENIZERS_PARALLELISM'] = "True"

    while ex:

        #   List
        close = ['exit', 'close']
        ai.SpeechToText()

        if ai.WakePyChatUp(ai.text) is True:res = 'Hello, I\'m PyChat, What can i do for you?'
        elif 'time' in ai.text:res = ai.AiTime()
        elif 'date' in ai.text:res = ai.AiDate()
        elif any(i in ai.text for i in close ): 

            res = np.random.choice(['Tata', 'Bye'])
            ex = False

        else:
            if ai.text=='ERROR': res = 'I\'m sorry, come again?'

            else:

                chat = nlp(transformers.Conversation(ai.text), pad_token_id=50250)
                res = str(chat)
                res = res[res.find('bot >>')+6:].strip()

        ai.TextSpeech(res)
    print('--- PyChat left the voice chat ---')