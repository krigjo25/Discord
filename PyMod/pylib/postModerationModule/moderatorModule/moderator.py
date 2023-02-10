
#   Python Repositories
import datetime
import asyncio
import humanfriendly as hf

#   Discord Repositories
import discord as d
from discord.utils import get
from discord import utils, PermissionOverwrite, Permissions

from discord.abc import GuildChannel
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, command, before_invoke, group, after_invoke
from discord.ext.commands.core import has_permissions
from pylib.dictionaries.systemmessages import Dictionaries

class InvokeBefore(): pass
class ModerationChecks(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.now= datetime.datetime.strftime('%H:%M, %d.%b - %y')  
        self.embed = Embed(color=Colour.dark_purple(), description= '')

class messagesModeration(Cog):

    @group(pass_contex = True)
    @has_permissions(manage_channels = True)
    async def msg(self, ctx): pass

    @msg.command()
    async def polls(self, ctx, title, ch):

        """

            #   Creating a poll with default two values to choose from
            #   Using reaction to vote
            #   Title of the poll, how many options and Questions

        """

        pass

    #   Checking wheter whom is offline and online
    @msg.command()
    async def OnlineMembers(self, ctx, args=None):

        #   Retriving the server
        warn = ''
        off = True
        srv = ctx.guild

        bot = self.bot.user
        self.embed.title = 'Server Members'
        self.embed.description = 'List of members'

        try: pass
        except Exception as e : pass
        else :
            
            if args == None:

                #   Fetching members
                for member in ctx.guild.members:

                    #   Add emoji to status
                    match str(member.status):

                        case "dnd": status = ":technologist:"
                        case "idle": status = ":dash:"
                        case "online": status = ":heart_on_fire:"
                        case "offline": status = ":sleeping:"

                    #   Fetch user nick
                    if member.nick == None: nick = ''
                    else: nick = f'Nick : {member.nick}\n'

                    if member.bot == False: self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {self.warn}', inline=False)

            else:

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
                        elif status == 'offline': status, off = False

                        #   Fetch user nick
                        if nick == 'None':nick = ''
                        else:nick = f'Nick : {member.nick}\n'
    
                        if off != False & member.bot == False: self.embed.add_field(name=f'{member.name}, #{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {warn}', inline=False)

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

                        if off != False and member.bot == False:
                            self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {warn}', inline=False)

            await ctx.send(embed = self.embed)

        #   Clear memory
        return
    @msg.command()
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

class ChannelModeration(Cog):

    '''
        #   Channel moderation
        #   Commands for Moderators with manage_channels & manage_messages

    '''

    def __init__(self, bot):

        self.bot = bot
        self.warn = 0
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%H:%M, %d.%b - %y')
        self.embed = Embed(color=Colour.dark_purple(), description= '')

        return

    @before_invoke(coro= "ch")
    async def CheckModChannel(self, ctx):

        #   Fetching the channel "auditlog"
        ch = get(ctx.guild.channels, name = "auditlog")

        try :
            if ch: return True
        
        except TypeError as e: print(e)
        else:

            perms = { 
                        ctx.guild.default_role:PermissionOverwrite(view_channel=False)
                    }

            ch = await ctx.guild.create_text_channel("auditlog", overwrites=perms)

            #   Prepare and send embeded message
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Auto Generated Channel'
            self.embed.description = f"Created to have easy accsess to bot commands used by admin / moderator"
            await ch.send(embed=self.embed)
    
        #   Clear some memory
        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return
        print("test")

        return

    @after_invoke(coro = "ch")
    async def ClearMemory(self, ctx):

        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return

    @group(pass_contex = True)
    @has_permissions(manage_channels = True)
    async def ch(self, ctx):

        #   Calling a command to invoke first
        await self.CheckModChannel(ctx)
        await self.ClearMemory(ctx)

    #   Create a channel
    @ch.command()
    async def Create(self, ctx, ch):

        """
            #   Fetch given channel
            #   Fetch the auditlog
            #   Check if both exist
            #   If both does not raise any errors create a new Channel
        """
        #   Fetch channel
        arg = ch
        ch = get(ctx.guild.channels, name = f"{ch}")
        
        chlog = get(ctx.guild.channels, name = "auditlog")

        try :
            
            if ch: raise ValueError(f"Channel {ch} already exists")
            if not chlog : raise Exception("Channel auditlog does not exist yet")

        except Exception as e:

            self.embed.color = Colour.dark_red()
            self.embed.title = f"An Exception occured"
            self.embed.description = f"{e} Try another name."
            await ctx.send(embed=self.embed)

            #   Clear some memory
            del ch, arg, chlog

            return

        else :

            perms = { 
                            ctx.guild.default_role:PermissionOverwrite(view_channel=False)
                    }

            ch = await ctx.guild.create_text_channel(f'{arg}', overwrites=perms)

            #   Prepare and send embeded message
            self.embed.color = Colour.dark_red()
            self.embed.title = f'{ctx.author.name} Created the channel : \"{ch}\"'
            await chlog.send(embed=self.embed)

        #   Clear some memory
        del ch, arg, chlog

        return 

    #   Delete a channel
    @ch.command()
    async def Delete(self, ctx, ch):

        """
                #   Fetch both channels
                #   Check if they exist
                #   Delete the channel
        """

        #   Fetch channel
        arg = get(ctx.guild.channels, name = f"{ch}")
        chlog = get(ctx.guild.channels, name = "auditlog")

        try :
            #   If channel does not exist raise ValueError
            if not arg: raise ValueError(f"Channel \"{ch}\" Does not Exists")
            elif not chlog : raise Exception("Channel auditlog does not exist yet")

        except Exception as e:

                self.embed.color = Colour.dark_red()
                self.embed.title = f"An Exception occured"
                self.embed.description = f"{e}\nTry another name."
                await ctx.send(embed=self.embed)
        else :
            #   Delete GuildChannel
            await GuildChannel.delete(ch)

        #   Clear memory
        del ch, arg, chlog
        return 

    #   Clearing all messages
    @ch.command()
    async def Clear(self, ctx, ch, x):

        """
            #   Initializing the channels
            #   Checking wheter the values are correct or not
            #   Print a message
            #   Clearing a selected chat
        """

        #   Initializing Channels
        ch = get(ctx.guild.channels, name = ch)
        chlog = get(ctx.guild.channels, name = "auditlog")

        try :

            if not str(x).isdigit(): raise ValueError("You can not use alphabetical or ghlupical letters")
            elif int(x) < 0 or int(x) > 1000: raise ValueError("Choose an integer between 1-1000")
            else : x = int(x)

            if not ch : raise TypeError("Channel does not exist in the server")
            elif not chlog : raise TypeError("Could not find the auditlog channel")

        except Exception as e: 
            
            self.embed.title = f"An error occured"
            self.embed.description = f'The channel {ch}, were not cleared as requested due to\n{e}'
            self.embed.color = Colour.dark_red()
            ch.send(embed = self.embed)

        else:

            #   Prepare & send the embed message
            self.embed.title = f"{ctx.author} has cleared {x} chat lines in {ch} channel."
            self.embed.color = Colour.dark_red()
            await chlog.send(embed = self.embed)

        #   Remove content from the channel
        x = await ch.purge(limit=x)

        #   Saving some memory
        del ch, chlog, x

        return

class MemberModeration(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.now = datetime.datetime.now().strftime('%H:%M, %a, %d.%b - %y')
        self.embed = Embed(color=Colour.dark_purple(), description= '')

        return

    #  :x: Warn
    @group(pass_context = True)
    @has_permissions(moderate_members=True)
    async def Member(self, ctx): 
        self.embed.color = Colour.dark_red()

    @Member.command()
    async def Warn(self, ctx, member:d.Member, *, reason=None):

        #   Fetch the channel log
        chlog = get(ctx.guild.channels, name='auditlog')

        try:
            if reason == None: raise TypeError("Please provide a reason for the warn")
            elif member == ctx.author: raise TypeError(" Can not warn your self")

        except Exception as e :

            self.embed.title = "An error occured"
            self.embed.description =f"{e}"

        else:

            #   Prepare the embed message
            self.embed.title = f'**{member}** has been warned'
            self.embed.description = f' **Due to**\n *{reason}*.\n\n by\n**{ctx.author.name}**,\n{self.now}*'

            #   Message the user about the warn
            message = f'Greetings **{member}**.\n You recieve this Notification, because you have been warned by **{ctx.author}**.\n\n Due to :\n *{reason}*\n\nPlease read and follow the suggested guidelines for behavior in our disocrd channel'
            await member.send(message)

        await chlog.send(embed=self.embed)

        #   Clear some memory
        del message, reason, chlog, member
        return

   #   Mute Members
    @Member.command()
    async def Sush(self, ctx, member:d.Member, time=None, *, reason=None):

        """

            #   Fetch the channel
            #   Check if "time" argument is digits
            #   #   Set the time as int if it is a digit
            #   Check if the channel exists
            #   Check if there is a reason for unmute
            #   Check if the time is less than 1 week
            #   Check if the author is the member
            #   Calculate the time
            #   Prepare and messages
            #   timeout and send the message

        """

        #   Fetching the channel
        ch = get(ctx.guild.channels, name='auditlog')

        try:

            if not str(time).isdigit(): raise Exception("The argument has to be only seconds")
            else : time = int(time)

            if not ch : raise Exception("Auditlog does not exists")

            if reason == None: raise Exception(f" Could not sush **{member}** due to there were no reason to mute the member")
            if time > 604800: raise Exception(f' Could not sush **{member}** due to a limitation for 1w')
            elif member == ctx.author: raise Exception(f"Could not sush your self.")

        except Exception as e: 

            self.embed.title = "An Exception occured"
            self.embed.description = f"{e}"
            await ch.send(embed = self.embed)

            #   Clear some memory
            del time, ch, reason, member

            return

        else:

            #   Calculating the time
            time = hf.parse_timespan(time)

            #   Prepare, send & Clean up embed
            self.embed.title = f' **{member}** has been sushed'
            self.embed.description = f'by **{ctx.author.name}** \n for {datetime.timedelta(seconds=time)}\nDue to\n**{reason}.**\n*{self.now}*'

            self.embed.color = Colour.dark_red()
            await ch.send(embed=self.embed)

            #   Prepare and send the member, the message and sush the member
            message = f"""Greetings, **{member}**.\n
            You recieve this message, because you have been sushed by **{ctx.author}**\n
            You are sushed for **{datetime.timedelta(seconds=time)}**.\n
            During this time you will not able to use {ctx.guild} channels.\n
            The reason for this intervention is\n
            *{reason}*"""

            await member.send(f'{message}')
            await member.timeout(until = utils.utcnow() + datetime.timedelta(seconds=time), reason = reason)

            #   Automatic un-mute & Notify the user
            await asyncio.sleep(time)
            await member.send(f'Greetings **{member}**.\n\n Your sush, has been lifted you can now use {ctx.guild}')

        return

    @Member.command()
    async def Lift(self, ctx, member:d.Member):

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
    @Member.command()
    @has_permissions(kick_members= True)
    async def kick(self, ctx, member:d.Member, *, reason=None):

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

