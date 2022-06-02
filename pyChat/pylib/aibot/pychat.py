
#   pylib Repositories
from pylib.dictionary.pyChatSamp import Samp
from pylib.dictionary.pyChatgreets import GreetMember
from pylib.dictionary.pyChatFunctions import StringManagement

class PyChat():

    def __init__(self, name):

        self.name = name
        print(f'--- Starting up the AI, {name} --')

        return

    @staticmethod
    def PyChatSamp(text):

        #   listed functions
        faq =  [Samp.FrequentlyAskedQuestionsSAMP(text),
                        #Samp.FrequentlyAskedQuestionsECRPG(text),
                        GreetMember.Greetings(text),
                        ]
        #   Filter out None
        faq = list(filter(None, faq))
        for i, j in faq:return j

        return

    def PyChatResponse(text):return print(f'AI > {text}')
    def PyChatWakeUp(self, text):return True if self.name in text else False

    def PyChatGreet():
        return
