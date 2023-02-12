#   Python Repositories
import datetime
import humanfriendly as hf

#   Discord Repositories
import discord as d
from discord.utils import get
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, before_invoke, group, after_invoke, has_permissions



class MemberModeration(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.now = datetime.datetime.now().strftime('%H:%M, %a, %d.%b - %y')
        self.embed = Embed(color=Colour.dark_purple(), description= '')

        return

    @before_invoke("Member")
    async def CheckModChannel(self, ctx):

        #   Fetching the channel "auditlog"
        ch = get(ctx.guild.channels, name = "auditlog")

        try :
            if ch: return True
        
        except TypeError as e: print(e)
        else:

            perms = { 
                        ctx.guild.default_role:d.PermissionOverwrite(view_channel=False)
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

    @after_invoke("Member")
    async def ClearMemory(self, ctx):

        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return

    #  :x: Warn
    @group(pass_context = True)
    @has_permissions(moderate_members=True)
    async def Member(self, ctx):

        self.embed.color = Colour.dark_purple()
        await self.CheckModChannel()
        await self.ClearMemory()

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
        del message, reason, chlog
        del member

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
            elif time > 604800: raise Exception(f' Could not sush **{member}** due to a limitation for 1w')
            else : time = int(time)

            if not ch : raise Exception("Auditlog does not exists")
            if reason == None: raise Exception(f" Could not sush **{member}** due to there were no reason to mute the member")
            if member == ctx.author: raise Exception(f"Could not sush your self.")

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
            await member.send(f"""Greetings, **{member}**.\nYou recieve this message, because you have been sushed by **{ctx.author}**\nYou are sushed for **{datetime.timedelta(seconds=time)}**.\nDuring this time you will not able to use {ctx.guild} channels.\nThe reason for this intervention is\n*{reason}*""")
            await member.timeout(until = d.utils.utcnow() + datetime.timedelta(seconds=time), reason = reason)

        del member, reason, time
        del ch

        return

    @Member.command()
    async def Lift(self, ctx, member:d.Member):

        """
            #   Fetching the channel and role
            #   Checking for exceptions
            #   Remove the member role
            4   send the selected member a message
        """

        #   Fetch channel and role
        ch = get(ctx.guild.channels, name='auditlog')
        role = get(ctx.guild.roles, name ='@sushed')

        try :
            #   Check for exceptions
            if not ch: raise Exception("Auditlog channel does not exist")
            if not role: raise Exception("@Sushed role does not exit")

        except Exception as e:

            self.embed.title = "An Exception Occured"
            self.embed.description = f"{e}"
            ctx.send(embed = self.embed)

            return
        else:

            #   Prepare, send and clean up embed
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Sush Lifted for {member}'
            self.embed.description = f"by **{ctx.author.name}**\n Date: {self.now} User has been notified by a direct message."
        
        await ch.send(embed= self.embed)

        #   Removing role, timeout & Notify the user
        await member.remove_roles(role)
        await member.timeout(until=None, reason="unmuted")
        await member.send(f'Greetings **{member}**.\n\n The sush has been lifted you can now use {ctx.guild}')

        return

    #   Kick Members
    @Member.command()
    @has_permissions(kick_members= True)
    async def kick(self, ctx, member:d.Member, *, reason=None):

        """
            #   Fetching the auditlog channel
            #   Checks for exceptions
            #   Prepare the embed message
            #   Sending the member notification for the kick
            #   Kicking the member
        """

        #   Fetching the channel
        ch = get(ctx.guild.channels, name='auditlog')

        try :

            if reason == None: raise Exception(f"**{ctx.author.name}** Provide a reason to kick **{member.name}**")
            if not ch : raise Exception("There is no channel named auditlog")

        except Exception as e :

            self.embed.title = "An Exception Occured"
            self.embed.description = f"{e}, try again."
            self.embed.color = Colour.dark_red()
            await ctx.send(embed=self.embed)

        else:

            #   Prepare embed
            self.embed.title = f'**{member}** has been kicked from the server'
            self.embed.description = f' by\n**{ctx.author.name}**\n Due to\n*{reason}.*\n Date : *{self.curTime}*'

            #   Creating a message to the user, send it to his DM, then kick

            await member.send(f"Greetings **{member}**.\nYou recieve this message, because you have been kicked off **{ctx.guild.name}** by **{ctx.author}**.\n\nDue to :\n **{reason}**")
            await member.kick(reason=reason)

        #   Send & Clean up embed
        self.embed.color = Colour.dark_red()
        await ch.send(embed=self.embed)

        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return
