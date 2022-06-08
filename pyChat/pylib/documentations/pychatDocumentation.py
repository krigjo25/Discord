
from os import getenv, environ
from dotenv import load_dotenv

from transformers import pipeline,Conversation
from discord.ext.commands import Cog


from pylib.dictionary.pyChatFunctions import StringManagement

from pylib.list.pychatlist import FrequentlyAskedPyChatQuestions

load_dotenv()

class FAQ(Cog):

    def __init__(self, bot):
        self.bot = bot
        
        pass

    def GeneralPyChatQuestions(self, text):

        #   Initializing lists
        faq = FrequentlyAskedPyChatQuestions()

        # Initializing variables
        text = str(text).lower()
        text = StringManagement.ReplaceCharacters(text)
        #   Returns a list of SAMP Support
        nlp = pipeline('conversational', model='microsoft/DialoGPT-small')
        environ['TOKENIZERS_PARALLELISM'] = "True"

        if text in faq:

            #   Variable Initialation
            svr = len(self.bot.guilds)

            link = {
                    }

            res = {
                            'what are you pychat':f'''Greetings, i\'m PyChat\nThank you for being curious about me, it makes me happy.\nI\'m an Artificial Intellegence or abbrivation AI & i\'m designed to be your friend and help you out.\n\n**More details about me**\nI watch around *{svr}* **Discord Servers**.\nI were public  **released** at *{getenv('PyChatRelease')}* & :new: **Upgraded** *{getenv('PyChatUpdated')}*.\nMy **Current release** is *{getenv('PyChatv')}* :person_with_probing_cane: & I\'m **maintained** by *@Krigjo25#5588*:flag_no:'\nI\'m **hosted** *locally* from Norway:flag_no:.\nIf you go to the link you can check some information about me https://www.github.com.''',
                            'pychat changelog':self.ReadChangelog(),
            }

            res = res[text]

            return res

        else:
            #   The nlp
            chat = nlp(Conversation(text), pad_token_id=50250)
            res = str(chat)
            res = res[res.find('bot >>')+6:].strip()
        
            return res
        return

    def ReadChangelog(self):

        with open('Pybut/changelog.md', 'r') as f:

            changelog = f.read(415)

            #   Closing the document
            f.close()

        return changelog