
#   Python Repositories
from os import getenv
from sys import api_version
from types import NoneType

#   dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord.message import Message
from discord.ext.commands import Bot

#   pylib Repositories
from pylib.dictionary.pyChatSamp import Samp
from pylib.dictionary.pyChatgreets import GreetMember
from pylib.dictionary.pyChatFunctions import StringManagement

load_dotenv()

class DiscordBot(Bot):
    def __init__(self, command_prefix='?', help_command=None, description=None, owner_id = 340540581174575107, **options):
        super().__init__(command_prefix = command_prefix, help_command=help_command, description=description, owner_id = owner_id, **options)


        return

    async def on_ready(self):

        srv= []
        svr = self.guilds

        for i in svr:
            srv.append(i)

        print(f'''Discord.py v{api_version} has been loaded.\n
{self.user.name} has establized a connection following servers :\n
{srv[0]}''')


        return

        
    async def on_message(self, message:Message):

        if message.author == self.user: return

        else:

            #   Procsess commands
            await self.process_commands(message)

            #   Initializing variables
            msg = message.channel
            userInput = str(message.content).capitalize()

            #   Initializing classes
            userInput = StringManagement.ReplaceCharacters(userInput)

            response =  [Samp.QuestionsRelatedToSamp(userInput),
                        [GreetMember.Greetings(userInput)],
                        ]
           


            print(f' two Response : \n {(response)}\n')

            if not None: 

                #print(f'Question : {response[0][0]}')
                #print(f' Answer : {response[0][1]}')

                #   Works for greetings
                #   Not for samp()
                for i, j in response[1]:

                    print(f'Question : {i}')
                    print(f' Answer : {j}')
                


            if userInput in i: await msg.send(j)

        return
