
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
    def __init__(self, command_prefix='?', help_command=None, description=None, owner_id = 340540581174575107, **options):
        super().__init__(command_prefix = command_prefix, help_command=help_command, description=description, owner_id = owner_id, **options)


        return

    async def on_ready(self):

        srv= []
        svr = self.guilds

        for i in svr:
            srv.append(i)

        print(f'''Discord.py v{api_version} has been loaded.
{self.user.name} has establized a connection following servers :\n
{srv[0]} & {srv[1]}''')

        return

        
    async def on_message(self, message:Message):

    #   Procsess commands
        await self.process_commands(message)

        return
