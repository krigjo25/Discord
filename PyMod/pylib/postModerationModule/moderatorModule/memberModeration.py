#   Python Repositories
import datetime
import humanfriendly as hf

#   Discord Repositories
import discord as d
from discord import utils
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, before_invoke, group, after_invoke, has_permissions



class MemberModeration(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.now = datetime.datetime.now().strftime("%a, %d.%b-%y")
        self.embed = Embed()

        return

    @group(pass_context = True)
    @has_permissions(moderate_members=True)
    async def member(self, ctx):  return

    @member.command()
    async def Warn(self, ctx, member:d.Member, *, reason=None):

        #   Fetch the channel log
        chlog = utils.get(ctx.guild.channels, name='auditlog')

        try:
            if member == ctx.author: raise Exception("Can not warn your self")
            elif reason == None: raise Exception("Please provide a reason for the warn")

        except Exception as e :

            self.embed.color = Colour.dark_red()
            self.embed.title = "An Exception Occured"
            self.embed.description =f"{e}, Try again !"

            del chlog, member, reason

            return

        else:

            #   Prepare the embed message
            self.embed.color = Colour.dark_red()
            self.embed.description = f'*{reason}*.'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f'**{member}** has been warned by {ctx.author.name} Date: {self.now}'

            #   Message the user about the warn
            message = f'Greetings **{member}**.\n You recieve this Notification, because you have been warned by **{ctx.author}**.\n\n Due to :\n *{reason}*\n\nPlease read and follow the suggested guidelines for behavior in our disocrd channel'
            await member.send(message)

        await chlog.send(embed=self.embed)

        #   Clear some memory
        del message, reason, chlog
        del member

        return

   #   Mute Members
    @member.command()
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
        role = utils.get(ctx.guild.roles, name ='Sushed')
        ch = utils.get(ctx.guild.channels, name='auditlog')

        try:

            #   Checking if the selected member is the command invoker
            if member == ctx.author: raise Exception(f"Could not sush your self.")
            elif len(time) < 2: raise Exception(f"{time}s / m / h / d)")
            elif int(time[0]) > 604800: raise Exception(f' Could not sush **{member}** due to a limitation for 1w')
            elif not ch : raise Exception("Auditlog does not exists")
            elif reason == None: raise Exception(f" Could not sush **{member}** due to there were no reason to mute the member")

        except Exception as e: 

            self.embed.color = Colour.dark_red()
            self.embed.title = "An Exception Occured"
            self.embed.description = f"{e}"
            await ctx.send(embed = self.embed)

            #   Clear some memory
            del time, ch, reason, member

            return

        else:

            #   Calculating the time
            time = hf.parse_timespan(time)

            #   Prepare, send & Clean up embed
            self.embed.color = Colour.dark_red()
            self.embed.title = f"**{member.name}** has been sushed by {ctx.author.name} for {time} seconds. Date : {self.now}"
            self.embed.description = f"*{reason}*."
            await ch.send(embed=self.embed)

            #   Prepare and send the member, the message and sush the member
            await member.add_roles(role)
            await member.send(f"""Greetings, **{member.name}**.\nYou recieve this message, because server moderator {ctx.author.name} gave you an timeout for **{datetime.timedelta(seconds=time)}**.\nYou will not be able to use the {ctx.guild}'s channels, during this given time.\nThe reason for this intervention is\n*{reason}*""")
            await member.timeout(until = d.utils.utcnow() + datetime.timedelta(seconds=time), reason = reason)

        #   Clear some memory
        del member, reason, time
        del ch

        return

    @member.command()
    async def Lift(self, ctx, member:d.Member):

        """
            #   Fetching the channel and role
            #   Checking for exceptions
            #   Remove the member role
            4   send the selected member a message
        """

        #   Fetch channel and role
        ch = utils.get(ctx.guild.channels, name='auditlog')
        role = utils.get(ctx.guild.roles, name ='Sushed')

        try :
            #   Check for exceptions
            if not ch: raise Exception("Auditlog channel does not exist")
            if not role: raise Exception("@Sushed role does not exit")

        except Exception as e:

            self.embed.description = f"{e}"
            self.embed.color = Colour.dark_red()
            self.embed.title = "An Exception Occured"
            await ctx.send(embed = self.embed)

            del ch, role
            return

        else:

            #   Prepare & send embed message
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Sush Lifted for {member}'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.description = f"by **{ctx.author.name}**\n Date: {self.now} User has been notified by a direct message."
        
        await ch.send(embed= self.embed)

        #   Removing role, timeout & Notify the user
        await member.remove_roles(role)
        await member.timeout(until=None, reason="unmuted")
        await member.send(f'Greetings **{member}**.\n\n The sush has been lifted you can now use {ctx.guild}')

        #   Clear some memory
        del role, ch, member
        return

    #   Kick Members
    @member.command()
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
        ch = utils.get(ctx.guild.channels, name='auditlog')

        try :

            if member == ctx.author: raise Exception("Can not kick your self")
            if reason == None: raise Exception(f"**{ctx.author.name}** Provide a reason to kick **{member.name}**")
            if not ch : raise Exception("There is no channel named auditlog")

        except Exception as e :

            self.embed.title = "An Exception Occured"
            self.embed.description = f"{e}, try again."
            self.embed.color = Colour.dark_red()
            await ctx.send(embed=self.embed)

            #   Clear some memory
            del ch, reason, member

        else:

            #   Prepare embed
            self.embed.color = Colour.dark_red()
            self.embed.description = f' *{reason}*.'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f'**{member}** has been kicked from the server by {ctx.author.name} Date : {self.now}'

            #   Creating a message to the user, send it to his DM, then kick
            await member.send(f"Greetings **{member}**.\nYou recieve this message, because moderator {ctx.author.name} kicked you from {ctx.guild.name}\nDue to :\n *{reason}*")
            await member.kick(reason=reason)

        #   Send & Clean up embed
        await ch.send(embed=self.embed)

        return

    @member.before_invoke
    async def CheckModChannel(self, ctx):

        #   Fetching the channel "auditlog"
        ch = utils.get(ctx.guild.channels, name = "auditlog")

        try :
            if ch: return True
        
        except TypeError as e: print(e)
        else:

            #   Creating a channel
            perms = {ctx.guild.default_role:d.PermissionOverwrite(view_channel=False)}
            ch = await ctx.guild.create_text_channel("auditlog", overwrites=perms)

            #   Prepare and send embeded message
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Auto Generated Channel'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.description = f"Created to have easy accsess to bot commands used by admin / moderator"
            await ch.send(embed=self.embed)
    
        #   Clear some memory
        del perms, ch
        self.embed.description =""

        return

    @member.before_invoke
    async def CheckRole(self, ctx):

        #   Fetching the channel "auditlog"
        ch = utils.get(ctx.guild.channels, name = "auditlog")
        role = utils.get(ctx.guild.roles, name = "Sushed")

        try :
            if role:
                #   Clear some memory
                del role, ch
                return True
        
        except TypeError as e: print(e)
        else:

            # Role Configurations
            perm = d.Permissions(send_messages = False, request_to_speak = False, send_tts_messages = False, use_voice_activations = False)
            await ctx.guild.create_role(name=f'{role}', permissions = perm, reason = f"Auto Generated - by Pymod")

            #   Prepare and send embeded message
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Auto Generated Role'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.description = f"Created to store sushed members"
            await ch.send(embed=self.embed)

        del role, perm, ch

        return

    @member.after_invoke
    async def ClearMemory(self):

        #   Clear some Memory
        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.description = ""
        self.embed.remove_thumbnail()
        self.embed.color = Colour.dark_purple()

        return

