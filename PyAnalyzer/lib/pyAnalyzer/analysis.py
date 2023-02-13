#  Repositories
import pandas as pd


#   Discord Repositories
import discord as d
from discord import Forbidden
from discord.embeds import Embed
from discord.ext.commands import command, group, before_invoke, after_invoke, Cog

class ServerAnalysis(Cog):

    '''
        #   Fetching the Discord Server information
        #   Fetching roles
        #   Fetching Posts
    '''
    def __init__(self, bot):

        self.embed = Embed()
        self.bot = bot

        return
    @after_invoke("Analysis")
    def ClearMemory(self, ctx):

        #   Clear some Memory
        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.remove_thumbnail()
        self.embed.color = d.Colour.dark_purple()

        return

    @group(pass_context = True)
    @d.has_permission(administrator = True)
    async def Analysis(self, ctx):

        await self.ClearMemory(ctx)

        return

    @Analysis.command()
    async def server(self, ctx):

        #   Initializing variables

        try:

            banned = len([i async for i in ctx.guild.bans(limit=None)])

            #   Creating a Dataframe
            overview = [ctx.guild.name, ctx.guild.id, f'{ctx.guild.owner},', ctx.guild.created_at.date(), '  ', len(ctx.guild.roles), len(ctx.guild.premium_subscribers),  banned, ctx.guild.member_count, len(ctx.guild.channels), len(ctx.guild.scheduled_events)]
            row = ['**ServerName**: ', '**ServerID**: ', '**Owner(s)**: ', '**Created**: ', ' ', '**Total roles**: ', '**Total Boosts** :', '**Total banned** :', '**Total Members**: ', '**Total Channels :**', '**Scheduled Events** :']
            overview = pd.DataFrame(overview, index = row, columns = [''])
        
        except Exception as e: print(e)
        else:

            #   Prepare & Send message
            self.embed.title = f'Server Information'
            self.embed.description = f'{overview}'

            #   Send the message
            await ctx.send(embed = self.embed)

            #   Cleaning up the Code
            del row
            del banned
            del overview

            return

    @Analysis.command()
    async def role(self, ctx):

        #    Creating a DataFrame
        row = []
        column = ['']

        roleID = []
        roleName = []
        memberCount = []

        #   Extracting role infomration
        for i in await ctx.guild.fetch_roles():

            #   Appending to the dataframe
            row.append('')
            roleID.append([i.id])
            roleName.append([i.mention])
            memberCount.append(len(ctx.guild.get_role(i.id)))

        roleID = pd.DataFrame(roleID, index = row, columns = column)
        roleName = pd.DataFrame(roleName, index = row, columns = column)
        memberCount = pd.DataFrame(memberCount, index = row, columns = column)
            
        #   Send embed message  
        #   Metadata
        self.embed.url = ''
        self.embed.set_image(url='')

        #   Prepare & send message
        self.embed.title = f'Role Overview for {ctx.guild}'
        self.embed.description = f'Counting **{len(ctx.guild.roles)} Roles'
        self.embed.add_field(name = 'Role ID', value = roleID, inline= True)
        self.embed.add_field(name = 'Role Name', value = roleName, inline= True)
        self.embed.add_field(name = 'Member Count', value = memberCount, inline= True)
        await ctx.send(embed = self.embed)

        #   Cleaning up the Code
        del roleID, roleName, memberCount

        return

    @command(name= 'ca', pass_context=True)
    async def ChannelAnalysis(self, ctx):

        row = []
        column = ['']
        categoryID = []
        channelName = []
        categoryName = []
        categoryType = []
        channelCount = []
        

        txt = 0
        voice = 0

        for i in ctx.guild.channels:

            try:

                if str(i.type) == 'category':
    
                    row.append('')
                    categoryID.append([i.id])
                    categoryName.append([i.name])
                    categoryType.append(str(i.type))

                match str(i.type):
                    case "voice": voice += 1
                    case "text": txt += 1

            except Forbidden as e : print(e)

        channelCount.append([f'{voice} Voice Channel'])
        channelCount.append([f'{txt} Text Channels'])

        #   Create DataFrame

        categoryID = pd.DataFrame(categoryID, index = row, columns= column)
        categoryName = pd.DataFrame(categoryName, index = row, columns= column)
        categoryType = pd.DataFrame(categoryType, index = row, columns= column)

        channelName = pd.DataFrame(channelName, index = i, columns = column)
        channelCount = pd.DataFrame(channelCount, index = ['',''], columns= column)
        #   Prepare & send embed message
        self.embed.title = 'Category Analysis'
        self.embed.add_field(name ='Category ID', value = categoryID)
        self.embed.add_field(name ='Category Name', value = categoryName)
        self.embed.add_field(name ='Category Type', value = categoryType)
        self.embed.add_field(name ='Channel Count', value = channelCount)

        await ctx.send(embed=self.embed)

        return

    @command(name='loga', pass_context = True)
    async def AuditLogAnalysis(self, ctx):

        #   Initializing a list
        row = ['']
        column = ['']
        totalEntries = []
        totalTargets = []
        totalModerators = []

        mod = 0
        target = 0
        action = 0

        try:

            async for entry in ctx.guild.aduit_logs(limit = 10):

                if entry.action: action +=1
                if entry.user: mod += 1
                if entry.target: target += 1

            totalEntries.append(action)
            totalModerators.append(mod)
            totalTargets.append(target)

        except Exception as e: await ctx.send('Can not access the audit log')

        else :
            totalEntries = pd.DataFrame(totalEntries, index = row, columns = column)

            #   Prepare & send embed
            self.embed.title = 'Audit log Analysis'
            self.embed.add_field(name = 'Total Audit logs', value = totalEntries)
        await ctx.send(embed = self.embed)

        return

    @command(name = 'bota', pass_context=True)
    async def BotInfo(self, ctx):

        if not hasattr(self.bot, 'appinfo'):self.bot.appinfo = await self.bot.application_info()

        #   If the bot is public
        if self.bot.appinfo.bot_public == True: bot = 'https://discord.com/api/oauth2/authorize?client_id=903619759587852338&permissions=2757671636208&scope=bot'
        else:

            #   Does the bot require a code?
            if self.bot.appinfo.bot_require_code_grant == True: bot ='Requires a Authorication'
            else: bot = 'Hidden'


        #   botInfo
        botInfo = [
                    bot,
                    self.bot.appinfo.terms_of_service_url,
                    self.bot.appinfo.privacy_policy_url,
                ]

        row = ['**Bot invitation** :', '**Terms of service** :', '** Privacy Policy** :',]
        column = ['']

        botInfo = pd.DataFrame(botInfo, index = row, columns = column)

        #   botStats Dataframe

        #   Fetch bot stats, Post counts, command counts
        botStats = [ len(self.bot.guilds), '?faq',
        ]

        row = ['**Watching** :', '**prefix**',]
        botStats = pd.DataFrame(botStats, index = row, columns = column)

        #   Prepare and send embed
        self.embed.title = f'Analysis of {self.bot.appinfo.name}'
        self.embed.url = 'https://discord.gg/BUXqG5m27a'
        self.embed.description = f'{self.bot.appinfo.description}'
        self.embed.set_thumbnail(url = f'{self.bot.appinfo.icon}')
        self.embed.set_author(name = f'{self.bot.appinfo.owner}', url = '', icon_url= '')
        self.embed.add_field(name = 'Genral Information', value = botInfo)
        self.embed.add_field(name = 'Bot Statics', value = botStats)


        await ctx.send(embed = self.embed)

        #   Clean up
        self.embed.url = ''
        self.embed.title = ''
        self.embed.description = ''
        self.embed.remove_thumbnail()
        self.embed.remove_author()
        self.embed.clear_fields()

        return
