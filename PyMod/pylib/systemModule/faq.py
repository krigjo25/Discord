
#   Discord Repositories
from discord.embeds import Embed
from discord import Color
from discord.ext.commands import command, Cog

class FrequentlyAskedQuestions(Cog):

    cmdPre = '?'

    def __init__(self,bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

#   Frequently Asked Question

    @command(name='help', pass_context=True)
    async def FrequentlyAskedQuestions(self, ctx, *, args = None):

        #   Initializing Classes
        faq = FrequentlyAskedQuestions
        #sys = SystemModule
        #avs = AdminiralVonSnider
        
        if args == None:

            self.embed.title = ':classical_building: Frequently Asked Questions:question:'
            self.embed.description = f' Usage ** {faq.cmdPre}help (Category)** for more details\n\n'
            self.embed.add_field(name=':people_holding_hands: Community Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)

            #   Moderator Commands
            if ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.manage_roles:
                self.embed.add_field(name='Moderator Module', value = 'A joke here', inline=True)

            if ctx.author.guild_permissions.administrator:
                self.embed.add_field(name='Administrator Module', value='A joke here', inline=True)

        else:
            
            args = str(args).lower().replace(" ", "")


            #   Bot-Modules

            if  args == 'communitymodule': self.embed = self.CommunityModule()

            #   Administration
            elif args == 'moderatormodule': self.embed = self.ModeratorModule(ctx)
            elif args == 'administratormodule': self.embed = self.AdministratorModule()

            else:
                self.embed.title = 'Frequently Asked Questions:question:'
                self.embed.title = f'Usage ** {faq.cmdPre}help (Category)** for more details\n\n'
                self.embed.add_field(name=':people_holding_hands: Community Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)

                #   Moderator Commands
                if ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.manage_roles:
                    self.embed.add_field(name='Moderator Module', value = 'A joke here', inline=True)

                #   Administrator commands
                if ctx.author.guild_permissions.administrator:
                    self.embed.add_field(name='Administrator Module', value='A joke here', inline=True)

        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        return

    def CommunityModule(self):

        faq = FrequentlyAskedQuestions

        self.embed.title=':people_holding_hands: Community-Module'
        self.embed.description='Use ** ?help (Command)**, for more details, sir.\n\n'

        self.embed.add_field(name='/', value='- for built-ins ', inline=True)
        self.embed.add_field(name= f'{faq.cmdPre}liro', value='list of roles')
        self.embed.add_field(name= f'{faq.cmdPre}ping', value='Checkout the bots latency')
        self.embed.add_field(name= f'{faq.cmdPre}memberlist', value ='list of members', inline=True)
        self.embed.add_field(name= f'{faq.cmdPre}yesnomaybe ', value='- Randomly chooses between yes / no or maybe', inline=True)
        self.embed.add_field(name= f'{faq.cmdPre}botinfo \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
        self.embed.add_field(name= f'{faq.cmdPre}meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)

        return self.embed

    #   Server Moderation
    def ModeratorModule(self,ctx):

        faq = FrequentlyAskedQuestions

        self.embed.title = 'Moderator Module'

        if ctx.author.guild_permissions.kick_members:

            self.embed.add_field(name = f':bar_chart: {faq.cmdPre}poll', value = '- Run a poll', inline=True)
            self.embed.add_field(name = f'{faq.cmdPre}kick', value = '- Kicks a user off the server ', inline=True)
            self.embed.add_field(name = f'{faq.cmdPre}online', value= '- Checks whom is online / offline', inline=True)

        if ctx.author.guild_permissions.manage_roles:

            self.embed.add_field(name=f'{faq.cmdPre}remro', value='- Demote a person from the role', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}dero', value='- Deletes a role from the server', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}crero', value='- Creates a role in the server', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}sero', value='- Promotes a regular user to given role', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}colro', value='- Promotes a regular user to given role', inline=True)
            pass

        if ctx.author.guild_permissions.manage_channels:

            self.embed.add_field(name=f'{faq.cmdPre}chdel', value='- Deletes a channel from the server ', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}cls', value= '- Clears the given channel Chat:bangbang:', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}chcre', value='- Create a new channel default : hidden ', inline=True)

        if ctx.author.guild_permissions.moderate_members:

            self.embed.add_field(name=f'{faq.cmdPre}lift', value= '- lift a sush from a member', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}sush', value= '- Shush a member for ammount of time ', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}warn', value= '- Warn a member for their behavior', inline=True)

        return self.embed

    def AdministratorModule(self):

        faq = FrequentlyAskedQuestions

        self.embed.title = 'Administrator Module'
        self.embed.add_field(name=f':bar_chart: {faq.cmdPre}poll', value='-Run a poll', inline=True)
        self.embed.add_field(name=f'{faq.cmdPre}unban', value= '- unban a member ', inline=True)
        self.embed.add_field(name=f':bar_chart: {faq.cmdPre}banlist', value='-View banned members', inline=True)
        self.embed.add_field(name=f'{faq.cmdPre}announce', value= '- Talk as the bot in a given channel', inline=True)
        self.embed.add_field(name=f':no_pedestrians: {faq.cmdPre}ban', value='- Probhits a Discord user to enter your channel', inline=True)

        return self.embed