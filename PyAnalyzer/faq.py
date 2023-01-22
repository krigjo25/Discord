
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

        #   Initializing Classes
        server = FrequentlyAskedQuestionHelpPanel()
        if args == None:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.description = ' Usage ** ?help (Category)** for more details\n\n'
            self.embed.add_field(name=':information_source: Server Information', value='Analyze the server', inline=True)
            self.embed.add_field(name='Channel Analysis', value='- Channel analysis', inline=True)
            self.embed.add_field(name='Member Analysis',value='Member analysis', inline=True)

        else:

            args = str(args).lower().replace(" ", "")

            #   Bot-Modules
            if args == 'server' or args == 'serveranalysis': server.ServerAnalysis()
            elif args == 'channel' or args == 'channelanalysis': server.ChannelAnalysis()
            elif args == 'member' or args == 'memberanalysis': self.embed = server.MemberAnalysis()

        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        return

class FrequentlyAskedQuestionHelpPanel(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    def ServerAnalysis(self):

        url = 'https://online.stat.psu.edu/statprogram/sites/statprogram/files/2018-08/statistics-review.jpg'
        self.embed.title='Server Analysis'
        self.embed.set_thumbnail(url = url)
        self.embed.add_field(name='?ra', value='Role Analysis', inline=True)
        self.embed.add_field(name='?bota', value='Bot Analysis', inline=True)
        self.embed.add_field(name='?ca', value='Channel Analysis', inline=True)
        self.embed.add_field(name='?loga', value='Audit log Analysis', inline=True)
        self.embed.add_field(name='?sa', value='- Server Overal Analysis', inline=True)

        #   Clean up
        self.embed.title = ''
        self.embed.remove_thumbnail()
        self.embed.clear_fields()
        
        return self.embed
    
    def MemberAnalysis(self):

        url = 'https://online.stat.psu.edu/statprogram/sites/statprogram/files/2018-08/statistics-review.jpg'
        self.embed.title='Member Analysis'
        self.embed.set_thumbnail(url = url)
        self.embed.add_field(name='?mpa', value='Member Profile Analysis', inline=True)
        self.embed.add_field(name='?topma', value='Top Member Analysis', inline=True)

        #   Clean up
        self.embed.title = ''
        self.embed.remove_thumbnail()
        self.embed.clear_fields()
        
        return self.embed

    def ChannelAnalysis(self):

        url = 'https://online.stat.psu.edu/statprogram/sites/statprogram/files/2018-08/statistics-review.jpg'
        self.embed.title='Channel Analysis'
        self.embed.set_thumbnail(url = url)
        self.embed.add_field(name='?pa', value='Post Analysis', inline=True)

        #   Clean up
        self.embed.title = ''
        self.embed.remove_thumbnail()
        self.embed.clear_fields()
        
        return self.embed
