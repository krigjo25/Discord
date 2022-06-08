
#   Python Repositories
import numpy as np
from datetime import datetime
#   Discord Repositories
from discord.ext.commands import Cog
#   pylib Repositories
from pylib.documentations.pychatDocumentation import FAQ
from pylib.documentations.sampDocumentations import SampFAQ
#from pylib.documentations.ecrpgDocumentation import ECRPGFAQ

#   Custom functions
from pylib.dictionary.pyChatFunctions import StringManagement

class PyChat(Cog):

    def __init__(self, bot ):

        self.bot = bot
        self.name = self.bot.user
        print(f'--- Starting up the AI, {self.name} --')

        return

    @staticmethod
    def AiDateTime(text):

        """
            Returns time or date 
        """

        #   Initializing variables
        text = str(text).capitalize()
        time = datetime.now().time().strftime('%H:%M')
        date = datetime.now().date().strftime('%d. %b, %Y')

        if 'date' in text:res =  f'Today\'s date : {date}'
        elif 'time' in text:res = f'Current time : {time}'
        else: return

        return res
    
    @staticmethod
    def PyChatSampDocumentations(text):

        #   Initializing variables
        text = str(text).capitalize()
        text = StringManagement.ReplaceCharacters(text)

        #   listed functions
        faq =  [

                SampFAQ.SAMPGlitches(text),
                SampFAQ.CommonSAMPErrors(text),
                SampFAQ.GeneralSAMPQuestions(text),

                ]

        #   Filter out None
        faq = list(filter(None, faq))

        for i in faq:return i

        return


    def PyChatDocumentations(self, text):
    
        text = StringManagement.ReplaceCharacters(text)
        
        faq = [
                FAQ.GeneralPyChatQuestions(self, text)
            ]
        print(faq)
        faq = list(filter(None, faq))

        for i in faq:return i

        return

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
