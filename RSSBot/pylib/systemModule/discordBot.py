
<<<<<<< HEAD

#   Python Reporosity
from os import getenv
from sys import api_version

#   dotenv Reporosory
from dotenv import load_dotenv

#   Discord Reporosory
from discord import Intents
from discord.message import Message
from discord.ext.commands import Bot

#   pylib Responsories
#from databasePython import MariaDB
=======
#   Python Repositories
from os import getenv
from sys import api_version

#   dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord.message import Message
from discord.ext.commands import Bot

#   pylib Repositories
from pylib.systemModule.databasePython import MariaDB
>>>>>>> parent of 9538d83 (Merge branch 'main' of https://github.com/krigjo25/Discord)

load_dotenv()

class DiscordBot(Bot):
<<<<<<< HEAD

    def __init__(self, command_prefix='?', help_command=None, description=None, **options):
        super().__init__(command_prefix=command_prefix, help_command=help_command, description=description, **options)

    async def on_ready(self):
        
=======
    def __init__(self, command_prefix='@', help_command=None, owner_id = 340540581174575107, description=None, **options):
        super().__init__(command_prefix, help_command=help_command, owner_id = owner_id, description=description, **options)
        return

    async def on_ready(self):

>>>>>>> parent of 9538d83 (Merge branch 'main' of https://github.com/krigjo25/Discord)
        srv= []
        svr = self.guilds

        for i in svr:
<<<<<<< HEAD
            
            srv.append(i)

        print(f'''Discord.py v{api_version} is loaded.\n{self.user.name} has establized a connection with {srv[0]},\n {srv[1],}''')
        
        return

    async def on_message(self, message:Message):

        #   Initialize Classes
        #db = MariaDB()

        mention = bool(message.mentions)

        if mention == True:

        #   Declearing a list
            dndList = []
            mention = message.mentions[0]

            #   Initializing connection to the database
            database = getenv('database1')
            query = f'SELECT * FROM discordAfkMessages WHERE memberName = "{mention}"'
            data = '#data = db.SelectFromTable(database, query)'

            for i in data:
                dndList.append(i[1])
                dndList.append(i[2])
            print(bool(dndList)) 
            if bool(dndList) == True:

            #   Send the message into the given channel
                await message.channel.send(f' ***{dndList[0]}*** is in **Do Not Disturb** Mode. *{dndList[1]}***')

    #   Procsess commands

        #db.CloseConnection()
        await self.process_commands(message)
=======
            srv.append(i)

        print(f'''Discord.py v{api_version} has been loaded.
{self.user.name} has establized a connection following servers :\n
{srv[0]}''')

        return
        
    async def on_message(self, message:Message):

    #   Procsess commands
        await self.process_commands(message)

        return
>>>>>>> parent of 9538d83 (Merge branch 'main' of https://github.com/krigjo25/Discord)
