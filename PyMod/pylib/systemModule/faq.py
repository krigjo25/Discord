
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

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.title = f' Usage ** {faq.cmdPre}help (Category)** for more details\n\n'
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

        self.embed.title=':people_holding_hands: Community-Module'
        self.embed.description='Use ** ?help (Command)**, for more details, sir.\n\n'

        self.embed.add_field(name='/', value='- for built-ins ', inline=True)
        self.embed.add_field(name='?memberlist', value ='list of members', inline=True)
        self.embed.add_field(name='?dnd ', value='- Notifies others about your absence', inline=True)
        self.embed.add_field(name='?back ', value='- Shows that you\'re a no lifer again', inline=True)
        self.embed.add_field(name='?yesnomaybe ', value='- Randomly chooses between yes / no or maybe', inline=True)
        self.embed.add_field(name='?botinfo \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
        self.embed.add_field(name='?meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)
        #self.embed.add_field(name=':x:?pre-mod', value='How does the pre-mod work')

        return self.embed

    #   Server Moderation
    def ModeratorModule(self,ctx):

        faq = FrequentlyAskedQuestions

        self.embed.title = 'Moderator Module'
        print('lol')


        if ctx.author.guild_permissions.kick_members:

            
            self.embed.add_field(name=':bar_chart: ?poll', value='- Run a poll', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}online', value= '- Checks whom is online / offline', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}kick', value='- Kicks a user off the server ', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}warn', value= '- Manually Warn a member for their behavior', inline=True)

        if ctx.author.guild_permissions.manage_roles:

            self.embed.add_field(name=f'{faq.cmdPre}remove', value='- Demote a person from the role', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}delRole', value='- Deletes a role from the server', inline=True)
            #self.embed.add_field(name=f':x:{faq.cmdPre}rolelist', value='- Promotes a regular user to given role', inline=True)
            #self.embed.add_field(name=f':x:{faq.cmdPre}roleColorlist', value='- Promotes a regular user to given role', inline=True)
            #self.embed.add_field(name=f':x:{faq.cmdPre}roleCreat)', value='- Creates a role in the server', inline=True)
            #self.embed.add_field(name=f':x:{faq.cmdPre}setRole', value='- Promotes a regular user to given role', inline=True)
            #self.embed.add_field(name=f':x:{faq.cmdPre}roleColor', value='- Promotes a regular user to given role', inline=True)

        if ctx.author.guild_permissions.manage_channels:


            #self.embed.add_field(name='?chPri', value='- Channel Privileges ', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}chdel', value='- Deletes a channel from the server ', inline=True)
            self.embed.add_field(name=f'{faq.cmdPre}cls', value= '- Clears the given channel Chat:bangbang:', inline=True)
            #self.embed.add_field(name=f'{faq.cmdPre}chcre', value='- Create a new channel default : hidden ', inline=True)
            
        if ctx.author.guild_permissions.mute_members:

            self.embed.add_field(name=f'{faq.cmdPre}sush', value= '- Shush a member for a number of sec', inline=True)

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