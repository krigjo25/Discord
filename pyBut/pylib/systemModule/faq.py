
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
        pygame = PyGames()
        sys = SystemModule()
        nl = NationalModule()
        avs = AdminiralVonSnider()
        inl = InternationalModule()
        
        if args == None:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.description = ' Usage ** ?help (Category)** for more details\n\n'
            self.embed.add_field(name=':handshake: Welcome Module', value='This is our new home', inline=True)
            self.embed.add_field(name=':people_wrestling: Game Module', value='- Gamers does not take showers they do steamy once', inline=True)
            self.embed.add_field(name=':people_holding_hands: Community Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)
            self.embed.add_field(name=':signal_strength: RSS-Module',value='An Irishman arrived at J.F.K. Airport and wandered around the terminal with tears streaming down his cheeks...', inline=True)

            #   Moderator Commands
            if ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.manage_roles:
                self.embed.add_field(name='Moderator Module', value = 'A joke here', inline=True)

            #   Administrator Commands
            if ctx.author.guild_permissions.administrator:
                self.embed.add_field(name='Administrator Module', value='A joke here', inline=True)

        else:

            args = str(args).lower().replace(" ", "")

        #   Bot-Modules


            if args == 'game' or args == 'gamemodule': pygame.GameModule()
            elif args == 'minigames' or args == 'minigamesmodule': pygame.miniGamesModule()

            elif args == 'welcome' or args == 'welcomemodule':self.embed = sys.WelcomeModule()
            elif args == 'community' or args == 'communitymodule': self.embed = sys.CommunityModule()

            elif args == 'rssmodule' or args == 'worldnews' or args == 'finance&economy':self.embed = RSSModule.RSSModule(args)

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

        #   Administration
            elif args == 'moderatormodule': avs.ModeratorModule()
            elif args == 'administratormodule': avs.AdministratorModule()

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
        self.embed.add_field(name='Rules Module', value=' Customize a rule set and the person has to agree in order to get a role / be able to view other channels', inline=True)

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

class PyGames(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    def GameModule(self):

        self.embed.title=':people_wrestling: Games Module'
        self.embed.description='Use ** ?help (Category)**, for more details, sir.\n\n'
        self.embed.add_field(name='miniGames Module', value='- :rock:, :scissors:, :page_facing_up:', inline=True)
        #self.embed.add_field(name='discordGames', value='- ServerInfo, stats etc', inline=True)

        return self.embed

    def miniGamesModule(self):

        self.embed.title = 'Minigames Module'
        self.embed.add_field(name='?rsp', value='- :rock:, :scissors:, :page_facing_up:', inline=True)
        self.embed.add_field(name=':question: ?jumble', value=' - unscrabble a jumble', inline=True)
        self.embed.add_field(name=':person_in_lotus_position: ?ask (Question)', value='- How can cops be the worst pool players?\n They always shoot the eight ball first', inline=True)
        self.embed.add_field(name=':seven:, :eight:, :nine: ?int (easiest / easy / normal / hard / kimpossible)', value='- How could the two four skip a meal?\n they already eight ', inline=True)

        return self.embed

class AdminiralVonSnider(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    #   Server Moderation
    def ModeratorModule(self, ctx):

        self.embed.title = 'Moderator Module'
        self.embed.add_field(name='?cls (channel name) (1-100)', value= '- Clears the given channel Chat:bangbang:', inline=True)
        self.embed.add_field(name='?warn (MemberName) (Reason)', value= '- Manually Warn a member for their behavior', inline=True)

        if ctx.author.guild_permissions.kick_members:

            self.embed.add_field(name=':bar_chart: ?poll', value='- Run a poll', inline=True)
            self.embed.add_field(name='?online (on/off)', value= '- Checks whom is online / offline', inline=True)
            self.embed.add_field(name='?kick (member) (reason)', value='- Kicks a user off the server ', inline=True)

        if ctx.author.guild_permissions.manage_roles:

            self.embed.add_field(name='?remove (name)', value='- Demote a person from the role', inline=True)
            self.embed.add_field(name=':x:?setRole (name)', value='- Promotes a regular user to given role', inline=True)
            self.embed.add_field(name=':x:?roleCreate (name))', value='- Creates a role in the server', inline=True)
            self.embed.add_field(name='?delRole (Name)', value='- Deletes a role from the server', inline=True)

        if ctx.author.guild_permissions.manage_channels:
            self.embed.add_field(name='?chdel (Channel Name)', value='- Deletes a channel from the server ', inline=True)
            self.embed.add_field(name='?chcre (Channel Name)', value='- Create a new channel default : hidden ', inline=True)

        if ctx.author.guild_permissions.mute_members:
            self.embed.add_field(name='?sush (MemberName) (sec) (reason)', value= '- Shush a member for a number of sec', inline=True)

        return self.embed

    def AdministratorModule(self):

        self.embed.title = 'Administrator Module'
        self.embed.add_field(name=':bar_chart: ?banlist', value='-View banned members', inline=True)
        self.embed.add_field(name=':bar_chart: ?poll', value='-Run a poll', inline=True)
        self.embed.add_field(name='?unban (member Name)', value= '- unban a member ', inline=True)
        self.embed.add_field(name=':no_pedestrians: ?ban (member) (reason)', value='- Probhits a Discord user to enter your channel', inline=True)
        self.embed.add_field(name='?announce (channelName) (message)', value= '- Talk as the bot in a given channel', inline=True)

        return self.embed

#   Rss module
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

            self.embed.title = 'CNN Offical News Channel'
            self.embed.description = ' '
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

            self.embed.title = 'CNBC Offical News Channel'
            self.embed.description = ' '
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

            self.embed.title = 'Euronews Offical News Channel'
            self.embed.description = ' '
            self.embed.add_field(name ='Euronews World', value ='Euronews World News')
            self.embed.add_field(name ='Euronews Misc', value ='euronews Miscellaneous News')

        return self.embed

    def WionNews(self, args):

        if args == 'wionworld':

            self.embed.title = 'Wion World News'
            self.embed.add_field(name ='?wworld', value ='Wion World ')
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

            self.embed.title = 'Wion Offical News Channel'
            self.embed.description = ' '
            self.embed.add_field(name ='Wion World', value ='Wion World News')
            self.embed.add_field(name ='Wion Sports', value ='Wion Sports News')
            self.embed.add_field(name ='Wion Business', value ='Wion Business and economy News')

        return self.embed

    def France24News(self, args):

        if args == 'frworld':

            self.embed.title = 'France24 24 World News'
            self.embed.add_field(name ='?24africa', value ='France24 Africa News ')
            self.embed.add_field(name ='?24america', value ='France24 Americans News ')
            self.embed.add_field(name ='?24asia', value ='France24 Asia News')
            self.embed.add_field(name ='?24europe', value ='France24 Europe News ')
            self.embed.add_field(name ='?24me', value ='France24 Middle East News ')
            self.embed.add_field(name ='?24world', value ='France24 World News')

        else:

            self.embed.title = 'France24 Offical News Channel'
            self.embed.description = ' '
            self.embed.add_field(name ='?frworld', value ='France24 World News')
            self.embed.add_field(name ='?frsport', value ='France24 Sports News')
            self.embed.add_field(name ='?frbus', value ='France24 Business and economy News')

        return self.embed

    def BBCNews(self, args):

        if args == 'bbcworld':

            self.embed.title = 'BBC 24 World News'
            self.embed.add_field(name ='?bbcafrica', value ='France24 Africa News ')
            self.embed.add_field(name ='?bbcamerica', value ='France24 Americans News ')
            self.embed.add_field(name ='?bbcasia', value ='France24 Asia News')
            self.embed.add_field(name ='?bbceurope', value ='France24 Europe News ')
            self.embed.add_field(name ='?bbcme', value ='France24 Middle East News ')
            self.embed.add_field(name ='?bbcworld', value ='France24 World News')
            
        elif args == 'bbcsports':

            self.embed.title = 'France Sports News'

            self.embed.add_field(name ='?wsports', value ='Wion Sports')
            self.embed.add_field(name ='?wcricket', value ='Wion Cricket')
            self.embed.add_field(name ='?wfootball', value ='Wion Football')

        elif args == 'bbcbusiness':

            self.embed.title = 'France Business'

            self.embed.add_field(name ='?wbe', value ='Wion Business & Economy')
            self.embed.add_field(name ='?wtech', value ='Wion Technology')


        else:

            self.embed.title = 'BBC Offical News Channel'
            self.embed.description = ''
            self.embed.add_field(name ='BBC World', value ='BBC World News')
            self.embed.add_field(name ='Wion Sports', value ='Wion Sports News')

        return self.embed

    def SkyNews(self, args):

        if args == 'skyworld':

            self.embed.title = 'SkyNews Offical News Channel'
            self.embed.add_field(name ='?skyworld', value ='France24 Africa News ')
            self.embed.add_field(name ='?skyrecent', value ='France24 Americans News ')
            self.embed.add_field(name ='?skytech', value ='France24 Asia News')
            self.embed.add_field(name ='?skyent', value ='France24 Europe News ')
            self.embed.add_field(name ='?skystrange', value ='France24 Middle East News ')
            self.embed.add_field(name ='?skypol', value ='France24 World News')

        else:

            self.embed.title = 'SkyNews News'
            self.embed.description = 'SkyNews Offical News Channel'
            self.embed.add_field(name ='SkyNews World', value ='Wion World News')

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

        if args == 'usa':

            self.embed.title = 'National News USA'
            self.embed.description = ' United States National News '
            self.embed.add_field(name ='?cusa', value ='CNN National news')
            self.embed.add_field(name = '?cnbcusa', value = 'CNBC National News')
            self.embed.add_field(name = '?skycusa', value = 'SkyNews National News')

        elif args == 'india':

            self.embed.title = 'National News India'
            self.embed.description = ' '
            self.embed.add_field(name ='?windia', value ='Wion National News')

        elif args == 'france':

            self.embed.title = 'National News France'
            self.embed.description = ' '
            self.embed.add_field(name ='?24fr', value ='Wion National News')

        elif args == 'unitedkingdom':

            self.embed.title = 'National News United Kingdom'
            self.embed.description = ' '
            self.embed.add_field(name ='?skyuk', value ='SkyNews National News')
            self.embed.add_field(name ='?bbcuk', value ='BBC National News')
            self.embed.add_field(name ='?bbceng', value ='BBC National - England News')
            self.embed.add_field(name ='?bbcirish', value ='BBC National - Northen Ireland News')
            self.embed.add_field(name ='?bbcwales', value ='BBC National - Wales News')
            self.embed.add_field(name ='?bbscot', value ='BBC National - Scotland News')
            self.embed.add_field(name ='?rtru', value ='RT National News')
            

        else:

            self.embed.title = '404 Country Not Found'
            self.embed.description = f'There is no news shown for {args}'

        return self.embed
