
#   Discord Repositories
from discord.ext.commands import Cog


# Anti-Spam Repositories
from antispam import AntiSpamHandler

# Anti-Spam Options
from antispam.dataclasses.options import Options

# Anti-Spam Consequenses
from lib.BotModerationModule.plugins.spamTracker import Tracker

class AntiSpam(Cog):
    def __init__(self, bot):
        self.bot = Cog()
        self.handler = AntiSpamHandler(self.bot, options=Options(ignore_bots=False, no_punish=True))
        self.tracker = MyCustomTracker(self.handler, 3)
        self.handler.register_plugin(self.tracker)
    

    @Cog.listener()
    async def on_message(self, message):
        await self.handler.propagate(message)
        await self.tracker.do_punishment(message)
        await bot.process_commands(message)


