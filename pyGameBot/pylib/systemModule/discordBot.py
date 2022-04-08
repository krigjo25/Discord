
#   Python Reporosity
from os import getenv
from sys import api_version

#   dotenv Reporosory
from dotenv import load_dotenv

#   Discord Reporosory
from discord.message import Message
from discord.ext.commands import Bot

#   pylib Reporosory
from pylib.systemModule.databasePython import MariaDB

load_dotenv()

class DiscordBot(Bot):
    def __init__(self, command_prefix='*', help_command=None, description=None, **options):
        super().__init__(command_prefix, help_command=help_command, description=description, **options)


    async def on_ready(self):
        srv= []
        svr = self.guilds

        for i in svr:
            srv.append(i)

        print(f'Discord.py v{api_version} has been loaded.\n{self.user.name} has establized a connection following servers :\n\n{srv[0]}')

        return

        
    async def on_message(self, message:Message):


    #   Process commands
        await self.process_commands(message)
        return
