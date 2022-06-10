
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

        return

    def ReadChangelog():

        with open('pyChat/changelog.md', 'r') as f:

            changelog = f.read(415)
            print(f)
            #   Closing the document
            f.close()

        return changelog

    def GeneralPyChatQuestions(self, text):

        #   Initializing lists
        faq = FrequentlyAskedPyChatQuestions()

        # Initializing variables
        text = str(text).lower()
        text = StringManagement.ReplaceCharacters(text)

        if text in faq:

            #   Variable Initialation
            svr = len(self.bot.guilds)

            link = {
                    'what are you pychat':'https://github.com/krigjo25/Discord/blob/main/pyChat/readme.md',
                    }

            res = {
                            'what are you pychat':f'''Greetings, i\'m PyChat\nGreetings, I\'m PyChat Thank you for being curious about me, it makes me happy.\nI\'m an Artificial Intelligence or abbreviation AI & I\'m designed to be your friend and help you out.\n\n**More details about me**\n I watch around around *{svr}* **Discord Servers**.\nI was publicly **released** at *{getenv('PyChatRelease')}* & :new: **Upgraded** *{getenv('PyChatUpdated')}*.\nMy **Current release** is *{getenv('PyChatv')}* :person_with_probing_cane: & & I\'m  **maintained** by *@Krigjo25#5588*:flag_no:'\nI\'m **hosted** *locally* from Norway:flag_no:.\nIf you go to the link you can check some information about me {link[text]}''',
                            #'pychat changelog':FAQ.ReadChangelog(),
            }

            res = res[text]
            print(res)
            return res

        return
