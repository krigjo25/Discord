#   Discord Repositories

from discord import Colour
from discord.embeds import Embed
from discord.ext.commands import command, Cog

class FrequentlyAskedQuestions(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Colour.dark_purple())
        self.prefix = "?"

        return

#   Frequently Asked Question

    @command(name='faq', pass_context=True)
    async def FrequentlyAskedQuestions(self,ctx, args=None):

        try: pass
        except Exception as e: pass
        else: pass
        if args != None:

            match args:
                case "server": self.embed = self.ServerAnalysis()
                case "channel": self.embed = self.ChannelAnalysis()
                case "member": self.embed = self.MemberAnalysis()
        else:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.add_field(name= 'Server Analysis', value = '?faq server')
            self.embed.add_field(name= 'Channel Analysis', value = '?faq channel')
            self.embed.add_field(name= 'Member Analysis', value = '?faq member')

        await ctx.send(embed=self.embed)

        self.embed.clear_fields()
        del args

        return

    def ServerAnalysis(self): 

        '''
            #   Commands for Server Analysis
        '''
        
        self.embed.title = 'Server Analysis'
        self.embed.add_field(name = f'{self.prefix}analysis server', value = 'Run a server analysis')
        self.embed.add_field(name = f'{self.prefix}analysis role', value = 'Run a role Analysis')
        self.embed.add_field(name = f'{self.prefix}analysis channel', value = 'Run a Channel Analysis')
        self.embed.add_field(name = f'{self.prefix}analysis auditlog', value = 'Run Audit log Analysis')
        self.embed.add_field(name = f'{self.prefix}analysis bot', value = 'Run a Bot Analysis')

        return self.embed

    def ChannelAnalysis(self): 

        '''
        #   Commands for Channel Analysis
        '''
        self.embed.title = 'Frequently Asked Questions:question:'

        self.embed.add_field(name= f'{self.prefix}analysis Post', value = 'Run a Post Analysis')
        self.embed.add_field(name= f'{self.prefix}analysis emoji', value = 'Run a Emoji Analysis')
        self.embed.add_field(name= f'{self.prefix}analysis reaction', value = 'Run a Reaction Analysis')
        self.embed.add_field(name= f'{self.prefix}analysis sticker', value = 'Run a Sticker Analysis')

        return self.embed
    
    def MemberAnalysis(self):

        '''
        #   Commands for Member Analysis
        '''
        self.embed.title = 'Frequently Asked Questions:question:'
        self.embed.add_field(name= f'{self.prefix}analysis member (member name)', value = 'Run aMember Profile Analysis')
        self.embed.add_field(name= f'{self.prefix}analysis top', value = 'Top Members')

        return self.embed
