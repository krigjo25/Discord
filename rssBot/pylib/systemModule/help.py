
#   Discord Repositories
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import command, Cog

class HelpCommand(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

#   Frequently Asked Question

    @command(name='help', pass_context=True)
    async def FrequentlyAskedQuestions(self, ctx, *, args=None):

        #   Initialize variables

        #   Initialize classes
        rss = RSSModule(bot=self.bot)
        nl = NationalModule(bot=self.bot)
        inl = InternationalModule(bot=self.bot)

        if args == None:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.title = ' Usage ** ?help (Category)** for more details\n\n'
            self.embed.add_field(name=':people_holding_hands: Community Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)
            self.embed.add_field(name=':signal_strength: RSS Module',value='An Irishman arrived at J.F.K. Airport and wandered around the terminal with tears streaming down his cheeks...', inline=True)

        else:

            args = str(args).lower().replace(" ", "")

            if args == 'communitymodule':self.embed = self.CommunityModule()

            elif args == 'rssmodule':self.embed = self.RSSModule()

                #   National News
            elif args == 'national':self.embed = nl.NationalNews()
            elif args == 'usa': self.embed = nl.UnitedStatesNews()

            # International news
            elif args == 'international':self.embed = inl.InternationalNews()
            elif args == 'cnnnews' or args == 'cnnworld' or args == 'cnnmisc':self.embed = inl.CnnNews(args)
            elif args == 'cnbcnews' or args == 'cnbcworld' or args == 'cnbcmisc':self.embed = inl.CNBCNews(args)

            else:

                self.embed.title = 'Module Not found'
                self.embed.description = ' Meep, Morp, zeet'

        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        return

    def CommunityModule(self):

        self.embed.title=':people_holding_hands: Community Module'
        self.embed.add_field(name='?botinfo \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
        self.embed.add_field(name='?memberlist', value ='list of members', inline=True)
        self.embed.add_field(name='?dnd (message) ', value='- Busy, or going afk, notify your friends that you have a life', inline=True)
        self.embed.add_field(name='?back ', value='- Shows that you\'re a no lifer again', inline=True)
        self.embed.add_field(name='?meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)
        self.embed.add_field(name='/', value='- for built-ins ', inline=True)
        #self.embed.add_field(name=':x:?pre-mod', value='How does the pre-mod work')
        print(self.embed)

        return self.embed

    def RSSModule(self):

        self.embed.title = 'RSS Module'
        self.embed.add_field(name='National', value = 'National News for selected country')
        self.embed.add_field(name='International', value = 'International News feeds')

        return self.embed

class RSSModule(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

class InternationalModule(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    def InternationalNews(self):

        self.embed.title = 'International News'
        self.embed.description = 'News From all the world'
        self.embed.add_field(name ='CNN News', value ='Cnn World News')
        self.embed.add_field(name ='CNBC News', value ='CNBC World News')

        return self.embed

    def CnnNews(self, args):

        if args == 'cnnworld':

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
            self.embed.add_field(name ='?cvideo', value ='Top 10 Cnn Videos')
            self.embed.add_field(name ='?cmr', value ='Top 10 Cnn Motor Sport News')
            self.embed.add_field(name ='?ctravel', value ='Top 10 Cnn Travel News')
            self.embed.add_field(name ='?ctech', value ='Top 10 Cnn Technologies News')

        else:

            self.embed.title = 'CNN News'
            self.embed.description = 'Cnn Offical News Chanel'
            self.embed.add_field(name ='CNNWorld', value ='Cnn World News')
            self.embed.add_field(name ='CNNMisc', value ='Cnn Miscellaneous News')

        return self.embed

    def CNBCNews(self, args):

        if args == 'cnbcworld':

            self.embed.title = 'CNBC World News'
            self.embed.add_field(name ='?cnbcafrica', value ='To get the news from the region')
            self.embed.add_field(name ='?camerica', value ='To get the news from the region')
            self.embed.add_field(name ='?casia', value ='To get the news from the region')
            self.embed.add_field(name ='?ceurope', value ='To get the news from the region')
            self.embed.add_field(name ='?cWorld', value ='Cnn World News')

        elif args == 'cnbcmisc':

            self.embed.title = 'CNBC Misc News'
            self.embed.add_field(name ='?ctop', value ='Top 10 Cnn News')
            self.embed.add_field(name ='?cetn', value ='Top 10 Cnn Entertainment News')
            self.embed.add_field(name ='?css', value ='Top 10 Cnn Space & Science News')
            self.embed.add_field(name ='?ccash', value ='Top 10 Cnn Money News')
            self.embed.add_field(name ='?cvideo', value ='Top 10 Cnn Videos')
            self.embed.add_field(name ='?cmr', value ='Top 10 Cnn Motor Sport News')
            self.embed.add_field(name ='?ctravel', value ='Top 10 Cnn Travel News')
            self.embed.add_field(name ='?ctech', value ='Top 10 Cnn Technologies News')

        else:

            self.embed.title = 'CNBC News'
            self.embed.description = 'CBC Offical News Chanel'
            self.embed.add_field(name ='CNBC World', value ='Cnn World News')
            self.embed.add_field(name ='CNBC Misc', value ='Cnn Miscellaneous News')

        return self.embed
            

class NationalModule(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    def NationalNews(self):

        self.embed.title = 'National News'
        self.embed.description = ' '
        self.embed.add_field(name ='USA', value ='USA National News')

        return self.embed

    def UnitedStatesNews(self):
        self.embed.title = 'National news USA'
        self.embed.description = ' United States National News '
        self.embed.add_field(name ='?cusa', value ='CNN National news')
        self.embed.add_field(name = '?cnbcusa', value = 'CNBC National News')

        return self.embed

