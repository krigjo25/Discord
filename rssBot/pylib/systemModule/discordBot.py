import mariadb
#   Python Reporosity
from os import getenv
from sys import api_version

#   dotenv Reporosory
from dotenv import load_dotenv

#   Discord Reporosory
from discord.message import Message
from discord.ext.commands import Bot

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

        print(f'Discord.py v{api_version} is loaded.\n {self.user.name} has establized a connection with {srv[0]} and {srv[1]}')

    async def on_message(self, message:Message):

        mention = bool(message.mentions)
        #   If a member is mentioned send this message
        if mention == True:

        #   Declearing a list
            dndList = []
            mention = message.mentions[0]
                
        #   Creating a connection to the database
            conn = mariadb.connect(
                                    host=getenv('HOST'),
                                    user=getenv('USER'),
                                    port=int(getenv('PORT')),
                                    database=getenv('DATABASE'),
                                    password=getenv('PASSWORD'),
                )

            cur = conn.cursor()

        #   Creating a statement, execute and add the results to the list
            query = f'SELECT * FROM discordAfkMessages WHERE memberName = "{mention}"'
            cur.execute(query)
            data = cur.fetchall()
            conn.close()
            for i in data:
                dndList.append(i[1])
                dndList.append(i[2])
            print(bool(dndList)) 
            if bool(dndList) == True:

            #   Send the message into the given channel
                await message.channel.send(f' ***{dndList[0]}*** is in **Do Not Disturb** Mode. *{dndList[1]}***')

       # await mention.channel.send('lol')

        #await self.handler.propagate(message)
        #await self.tracker.do_punishment(message)

    #   Procsess commands
        await self.process_commands(message)
