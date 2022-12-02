#  Repositories
import pandas as pd
import emoji
#   Discord Repositories
from discord import Forbidden
from discord.embeds import Embed
from discord.ext.commands import command, Cog


class ChannelAnalysis(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed()
        return

    @command(name = 'pa', pass_context=True)
    async def PostAnalysis(self, ctx):

        #   Initializing variables, sending a process message
        srv = ctx.guild

        #   DataFrame lists
        postCount = []
        channelID = []
        emojiCount = []
        channelName = []
        channelType = []
        threadCount = []
        memberCount = []
        ageRestriction = []
        
        

        #
        th = 0
        row = []
        column = ['**Channel ID**', '**Channel Name**','**Total Threads**', '**Total Posts**']
        column = ['']

        #   Voive Channels
        #   Text Channels
        for i in srv.text_channels:


            if i.is_nsfw(): age = 'Yes'
            else : age = 'No'
            
            if i.threads : th = len([j for j in i.threads])
            else : th = 0

            try :

                emo = 0
                post = 0
                await ctx.send(f'Collecting data from **{i.name}**')


                #   Fetching all messages and counting
                async for j in i.history(limit = None):


                    post += 1
                    if str(j.content) in emoji.distinct_emoji_list(str(j.content)): emo += 1

                emo = [emo]
                post = [post]
                chID = [i.id]
                thread = [th]
                chName = [i.mention]
                member = [len(i.members)]
                
                
                        


                #   Channel information
                channelID.append(chID)
                channelName.append(chName)
                ageRestriction.append(age)

                #   Channel counts
                emojiCount.append(emo)
                postCount.append(post)
                threadCount.append(thread)
                memberCount.append(member)

                #   Clean up
                del chID
                del post
                del chName
                del thread
                del member

            except Forbidden:
                print(f'channel {i.name} could not be accsessed')
                continue

        for i in range(len(channelID)):
            row.append('')

    
        channelID = pd.DataFrame(channelID, index = row, columns = column)
        channelName = pd.DataFrame(channelName, index = row, columns = column)
        ageRestriction = pd.DataFrame(ageRestriction, index = row, columns = column)
        
        postCount = pd.DataFrame(postCount, index = row, columns = column)
        emojiCount = pd.DataFrame(emojiCount, index = row, columns = column)
        threadCount = pd.DataFrame(threadCount, index = row, columns = column)
        memberCount = pd.DataFrame(memberCount, index = row, columns = column)

        #   Prepare & send embeded message
        self.embed.title = 'Channel Analysis'
        self.embed.add_field(name ='Channel ID', value=channelID)
        self.embed.add_field(name ='Channel Name', value=channelName)
        self.embed.add_field(name ='Age Restriction', value = ageRestriction)

        self.embed.add_field(name ='Total Channel Posts', value = postCount)
        self.embed.add_field(name ='Total Channel Emoji', value = emojiCount)
        self.embed.add_field(name ='Total Channel Threads', value = threadCount)
        self.embed.add_field(name ='Total Channel Watchers', value = memberCount)

        await ctx.send(embed = self.embed)

        #   Cleaning up the Code
        del channelID
        del postCount
        del threadCount
        del channelName
        del memberCount
        del ageRestriction

        self.embed.clear_fields()
        self.embed.description = ''

        return

    @command(name = 'ea', pass_context=True)
    async def emojiAnalysis(self, ctx):

        await ctx.send('Under Construction')

        return

    @command(name = 'rea', pass_context=True)
    async def reactionAnalysis(self, ctx):
        await ctx.send('Under Construction')
        return
