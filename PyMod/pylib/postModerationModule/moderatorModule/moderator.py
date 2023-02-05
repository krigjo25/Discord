
#   Python Repositories
import datetime
import asyncio
import humanfriendly

#   Discord Repositories
from discord.utils import get
from discord import Guild, Member, utils
from discord.abc import GuildChannel
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, command
from discord.ext.commands.core import has_permissions
from pylib.postModerationModule.moderatorModule.rolePermissions import ModerationChecks
from pylib.dictionaries.systemmessages import Dictionaries


class ChannelModeration(Cog):

    '''
        Commands which requires permission such as
        manageChannels, manageThreads, manageMessages
    '''

    def __init__(self, bot):

        self.bot = bot
        self.warn = 0    
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%H:%M, %d.%b - %y')  
        self.embed = Embed(color=Colour.dark_purple(), description= '')

        return

    #   :x: Creating a channel
    @command(name="chcre")
    @has_permissions(manage_channels=True)
    async def CreateChannel(self, ctx, chName):

        # Declaring variables
        srv = ctx.guild
        #getRole = get(srv.roles, {role})
        ch = get(srv.channels, name=chName)
        chlog = get(srv.channels, name='moderationlog')

        #   Create a new channel
        #if not ch: await GeneralModeration.CheckChannel(ch)
        #else:self.embed.title = f'{ch} Already exists.'

        #   3:  prepare, send & Clean up embed
        self.embed.color = Colour.dark_red()
        self.embed.description=f''
        await chlog.send(embed=self.embed)

        self.embed.clear_fields()
        self.embed = Embed(color=Colour.dark_purple())

        return

    #   Delete a channel
    @command(name="chdel")
    @has_permissions(manage_channels=True)
    async def DeleteChannel(self, ctx, ch):

        '''
            #   1 Declare necsessary variables
            #   2 Delete the channel and prepare the embed
            #   3 Send & Clean up the embeded message
        '''

        #   Declaring variables
        srv = ctx.guild
        srvch = GuildChannel

        ch = get(srv.channels, name=ch)
        chlog = get(srv.channels, name='moderationlog')

        #   Checking wheter the channel exist or not

        if ch:

            self.embed.title = f'{ctx.author.name} has Deleted the {ch} channel.'
            ch = await srvch.delete(ch)
            

        else:
            self.embed.title = f'The Channel Does not exist'

        #   prepare, Send & Clean up embeded message
        self.embed.color = Colour.dark_red()
        self.embed.description=f''
        await chlog.send(embed=self.embed)

        self.embed.clear_fields()
        self.embed.color = Embed(color=Colour.dark_purple())

        return

class ManageModeration(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.warn = 0    
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%H:%M, %a, %d.%b - %y')  
        self.embed = Embed(color=Colour.dark_purple(), description= '')

        return

        #   General moderator commands

    #   Clearing all messages
    @command(name="cls")
    @has_permissions(manage_messages=True)
    async def ClearChat(self, ctx, ch, x):

        #   Initializing variables
        x = int(x)
        srv = ctx.guild
        ch = get(srv.channels, name=ch)
        purge = await ch.purge(limit=x)

        # Generate a log channel
        chlog = await ModerationChecks.CheckChannel(self, ctx, 'auditlog')
        await chlog.send(f'**{len(purge)}** lines purged, in **{ch}** by **{ctx.author.name}**')

        return

    #   Default Moderator comamnds
    @command(name='poll', pass_context= True)
    @has_permissions(manage_messages=True)
    async def polls(self, ctx, title, ch):

        """

            #   creating a poll with default two values to choose from
            #   Using reaction to vote
            #   Title of the poll, how many options and Questions

        """

        #   Initializing variables
        i = 1
        li = []
        srv = ctx.guild
        ch = get(srv.channels, name=f'{ch}')

        #   Creating a channel to log the warning 
        if not ch:
            ch = await ModerationChecks.CheckChannel(self, ctx, ch)

        #   Prepare, send and clean up
        self.embed.title = f'{title}:question:,'
        self.embed.description = 'Please type in how many opinions you\'d like:question:'

        await ctx.send(embed=self.embed)

        self.embed.clear_fields()

        def msgCheck(arg):

            author = ctx.author
            arg = str(arg.content)

            return author != self.bot.user and arg

        arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
        x = int(arg.content)

        # Creating the Options
        while i <= x:

            j = 0

            self.embed.description = f'Name your option NO {i}'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option = str(arg.content)

            li.append(option)
            self.embed.add_field(name= f'Option nr {i} ', value = li[j])

            j += 1
            i += 1

        # Prepare, send & clean up embed

        self.embed.title ='Summary'
        self.embed.description = f'Question : *{title}*\n **start** / **q**'
        await ctx.send(embed=self.embed)


        #   Retrieve the channel name & Check if it exists
        arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
        arg = str(arg.content)

        if arg != 'q':

            #   Issues to retrieve the channel name
            #ch = await ModerationChecks.CheckChannel(self, ctx, ch)

            #   Prepare, send & Clean up embed
            self.embed.title = f'{title}:question:'
            self.embed.description = f' Greetings fellas, its time for a poll, choose between \n {option}'

            message = await ctx.send(embed=self.embed)

            self.embed.clear_fields()

            while i > x:

                i = 0
                i += 1
            await message.add_reaction(Dictionaries.BotPoll(i))

        elif title == 'q' or arg == 'q':

            return await ctx.send('The poll has ended')

        return

    #   Checking wheter whom is offline and online
    @command(name='online', pass_context=True)
    @has_permissions(manage_messages=True)
    async def OnlineMembers(self, ctx, args=None):

        #   Retriving the server
        warn = ''
        off = True
        srv = ctx.guild

        bot = self.bot.user
        self.embed.title = 'Server Members'
        self.embed.description = 'List of members'

        if args == None:

            #   Fetching members
            for member in srv.members:

                #   Initializing  variables
                nick = str(member.nick)
                status = str(member.status)

                #   Add emoji to status
                if status == 'idle': status = ':dash:'
                elif status == 'offline': status = ':sleeping:'
                elif status == 'dnd': status = ':technologist:'
                if status == 'online': status = ':heart_on_fire:'

                #   Fetch user nick
                if nick == 'None': nick = ''
                else: nick = f'Nick : {member.nick}\n'

                if member.bot == False:

                    self.embed.add_field(name=f'{member.name} #{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {self.warn}', inline=False)

            await ctx.send(embed = self.embed)
            self.embed.clear_fields()

        if args != None:

            args = str(args).lower()

            if args == 'on':

                #   Fetching members
                for member in srv.members:

                    #   Initializing variables
                    status = str(member.status)
                    nick = str(member.nick)

                    #   Add emoji to status
                    if status == 'idle': status = ':dash:'
                    elif status == 'dnd': status = ':technologist:'
                    elif status == 'online': status = ':heart_on_fire:'
                    elif status == 'offline': status, off = ':sleeping:', False

                    #   Fetch user nick
                    if nick == 'None':nick = ''
                    else:nick = f'Nick : {member.nick}\n'
 
                    if off != False & member.bot == False:

                        self.embed.add_field(name=f'{member.name}, #{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {warn}', inline=False)

                await ctx.send(embed = self.embed)
                self.embed.clear_fields()

            elif args == 'off':

                #   Fetching members
                for member in srv.members:

                    status, nick = str(member.status), str(member.nick)

                    #   Add emoji to status
                    if status != 'offline': off = False
                    elif status == 'offline':status = ':sleeping:'

                    #   Fetch user nick
                    if nick == 'None':nick = ''
                    else:nick = f'Nick : {member.nick}\n'

                    if off != False & member.bot == False:
                        self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {warn}', inline=False)

                await ctx.send(embed = self.embed)
                self.embed.clear_fields()

    @command(name = 'bots', pass_context=True)
    @has_permissions(manage_messages=True)
    async def ServerBots(self, ctx, args=None):

        #   Initializing variables
        srv = ctx.guild

        self.embed.title = 'Server Bots'
        self.embed.description = 'List of members'

        if args == None:

            #   Fetching members
            for member in srv.members:

                #   Initializing  variables
                nick = str(member.nick)
                status = str(member.status)

                #   Add emoji to status
                if status == 'idle': status = ':dash:'
                elif status == 'offline': status = ':sleeping:'
                elif status == 'dnd': status = ':technologist:'
                if status == 'online': status = ':heart_on_fire:'

                #   Fetch user nick
                if nick == 'None': nick = ''
                else: nick = f'Nick : {member.nick}\n'

                if member.bot == True:

                    self.embed.add_field(name=f'{member.name} #{member.discriminator}',value=f'{nick}\n Status : {status}', inline=False)

            await ctx.send(embed = self.embed)
            self.embed.clear_fields()

class MemberModeration(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%a, %d.%b -%y')  
        self.embed = Embed(color=Colour.dark_purple(), description= '')

        return

    #  :x: Warn
    @command(name="warn")
    @has_permissions(manage_messages=True)
    async def UserWarn(self, ctx, member:Member, *, reason=None):

        #   Initializing variables
        srv = ctx.guild
        chlog= get(srv.channels, name='auditlog')

        #   Creating a channel to log the warning 
        if not ch:
            ch = await ModerationChecks.CheckChannel(self, ctx, 'auditlog')

        #   Counting warnings

        #   How to make sure only the user retrieve the warning?

        if reason == None or member == ctx.author:

            self.embed.title  = 'Warning not sent'
            self.embed.description = ' please provide a reason for the warn'

            if member == ctx.author:self.embed.description = 'Can not warn your self'

        else:


            message = f'Greetings **{member}**.\n You recieve this Notification, because you have been warned by **{ctx.author}**.\n\n Due to :\n *{reason}*\n\nPlease read and follow the suggested guidelines for behavior in our disocrd channel'
            await member.send(message)

            self.embed.title = f'**{member}** has been warned'
            self.embed.description = f' **Due to**\n *{reason}*.\n\n by\n**{ctx.author.name}**,\n{self.curTime}*'

        self.embed.color = Colour.dark_red()
        await chlog.send(embed=self.embed)
        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return

   #   Mute Members
    @command(name="sush")
    @has_permissions(moderate_members = True)
    async def SushMember(self, ctx, member:Member, time=None, *, reason=None):

        """

            #  1 Removing and set a new role to the player
            #  2 send the selected member a message
            #  3 Log the mute in a channel called moderation Log

        """

        #   Initializing variables
        srv = ctx.guild
        role = get(srv.roles, name ='Sushed')
        ch = get(srv.channels, name='auditlog')
        time = humanfriendly.parse_timespan(time)

        #   Creating log channel if not exist :x:
        if not role:

            if role == None:
                ch, role = await ModerationChecks.CheckRole(self, ctx, f'{role}')
                role = get(srv.roles, name =role)

        if reason == None or time > 604800:

            self.embed.description = f' Could not sush **{member}** due to there were no reason or time to shush'

            if time > 604800:self.embed.description = f' Could not sush **{member}** due to a limitation for 1w'

            #   Prepare, send & Clean up embed
            self.embed.color = Colour.dark_red()
            self.embed.title = 'An erro occurred'

            await ch.send(embed=self.embed)
            self.embed.clear_fields()
            self.embed.color = Colour.dark_purple()

        else:

            #   Prepare, send & Clean up embed
            self.embed.title = f' **{member}** has been sushed'
            self.embed.description = f'by **{ctx.author.name}** \n for {datetime.timedelta(seconds=time)}\nDue to\n**{reason}.**\n*{self.curTime}*'

            self.embed.color = Colour.dark_red()
            await ch.send(embed=self.embed)
            self.embed.clear_fields()
            self.embed.color = Colour.dark_purple()

            #   Set role, set timeout & send member DM

            await member.add_roles(role)
            await member.timeout(until = utils.utcnow() + datetime.timedelta(seconds=time), reason = reason)

            message = f'''Greetings, **{member}**.
            
            You recieve this message, because you have been sushed by **{ctx.author}**
            You are sushed for **{datetime.timedelta(seconds=time)}**.
            
            During this time you will not able to use {ctx.guild} channels.
            
            The reason for this intervention is
            *{reason}*'''
            await member.send(f'{message}')

        
            # Automatic un-mute & Notify the user
            await asyncio.sleep(time)
            await member.remove_roles(role)
            await member.send(f'Greetings **{member}**.\n\n Your sush, has been lifted you can now use {ctx.guild}')

        return

    @command(name="lift")
    @has_permissions(moderate_members = True)
    async def LiftSush(self, ctx, member:Member):

        """

            1   Checking if there is a role called 'Sushed'
            2   Checking if there is a log channel
            3   Removing the role and lift the sush
            4   send the selected member a message


        """

        srv = ctx.guild
        ch = get(srv.channels, name='auditlog')
        role = get(srv.roles, name ='@sushed')

        #await ModerationChecks.CheckRole(self, ctx, role)
        if not ch:
            ch = await ModerationChecks.CheckChannel(self, ctx, 'auditlog')

        #   Prepare, send and clean up embed
        self.embed.color = Colour.dark_red()
        self.title = f'the sush has been lifted for {member}'
        self.embed.description = f'by\n **{ctx.author.name }**\nDate:\n *{self.curTime}*'
        
        await ch.send(embed= self.embed)

        #   Removing role, timeout & Notify the user
        await member.remove_roles(role)
        await member.timeout(until=None, reason=None)
        await member.send(f'Greetings **{member}**.\n\n The sush has been lifted you can now use {ctx.guild}')

        return

    #   Kick Members
    #   Kick a user from the server :x:
    @command(name='kick')
    @has_permissions(kick_members= True)
    async def Kick(self, ctx, member:Member, *, reason=None):

        """


            1   Checking if there is a log channel
            2   Prepare & send messages
            3   Kick the member

        """
        #   Initializing variables
        srv = ctx.guild
        t = 'test Kick'
        ch = get(srv.channels, name='auditlog')

        #   Checking wheter there is a log channel :x:
        if not ch:
            ch = await ModerationChecks.CheckChannel(self, ctx, 'auditlog')


        if reason == None:
            self.embed.title = f'**{ctx.author.name}** Provide a reason to kick **{member.name}**'

        else:

            #   Prepare embed
            self.embed.title = f'**{member}** has been kicked from the server'
            self.embed.description = f' by\n**{ctx.author.name}**\n Due to\n*{reason}.*\n Date : *{self.curTime}*'

            # Creating a message to the user, send it to his DM, then kick
            message = f'Greetings **{member}**.\nYou recieve this message, because you have been kicked off **{ctx.guild.name}** by **{ctx.author}**.\n\nDue to :\n **{reason}**'
            await member.send(message)
            await member.kick(reason=reason)

        #   Send & Clean up embed
        self.embed.color = Colour.dark_red()
        await ch.send(embed=self.embed)

        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return

    @command(name = 'auditlog')# :x:
    @has_permissions(view_audit_log = True)
    async def ReadAuditlog(self, ctx, limit = 3):

        #   Initializing variables
        srv = ctx.guild
        t = 'test Kick'
        ch = get(srv.channels, name='auditlog')

        '''
            with open (f'audit_logs_{srv.name}') as f:
            async for entry in srv.audit_logs(limit=limit):
                f.write(f'{entry.user} did {entry.action} to{ entry.target} reason {entry.reason}')
        '''

        async for entry in Guild.audit_logs(limit = limit):
            self.embed.add_field(name = f'{entry.user} did {entry.action}', value = f'{entry.target} reason {entry.reason} ')
        
        self.embed.title = 'Audit logs'
        self.embed.description = 'Some snippets from the auditlog'
        await ctx.send(embed = self.embed)

        return