#   Python Reporosity
from os import getenv
from sys import api_version

#   dotenv Reporosory
from dotenv import load_dotenv

#   Discord Reporosory
from discord.message import Message
from discord.ext.commands import Bot

#   pylib Reporosory
from pylib.systemModule.databasePython import mariaDB

# Anti-Spam Plugins
#from antispam import AntiSpamHandler

# Anti-Spam Options
#from antispam.dataclasses.options import Options

# Anti-Spam Consequenses
#from lib.BotModerationModule.plugins.spamTracker import SpamTracker

load_dotenv()

class DiscordBot(Bot):
    def __init__(self, command_prefix='?', help_command=None, description=None, **options):
        super().__init__(command_prefix, help_command=help_command, description=description, **options)
        #self.handler = AntiSpamHandler(self, options=Options(ignore_bots=False, no_punish=True))
        #self.tracker = SpamTracker(self.handler, 3)
        #self.handler.register_plugin(self.tracker)

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

        #   Selecting mentioned members from the database
        mention = bool(message.mentions)

        #   If a member is mentioned send this message
        if mention == True:

        #   Declearing a list
            dndList = []
            mention = message.mentions[0]
            
        #   Initializing classes
        db = mariaDB

        #   Initializing the variables for the connection
        table = getenv('table1')
        column = getenv('column1')
        database = getenv('database1')

        query = f'SELECT * FROM {table} WHERE {column} = "{mention}"'

        data = db.selectFromTable(database, query)

        for i in data:
            dndList.append(i[1])
            dndList.append(i[2])

        if bool(dndList) == True:

            #   Send the message into the given channel
                await message.channel.send(f' ***{dndList[0]}*** is away from the keyboard, the note : **{dndList[1]}**')
        
       # await mention.channel.send('lol')
    #   Anti-Spam

        #await self.handler.propagate(message)
        #await self.tracker.do_punishment(message)

    #   Procsess commands
        await self.process_commands(message)

        return
