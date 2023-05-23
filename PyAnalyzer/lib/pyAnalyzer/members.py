#  Repositories
import pandas as pd
import numpy as np
import emoji

#   Discord Repositories
import discord as d
from discord import utils
from discord.embeds import Embed
from discord import Color, Member, Message, Forbidden
from discord.ext.commands import command, Cog
from discord.ext.commands.errors import MemberNotFound


class MemberAnalysis(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed()

        return

    member = d.SlashCommandGroup(name= 'member', description= 'Member analysis')
    @member.command(name='mpa', pass_context = True)
    async def MemberProfileAnalyzer(self, ctx:d.ApplicationContext, *, member:Member = None, message = Message):

        #   Counters
        th, emo, post = 0, 0, 0

        try:

            if member == None: raise Exception('Member not found, try again')

            if str(member.web_status) != 'offline': 
                status = f'**Web Status** :'
                MemberStatus = f'{member.web_status}'

            elif str(member.mobile_status) != 'offline': 
                status = f'**Mobile Status** :'
                MemberStatus = f'{member.mobile_status}'

            elif str(member.desktop_status) != 'offline': 
                status = f'**Client Status** :'
                MemberStatus = f'{member.desktop_status}'
            else: 
                status = '**Status** :'
                MemberStatus = 'Offline'

            #   Member avatar
            if member.avatar != None: avatar = member.avatar
            else: avatar = member.default_avatar
            
            if member.premium_since == None: boost = 'No'
            else: boost = member.premium_since
            
            role, mutual = '', ''
            permissions = []
            
            for i in member.roles: role += f'{i.mention}\n'

            for i in member.mutual_guilds:mutual += f'{i.name}'

            for i in member.guild_permissions:
                perm = [i]
                permissions.append(perm)

        except Exception as e: print(e)

        else:

            await ctx.respond(f'Collecting Data from {member}.\nIt may take several minutes to collect the information, please hold on')

            #   Fetching the profile information
            profileInfo = [
                            [member.display_name], [member.id], [member.activity],
                            [member.color], [member.bot], [member.banner],
                            [MemberStatus], [boost], [member.created_at.date()],
                        ]

            #   Initializing
            memberCount = {}
    
            for i in ctx.guild.text_channels:

                members = []

                async with i.typing():

                    #   Fetching threads
                    if i.threads: 
                        for k in i.threads:
                            if k.owner_id == member.id: th += 1
            
                    async for j in i.history(limit = None):

                        #   Counting emojis
                        if str(member) == str(j.author) and str(j.content) in emoji.distinct_emoji_list(str(j.content)): emo += 1
                        #   Counting posts
                        if j.author.name in memberCount: memberCount[j.author.name] += 1
                        else : memberCount[j.author.name] = 1

                    name = max(zip(memberCount.values(), memberCount.keys()))[1]
                    post = max(zip(memberCount.values(), memberCount.keys()))[0]
                    members.append(name)

                    if member.name in members: post = f'{post} \U0001F947'

                    #   If the member in second / third place
                    else: 
                        post = memberCount[member.name]

                    #   Clean up
                    del members


            #   Dataframe for profileInfo
            column = ['']
            row = ['**Nick**', '**ID** :', '**Activity** :', '**Account Color** :', '**Bot** :', '**Banner** :', status, '**Nitro** :', '**Account Created** :',]
            profileInfo = pd.DataFrame(profileInfo, index = row, columns = column)

            #   Dataframe for GuildInfo
            row = ['**Pending** :', '**Mutual Guilds** :', '**Roles** :', '**Highest Roles** :',]
            memberGuild = [[member.pending], [mutual],[role], [member.top_role.mention],]
            memberGuild = pd.DataFrame(memberGuild, index = row, columns = column)

            #   Dataframe for memberStats
            row = ['**Total Post** :', '**Total Emojis**:', '**Total Threads** :',]
            memberStats = [[post], [emo], [th]]
            memberStats = pd.DataFrame(memberStats, index= row, columns = column)

            #   Prepare embed message
            
            self.embed.url = member.jump_url
            self.embed.set_thumbnail(url = avatar)
            self.embed.title = f'Profile information of {member}'


            self.embed.add_field(name = 'Profile Information', value= f'{profileInfo}', inline=True)
            self.embed.add_field(name = 'Guild Information', value=f'{memberGuild}', inline=True)
            self.embed.add_field(name = 'Other Informations', value=f'**System** :{member.system}\n', inline=True)
            self.embed.add_field(name = 'Member Stats', value= memberStats, inline=True)


            await ctx.respond(embed=self.embed)

            #   Cleaning up the Code
            del row, column, memberGuild
            del profileInfo, memberCount

            self.embed.url = ''
            self.embed.clear_fields()
            self.embed.remove_thumbnail()

            return

    @member.command()
    async def TopPoster(self, ctx:d.ApplicationContext):

        #   Initializing lists
        post, member, channel = [], [], []

        for i in ctx.guild.text_channels:

            try:
                #   Declare dictionaries
                memberCount = {}

                ch = [i.name]
                channel.append(ch)
                ch = ctx.guild.get_channel(i.id)

                await ctx.send(f'Collecting Member Data from **{ch.name}**...')

                #   Iterating throught the history
                async for j in ch.history(limit = None):

                    #   Counting posts
                    if j.author.name in memberCount: memberCount[j.author.name] += 1
                    else : memberCount[j.author.name] = 1

                if memberCount:
                    #   fetch the member with most posts
                    name = max(zip(memberCount.values(), memberCount.keys()))[1]
                    value = max(zip(memberCount.values(), memberCount.keys()))[0]

                    member.append(name)
                    post.append(value)

                else: 
                    member.append('Jhon Doe')
                    post.append(0)

                #   Cleaning up
                del ch
                del memberCount

            except Exception as e :

                await ctx.send(f' Can not access {i.name}')
                continue

        #   Creating Dataframes

        #   Channel Dataframe
        column, row = [''], []

        for i in range(len(channel)): row.append('')

        channel = pd.DataFrame(channel, index = row, columns= column)
        
        #   Member Dataframe
        member = pd.DataFrame(member, index = row, columns= column)

        #   Postcount Dataframe
        post = pd.DataFrame(post, index = row, columns = column)

        #   Prepare embed message & Send message
        self.embed.title = 'Top Posters'
        self.embed.add_field(name='Channel', value = channel)
        self.embed.add_field(name='Member Name', value = member)
        self.embed.add_field(name='Total Post', value = post)

        await ctx.respond(embed=self.embed)

        #   Clean up
        self.embed.clear_fields()
        del post, member, channel

        return
