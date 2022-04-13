

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

load_dotenv()

class DiscordBot(Bot):

    def __init__(self, command_prefix='?', help_command=None, description=None, **options):
        super().__init__(command_prefix, help_command=help_command, description=description, **options)

    async def on_ready(self):
        
        srv= []
        svr = self.guilds

        for i in svr:
            
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
