
#   Discord Repositories
from discord.embeds import Embed
from discord import Color
from discord.ext.commands import Cog, command, has_permissions, after_invoke, before_invoke

class FrequentlyAskedQuestions(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.prefix = "?"
        self.embed = Embed(color=Color.dark_purple())

        return
    @command(name = "help", pass_context = True)
    async def faq(self, ctx, *, arg= None):

        try :

            if arg != None: arg = str(arg).lower().replace(" ", "")

            if not str(arg).isalpha(): raise Exception()

        except Exception as e : print(e)
        else:


            if arg == None:

                self.embed.color = Color.dark_purple()
                self.embed.title = ':classical_building: Frequently Asked Questions:question:'
                self.embed.description = f' Usage ** {self.prefix}help (Category)** for more details\n\n'
                self.embed.add_field(name=':people_holding_hands: Community Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)

                #   Moderator Commands
                if ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.manage_roles: self.embed.add_field(name='Moderator Module', value = 'A joke here', inline=True)

                #   Administrator commands
                if ctx.author.guild_permissions.administrator:self.embed.add_field(name='Administrator Module', value='A joke here', inline=True)
            else :

                match arg:
                    case "communitymodule": self.embed = self.CommunityModule()
                    case "moderationmodule": self.embed = self.ModeratorModule(ctx)
                    case "administratormodule": self.embed = self.AdministratorModule(ctx)

        await ctx.send(embed = self.embed)

        #   Clear some memory
        self.embed.clear_fields()

        return

    def CommunityModule(self):

        self.embed.color = Color.dark_purple()
        self.embed.title=':people_holding_hands: Community Module'
        self.embed.description=f'Use ** {self.prefix}help (Command)**, for more details, sir.\n\n'

        self.embed.add_field(name='/', value='- for built-ins ', inline=True)
        self.embed.add_field(name= f'{self.prefix}liro', value='list of roles')
        self.embed.add_field(name= f'{self.prefix}ping', value='Checkout the bots latency')
        self.embed.add_field(name= f'{self.prefix}memberlist', value ='list of members', inline=True)
        self.embed.add_field(name= f'{self.prefix}yesnomaybe ', value='- Randomly chooses between yes / no or maybe', inline=True)
        self.embed.add_field(name= f'{self.prefix}botinfo \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
        self.embed.add_field(name= f'{self.prefix}meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)

        return self.embed

    #   Server Moderation
    def ModeratorModule(self, ctx):

        self.embed.title = 'Moderator Module'
        self.embed.color = Color.dark_purple()

        if ctx.author.guild_permissions.kick_members:

            self.embed.add_field(name = f'{self.prefix}member kick', value = '- Kicks a user off the server ', inline=True)
            self.embed.add_field(name = f'{self.prefix}online', value= '- Checks whom is online / offline', inline=True)

        if ctx.author.guild_permissions.manage_roles:

            self.embed.add_field(name=f'{self.prefix}role Demote', value='- Demote a person from the role', inline=True)
            self.embed.add_field(name=f'{self.prefix}role List', value='- list roles', inline=True)
            self.embed.add_field(name=f'{self.prefix}role Delete', value='- Deletes a role from the server', inline=True)
            self.embed.add_field(name=f'{self.prefix}role Create', value='- Creates a role in the server', inline=True)
            self.embed.add_field(name=f'{self.prefix}role Set', value='- Promotes a regular user to given role', inline=True)
            self.embed.add_field(name=f'{self.prefix}role Color', value='- Promotes a regular user to given role', inline=True)
            pass

        if ctx.author.guild_permissions.manage_channels:

            self.embed.add_field(name=f'{self.prefix}ch Delete', value='- Deletes a channel from the server ', inline=True)
            self.embed.add_field(name=f'{self.prefix}ch Clear', value= '- Clears the given channel Chat:bangbang:', inline=True)
            self.embed.add_field(name=f'{self.prefix}ch Create', value='- Create a new channel default : hidden ', inline=True)

        if ctx.author.guild_permissions.moderate_members:

            self.embed.add_field(name = f':bar_chart: {self.prefix}Member poll', value = '- Run a poll', inline=True)
            self.embed.add_field(name=f'{self.prefix}Member Lift', value= '- lift a sush from a member', inline=True)
            self.embed.add_field(name=f'{self.prefix}Member Sush', value= '- Shush a member for ammount of time ', inline=True)
            self.embed.add_field(name=f'{self.prefix}Member Warn', value= '- Warn a member for their behavior', inline=True)

        return self.embed

    #   Server Adminsistration
    async def AdministratorModule(self, ctx):

        self.embed.color = Color.dark_purple()
        self.embed.title = 'Administrator Module'
        self.embed.add_field(name=f':bar_chart: {self.prefix}poll', value='-Run a poll', inline=True)
        self.embed.add_field(name=f'{self.prefix}Member unban', value= '- unban a member ', inline=True)
        self.embed.add_field(name=f':bar_chart: {self.prefix}Member banlist', value='-View banned members', inline=True)
        self.embed.add_field(name=f'{self.prefix}Member announce', value= '- Talk as the bot in a given channel', inline=True)
        self.embed.add_field(name=f':no_pedestrians: {self.prefix}Member ban', value='- Probhits a Discord user to enter your channel', inline=True)

        return self.embed