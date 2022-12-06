#  Repositories
import pandas as pd


#   Discord Repositories
from discord.embeds import Embed
from discord import Forbidden
from discord.ext.commands import command, Cog

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

    @command(name = 'sa', pass_context = True)
    async def DiscordServerInformation(self, ctx):

        #   Initializing variables

        try:

            #   Initializing variables
            srv = ctx.guild
            banned = len([i async for i in srv.bans(limit=None)])

            #   Creating a Dataframe
            overview = [srv.name, srv.id, f'{srv.owner},', srv.created_at.date(), '  ', len(srv.roles), len(srv.premium_subscribers),  banned, srv.member_count, len(srv.channels), len(srv.scheduled_events)]
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

            self.embed.clear_fields()
            self.embed.description = ''

            return

    @command(name='ra', pass_context = True)
    async def RoleAnalyzer(self, ctx):

        #   Initializing variables
        string = ''
        srv = ctx.guild
        count = len(srv.roles)
       
        #    Creating a DataFrame
        row = []
        column = ['']

        roleID = []
        roleName = []
        memberCount = []

        #   Extracting role infomration
        for i in await srv.fetch_roles():

            #   Fetch roles roles
            j = srv.get_role(i.id)

            rolename = [i.mention]
            roleid = [i.id]

            #   Appending to the dataframe
            row.append('')
            roleID.append(roleid)
            roleName.append(rolename)
            memberCount.append(len(j.members))

            #   Cleaning up
            del roleid 
            del rolename
  
        roleID = pd.DataFrame(roleID, index = row, columns = column)
        roleName = pd.DataFrame(roleName, index = row, columns = column)
        memberCount = pd.DataFrame(memberCount, index = row, columns = column)
            
        #   Send embed message  
        #   Metadata
        self.embed.url = ''
        self.embed.set_image(url='')

        #   Prepare & send message
        self.embed.title = f'Role Overview for {srv}'
        self.embed.description = f'Counting **{count} Roles'
        self.embed.add_field(name = 'Role ID', value = roleID, inline= True)
        self.embed.add_field(name = 'Role Name', value = roleName, inline= True)
        self.embed.add_field(name = 'Member Count', value = memberCount, inline= True)
        await ctx.send(embed = self.embed)

        #   Cleaning up the Code
        del roleID
        del roleName
        del memberCount

        self.embed.clear_fields()
        self.embed.description = ''



        return

    @command(name= 'ca', pass_context=True)
    async def ChannelAnalysis(self, ctx):

        categoryID = []
        categoryName = []
        categoryType = []
        channelCount = []

        channelName = []

        txt = 0
        voice = 0
        for i in ctx.guild.channels:

            try:

                if str(i.type) == 'category':
    
                    cid = [i.id]
                    cname = [i.name]
                    ctype = [str(i.type)]

                    categoryID.append(cid)
                    categoryName.append(cname)
                    categoryType.append(ctype)

                if str(i.type) =='voice':voice += 1
                elif str(i.type) == 'text':txt += 1

            except Forbidden as e : print(e)

        txt = [f'{txt} Text Channels']
        voice = [f'{voice} Voice Channel']

        channelCount.append(voice)
        channelCount.append(txt)

        #   Create DataFrame
        column = ['']
        row = []


        for i in range(len(categoryID)):
            row.append('')

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

        self.embed.clear_fields()

    @command(name='loga', pass_context = True)
    async def AuditLogAnalysis(self, ctx):
        
        srv = ctx.guild

        #   Initializing a list
        totalEntries = []
        totalTargets = []
        totalModerators = []

        try:
            mod = 0
            target = 0
            action = 0
            
            async for entry in srv.aduit_logs(limit = 10):

                if entry.action: action +=1
                if entry.user: mod += 1
                if entry.target: target += 1

            totalEntries.append(action)
            totalModerators.append(mod)
            totalTargets.append(target)

        except Exception as e:
            print(e)
            await ctx.send('Can not accsess the audit log')

        #   Creating the dataframes

        #   Total entries
        row = ['']
        column = ['']
        totalEntries = pd.DataFrame(totalEntries, index = row, columns = column)

        #   Prepare & send embed
        self.embed.title = 'Audit log Analysis'
        self.embed.add_field(name = 'Total Audit logs', value = totalEntries)
        return

    @command(name = 'bota', pass_context=True)
    async def BotInfo(self, ctx):

        if not hasattr(self.bot, 'appinfo'):self.bot.appinfo = await self.bot.application_info()

        #   If the bot is public
        if self.bot.appinfo.bot_public == True: bot = 'https://discord.com/api/oauth2/authorize?client_id=903619759587852338&permissions=2757671636208&scope=bot'
        else:
            #   Does the bot require a code?
            if self.bot.appinfo.bot_require_code_grant == True: bot ='Requires a code'
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
