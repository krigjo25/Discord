
#   Discord Repositories
import discord as d
from discord.embeds import Embed
from discord.ext.commands import Cog

class FrequentlyAskedQuestions(Cog):

    """
        By              : Krigjo25
        Creation date   : 23.01-23
        Last Update     : 26.02-23

        Discord command menu
        Gamers module,
        Community module.

    """

    help = d.SlashCommandGroup(name = 'help', description = 'Frequently asked questions')

    def __init__(self,bot):

        self.bot = bot
        self.embed = Embed(color=d.Colour.dark_purple())

    @help.command()
    async def frequentlyaskedquestion(self, ctx:d.ApplicationContext, arg = None):

        """
            Available bot commands

            >   Creation Date   : 23.02-23
            >   Last update     : 27.02-23
        """

        if arg == None:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.add_field(name=':people_holding_hands: Community Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)
            self.embed.add_field(name=':signal_strength: Gamers Module',value='An Irishman arrived at J.F.K. Airport and wandered around the terminal with tears streaming down his cheeks...', inline=True)
            await ctx.respond(embed=self.embed)
        else :
            arg = str(arg).lower().replace(" ", "")
            match arg:

                case "gamersmodule" : self.embed = self.GamersModule()
                case "wordgames" : self.embed = self.GamersModule(arg)
                case "mathgames" : self.embed = self.GamersModule(arg)
                case "adventure" : self.embed = self.GamersModule(arg)
                case "communitymodule" : self.embed = self.CommunityModule()
            await ctx.respond(embed= self.embed)

        del arg#   Clear some memory
        return

    @help.after_invoke
    async def clear_memory(self, ctx: d.ApplicationContext):

        """
            Clearing data chace

            >   Creation Date   : 23.02-23
            >   Last update     :
        """

        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.description = ""
        self.embed.remove_thumbnail()
        self.embed.color = d.Colour.dark_purple()

        del ctx #   Clearing some memory
        return

    def CommunityModule(self):

        self.embed.title=':people_holding_hands: Community Module'
        self.embed.description = 'Available commands'
        self.embed.add_field(name='/community botinfo \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
        self.embed.add_field(name='/community list', value ='list of members', inline=True)
        self.embed.add_field(name='?meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)

        return self.embed

    def GamersModule(self, arg = None):

        self.embed.title = 'Gamers Module'
        self.embed.description = 'Games created with Python'
        if arg == None:
            self.embed.add_field(name ='Math Games', value =' Such as guess the number, little proffessor')
            self.embed.add_field(name ='Word Games', value =' Such as Eightball, Jumble, Scrabble, Rock, Scissors and paper')
            self.embed.add_field(name ='Reaction Games', value =' Such as Eightball, Jumble, Scrabble, Rock, Scissors and paper')
        
        elif arg == "mathgames":

            self.embed.add_field(name='/math guessthenumber', value=' - Guess the number', inline=True)
            self.embed.add_field(name='/math littleprofessor', value='- Little Proffessor', inline=True)
        
        elif arg == "wordgames":

            self.embed.add_field(name='/word eightball', value='- Ask a Philisopher a question', inline=True)
            self.embed.add_field(name=':question: /word jumble', value=' - unscrabble a jumble', inline=True)
            self.embed.add_field(name=':question: /word scrabble', value=' - unscrabble a jumble', inline=True)

        elif arg == "reactiongames":
            self.embed.add_field(name='/reaction rockscissorpaper', value='- :rock:, :scissors:, :page_facing_up:', inline=True)

        else: self.embed.description = "Did not find the game you looking for"

        del arg#    Clear some argument

        return self.embed
