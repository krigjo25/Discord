
#   Discord Repositories
from discord.utils import get
from discord.embeds import Embed
from discord import Color, Member
from discord.ext.commands import command, Cog
from discord.ext.commands.core import has_any_role

class HelpCommand(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

#   Frequently Asked Question

    @command(name='help', pass_context=True)
    async def FrequentlyAskedQuestions(self,ctx, args=None):

        if args == None:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.title = ' Usage ** ?help (Category)** for more details\n\n'
            self.embed.add_field(name=':people_holding_hands: Community', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)
            self.embed.add_field(name=':tv: RSS',value='An Irishman arrived at J.F.K. Airport and wandered around the terminal with tears streaming down his cheeks...', inline=True)

            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

        else:
            args = str(args)
            args.lower()

        #   Bot-Modules

        #   Community-Module
            if args == 'community':

                self.embed.title=':people_holding_hands: Community Module'
                self.embed.description='Use ** ?help (Command)**, for more details, sir.\n\n'
                self.embed.add_field(name='?botinfo \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
                self.embed.add_field(name='?memberlist', value ='list of members', inline=True)
                self.embed.add_field(name='?dnd (message) ', value='- Busy, or going afk, notify your friends that you have a life', inline=True)
                self.embed.add_field(name='?back ', value='- Shows that you\'re a no lifer again', inline=True)
                self.embed.add_field(name='?meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)
                self.embed.add_field(name='/', value='- for built-ins ', inline=True)
                self.embed.add_field(name=':x:?pre-mod', value='How does the pre-mod work')

        #   RRS - Feeds
            elif args == 'rss':

                self.embed.title = 'RSS Module'
                self.embed.add_field(name='CNNnews', value = 'Cnn RSS feeds')
                #self.embed.add_field(name='BBCNews', value = 'BBC RSS feeds')
                self.embed.add_field(name='GameNews', value = 'Game RSS feeds')
                #self.embed.add_field(name='PandemicNews', value = 'Pandemic RSS feeds')
                self.embed.add_field(name='Miscerillious commands', value = '*rss (rss url)')
                #self.embed.add_field(name='NationalNews', value = 'National News for selected country')

            elif args == 'cNNnews':

                self.embed.title = 'CNN News'
                self.embed.add_field(name ='CNNWorld', value ='Cnn World News')
                self.embed.add_field(name ='CNNMisc', value ='Cnn Misc News')

            elif args == 'cnnworld':

                self.embed.title = 'CNN World News'
                self.embed.add_field(name ='?cafrica', value ='To get the news from the region')
                self.embed.add_field(name ='?camerica', value ='To get the news from the region')
                self.embed.add_field(name ='?casia', value ='To get the news from the region')
                self.embed.add_field(name ='?ceurope', value ='To get the news from the region')
                self.embed.add_field(name ='?cWorld', value ='Cnn World News')

            elif args == 'cnnmisc':

                self.embed.title = 'CNN Misc News'
                self.embed.add_field(name ='?ctop', value ='Top 10 Cnn News')
                self.embed.add_field(name ='?cetn', value ='Top 10 Cnn Entertainment News')
                self.embed.add_field(name ='?css', value ='Top 10 Cnn Space & Science News')
                self.embed.add_field(name ='?ccash', value ='Top 10 Cnn Money News')
                #self.embed.add_field(name ='?cvideo', value ='Top 10 Cnn Videos')
                #self.embed.add_field(name ='?cmr', value ='Top 10 Cnn Motor Sport News')
                self.embed.add_field(name ='?ctravel', value ='Top 10 Cnn Travel News')
                self.embed.add_field(name ='?ctech', value ='Top 10 Cnn Technologies News')

            elif args == 'nationalNews':
                self.embed.title = 'National News'
                self.embed.add_field(name ='?cusa', value ='Top 10 Cnn News of USA')

            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
            return