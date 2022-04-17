
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
        avs = AdminiralVonSnider
        
        if args == None:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.title = ' Usage ** ?help (Category)** for more details\n\n'
            self.embed.add_field(name=':people_holding_hands: Community Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)
            self.embed.add_field(name=':people_wrestling: Game Module', value='-Gamers does not take showers they do steamy once', inline=True)

            #   Moderator Commands
            if ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.manage_roles:
                self.embed.add_field(name='Moderator Module', value = 'A joke here', inline=True)

            if ctx.author.guild_permissions.administrator:
                self.embed.add_field(name='AdministratorModule', value='A joke here', inline=True)

        else:

            args = str(args).lower().replace(" ", "")

        #   Bot-Modules

            if  args == 'communitymodule': self.embed = sys.CommunityModule()

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