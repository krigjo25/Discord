#  Repositories
from datetime import date

#   Discord Repositories
from discord.embeds import Embed
from discord import Color, Member
from discord.ext.commands import command, Cog

class ServerAnalysis(Cog):

    def __init__(self, bot):

        self.embed = Embed()
        self.bot = bot

        return

    @command(name = 'serverinfo', pass_context = True)
    async def DiscordServerInformation(self, ctx):

        #   Fetching the guild name, rank, days online
        srv = ctx.guild  
        create = srv.created_at
        today = date.today()
        delta = 0#today - create


        #   Counting roles in the guild
        role = len(srv.roles)

        #   Counting members
        total = len([i for i in srv.members])
        bot = len([i for i in srv.members if i.bot])
        members = len([i for i in srv.members if not i.bot])
        nitro = 0#len([i for i in srv.members if nitro])
        boost = len(srv.premium_subscribers)

        #   Counting bans in the guild
        banned = len([i async for i in srv.bans(limit=2000)])

        #   Counting Channels
        totalChannels = len([i for i in srv.channels if str(i.type) != 'category'])
        voiceChannels = len([i for i in srv.channels if str(i.type) == 'text'])
        textChannels = len([i for i in srv.channels if str(i.type) == 'voice'])
        categories = len([i for i in srv.channels if str(i.type) == 'category'])

        #   Prepare the message
        self.embed.title = f'Server Information'
        self.embed.add_field(name = f'Server Name', value =f'**{srv}**\n ID: **{srv.id}**\n Created : **{srv.created_at}**\n {delta} days ago', inline = True)
        self.embed.add_field(name = f'Total Server Roles', value =f'{srv} has total of **{role}** roles', inline = True)
        self.embed.add_field(name = f'Total Members', value = f'{srv} has the total of **{total}** members in the server.\n **{members}** are members.\n **{bot}** are bots.\n**{nitro}** of the members has nitro.\n**{boost}** of the members has Boosted the server.', inline = True)
        self.embed.add_field(name = f'Total banned Members', value = f'{srv} has the total of **{banned}** banned members', inline = True)
        self.embed.add_field(name = f'Total Channels', value = f'{srv} has the total of **{totalChannels}** Channels.\n**{voiceChannels}** is Voice Channels\n**{textChannels}** is Text Channels.\n**{categories}** is categories.', inline = True)

        #   Send the message
        await ctx.send(embed = self.embed)

        #   Clean up
        del bot
        del nitro
        del total
        del banned
        del members
        del categories
        del textChannels
        del totalChannels
        del voiceChannels

        #   Clearing embed fields
        self.embed.clear_fields()

        return

    @command(name='roleinfo', pass_context = True)
    async def RoleAnalyzer(self, ctx):

        srv = ctx.guild
        #   Counting roles
        count = len(srv.roles)

        #   Extracting role infomration
        role = await srv.fetch_roles()

        for i in role:

            #   Finding roles
            id = srv.get_role(i.id)
            id = len(id.members)
    

            #   Create a new field
            self.embed.add_field(name = f'{i.name}', value = f' Role ID : **{i.id}**,\n Members : **{id}**,')


        #   Send embed message

        self.embed.title = f'Role Overview for {srv}'
        self.embed.description = f'Counting **{count}** Roles'
        await ctx.send(embed = self.embed)

        return

    @command(name='mi', pass_context = True)
    async def MemberAnalyzer(self, ctx, *, member:Member = None):

        if member == None: return
        else:



                #self.embed.add_field(name = f'sdf')

            self.embed.title = f'Profile information of {member}'
            self.embed.description = f'Member Avatar : **{member.avatar}**\nMember ID : **{member.id}**\nBot : **{member.bot}**\nAccount Color :**{member.accent_color}**\nBanner : **{member.banner}**\nStatus : **{member.status}**\nSystem : **{member.system}**\nAccount Created : **{member.created_at}**\n Avatar : {member.default_avatar}\n Flags : {member.display_name}'
            '''
            Profile Information\n

            Member Avatar : {member.default_avatar}\n
            Member Avatar : **{member.avatar}**\n
            Nick : {member.display_name}\n
            Member ID : **{member.id}**\n
            Status : **{member.status}**\n
            Bot : **{member.bot}**\n

            Account Color :**{member.accent_color}**\n
            Banner : **{member.banner}**\n

            Role Information:
            Roles : {member.roles}\n
            Highest role : {member.top_role}\n
            
            Permissions and Colour
            Color : {member.color}\n
            Permissions : {member.permissions}\n
            System : **{member.system}**\n
            Account Created : **{member.created_at}**\n
            '''
            await ctx.send(embed=self.embed)




class RoleAnalysis(Cog):

    def __init__(self, bot):

        self.embed = Embed()
        self.bot = bot

        return

    @command(name='roles', pass_context = True)
    async def RoleAnalyzer(self, ctx):

        srv = ctx.guild
        #   Counting roles
        count = len(srv.roles)

        #   Extracting role infomration
        role = await srv.fetch_roles()

        for i in role:

            #   Finding roles
            id = srv.get_role(i.id)
            id = len(id.members)
    

            #   Create a new field
            self.embed.add_field(name = f'{i.name}', value = f' Role ID : **{i.id}**,\n Members : **{id}**,')


        #   Send embed message

        self.embed.title = f'Role Overview for {srv}'
        self.embed.description = f'Counting **{count}** Roles'
        await ctx.send(embed = self.embed)

        return

class MemberAnalysis(Cog):
    pass

class PostAnalysis(Cog):
    pass

class ThreadAnalysis(Cog):
    pass

