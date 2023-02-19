
#   Discord Repositories
import discord as d
from discord.embeds import Embed
from discord import Color
from discord.ext.commands import Cog, slash_command, has_permissions, after_invoke, before_invoke

class FrequentlyAskedQuestions(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return
    help = d.SlashCommandGroup(name = "help", description = "Bot Documentation")

    @help.command()
    async def community(self, ctx:d.ApplicationContext):

        self.embed.color = Color.dark_purple()
        self.embed.title=':people_holding_hands: Community Module'

        self.embed.add_field(name= f'/list roles', value='list of roles')
        self.embed.add_field(name= f'/list members', value ='list of members', inline=True)
        self.embed.add_field(name= f'/random ', value='- Randomly chooses between yes / no or maybe', inline=True)
        self.embed.add_field(name= f'/botinfo \n(optional parameter: log, latency)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
        self.embed.add_field(name= f'/help meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)

        return self.embed

    #   Server Moderation
    @help.command()
    @has_permissions()
    async def moderator(self, ctx:d.ApplicationContext):

        self.embed.title = 'Moderator Module'
        self.embed.color = Color.dark_purple()

        if ctx.author.guild_permissions.kick_members: pass
        if ctx.author.guild_permissions.manage_roles:pass

        if ctx.author.guild_permissions.manage_channels:

            self.embed.add_field(name=f'/channel Delete', value='- Deletes a channel from the server ', inline=True)
            self.embed.add_field(name=f'/channel Clear', value= '- Clears the given channel Chat:bangbang:', inline=True)
            self.embed.add_field(name=f'/channel Create', value='- Create a new channel default : hidden ', inline=True)

        if ctx.author.guild_permissions.moderate_members: pass
        return self.embed

    #   Server Adminsistration
    async def AdministratorModule(self, ctx:d.ApplicationContext): return