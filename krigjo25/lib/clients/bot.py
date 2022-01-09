import mariadb

from os import getenv
from sys import api_version
from dotenv import load_dotenv
from discord.ext.commands import Bot

# Anti-Spam Plugins
#from antispam import AntiSpamHandler

# Anti-Spam Options
#from antispam.dataclasses.options import Options

# Anti-Spam Consequenses
#from lib.BotModerationModule.plugins.spamTracker import SpamTracker


class DiscordBot(Bot):
    def __init__(self, command_prefix='*', help_command=None, description=None, **options):
        super().__init__(command_prefix, help_command=help_command, description=description, **options)
        #self.handler = AntiSpamHandler(self, options=Options(ignore_bots=False, no_punish=True))
        #self.tracker = SpamTracker(self.handler, 3)
        #self.handler.register_plugin(self.tracker)

    async def on_ready(self):
        print(f'Discord.py v{api_version}, loaded.\n {self.user.name} has establized a connection with {self.guilds}')


#    async def on_message(self, message):
#        pass

        #await self.handler.propagate(message)
        #await self.tracker.do_punishment(message)
        #await self.process_commands(message)