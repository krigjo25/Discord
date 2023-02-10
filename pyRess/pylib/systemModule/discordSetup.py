
#   Python Repositories
from os import getenv
from sys import api_version

#   dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord.message import Message
from discord.ext.commands import Bot

load_dotenv()

class DiscordBot(Bot):
    def __init__(self, command_prefix='?', help_command=None, owner_id = 340540581174575107, description=None, **options):
        super().__init__(command_prefix, help_command=help_command, owner_id = owner_id, description=description, **options)
        return

    async def on_ready(self):

        #   Initialize a list of guilds
        svr = [i for i in self.guilds]

        #   Print API name and version
        print(f'Py-cord.py v{api_version} has been loaded')

        for i in svr: print(f'{self.user.name} has establized an connection to {i}')

        return
        
    async def on_message(self, message:Message):

    #   Procsess commands
        await self.process_commands(message)

        return
