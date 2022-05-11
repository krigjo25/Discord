
#   Discord Repositories
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import command, Cog

class FrequentlyAskedQuestions(Cog):

    cmdPre = 'faq.cmdPre'

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
        faq =FrequentlyAskedQuestions

        if args == None:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.title = f' Usage ** {faq.cmdPre}help (Category)** for more details\n\n'
            self.embed.add_field(name= f':people_holding_hands: Community Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)
            self.embed.add_field(name= f':signal_strength: RSS Module',value='An Irishman arrived at J.F.K. Airport and wandered around the terminal with tears streaming down his cheeks...', inline=True)

        else:

            args = str(args).lower().replace(" ", "")

            if args == 'communitymodule':self.embed = self.CommunityModule()

            elif args == 'rssmodule' or args == 'worldnews' or args == 'finance&economy':self.embed = rss.RSSModule(args)

            #   National News
            elif args == 'national': self.embed = nl.CountryNews()
            elif args == 'usa' or args == 'india' or args == 'france': self.embed = nl.NationalNews(args)
            elif args == 'unitedkingdom':self.embed = nl.NationalNews()

            # International news
            elif args == 'bbc' or args == 'bbcworld':self.embed = inl.BBCNews
            elif args == 'cnn' or args == 'cnnworld' or args == 'cnnmisc':self.embed = inl.CnnNews(args)
            elif args == 'cnbc' or args == 'cnbcworld' or args == 'cnbcmisc':self.embed = inl.CNBCNews(args)
            elif args == 'euronews' or args == 'euronewsworld' or args == 'euronewsmisc':self.embed = inl.EuroNews(args)
            elif args == 'fr24' or args == 'frworld': self.embed = inl.France24News(args) 
            elif args == 'international':self.embed = inl.InternationalNews()
            elif args == 'rt' or args == 'rtworld':self.embed = inl.RTNews()
            elif args == 'skynews' or args == 'skyworld':self.embed = inl.SkyNews()
            elif args == 'wionworld' or args == 'wionsports' or args == 'wionbusiness': self.embed = inl.WionNews(args)

            else:

                self.embed.title = 'Module Not found'
                self.embed.description = ' Meep, Morp, zeet'

        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        return

    def CommunityModule(self):

        faq = FrequentlyAskedQuestions

        self.embed.title=':people_holding_hands: Community Module'
        self.embed.add_field(name=f'{faq.cmdPre}botinfo \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
        self.embed.add_field(name=f'x{faq.cmdPre}memberlist', value ='list of members', inline=True)
        self.embed.add_field(name=f'{faq.cmdPre}meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)
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
            self.embed.add_field(name='World News', value = 'News for selected Channel')
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
        self.embed.add_field(name ='BBC News', value ='BBC World News')
        self.embed.add_field(name ='CNN News', value ='Cnn World News')
        self.embed.add_field(name ='CNBC News', value ='CNBC World News')
        self.embed.add_field(name ='Euronews News', value ='EuroNews World News')
        self.embed.add_field(name ='France24 News', value ='France24 World News')
        self.embed.add_field(name ='RT News', value ='RT World News')
        self.embed.add_field(name ='SkyNews News', value ='SkyNews World News')
        self.embed.add_field(name ='Wion News', value ='Wion World News')

        return self.embed

    def CnnNews(self, args):

        faq = FrequentlyAskedQuestions

        if args == 'cnnworld':

            self.embed.title = 'CNN World News'
            self.embed.add_field(name = f'{faq.cmdPre}cafrica', value = 'CNN News from Afria ')
            self.embed.add_field(name = f'{faq.cmdPre}camerica', value = 'CNN News from America')
            self.embed.add_field(name = f'{faq.cmdPre}casia', value = 'CNN News from Asia')
            self.embed.add_field(name = f'{faq.cmdPre}ceurope', value = 'CNN News from Europe')
            self.embed.add_field(name = f'{faq.cmdPre}cworld', value = 'Cnn News from the World')
            self.embed.add_field(name = f'{faq.cmdPre}cmeast', value = 'Cnn News from Middle East')

        elif args == 'cnnmisc':

            self.embed.title = 'CNN Misc News'
            self.embed.add_field(name = f'{faq.cmdPre}ctop', value = 'CNN Top News')
            self.embed.add_field(name = f'{faq.cmdPre}cetn', value = 'CNN Entertainment News')
            self.embed.add_field(name = f'{faq.cmdPre}css', value = 'CNN Space & Science News')
            self.embed.add_field(name = f'{faq.cmdPre}ccash', value = 'CNN Money News')
            self.embed.add_field(name = f'{faq.cmdPre}cvideo', value = 'Top CNN Videos')
            self.embed.add_field(name = f'{faq.cmdPre}cmr', value = 'CNN Motor Sport News')
            self.embed.add_field(name = f'{faq.cmdPre}ctravel', value = 'CNN Travel News')
            self.embed.add_field(name = f'{faq.cmdPre}ctech', value = 'CNN Technologies News')

        else:

            self.embed.title = 'CNN Offical News Channel'
            self.embed.description = ' '
            self.embed.add_field(name ='CNNWorld', value ='Cnn World News')
            self.embed.add_field(name ='CNNMisc', value ='Cnn Miscellaneous News')

        return self.embed

    def CNBCNews(self, args):

        faq = FrequentlyAskedQuestions

        if args == 'cnbcworld':

            self.embed.title = 'CNBC World News'
            self.embed.add_field(name = f'{faq.cmdPre}cnbcasia', value = ' CNBC News from Asia')
            self.embed.add_field(name = f'{faq.cmdPre}cnbceurope', value = 'CNBC News from Europe')
            self.embed.add_field(name = f'{faq.cmdPre}cnbcworld', value = 'CNBC News from the World')

        elif args == 'cnbcmisc':

            self.embed.title = 'CNBC Misc News'
            self.embed.add_field(name = f'{faq.cmdPre}cnbcbus', value = 'CNBC Business')
            self.embed.add_field(name = f'{faq.cmdPre}cnbcsbus', value = 'CNBC Small Business')
            self.embed.add_field(name = f'{faq.cmdPre}cnbcstate', value = 'CNBC Real Estate')
            self.embed.add_field(name = f'{faq.cmdPre}cnbctech', value = 'CNBC Technologies')
            self.embed.add_field(name = f'{faq.cmdPre}cnbctravel', value = 'CNBC Travel')
            self.embed.add_field(name = f'{faq.cmdPre}cnbccare', value = 'CNBC Health Care')
            self.embed.add_field(name = f'{faq.cmdPre}cnbcenergy', value = 'CNBC Energy')
            self.embed.add_field(name = f'{faq.cmdPre}cnbcmedia', value = 'CNBC Social Media')
            self.embed.add_field(name = f'{faq.cmdPre}cnbsports', value = 'CNBC Sports')
            self.embed.add_field(name = f'{faq.cmdPre}cnbcom', value = 'CNBC Commentary')

        else:

            self.embed.title = 'CNBC Offical News Channel'
            self.embed.description = ' '
            self.embed.add_field(name ='CNBC World', value ='Cnn World News')
            self.embed.add_field(name ='CNBC Misc', value ='Cnn Miscellaneous News')

        return self.embed
            
    def EuroNews(self, args):

        faq = FrequentlyAskedQuestions

        if args == 'euronewsworld':

            self.embed.title = 'Euronews World News'
            self.embed.add_field(name = f'{faq.cmdPre}eworld', value = 'Euronews World ')
            self.embed.add_field(name = f'{faq.cmdPre}europe', value = 'Euronews Europe')
            
        elif args == 'euronewsmisc':

            self.embed.title = 'CNBC Misc News'

            self.embed.add_field(name = f'{faq.cmdPre}eports', value = 'Euronews sports')
            self.embed.add_field(name = f'{faq.cmdPre}etravel', value = 'Euronews Travel')
            self.embed.add_field(name = f'{faq.cmdPre}egreen', value = 'Euronews Green')
            self.embed.add_field(name = f'{faq.cmdPre}ecult', value = 'Euronews Culture')
            self.embed.add_field(name = f'{faq.cmdPre}enext', value = 'Euronews Next')

        else:

            self.embed.title = 'Euronews Offical News Channel'
            self.embed.description = ' '
            self.embed.add_field(name ='Euronews World', value ='Euronews World News')
            self.embed.add_field(name ='Euronews Misc', value ='euronews Miscellaneous News')

        return self.embed

    def WionNews(self, args):

        faq = FrequentlyAskedQuestions

        if args == 'wionworld':

            self.embed.title = 'Wion World News'
            self.embed.add_field(name = f'{faq.cmdPre}wworld', value = 'Wion World ')
            self.embed.add_field(name = f'{faq.cmdPre}wsa', value = 'Wion South Asia')
            
        elif args == 'wionsports':

            self.embed.title = 'Wion Sports News'

            self.embed.add_field(name = f'{faq.cmdPre}wsports', value = 'Wion Sports')
            self.embed.add_field(name = f'{faq.cmdPre}wcricket', value = 'Wion Cricket')
            self.embed.add_field(name = f'{faq.cmdPre}wfootball', value = 'Wion Football')

        elif args == 'wionbusiness':

            self.embed.title = 'Wion Business'

            self.embed.add_field(name = f'{faq.cmdPre}wbe', value = 'Wion Business & Economy')
            self.embed.add_field(name = f'{faq.cmdPre}wtech', value = 'Wion Technology')


        else:

            self.embed.title = 'Wion Offical News Channel'
            self.embed.description = ' '
            self.embed.add_field(name = 'Wion World', value = 'Wion World News')
            self.embed.add_field(name = 'Wion Sports', value = 'Wion Sports News')
            self.embed.add_field(name = 'Wion Business', value = 'Wion Business and economy News')

        return self.embed

    def France24News(self, args):

        faq = FrequentlyAskedQuestions

        if args == '24world':

            self.embed.title = 'France24 24 World News'
            self.embed.add_field(name = f'{faq.cmdPre}24africa', value = 'France24 Africa News ')
            self.embed.add_field(name = f'{faq.cmdPre}24america', value = 'France24 Americans News ')
            self.embed.add_field(name = f'{faq.cmdPre}24asia', value = 'France24 Asia News')
            self.embed.add_field(name = f'{faq.cmdPre}24europe', value = 'France24 Europe News ')
            self.embed.add_field(name = f'{faq.cmdPre}24me', value = 'France24 Middle East News ')
            self.embed.add_field(name = f'{faq.cmdPre}24world', value = 'France24 World News')

        else:

            self.embed.title = 'France24 Offical News Channel'
            self.embed.description = ''
            self.embed.add_field(name = f'{faq.cmdPre}24world', value = 'France24 World News')
            self.embed.add_field(name = f'{faq.cmdPre}24sport', value = 'France24 Sports News')
            self.embed.add_field(name = f'{faq.cmdPre}24bus', value = 'France24 Business and economy News')

        return self.embed

    def BBCNews(self, args):

        faq = FrequentlyAskedQuestions

        if args == 'bbcworld':

            self.embed.title = 'BBC 24 World News'
            self.embed.add_field(name = f'{faq.cmdPre}bbcafrica', value = 'BBC Africa News ')
            self.embed.add_field(name = f'{faq.cmdPre}bbcamerica', value = 'BBC Americans News ')
            self.embed.add_field(name = f'{faq.cmdPre}bbcasia', value = 'BBC Asia News')
            self.embed.add_field(name = f'{faq.cmdPre}bbceurope', value = 'BBC Europe News ')
            self.embed.add_field(name = f'{faq.cmdPre}bbcme', value = 'BBC Middle East News ')
            self.embed.add_field(name = f'{faq.cmdPre}bbcworld', value = 'BBC World News')
            
        elif args == 'bbcsports':

            self.embed.title = 'BBC Sports News'

            self.embed.add_field(name =f'{faq.cmdPre}wsports', value ='Wion Sports')
            self.embed.add_field(name =f'{faq.cmdPre}wcricket', value ='Wion Cricket')
            self.embed.add_field(name =f'{faq.cmdPre}wfootball', value ='Wion Football')

        elif args == 'bbcbusiness':

            self.embed.title = 'BBC Business'

            self.embed.add_field(name =f'{faq.cmdPre}wbe', value ='Wion Business & Economy')
            self.embed.add_field(name =f'{faq.cmdPre}wtech', value ='Wion Technology')


        else:

            self.embed.title = 'BBC Offical News Channel'
            self.embed.description = ''
            self.embed.add_field(name ='BBC World', value ='BBC World News')
            self.embed.add_field(name ='BBC Sports', value ='BBC Sports News')

        return self.embed

    def SkyNews(self, args):

        faq = FrequentlyAskedQuestions

        if args == 'skyworld':

            self.embed.title = 'SkyNews Offical News Channel'
            self.embed.add_field(name =f'{faq.cmdPre}skyworld', value = 'SkyNews World ')
            self.embed.add_field(name =f'{faq.cmdPre}skyrecent', value = 'SkyNews Recent ')
            self.embed.add_field(name =f'{faq.cmdPre}skytech', value = 'SkyNews Technologies')
            self.embed.add_field(name =f'{faq.cmdPre}skyent', value = 'SkyNews Entertainment')
            self.embed.add_field(name =f'{faq.cmdPre}skystrange', value = 'SkyNews Strange ')
            self.embed.add_field(name =f'{faq.cmdPre}skypol', value = 'SkyNews Politics')

        else:

            self.embed.title = 'SkyNews '
            self.embed.description = 'SkyNews Offical News Channel'
            self.embed.add_field(name ='SkyNews World', value ='SkyNews World News')

        return self.embed

    def RTNews(self, args):

        faq = FrequentlyAskedQuestions

        if args == 'rtworld':

            self.embed.title = 'RT Offical News Channel'
            self.embed.add_field(name =f'{faq.cmdPre}skyworld', value ='France24 Africa News ')
            self.embed.add_field(name =f'{faq.cmdPre}skyrecent', value ='France24 Americans News ')
            self.embed.add_field(name =f'{faq.cmdPre}skytech', value ='France24 Asia News')
            self.embed.add_field(name =f'{faq.cmdPre}skyent', value ='France24 Europe News ')
            self.embed.add_field(name =f'{faq.cmdPre}skystrange', value ='France24 Middle East News ')
            self.embed.add_field(name =f'{faq.cmdPre}skypol', value ='France24 World News')

        else:

            self.embed.title = 'RT News'
            self.embed.description = 'RT Offical News Channel'
            self.embed.add_field(name ='RT World', value ='RT World News')

        return self.embed

class NationalModule(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    def CountryNews(self):

        self.embed.title = 'National News'
        self.embed.description = ''
        self.embed.add_field(name ='France', value ='French National News')
        self.embed.add_field(name ='India', value ='Indian National News')
        self.embed.add_field(name ='United Kingdom', value ='United Kingodm National News')
        self.embed.add_field(name ='USA', value ='USA National News')

        return self.embed

    def NationalNews(self, args):

        faq = FrequentlyAskedQuestions

        if args == 'usa':

            self.embed.title = 'National News USA'
            self.embed.description = ' United States National News '
            self.embed.add_field(name =f'{faq.cmdPre}cusa', value ='CNN National')
#            self.embed.add_field(name = f'{faq.cmdPre}cnbcusa', value = 'CNBC National News')
            self.embed.add_field(name = f'{faq.cmdPre}skycusa', value = 'SkyNews National')

        elif args == 'india':

            self.embed.title = 'National News India'
            self.embed.description = ' '
            self.embed.add_field(name =f'{faq.cmdPre}windia', value ='National News India')

        elif args == 'france':

            self.embed.title = 'National News France'
            self.embed.description = ' '
            self.embed.add_field(name =f'{faq.cmdPre}24fr', value = 'National News France')

        elif args == 'unitedkingdom':

            self.embed.title = 'National News United Kingdom'
            self.embed.description = ' '
            self.embed.add_field(name =f'{faq.cmdPre}skyuk', value ='SkyNews National')
            self.embed.add_field(name =f'{faq.cmdPre}bbcuk', value ='BBC National')
            self.embed.add_field(name =f'{faq.cmdPre}bbceng', value ='BBC National - England')
            self.embed.add_field(name =f'{faq.cmdPre}bbcirish', value ='BBC National - Northen Ireland')
#            self.embed.add_field(name =f'{faq.cmdPre}bbcwales', value ='BBC National - Wales News') x
#            self.embed.add_field(name =f'{faq.cmdPre}bbscot', value ='BBC National - Scotland News') x
            self.embed.add_field(name =f'{faq.cmdPre}rtru', value ='RT National News')
            

        else:

            self.embed.title = '404 Country Not Found'
            self.embed.description = f'There is no news shown for {args}'

        return self.embed
