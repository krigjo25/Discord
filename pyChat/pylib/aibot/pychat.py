
#   Python Repositories
import numpy as np
from datetime import datetime

#   pylib Repositories
from pylib.dictionary.samp import SampFAQ

class PyChat():

    def __init__(self, name):

        self.name = name
        print(f'--- Starting up the AI, {name} --')

        return

    @staticmethod
    def AiDate(text):

        """
            Returns time or date 
        """

        if 'time' in text or 'date' in text : 

            #   Today's date
            if 'date' in text:

                now = datetime.now().date().strftime('%d. %b, %Y')
                res = res = f'Today\'s date : {now}'
            
            elif 'date' in text:

                #   Get the current time
                now = datetime.now().time().strftime('%H:%M')
                res = f'Current time : {now}'
        

        return res

    @staticmethod
    def PyChatSampDocumentations(text):

        text = str(text).capitalize()

        #   listed functions
        faq =  [

                SampFAQ.Client(text),
                SampFAQ.Server(text),
                SampFAQ.Error(text),
                SampFAQ.CommonIssues(text),                
                
                ]

        #   Filter out None
        faq = list(filter(None, faq))

        for i, j in faq:return j

        return

    @staticmethod
    def PyChatEcrpgDocumentations(text):
        text = str(text).capitalize()

        #   listed functions
        faq =  []

        #   Filter out None
        faq = list(filter(None, faq))

        for i in faq:return i

        return

    def PyChatResponse(text):return print(f'AI > {text}')
    def PyChatWakeUp(self, text):return True if self.name in text else False

    def PyChatCloseDown():

        close = [   'Bye', 
                    'Cya', 
                    'See you',
                    'later' ]
        closeDown= [
                    'Bye',
                    'See you later',
                    'Tata',
                    'Farewell',
                    'Bye',]
        return np.random.choice(closeDown)
