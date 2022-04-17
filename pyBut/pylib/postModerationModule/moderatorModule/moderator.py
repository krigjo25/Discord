
#   Python Repositories
import datetime
import asyncio

#   Discord Repositories
from discord import Member
from discord.utils import get
from discord import PermissionOverwrite
from discord.embeds import Embed, Colour
from discord.ext.commands.core import has_permissions
from discord.ext.commands import Cog, command, has_any_role

class Moderator(Cog, name='Moderator-module'):

    def __init__(self, bot):
        self.bot = bot
        self.warn = 0    
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%d.%m - %Y')  
        self.embed = Embed(color=Colour.dark_purple(), description= '')

        return

        #Creating a channel
    @command(name="crech")
    @has_permissions(manage_messages=True)
    async def CreateChannel(self, ctx, chName):

        # Declaring variables
        srv = ctx.guild
        role = get(srv.roles, 'Moderator')

        ch = get(srv.channels, name=chName)
        mlog = get(srv.channels, name='moderationlog')

        perms = {
                            role:PermissionOverwrite(read_messages_history = True),
                            srv.default_role:PermissionOverwrite(view_channels=False)          
}

        if not mlog:

            perms = PermissionOverwrite(read_messages=False)

            await srv.create_text_channel(f'{ch}', overwrites=perms)

            self.embed.title = 'Auto generated channel'
            self.embed.colour = Embed(color=Colour.dark_red())
            self.embed.description = 'This channel is used for every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'
            await ch.send(embed=self.embed)

        if not ch:
                
                await srv.create_text_channel(f'{chName}', overwrites=perms)
                self.embed.title = f'{ctx.authhor} has Created a new channel {ch}'

        else :
            self.embed.title = f'{ch} Already exists.'

        #   3:  Log the ban
        self.embed.description=f''
        await mlog.send(embed=self.embed)
        self.embed = Embed(color=Colour.dark_purple())

        # Clearing all messages
    @command(name="cls")
    @has_permissions(manage_messages=True)
    async def ClearChat(self, ctx, chName, x):

            x = int(x)
            srv = ctx.guild
            channel = get(srv.channels, name=chName)

            if x <= 10000:

                await channel.purge(limit=x)
                await ctx.send(f'Sir, i purged **{x}** lines, in **{channel}**')

            else:

                await ctx.send('Sir, the limit is 10000 lines')

    #   Kick a user from the server
    @command(name='kick')
    @has_permissions(kick_members= True)

    async def Kick(self, ctx, member:Member, *, reason=None):

        if reason == None:

            await ctx.send(f'Please provide me a reason to kick **{member}**')

        elif reason != None:

            srv = ctx.guild
            ch = get(srv.channels, name='moderationlog')

            if not ch:

                #   Creating channel permissions
                perms = PermissionOverwrite(read_messages=False)

                await srv.create_text_channel(f'{ch}', overwrites=perms)

                self.embed.color = color = Colour.dark_red()
                self.embed.title = 'Auto generated channel'
                self.embed.description = 'This channel is used for every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'
                await ch.send(embed=self.embed)
                self.embed.clear_fields()
                self.embed.color = color = Colour.dark_purple()

            self.embed.color = color = Colour.dark_red()
            self.embed.title = f'**{member}** has been kicked by **{ctx.author}**.'
            self.embed.description = '**{reason}.**\n Date : **{self.curTime}**'

            await ch.send(embed=self.embed)
            self.embed.clear_fields()
            self.embed.color = color = Colour.dark_purple()

            # Creating a message to the user, send it to his DM, then kick
            message = f'Greetings **{member}**.\nYou recieve this message, because you have been kicked off **{ctx.guild.name}** by **{ctx.author}**.\n\nDue to :\n **{reason}**'
            await member.send(message)
            await member.kick(reason=reason)

    @command(name='poll', pass_context= True)
    @has_permissions(manage_messages=True)

    async def polls(self, ctx):

        """

            #   creating a poll with default two values to choose from
            #   Using reaction to vote
            #   Title of the poll, how many options and Questions

        """

        one = '1️⃣'
        two = '2️⃣'
        three = '3️⃣'
        four = '4️⃣'
        five = '5️⃣'
    
        srv = ctx.guild

        #   Prepare & Send the embed
        self.embed.title = ''
        self.embed.description = 'Type in a question or type \"q\" to quit '
        await ctx.send(embed=self.embed)

        def msgCheck(arg):

            author = ctx.author
            arg = str(arg.content)

            return author != self.bot.user and arg

        arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
        quiz = str(arg.content)

        self.embed.title = f'{quiz}:question:,'
        self.embed.description = 'Thank you, please type in how many opinions you\'d like:question:'
        await ctx.send(embed=self.embed)

        arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
        x = int(arg.content)
        
        # Creating the Options
        if x == 2:

            #   First option
            self.embed.description = 'Name your first option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option = str(arg.content)

            #   Second option
            self.embed.description = 'Name your second option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option2 = str(arg.content)

            options = f':one:{option}\n:two: {option2}\n'
        
        elif x == 3:
            #   First option
            self.embed.description = 'Name your first option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option = str(arg.content)

            #   Second option
            self.embed.description = 'Name your second option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option2 = str(arg.content)

            #   Third option
            self.embed.description = 'Name your third option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option3 = str(arg.content)

            options = f':one:{option}\n:two: {option2}\n :three:{option3}'

        elif x == 4:
            #   First option
            self.embed.description = 'Name your first option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option = str(arg.content)

            #   Second option
            self.embed.description = 'Name your second option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option2 = str(arg.content)

            #   Third option
            self.embed.description = 'Name your third option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option3 = str(arg.content)
            
            #   Fourth option
            self.embed.description = 'Name your fourth option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option4 = str(arg.content)
            
            options = f':one:{option}\n:two: {option2}\n :three:{option3}\n :four:{option4}'

        elif x == 5:
            #   First option
            self.embed.description = 'Name your first option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option = str(arg.content)

            #   Second option
            self.embed.description = 'Name your second option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option2 = str(arg.content)

            #   Third option
            self.embed.description = 'Name your third option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option3 = str(arg.content)
            
            #   Fourth option
            self.embed.description = 'Name your fourth option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option4 = str(arg.content)
        
            #   fifth option
            self.embed.description = 'Name your fifth option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option5 = str(arg.content)
            
            options = f':one:{option}\n:two: {option2}\n :three:{option3}\n :four:{option4}\n :five:{option5}'
        
        # Summuary for the question
        self.embed.title ='Summary'
        self.embed.description = f'Question : {quiz}\n Options :\n {options}\nWhich channel should the poll go in?'
        await ctx.send(embed=self.embed)

        #   Retrieve the channel name
        arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
        ch = str(arg.content)

        channel= get(srv.channels, name=ch)

        if not channel:  
            await srv.create_text_channel(f'{ch}')

        self.embed.title = f'{quiz}:question:'
        self.embed.description = f' Greetings fellas, its time for a poll, choose between \n {options}'
        r = await channel.send(embed=self.embed)

                # Add following reaction to the message
        

        if x == 2:

            await r.add_reaction(one)
            await r.add_reaction(two)

        elif x==3:

            await r.add_reaction(one)
            await r.add_reaction(two)
            await r.add_reaction(three)

        elif x==4:

            await r.add_reaction(one)
            await r.add_reaction(two)
            await r.add_reaction(three)
            await r.add_reaction(four)

        elif x==5:

            await r.add_reaction(one)
            await r.add_reaction(two)
            await r.add_reaction(three)
            await r.add_reaction(four)
            await r.add_reaction(five)

        if quiz == 'q' or ch == 'q':
            return await ctx.send('The poll has ended')

#   Online members
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

                #   Declare variables
                status = str(member.status)
                nick = str(member.nick)

                #   Add emoji to status
                if status == 'online': status = ':heart_on_fire:'
                elif status == 'idle': status = ':dash:'
                elif status == 'dnd': status = ':technologist:'
                elif status == 'offline': status = ':sleeping:'

                #   Fetch user nick
                if nick == 'None': nick = ''
                else: nick = f'Nick : {member.nick}\n'

                if member != bot:

                    self.embed.add_field(name=f'{member.name} #{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {self.warn}', inline=False)

            await ctx.send(embed = self.embed)
            self.embed.clear_fields()

        if args != None:
            args = str(args).lower()

            if args == 'online':

                #   Fetching members
                for member in srv.members:

                    #   Declare variables
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
 
                    if off != False:

                        self.embed.add_field(name=f'{member.name}, #{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {warn}', inline=False)

                await ctx.send(embed = self.embed)
                self.embed.clear_fields()

            elif args == 'offline':

                #   Fetching members
                for member in srv.members:

                    status, nick = str(member.status), str(member.nick)

                    #   Add emoji to status
                    if status != 'offline': off = False
                    elif status == 'offline':status = ':sleeping:'

                    #   Fetch user nick
                    if nick == 'None':nick = ''
                    else:nick = f'Nick : {member.nick}\n'

                    if off != False:
                        self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {warn}', inline=False)

                await ctx.send(embed = self.embed)
                self.embed.clear_fields()

    #   Warn
    @command(name="warn")
    @has_permissions(manage_messages=True)
    async def UserWarn(self, ctx, member:Member, *, reason=None):

        srv = ctx.guild

        ch= get(srv.channels, name='moderationlog')
        self.embed = Embed(color=Colour.dark_red(), description= '')

        #   Counting warnings
        #   How to make sure only the user retrieve the warning?

        if reason == None:

            self.embed.title  = 'Warning not sent'
            self.embed.description = ' please provide a reason for the warn'

        elif member == ctx.author:

            self.embed.title = 'An error occoured'
            self.embed.description = 'Can not warn your self'

        else:

            #   Creating a channel to log the warning 
            if not ch:

                #   Channel Permissions
                perm = PermissionOverwrite()
                perm.send_messages = False
                perm.read_messages = False
                perm.read_message_history = True

                #   Creating the channel
                await srv.create_text_channel(f'{ch.name}', overwrite=perm)
                self.embed.title = 'Auto generated channel'
                self.embed.description = 'This channel is used for every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'
                self.embed.add_field(name= f'**{member}** has been warned by **{ctx.author}** for **{reason}**', value='.')
                await ch.send(embed=self.embed)

            message = f'Greetings **{member}**.\n You recieve this Notification, because you have been warned by **{ctx.author}**,  \n\n Due to :\n **{reason}**\n\nPlease read and follow the suggested guidelines for behavior in our disocrd channel'
            await member.send(message)

            self.embed.title = f'**{member}** has been warned by **{ctx.author}** for **{reason}.** Date : **{self.curTime}**'
            self.embed.description = ''

        await ch.send(embed=self.embed)
        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return

    @command(name="sush")
    @has_permissions(mute_members = True)
    async def TimeSnozze(self, ctx, member:Member, sec, *, reason=None):

        """

            #  1 Removing and set a new role to the player
            #  2 send the selected member a message
            #  3 Log the mute in a channel called moderation Log

        """

        #   Initializing variables
        sec = int(sec)
        srv = ctx.guild

        ch = get(srv.channels, name='moderationlog')
        sushedRole = get(srv.roles, name ='@sushed')
        memberRole = get(srv.roles, name ='@Members')

        if not ch:

                #   Creating channel permissions
                perms = PermissionOverwrite(read_messages=False)

                await srv.create_text_channel(f'{ch}', overwrites=perms)

                #   Prepare & Send the embed
                self.embed.color = Colour.dark_red()
                self.embed.title = 'Auto generated channel'
                self.embed.description = 'This channel is used for every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'
                await ch.send(embed=self.embed)
                self.embed.clear_fields()
                self.embed.color = Colour.dark_purple()

        if not sushedRole:

                perm = PermissionOverwrite (speak=False, send_messages=False, read_message_history=False, read_messages=False)
                await srv.create_role(name='@sushed', permissions = perm, reason = 'Automatic Role assignment')

        if reason == None:

            self.embed.title = 'An erro occurred'
            self.description = f'Provide me a reason to mute **{member}** for **{sec}** sec'

        elif reason != None:

            await member.add_roles(sushedRole)
            await member.remove_roles(memberRole)

            await member.send(f'Greetings **{member}**.\n\n You recieve this message, bedcause you have been sushed by **{ctx.author}** \n You are sushed for **{sec}** seconds.\n During this time you will not able to chat in our channels, add reactions or be able to use voice channel. \n\n The reason for this intervention is **{reason}**')

            self.embed.color = Colour.dark_red()
            self.embed.title = f' **{member}** has been sushed by **{ctx.author}**, for {sec} sec Due to  **{reason}.** Date : **{self.curTime}**'
            self.embed.description = ''
            await ch.send(embed=self.embed)
            self.embed.clear_fields()
            self.embed.color = Colour.dark_purple()

            # Automatic un-mute
            await asyncio.sleep(sec)

            await member.remove_roles(sushedRole)
            await member.add_roles(memberRole)

            #   send the selected member a message
            await member.send(f'Greetings **{member}**.\n\n You recieve this message, bedcause you have been shushed by **{ctx.author}** \n The Shush has been lifted')

        return
