#  Repositories
from datetime import date

#   Discord Repositories
from discord.embeds import Embed
from discord import Color, Member, User 
from discord.ext.commands import command, Cog

class ServerAnalysis(Cog):

    def __init__(self, bot):

        self.embed = Embed()
        self.bot = bot

        return

    @command(name = 'server', pass_context = True)
    async def DiscordServerInformation(self, ctx):

        #   Fetching the guild name, rank, days online
        srv = ctx.guild  

        create = srv.created_at
        today = date.today()
        delta = 0#today - create

        #   Server Rank

        #   Counting roles in the guild
        role = len(srv.roles)

        #   Counting members
        totalMembers = len([i for i in srv.members])
        bot = len([i for i in srv.members if i.bot])
        members = len([i for i in srv.members if not i.bot])
        nitro = 0#len([i for i in srv.members if nitro])

        #   Counting bans in the guild
        banned = len([i async for i in srv.bans(limit=2000)])

        #   Counting Channels
        totalChannels = len([i for i in srv.channels if str(i.type) != 'category'])
        voiceChannels = len([i for i in srv.channels if str(i.type) == 'text'])
        textChannels = len([i for i in srv.channels if str(i.type) == 'voice'])
        categories = len([i for i in srv.channels if str(i.type) == 'category'])

        
        #   Counting total events


        #   Prepare the message
        self.embed.title = f'Server Information'
        self.embed.add_field(name = f'Server Name', value =f'**{srv}**\n ID: **{srv.id}**\n Created : **{srv.created_at}**\n {delta} days ago', inline = True)
        self.embed.add_field(name = f'Total Server Roles', value =f'{srv} has total of **{role}** roles', inline = True)
        self.embed.add_field(name = f'Total Members', value = f'{srv} has the total of **{totalMembers}** members in the server.\n **{members}** are members.\n **{bot}** are bots.\n**{nitro}** of the members has nitro.', inline = True)
        self.embed.add_field(name = f'Total banned Members', value = f'{srv} has the total of **{banned}** banned members', inline = True)
        self.embed.add_field(name = f'Total Channels', value = f'{srv} has the total of **{totalChannels}** Channels.\n**{voiceChannels}** is Voice Channels\n**{textChannels}** is Text Channels.\n**{categories}** is categories.', inline = True)

        #   Send the message
        await ctx.send(embed = self.embed)

        #   Clean up
        del banned
        del categories
        del textChannels
        del totalChannels
        del voiceChannels

        #   Clearing embed fields
        self.embed.clear_fields()

        return