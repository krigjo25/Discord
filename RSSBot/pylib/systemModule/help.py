
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

            elif args == 'rssmodule' or args == 'worldnews' or args == 'finance&economy':self.embed = rss.RSSModule(args)

            #   National News
            elif args == 'national': self.embed = nl.CountryNews()
            elif args == 'usa' or args == 'india': self.embed = nl.NationalNews(args)


            # International news
            elif args == 'international':self.embed = inl.InternationalNews()
            elif args == 'cnn' or args == 'cnnworld' or args == 'cnnmisc':self.embed = inl.CnnNews(args)
            elif args == 'cnbc' or args == 'cnbcworld' or args == 'cnbcmisc':self.embed = inl.CNBCNews(args)
            elif args == 'euronews' or args == 'euronewsworld' or args == 'euronewsmisc':self.embed = inl.EuroNews(args)
            elif args == 'wionworld' or args == 'wionsports' or args == 'wionbusiness': self.embed = inl.WionNews(args)

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
        self.embed.add_field(name='?meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)
        self.embed.add_field(name='/', value='- for built-ins ', inline=True)

        return self.embed

class RSSModule(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    def RSSModule(self, args):

        if args == 'worldnews':

            self.embed.add_field(name='National', value = 'National News for selected country')
            self.embed.add_field(name='International', value = 'International News feeds')

        else:

            self.embed.title = 'RSS Module'
            self.embed.add_field(name='World News', value = 'National News for selected country')
            self.embed.add_field(name='Finance & Economy', value = 'News about Enocomy and Finance')

        return self.embed

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
        self.embed.add_field(name ='Euronews News', value ='EuroNews World News')
        self.embed.add_field(name ='Wion News', value ='Wion World News')

        return self.embed

    def CnnNews(self, args):

        if args == 'cnnworld':

            self.embed.title = 'CNN World News'
            self.embed.add_field(name ='?cafrica', value ='CNN News from Afria ')
            self.embed.add_field(name ='?camerica', value ='CNN News from America')
            self.embed.add_field(name ='?casia', value ='CNN News from Asia')
            self.embed.add_field(name ='?ceurope', value ='CNN News from Europe')
            self.embed.add_field(name ='?cworld', value ='Cnn News from the World')
            self.embed.add_field(name ='?cmeast', value ='Cnn News from Middle East')

        elif args == 'cnnmisc':

            self.embed.title = 'CNN Misc News'
            self.embed.add_field(name ='?ctop', value ='CNN Top News')
            self.embed.add_field(name ='?cetn', value ='CNN Entertainment News')
            self.embed.add_field(name ='?css', value ='CNN Space & Science News')
            self.embed.add_field(name ='?ccash', value ='CNN Money News')
            self.embed.add_field(name ='?cvideo', value ='Top CNN Videos')
            self.embed.add_field(name ='?cmr', value ='CNN Motor Sport News')
            self.embed.add_field(name ='?ctravel', value ='CNN Travel News')
            self.embed.add_field(name ='?ctech', value ='CNN Technologies News')

        else:

            self.embed.title = 'CNN News'
            self.embed.description = 'Cnn Offical News Chanel'
            self.embed.add_field(name ='CNNWorld', value ='Cnn World News')
            self.embed.add_field(name ='CNNMisc', value ='Cnn Miscellaneous News')

        return self.embed

    def CNBCNews(self, args):

        if args == 'cnbcworld':

            self.embed.title = 'CNBC World News'
            self.embed.add_field(name ='?cnbcasia', value =' CNBC News from Asia')
            self.embed.add_field(name ='?cnbceurope', value ='CNBC News from Europe')
            self.embed.add_field(name ='?cnbcworld', value ='CNBC News from the World')

        elif args == 'cnbcmisc':

            self.embed.title = 'CNBC Misc News'
            self.embed.add_field(name ='?cnbcbus', value ='CNBC Business')
            self.embed.add_field(name ='?cnbcsbus', value ='CNBC Small Business')
            self.embed.add_field(name ='?cnbcstate', value ='CNBC Real Estate')
            self.embed.add_field(name ='?cnbctech', value ='CNBC Technologies')
            self.embed.add_field(name ='?cnbctravel', value ='CNBC Travel')
            self.embed.add_field(name ='?cnbccare', value ='CNBC Health Care')
            self.embed.add_field(name ='?cnbcenergy', value ='CNBC Energy')
            self.embed.add_field(name ='?cnbcmedia', value ='CNBC Social Media')
            self.embed.add_field(name ='?cnbsports', value ='CNBC Sports')
            self.embed.add_field(name ='?cnbcom', value ='CNBC Commentary')

        else:

            self.embed.title = 'CNBC News'
            self.embed.description = 'CBC Offical News Chanel'
            self.embed.add_field(name ='CNBC World', value ='Cnn World News')
            self.embed.add_field(name ='CNBC Misc', value ='Cnn Miscellaneous News')

        return self.embed
            
    def EuroNews(self, args):

        if args == 'euronewsworld':

            self.embed.title = 'Euronews World News'
            self.embed.add_field(name ='?eworld', value ='Euronews World ')
            self.embed.add_field(name ='?europe', value ='Euronews Europe')
            
        elif args == 'euronewsmisc':

            self.embed.title = 'CNBC Misc News'

            self.embed.add_field(name ='?eports', value ='Euronews sports')
            self.embed.add_field(name ='?etravel', value ='Euronews Travel')
            self.embed.add_field(name ='?egreen', value ='Euronews Green')
            self.embed.add_field(name ='?ecult', value ='Euronews Culture')
            self.embed.add_field(name ='?enext', value ='Euronews Next')

        else:

            self.embed.title = 'Euronews News'
            self.embed.description = 'Euronews Offical News Chanel'
            self.embed.add_field(name ='Euronews World', value ='Euronews World News')
            self.embed.add_field(name ='Euronews Misc', value ='euronews Miscellaneous News')

        return self.embed

    def WionNews(self, args):

        if args == 'wionworld':

            self.embed.title = 'Wion World News'
            self.embed.add_field(name ='?world', value ='Wion World ')
            self.embed.add_field(name ='?wsa', value ='Wion South Asia')
            
        elif args == 'wionsports':

            self.embed.title = 'Wion Sports News'

            self.embed.add_field(name ='?wsports', value ='Wion Sports')
            self.embed.add_field(name ='?wcricket', value ='Wion Cricket')
            self.embed.add_field(name ='?wfootball', value ='Wion Football')

        elif args == 'wionbusiness':

            self.embed.title = 'Wion Business'

            self.embed.add_field(name ='?wbe', value ='Wion Business & Economy')
            self.embed.add_field(name ='?wtech', value ='Wion Technology')


        else:

            self.embed.title = 'Wion News'
            self.embed.description = 'Euronews Offical News Chanel'
            self.embed.add_field(name ='Wion World', value ='Wion World News')
            self.embed.add_field(name ='Wion Sports', value ='Wion Sports News')
            self.embed.add_field(name ='Wion Business', value ='Wion Business and economy News')

        return self.embed

class NationalModule(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    def CountryNews(self):

        self.embed.title = 'National News'
        self.embed.description = ''
        self.embed.add_field(name ='USA', value ='USA National News')
        self.embed.add_field(name ='India', value ='Indian National News')

        return self.embed

    def NationalNews(self, args):

        if args == 'usa':

            self.embed.title = 'National News USA'
            self.embed.description = ' United States National News '
            self.embed.add_field(name ='?cusa', value ='CNN National news')
            self.embed.add_field(name = '?cnbcusa', value = 'CNBC National News')

        if args == 'india':

            self.embed.title = 'National News India'
            self.embed.description = ' '
            self.embed.add_field(name ='?windia', value ='Wion National News')

        else:

            self.embed.title = '404 Country Not Found'
            self.embed.description = f'There is no news shown for {args}'

        return self.embed