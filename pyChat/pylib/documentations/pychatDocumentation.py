
from os import getenv, environ
from dotenv import load_dotenv

from transformers import pipeline,Conversation
from discord.ext.commands import Cog

from pylib.list.pychatlist import FrequentlyAskedQuestions

load_dotenv()

class FAQ(Cog):

    def __init__(self, bot):
        self.bot = bot
        
        pass

    def GeneralPyChatQuestions(self, question):

        #   Initializing lists
        faq = FrequentlyAskedQuestions()

        #   Returns a list of SAMP Support
        nlp = pipeline('conversational', model='microsoft/DialoGPT-small')
        environ['TOKENIZERS_PARALLELISM'] = "True"

        if question in faq:

            #   Variable Initialation
            svr = len(self.bot.guilds)

            link = {
                    'Samp installation procedure':'https://www.sa-mp.com/download.php'
                    }

            response = {
                            'What are you PyChat':f'''
                            Thank you for being curious about me. It makes me happy\n
                            \n Greetings, i\'m PyChat.
                            \n I\'m an Artificial Intellegence or AI. I\'m designed to be you\'r NPL assistant & Documentation finder. I do watch {svr} Discord Servers.
                            \n i were public released at {getenv('PyChatRelease')} & Last upgraded {getenv('PyChatUpdated')}.
                            \n My Current release is {getenv('PyChatv')} & I\'m Maintained by @Krigjo25#5588'
                            \n Programmed by Krigjo25''',
            }

            response = response[question]

            return response

        else:
            #   The nlp
            chat = nlp(Conversation(question), pad_token_id=50250)
            res = str(chat)
            res = res[res.find('bot >>')+6:].strip()
        
            return res
        return

