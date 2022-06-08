
#   Python Repositories
import numpy as np
import transformers
import os

from os import getenv
from sys import api_version

#   Discord Repositories
from discord.message import Message
from discord.ext.commands import Bot
from pylib.list.samplist import CommonIssues, CommonGlitches, CommonSAMPGlitches, CommonSAMPIssues, FrequentlyAskedQuestions

#   pylib Repositories
from pylib.aibot.pychat import PyChat


class DiscordBot(Bot):
    def __init__(self, command_prefix='?', name='PyChat', help_command=None, description=None, owner_id = 340540581174575107, **options):
        super().__init__(command_prefix = command_prefix, help_command=help_command, description=description, owner_id = owner_id, **options)


        return

    async def on_ready(self):

        srv= []
        servers = ''
        svr = self.guilds

        for i in svr:
            servers += f'{i}\n' 

        print(f'''--- Starting up {self.user.name} -----\n {self.user.name} has establized a connection to\n{servers}''')


        return

        
    async def on_message(self, message:Message):


        #   Procsess commands
        await self.process_commands(message)

        if message.author == self.user: return

        else:

            #   Initializing variables
            msg = message.channel
            
            ai = PyChat(name='PyChat')
            text = message.content
            nlp = transformers.pipeline('conversational', model='microsoft/DialoGPT-small')
            os.environ['TOKENIZERS_PARALLELISM'] = "True"
            print(f'me > {text}')

            #   Date & Time
            time = ['Date', 'Time']

            #   SAMP Documentations
            #   Initializing variables / Lists
            
            # Have to find a better way to go through the list
            glitch = [
                        CommonIssues(), 
                        CommonGlitches(), 
                        CommonSAMPIssues(),
                        CommonSAMPGlitches(),
                        FrequentlyAskedQuestions(),
                    ]
            samp = ''

            for i in glitch: 
                if text in i:samp = text

            # Waking up PyCHat
            #if ai.PyChatWakeUp(text) is True: res = 'Greetings, I\'m PyChat, How can i be at your service today?'
            if text in time: res = ai.AiToday(text)
            elif text in samp:res = ai.PyChatSampDocumentations(text)
            elif 'PyChat' in text: res = ai.PyChatDocumentations(text) 


            #elif close in text: res = ai.PyChatCloseDown(text)
            else :

                if text=='ERROR': res = 'I\'m sorry, come again?'

                else:
                    #   The nlp
                    chat = nlp(transformers.Conversation(text), pad_token_id=50250)
                    res = str(chat)
                    res = res[res.find('bot >>')+6:].strip()

            print(f'AI > {res}')
            await msg.send(res)

        return
