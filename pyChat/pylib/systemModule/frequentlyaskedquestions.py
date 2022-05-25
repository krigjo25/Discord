
#   Discord Repositories
from discord.embeds import Embed
from discord import Color
from discord.ext.commands import command, Cog

class FrequentlyAskedQuestions(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

#   Frequently Asked Question

    @command(name='help', pass_context=True)
    async def FrequentlyAskedQuestions(self,ctx, args=None):

        #   Initializing Classes
        sys = SystemModule
        
        if args == None:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.title = ' Usage ** ?help (Category)** for more details\n\n'
            self.embed.add_field(name=':handshake: Welcome Module', value='This is our new home', inline=True)
            self.embed.add_field(name=':people_holding_hands: Community Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)

        else:

            args = str(args).lower().replace(" ", "")

        #   Bot-Modules

            if args == 'welcomemodule':self.embed = sys.WelcomeModule()
            elif  args == 'communitymodule': self.embed = sys.CommunityModule()

        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        return

class SystemModule(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    def WelcomeModule(self):

        self.embed.title=':handshake: Welcome Module'
        self.embed.description='Use ** ?help (Command)**, for more details, sir.\n\n'
        self.embed.add_field(name='On member connect / absence ', value='- Over 100 Welcome messages and leave messages. In order for \n it to work, set a channel as\n"system message channel ', inline=True)
        

        return self.embed

    def CommunityModule(self):

        self.embed.title=':people_holding_hands: Community-Module'
        self.embed.description='Use ** ?help (Command)**, for more details, sir.\n\n'
        self.embed.add_field(name='?botinfo \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
        self.embed.add_field(name='?memberlist', value ='list of members', inline=True)
        self.embed.add_field(name='?dnd (message) ', value='- Busy, or going afk, notify your friends that you have a life', inline=True)
        self.embed.add_field(name='?back ', value='- Shows that you\'re a no lifer again', inline=True)
        self.embed.add_field(name='?meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)
        self.embed.add_field(name='/', value='- for built-ins ', inline=True)
        self.embed.add_field(name=':x:?pre-mod', value='How does the pre-mod work')

        return self.embed

