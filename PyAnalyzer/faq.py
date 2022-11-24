
#   Discord Repositories
from discord.embeds import Embed
from discord import Color
from discord.ext.commands import command, Cog

class FrequentlyAskedQuestions(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

#   Frequently Asked Question

    @command(name='pybut', pass_context=True)
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
            if ctx.author.guild_permissions.kick_members: #or ctx.author.guild_permissions.manage_roles:
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

        self.embed.title = 'Discord Analyzor'
        self.embed.add_field(name='?cls (channel name) (1-100)', value= '- Clears the given channel Chat:bangbang:', inline=True)
        self.embed.add_field(name='?warn (MemberName) (Reason)', value= '- Manually Warn a member for their behavior', inline=True)

        return self.embed