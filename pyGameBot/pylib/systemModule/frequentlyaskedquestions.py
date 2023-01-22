
#   Discord Repositories
from discord.utils import get
from discord.embeds import Embed
from discord import Color, Member
from discord.ext.commands import command, Cog
from discord.ext.commands.core import has_any_role

class FrequentlyAskedQuestions(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

#   Frequently Asked Question

    @command(name='help', pass_context=True)
    async def FrequentlyAskedQuestions(self, ctx, *, args=None):

        #   Initialize classes
        game = PyGames(bot=self.bot)



        if args == None:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.description = ' Usage ** ?help (Category)** for more details\n\n'
            self.embed.add_field(name=':people_holding_hands: Community Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)
            self.embed.add_field(name=':signal_strength: Gamers Module',value='An Irishman arrived at J.F.K. Airport and wandered around the terminal with tears streaming down his cheeks...', inline=True)

        else:

            args = str(args).lower().replace(" ", "")

            if args == 'communitymodule':self.embed = self.CommunityModule()

            elif args == 'gamersmodule': self.embed = game.GamersModule(args)
            
            elif args == 'minigamesmodule' :self.embed = game.miniGamesModule(args)

        await ctx.send(embed=self.embed)

        #   Clear and save space
        del game
        del args

        self.embed.clear_fields()

        return

    def CommunityModule(self):

        self.embed.title=':people_holding_hands: Community Module'
        self.embed.add_field(name='?botinfo \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
        self.embed.add_field(name='?memberlist', value ='list of members', inline=True)
        self.embed.add_field(name='?meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)
        self.embed.add_field(name='/', value='- for built-ins ', inline=True)

        return self.embed

class PyGames(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    def GamersModule(self):

        self.embed.title = 'Gamers Module'
        self.embed.description = 'Games created with Python'
        self.embed.add_field(name ='miniGames', value ='USA National News')

        return self.embed

    def miniGamesModule(self, args):

        if args == 'mathgames':

            self.embed.add_field(name='?int', value=' - Guess the number', inline=True)
            self.embed.add_field(name='?lip', value='- Little Proffessor', inline=True)


        elif args == 'wordgames':

            self.embed.add_field(name='?ask', value='- Ask a Philisopher a question', inline=True)
            self.embed.add_field(name=':question: ?jumble', value=' - unscrabble a jumble', inline=True)
            self.embed.add_field(name=':question: ?scrabble', value=' - unscrabble a jumble', inline=True)
            self.embed.add_field(name='?rsp', value='- :rock:, :scissors:, :page_facing_up:', inline=True)

        #   Save space
        del args
        return self.embed
