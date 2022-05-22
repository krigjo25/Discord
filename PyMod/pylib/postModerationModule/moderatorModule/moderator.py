
#   Python Repositories
import datetime
import asyncio


#   Discord Repositories
from discord import Message
from discord.utils import get
from discord.colour import Color
from discord.abc import GuildChannel
from discord import PermissionOverwrite
from discord.embeds import Embed, Colour
from discord import Member, Permissions, utils
from discord.ext.commands.core import has_permissions

from discord.ext.commands import Cog, command, has_any_role
import humanfriendly

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

    
    #   Clearing all messages
    @command(name="cls")
    @has_permissions(manage_messages=True)
    async def ClearChat(self, ctx, ch, x):

        #   Declare variables
        x = int(x)
        srv = ctx.guild
        ch = get(srv.channels, name=ch)
        chlog = get(srv.channels, name = 'moderationlog')

        # Generate a log channel
        #await GeneralModeration.CheckChannel()
        purge = await ch.purge(limit=x)
        print(chlog)
        await chlog.send(f'**{len(purge)}** lines purged, in **{ch}** by **{ctx.author.name}**')

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

class GeneralModeration(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.warn = 0    
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%H:%M, %a, %d.%b - %y')  
        self.embed = Embed(color=Colour.dark_purple(), description= '')

        return

        #   General moderator commands

    #  :x: Warn
    @command(name="warn")
    @has_permissions(manage_messages=True)
    async def UserWarn(self, ctx, member:Member, *, reason=None):

        #   Creating a channel to log the warning 
        #await GeneralModeration.CheckChannel()

        #   Initializing variables
        srv = ctx.guild
        chlog= get(srv.channels, name='moderationlog')


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
        ch = utils.get(srv.channels, name=f'{ch}')

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

#   #   Checking wheter whom is offline and online
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

            if args == 'on':

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

                    if off != False:
                        self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {warn}', inline=False)

                await ctx.send(embed = self.embed)
                self.embed.clear_fields()
   
class MemberModeration(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.warn = 0    
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%a, %d.%b -%y')  
        self.embed = Embed(color=Colour.dark_purple(), description= '')

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
        role = get(srv.roles, name ='@sushed')
        time = humanfriendly.parse_timespan(time)
        chlog = get(srv.channels, name='moderationlog')

        #   Creating log channel if not exist :x:
        #await ModerationChecks.CheckRole(self, ctx, f'{role}')
        #await ModerationChecks.CheckChannel(self, ctx, f'{chlog}')

        if reason == None or time > 604800:

            self.embed.description = f' Could not sush **{member}** due to there were no reason or time to shush'

            if time > 604800:self.embed.description = f' Could not sush **{member}** due to a limitation for 1w'

            #   Prepare, send & Clean up embed
            self.embed.color = Colour.dark_red()
            self.embed.title = 'An erro occurred'

            await chlog.send(embed=self.embed)
            self.embed.clear_fields()
            self.embed.color = Colour.dark_purple()

        else:

            #   Prepare, send & Clean up embed
            self.embed.title = f' **{member}** has been sushed'
            self.embed.description = f'by **{ctx.author.name}** \n for {datetime.timedelta(seconds=time)}\nDue to\n**{reason}.**\n*{self.curTime}*'

            self.embed.color = Colour.dark_red()
            await chlog.send(embed=self.embed)
            self.embed.clear_fields()
            self.embed.color = Colour.dark_purple()

            #   Set role, set timeout & send member DM
            await member.add_roles(role)
            await member.timeout(until = utils.utcnow() + datetime.timedelta(seconds=time), reason = reason)
            await member.send(f'Greetings, **{member}**.\n\n You recieve this message, because you have been sushed by **{ctx.author}** \n You are sushed for **{datetime.timedelta(seconds=time)}**.\n\n During this time you will not able to use {ctx.guild} channels.\n\nThe reason for this intervention is\n*{reason}*')

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
        chlog = get(srv.channels, name='moderationlog')
        role = get(srv.roles, name ='@sushed')

        await RoleModeration.CheckRole(self, ctx, role)
        #await GeneralModeration.CheckChannel(self, ctx)

        #   Prepare, send and clean up embed
        self.embed.color = Colour.dark_red()
        self.title = f'the sush has been lifted for {member}'
        self.embed.description = f'by\n **{ctx.author.name }**\nDate:\n *{self.curTime}*'
        
        await chlog.send(embed= self.embed)

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
        chlog = get(srv.channels, name='moderationlog')

        #   Checking wheter there is a log channel :x:
        #ch = await GeneralModeration.CheckChannel(self, ctx, False)

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
        await chlog.send(embed=self.embed)

        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return

class RoleModeration(Cog):

    """
        Commands which requires manage_roles

    """

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    #   Role Management
    #   Create role
    @command(name='crero')
    @has_permissions(manage_roles = True)
    async def CreateRole(self, ctx, role, *, reason= None):

        """

            #   1   Create the role if not exist, if it exist send out a warning message
            #   2   Choose the permission of the role
            #   3   Choose the colour of the role with hexdecimals

        """

        #   Initializing classes
        manager = RolePermissions

        srv = ctx.guild
        findRole = get(srv.roles, name = f'{role}')

        if not findRole:

            #   Prepare,?liro Send & Clean up
            self.embed.title = f'Starting the process to create @{role}'
            self.embed.description = f'Would you like to create @{role} with **Basic** / **Moderation**/ **Custom** permissions? type **x** to exit '

            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            #   Waiting for response
            response = await self.bot.wait_for('message', timeout=30)
            answer = str(response.content).lower().replace(" ", "")
            print(answer)

            #   Checking respons issues 

            #if answer == 'basic':perms = manager.BasicPermissions( role)
            if answer =='admin':perms = manager.Administrator(role)
            #elif answer == 'custom':perms = manager.CustomPermissions(role)
            #elif answer == 'moderatorlvl1':perms = manager.Moderationlvl1(role)
            #elif answer == 'moderatorlvl2':perms = manager.Moderationlvl2(role)
            #elif answer == 'moderatorlvl3':perms = manager.Moderationlvl3(role)

            self.embed.title = f'the role, @{role} has been succsessfully created with {answer} previliges'
            await srv.create_role(name=f'{role}', permissions = perms, reason = f'{reason}')

        else:

            self.embed.title = f'{role} exists ?liro'

        #   Prepare, send, clean up & role creation
        self.embed.description = f''
        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        return

    #   Delete Role
    @command(name='dero') # :X
    @has_permissions(manage_roles = True)
    async def DeleteRole(self, ctx, *, role ):

        """
            1   Checking if there is any channels called 'moderationlog'
            2   Ask the user for comfirmation before removing the role

        """

        #   Creating log channel if not exist
        #await GeneralModeration.CheckChannel(self, ctx)

        #   Initializing variables
        srv = ctx.guild
        role = get(srv.roles, name=f'{role}')
        chlog = get(srv.channels, name='moderationlog')

        #   Prepare, send & clean up the embed message
        self.embed.title = f'Removing {role} role'
        self.embed.description = f'Do you want to remove the role?'

        await ctx.send(embed=self.embed)

        self.embed.clear_fields()

        #   Confirm the action
        confirmation = await self.bot.wait_for('message', timeout=60.0)
        confirmation = str(confirmation.content)

        if confirmation == 'yes' or confirmation == 'ye' or confirmation == 'y':

            #   Prepare the embed message and delete & role
            self.embed.title = f'{role} role, has been removed from the server'

            await role.delete()

        else:

            #   Prepare the embed message
            self.embed.title = f'Role removal canceled'

        #   Send & clean up the embed message
        self.embed.color = Colour.dark_red()
        self.embed.description = ''
        await chlog.send(embed=self.embed)

        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return
 
    #   Remove role 
    @command(name='remro')
    @has_permissions(manage_roles = True)
    async def RemoveMemberRole(self, ctx, *, member:Member, role, reason=None ):

        """
            1   Checking if there is any channels called 'moderationlog'
            2   When the command is invoked, ask the user for a confirmation
            3   Remove the user from the role

        """

        #   Creating log channel if not exist
        #await GeneralModeration.CheckChannel(self, ctx)

        #   Initializing variables
        srv = ctx.guild
        mRole = get(srv.roles, name=f'{role}')
        chlog = get(srv.channels, name='moderationlog')

        #   Prepare, Send & Clean up embed
        self.embed.color = Colour.dark_red()
        self.embed.title = f'removing {member} from {role}'
        self.embed.description = f'Are you sure you\'d like to remove {member} from {role}?'

        await chlog.send(embed=self.embed)

        #   Clean up
        self.embed.clear_fields()
        self.embed.color = Color.dark_purple()

        #   Retrieve the confirmation from the user
        confirm = await self.bot.wait_for('message')
        confirm = str(confirm.content).lower()

        if confirm == 'yes':

            #  Prepare the emebed message & Remove member
            self.embed.color = Color.dark_red()
            self.embed.title = f'{member} has been removed from {role} by {ctx.author} due to {reason} '

            member.remove_roles(member, mRole)

        else:

            #   Prepare the emebed message
            self.embed = Embed(color=Color.dark_red())
            self.embed.title = f'Role removal has been cancelled'

        self.embed.description=''
        await chlog.send(embed=self.embed)

        #   Clean up the embed message
        self.embed.clear_fields()
        self.embed.color = Color.dark_purple()

        return

class RolePermissions(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    async def BasicPermissions(self, ctx, role):

        perms = {

            role:Permissions(
                                ban_members = False, 
                                manage_guild = False, 
                                manage_roles = False, 
                                move_members = False,
                                mute_members = False,
                                manage_emojis = False,
                                view_audit_log = False,
                                deafen_members = False,
                                manage_webhooks = False,
                                manage_messages = False,
                                manage_channels = False,
                                change_nickname = False,
                                priority_speaker = False,
                                manage_nicknames = False,
                                view_guild_insights = False,
                                create_instant_invite = False,)
                }

        return perms

    async def Moderationlvl1(self, ctx, role):

        perms = {
            role:Permissions(
                                ban_members = False, 
                                manage_guild = False, 
                                manage_roles = False, 
                                move_members = False,
                                mute_members = False,
                                manage_emojis = False,
                                view_audit_log = False,
                                deafen_members = False,
                                manage_webhooks = False,
                                manage_messages = False,
                                manage_channels = False,
                                change_nickname = False,
                                priority_speaker = False,
                                manage_nicknames = False,
                                view_guild_insights = False,
                                create_instant_invite = False,)
                }

        return perms

    async def Moderationlvl2(self, ctx, role):

        perms = {
            role:Permissions(
                                ban_members = False, 
                                manage_guild = False, 
                                manage_roles = False, 
                                move_members = False,
                                mute_members = False,
                                manage_emojis = False,
                                view_audit_log = False,
                                deafen_members = False,
                                manage_webhooks = False,
                                manage_messages = False,
                                manage_channels = False,
                                change_nickname = False,
                                priority_speaker = False,
                                manage_nicknames = False,
                                view_guild_insights = False,
                                create_instant_invite = False,)
                }

        return perms

    async def Moderationlvl3(self, role):

        perms = {
            role:Permissions(
                                ban_members = False, 
                                manage_guild = False, 
                                manage_roles = False, 
                                move_members = False,
                                mute_members = False,
                                manage_emojis = False,
                                view_audit_log = False,
                                deafen_members = False,
                                manage_webhooks = False,
                                manage_messages = False,
                                manage_channels = False,
                                change_nickname = False,
                                priority_speaker = False,
                                manage_nicknames = False,
                                view_guild_insights = False,
                                create_instant_invite = False,)
                }

        return perms

    async def Administrator(self, role):
        print('test')
        perms = {
            role:Permissions(
                                administrator = True)
                }

        return perms

    async def CustomPermissions(self, ctx, roleName):

        #   1   Set a player's role
        sec = 60.0
        
        self.embed.title = f'Set the permissions for {roleName} '
        self.embed.description = 'Would you like to set the role\'s permissions?\n'
        await ctx.send(embed=self.embed)

        rolePerm = await self.bot.wait_for('message', timeout=sec)
        rolePerm = str(rolePerm.content).lower()

        self.embed.title = f' {roleName}\'s permissions'
        self.embed.description = 'Please type in Moderator Role, Administrator Role or User Role '
        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        role = await self.bot.wait_for('message', timeout=sec)
        role = str(voice.content).lower().replace(" ", "")

        if role == 'administratorrole':

            """
                administrator = admin,
                ban_members = bm,
                mention_everyone = me,
                kick_members    = km
                manage_channels = mc,
                manage_emojis = me,
                manage_guild 
                manage_messages
                manage_nicknames
                manage_permissions
                manage_roles
                manage_webhooks
                change_nickname
                create_instant_invite
                move_members
                mute_members
                deafen_members = dm
                priority_speaker
                view_audit_log = val,
                view_guild_insights = vgi,
                manage_permissions = mp
            """

            #   Administrator Permissions
            self.embed.add_field(name='Administrator permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            ar = await self.bot.wait_for('message', timeout=sec)
            ar = ar.content

            if ar == True:

                perm = Permissions(administrator = ar)

                return perm
    
            #   Ban Members Permissions
            self.embed.add_field(name='Ban Members permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            bm = await self.bot.wait_for('message', timeout=sec)
            bm = str(bm.content)

            #   Manage Channels Permissions
            self.embed.add_field(name='Manage Channels permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mc = await self.bot.wait_for('message', timeout=sec)
            mc = str(mc.content)

            #   Manage Emoji Permissions
            self.embed.add_field(name='Manage Emoji permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            me = await self.bot.wait_for('message', timeout=sec)
            me = str(me.content)

            #   Manage Channels Permissions
            self.embed.add_field(name='Manage Guild permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mg = await self.bot.wait_for('message', timeout=sec)
            mg = str(mg.content)

            #   Manage Channels Permissions
            self.embed.add_field(name='Manage Message permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mm = await self.bot.wait_for('message', timeout=sec)
            mm = str(mm.content)

            #   Manage Nickname Permissions
            self.embed.add_field(name='Manage Nickname permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mn = await self.bot.wait_for('message', timeout=sec)
            mn = str(mn.content)

            #   Manage Roles Permissions
            self.embed.add_field(name='Manage Roles permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mr = await self.bot.wait_for('message', timeout=sec)
            mr = str(mr.content)

            #   Manage Webhooks Permissions
            self.embed.add_field(name='Manage Webhooks permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mw = await self.bot.wait_for('message', timeout=sec)
            mw = str(mw.content)

            #   Change Nickname Permissions
            self.embed.add_field(name='Change NickName permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            cn = await self.bot.wait_for('message', timeout=sec)
            cn = str(cn.content)

            #   Create Instant Invite Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            cii = await self.bot.wait_for('message', timeout=sec)
            cii = str(cii.content)

            #   Move member Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            move = await self.bot.wait_for('message', timeout=sec)
            move = str(move.content)

            #   Mute Members Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            mute = await self.bot.wait_for('message', timeout=sec)
            mute = str(mute.content)

            #   Deafen members Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            dm = await self.bot.wait_for('message', timeout=sec)
            dm = str(dm.content)

            #   Priority Speaker Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            ps = await self.bot.wait_for('message', timeout=sec)
            ps = str(ps.content)

            #   View Audit log Permissions
            self.embed.add_field(name='View Audit log Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            val = await self.bot.wait_for('message', timeout=sec)
            val = str(val.content)

            #   View guild insights Permissions
            self.embed.add_field(name='View guild insights Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            vgi = await self.bot.wait_for('message', timeout=sec)
            vgi = str(vgi.content)

            perm = Permissions(ban_members=bm, manage_channels = mc, manage_emojis = me, manage_guild = mg, manage_messages = mm,  manage_nicknames = mn, manage_roles = mr, manage_webhooks = mw, change_nickname = cn, create_instant_invite = cii, move_members = move, mute_members = mute, deafen_members = dm, priority_speaker = ps, view_audit_log = val, view_guild_insights = vgi)

        elif role == 'moderatorrole':

            """

                manage_channels, manage_emojis, manage_guild, 
                manage_messages, manage_nicknames, manage_permissions, 
                manage_roles, manage_webhooks, change_nickname, create_instant_invite, 
                move_members, mute_members, deafen_members, priority_speaker, view_audit_log, view_guild_insights,

            """

            #   Kick Members Permissions
            self.embed.add_field(name='Kick Members permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            km = await self.bot.wait_for('message', timeout=sec)
            km = str(rmh.content)

            #   Manage Channels Permissions
            self.embed.add_field(name='Manage Channels permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mc = await self.bot.wait_for('message', timeout=sec)
            mc = str(mc.content)

            #   Manage Emoji Permissions
            self.embed.add_field(name='Manage Emoji permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            me = await self.bot.wait_for('message', timeout=sec)
            me = str(me.content)

            #   Manage Guild Permissions
            self.embed.add_field(name='Manage Guild permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mg = await self.bot.wait_for('message', timeout=sec)
            mg = str(mg.content)

            #   Manage Message Permissions
            self.embed.add_field(name='Manage Message permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mm = await self.bot.wait_for('message', timeout=sec)
            mm = str(mm.content)

            #   Manage Nickname Permissions
            self.embed.add_field(name='Manage Nickname permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mn = await self.bot.wait_for('message', timeout=sec)
            mn = str(mn.content)

            #   Manage Roles Permissions
            self.embed.add_field(name='Manage Roles permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mr = await self.bot.wait_for('message', timeout=sec)
            mr = str(mr.content)

            #   Manage Webhooks Permissions
            self.embed.add_field(name='Manage Webhooks permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mw = await self.bot.wait_for('message', timeout=sec)
            mw = str(mw.content)

            #   Change Nickname Permissions
            self.embed.add_field(name='Change NickName permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            cn = await self.bot.wait_for('message', timeout=sec)
            cn = str(cn.content)

            #   Create Instant Invite Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            cii = await self.bot.wait_for('message', timeout=sec)
            cii = str(cii.content)

            #   Move member Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            move = await self.bot.wait_for('message', timeout=sec)
            move = str(move.content)

            #   Mute Members Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            mute = await self.bot.wait_for('message', timeout=sec)
            mute = str(mute.content)

            #   Deafen members Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            dm = await self.bot.wait_for('message', timeout=sec)
            dm = str(dm.content)

            #   Priority Speaker Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            ps = await self.bot.wait_for('message', timeout=sec)
            ps = str(ps.content)

            perm = Permissions( kick_members=km, manage_channels = mc, manage_emojis = me, manage_guild = mg, manage_messages = mm, manage_nicknames = mn, manage_roles = mr,manage_webhooks = mw, change_nickname = cn, create_instant_invite = cii, move_members = move, mute_members = mute, deafen_members = dm, priority_speaker = ps )

        elif role == 'userrole':

            """ 
                #   Voice channels
                speak, request_to_speak, connect, stream

                #   Text Channels
                send_messages, read_message_history / view_channels, send_tts_messages,

                #   Misc
                add_reactions, attach_files,  embed_links, external_emojis, 
                use_slash_commands, use_voice_activation, value

            """

            #   Voice permissions
            self.embed.description = f'You selected {role} permissions'
            self.embed.add_field(name='Connect and speak in voice chat', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            conn = await self.bot.wait_for('message', timeout=sec)
            conn = str(conn.content)

            if conn == True:

                voice = True


            self.embed.add_field(name='Send Stream in voice channel', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            media= await self.bot.wait_for('message', timeout=sec)
            media= str(media.content)

            #   Send Messages permissions
            self.embed.add_field(name='Send Messages permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            msg = await self.bot.wait_for('message', timeout=sec)
            msg = str(msg.content)

            self.embed.add_field(name='Read entire history permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            rmh = await self.bot.wait_for('message', timeout=sec)
            rmh = str(rmh.content)

            perm = Permissions(
                                speak = voice,
                                stream = media,
                                connect = conn,
                                send_messages=msg,
                                read_message_history=rmh,)

        else:

            perm = ''
            self.embed.title = f'Procsess canceled'

            await ctx.send(embed=self.embed)

        return perm

class ModerationChecks(Cog):

    def __init__(self, bot):

        self.bot = bot

        self.curTime = self.now.strftime('%H:%M, %d.%b - %y')  
        self.embed = Embed(color=Colour.dark_purple(), description= '')

    async def CheckChannel(self, ctx, arg=None):

        t = 'Check Channel test'
        srv = ctx.guild
        ch = utils.get(srv.channels, name = f'{arg}')
        chlog = utils.get(srv.channels, name='moderationlog')
        '''
        if ch != None & ch != chlog:

            if not ch:

                perms = {
                            srv.default_role:PermissionOverwrite(view_channel=False)
                }

                self.embed.color = Colour.dark_red()
                ch = await srv.create_text_channel(f'{arg[0]}', overwrites=perms)
                self.embed.title = f'{ctx.author.name} has Created a new channel called {ch}'

        elif not chlog:

            perms = { 
                        srv.default_role:PermissionOverwrite(
                                                                    view_channel=False
                                                                )
                    }

            chlog = await srv.create_text_channel('moderationLog', overwrites=perms)

            #   3:  Prepare, send & clean up the embed message
            self.embed.color = Colour.dark_red()
            self.embed.title = 'Auto generated channel'
            self.embed.description = 'This channel is used to log every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'

        else:
            pass

        await chlog.send(embed=self.embed)

        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()
        print(t)
        '''
        return

    async def CheckRole(self, ctx, role, *, reason=None):

        #   Initializing variables
        srv = ctx.guild
        role = get(srv.roles, name=f'{role}')

        #   Pre-role assignment
        if role != '@sushed':

            perms = {

                        role:PermissionOverwrite(
                                                    read_message_history=False
                                            )          
                    }

            await srv.create_role(name=f'{role}', permissions = perms, reason = 'Automatic Role assignment')
            self.embed.title = 'Auto generated role'
            self.embed.description = '@Sushed is an automatically generated to mark muted members'

        else:
            pass

        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        return self.embed
 