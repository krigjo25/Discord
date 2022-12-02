#  Repositories
import pandas as pd
import numpy as np
import emoji

#   Asyncio responsories
from asyncio import sleep
#   Discord Repositories
from discord.embeds import Embed
from discord import Color, Member, Message, Forbidden
from discord.ext.commands import command, Cog
from discord.ext.commands.errors import MemberNotFound

class MemberAnalysis(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed()

        return

    @command(name='mpa', pass_context = True)
    async def MemberProfileAnalyzer(self, ctx, *, member:Member = None, message = Message):

        #   Counters
        th = 0
        post = 0
        emo = 0
        sticker = 0
        reaction = 0


        try:

            if member == None: return await ctx.send('Member not found, try again')
            
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
            
            role = ''
            mutual = ''
            permissions = []
            
            for i in member.roles:
                role += f'{i.mention}\n'
            for i in member.mutual_guilds:mutual += f'{i.name}'

            for i in member.guild_permissions:
                perm = [i]
                permissions.append(perm)
            


        except Exception as e: print(e)

        else:

            await ctx.send(f'Collecting Data from {member}')

            #   Fetching the profile information
            profileInfo = [
                            [member.display_name],
                            [member.id],
                            [member.activity],
                            [member.color], 
                            [member.bot],
                            [member.banner],
                            [MemberStatus],
                            [boost],
                            [member.created_at.date()],
                            
                ]

            for i in ctx.guild.text_channels:
                print(i)
                #msg = await i.fetch_message(i.last_message_id)
                print(message.content)

                #   Fetching threads
                if i.threads: 
                    for k in i.threads:
                        if k.owner_id == member.id: th += 1

                async for j in i.history(limit = None):

                    if str(member) == str(j.author): post += 1
                    if str(member) == str(j.author) and str(j.content) in emoji.distinct_emoji_list(str(j.content)): emo += 1
                    
                    async with i.typing():
                        await sleep(2)



            #   Dataframe for profileInfo
            column = ['']

            row = ['**Nick**', '**ID** :', '**Activity** :', '**Account Color** :', '**Bot** :', '**Banner** :', status, '**Nitro** :', '**Account Created** :',]
            profileInfo = pd.DataFrame(profileInfo, index = row, columns = column)

            #   Dataframe for GuildInfo

            row = ['**Pending** :', '**Mutual Guilds** :', '**Roles** :', '**Highest Roles** :',]
            memberGuild = [[member.pending], [mutual],[role], [member.top_role.mention],]
            memberGuild = pd.DataFrame(memberGuild, index = row, columns = column)


            row = ['**Total Post** :', '**Total Emojis**:' '**Total Threads** :']
            memberStats = [[post], [emo], [th]]
            memberStats = pd.DataFrame(memberStats, index= row, columns = column)
            print('test')

            #   Prepare embed message
            
            self.embed.url = member.jump_url
            self.embed.set_image(url=avatar)
            self.embed.title = f'Profile information of {member}'


            self.embed.add_field(name = 'Profile Information', value= f'{profileInfo}', inline=True)
            self.embed.add_field(name = 'Guild Information', value=f'{memberGuild}', inline=True)
            self.embed.add_field(name = 'Other Informations', value=f'**System** :{member.system}\n', inline=True)
            self.embed.add_field(name = 'Member Stats', value= memberStats, inline=True)


            await ctx.send(embed=self.embed)

            #   Cleaning up the Code
            del row
            del column
            del memberGuild
            del profileInfo

            self.embed.url = ''
            self.embed.clear_fields()
            self.embed.set_image(url='')

            return

    @command(name='topma', pass_context = True)
    async def TopPoster(self, ctx):


        srv = ctx.guild

        postCount = []
        memberList = []
        membersScore = []
        channelList = []

        for i in srv.text_channels:
            
            try:
                #   Declare dictionaries
                emojiCount = {}
                membersCount = {}
                reactionCount = {}

                ch = [i.name]
                channelList.append(ch)

                ch = srv.get_channel(i.id)

                await ctx.send(f'Collecting Member Data from **{ch.name}**...')

                #   Iterating throught the history
                async for j in ch.history(limit = 10):

                    #   Counting posts
                    if j.author.name in membersCount: membersCount[j.author.name] += 1
                    else :membersCount[j.author.name] = 1

                    #   Counting emojis
                    #   Couting reactions

                #   Iterating through the dictionary
                for key in membersCount:
                    li = [membersCount[key]]
                    postCount.append(li)

                    li = [key]
                    memberList.append(li)


                #   Cleaning up
                del emojiCount
                del membersCount
                del reactionCount

            except Exception as e :
                print(e)
                await ctx.send(f' Can not access {i.name}')
                continue


        print(memberList)

        #   Creating a dataframe
        column = ['']
        row = []

        for i in range(len(channelList)):
            row.append('')

        channelList = pd.DataFrame(channelList, index = row, columns= column)
        print('test')
        #memberList = pd.DataFrame(memberList, index = row, columns= column)
        print('test')
        #postCount = pd.DataFrame(postCount, index = row, columns= column)
        print('test')

        #   Prepare embed message & Send message
        self.embed.title = 'Top Posters'
        self.embed.add_field(name='Channel', value = channelList)
        #self.embed.add_field(name='MemberName', value = memberList)

        await ctx.send(embed=self.embed)

        #   Cleaning up
        del postCount
        del memberList
        del channelList

        return

