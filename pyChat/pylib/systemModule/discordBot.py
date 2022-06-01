
#   Python Repositories
import numpy as np
from os import getenv
from sys import api_version


#   dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord.message import Message
from discord.ext.commands import Bot

#   pylib Repositories
from pylib.aibot.pychat import PyChat
from pylib.dictionary.pyChatSamp import Samp
from pylib.dictionary.pyChatgreets import GreetMember
from pylib.dictionary.pyChatFunctions import StringManagement

load_dotenv()

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

        if message.author == self.user: return

        else:

            #   Initializing variables
            msg = message.channel
            text = str(message.content)
            print(text)
            ex = True
            ai = PyChat(name='PyChat')

            # Waking up PyCHat
            if ai.PyChatWakeUp(text) is True: res = 'Greetings, I\'m PyChat, What can i do for you today?'
            elif any(i in text for i in ai.closePyChat(text) ): 

                res = np.random.choice(ai.closePyChat())

            await msg.send(res)

            #   Procsess commands
            await self.process_commands(message)

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

            for i, j in response:
                await msg.send(j)
            '''
        return
