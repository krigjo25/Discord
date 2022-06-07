
#   Python Repositories
import numpy as np
from datetime import datetime

#   pylib Repositories
from pylib.documentations.sampDocumentations import SampFAQ
#from pylib.documentations.ecrpgDocumentation import ECRPGFAQ

class PyChat():

    def __init__(self, name):

        self.name = name
        print(f'--- Starting up the AI, {name} --')

        return

    @staticmethod
    def AiToday(text):

        """
            Returns time or date 
        """

        text = str(text).capitalize()
        time = datetime.now().time().strftime('%H:%M')
        date = datetime.now().date().strftime('%d. %b, %Y')

        if 'Date' in text:res =  f'Today\'s date : {date}'
        elif 'Time' in text:res = f'Current time : {time}'
        else: return

        return res
    
    @staticmethod
    def PyChatSampDocumentations(text):

        text = str(text).capitalize()

        #   listed functions
        faq =  [

                SampFAQ.SAMPGlitches(text),
                SampFAQ.CommonSAMPErrors(text),            
                
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

    def PyChatDocumentations(text):
        res = ''
        return res

    def PyChatResponse(text):return print(f'AI > {text}')
    def PyChatWakeUp(self, text):return True if self.name in text else False

    @staticmethod
    def PyChatCloseDown(text):

        text = str(text)

        procedure = [   'Bye', 
                        'Cya', 
                        'See you',
                        'later' 
                    ]
        
        if text in procedure:
        
            closeDown= [
                        'Bye',
                        'See you later',
                        'Tata',
                        'Farewell',
                        'Bye',]

            closeDown = np.random.choice(closeDown)

            return  closeDown

        return
