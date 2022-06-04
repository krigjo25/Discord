
#   Python Repositories
import numpy as np
import transformers
import os

from os import getenv
from sys import api_version

#   Discord Repositories
from discord.message import Message
from discord.ext.commands import Bot

#   pylib Repositories
from pylib.aibot.pychat import PyChat


class DiscordBot(Bot):
    def __init__(self, command_prefix='?', name='PyChat', help_command=None, description=None, owner_id = 340540581174575107, **options):
        super().__init__(command_prefix = command_prefix, help_command=help_command, description=description, owner_id = owner_id, **options)


        return

    async def on_ready(self):

        srv= []
        svr = self.guilds

        for i in svr:
            srv.append(i)

        print(f'''--- Starting up {self.user.name} -----\n {self.user.name} has establized a connection to {srv[0]}''')


        return

        
    async def on_message(self, message:Message):


        #   Procsess commands
        await self.process_commands(message)

        if message.author == self.user: return

        else:

            #   Initializing variables
            msg = message.channel
            ai = PyChat(name='PyChat')
            text = str(message.content).capitalize()
            nlp = transformers.pipeline('conversational', model='microsoft/DialoGPT-small')
            os.environ['TOKENIZERS_PARALLELISM'] = "True"
            print(f'me > {text}')

            # lists
            
            # Waking up PyCHat
            if ai.PyChatWakeUp(text) is True: res = 'Greetings, I\'m PyChat, How can i be at your service today?'
            elif 'samp' in text or 'Samp' in text or 'san andreas' in text or 'San andreas' in text: res = ai.PyChatSampDocumentations(text)
            elif 'time' in text or 'date' in text : res = ai.AiToday(text)
            #elif ai.PyChatCloseDown(text) in text: res = ai.PyChatCloseDown(text)
            else :

                if text=='ERROR': res = 'I\'m sorry, come again?'

                else:

                    chat = nlp(transformers.Conversation(text), pad_token_id=50250)
                    res = str(chat)
                    res = res[res.find('bot >>')+6:].strip()

            print(f'AI > {res}')
            await msg.send(res)

            '''
            #   Initializing variables
            msg = message.channel
            userInput = str(message.content).capitalize().replace('Whats', 'What is')

            #   Managing Strings
            userInput = StringManagement.ReplaceCharacters(userInput)

            #   listed functions
            response =  [Samp.FrequentlyAskedQuestionsSAMP(userInput),
                        #Samp.FrequentlyAskedQuestionsECRPG(userInput),
                        GreetMember.Greetings(userInput),
                        ]
            #   Filter out None
            response = list(filter(None, response))
            
            print(f'UserInput Test : {userInput}')
            print(f' Three Response : \n {(response)}\n')


                await msg.send(j)
            '''
        return
