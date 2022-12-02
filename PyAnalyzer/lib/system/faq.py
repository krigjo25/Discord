
#   Discord Repositories
from discord.embeds import Embed
from discord import Color
from discord.ext.commands import command, Cog

class FrequentlyAskedQuestions(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

#   Frequently Asked Question

    @command(name='faq', pass_context=True)
    async def FrequentlyAskedQuestions(self,ctx, args=None):

        if args == 'server':self.embed = self.HelpServer()
        elif args == 'channel':self.embed = self.HelpChannel()
        elif args == 'member': self.embed = self.HelpMember()
        elif args == 'bot': self.embed = self.HelpBot()
        else:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.add_field(name= 'Server Analysis', value = '?faq server')
            self.embed.add_field(name= 'Channel Analysis', value = '?faq channel')
            self.embed.add_field(name= 'Member Analysis', value = '?faq member')

        await ctx.send(embed=self.embed)

        self.embed.clear_fields()
        self.embed.description = ''

        return

    def HelpServer(self): 

        '''
            #   Commands for Server Analysis
        '''
        
        self.embed.title = 'Server Analysis'
        self.embed.add_field(name= '?sa', value = 'Run a server analysis')
        self.embed.add_field(name= '?ra', value = 'Run a role Analysis')
        self.embed.add_field(name= '?ca', value = 'Run a Channel Analysis')

        return self.embed

    def HelpChannel(self): 

        '''
        #   Commands for Channel Analysis
        '''
        self.embed.title = 'Frequently Asked Questions:question:'

        self.embed.add_field(name= '?pa', value = 'Run a Post Analysis')
        self.embed.add_field(name= '?ea', value = 'Run a Emoji Analysis')
        self.embed.add_field(name= '?rea', value = 'Run a Reaction Analysis')
        self.embed.add_field(name= '?sta', value = 'Run a Sticker Analysis')

        return self.embed
    
    def HelpMember(self):

        '''
        #   Commands for Member Analysis
        '''
        self.embed.title = 'Frequently Asked Questions:question:'
        self.embed.add_field(name= '?mpa (member name)', value = 'Run aMember Profile Analysis')
        self.embed.add_field(name= '?topma', value = 'Top Members')

        return self.embed
    
    def HelpBot(self):

        self.embed.title = 'Bot Analysis'
        self.embed.add_field(name= 'Bot Analysis', value = 'Under Constructions')

        return self.embed