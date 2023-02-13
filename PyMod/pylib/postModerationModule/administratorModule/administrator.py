#   Python Repositories
import datetime

#   Discord Repositories
import discord as d
from discord import utils
from discord.colour import Color
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, group, before_invoke, after_invoke
from discord.ext.commands.core import has_permissions

class Administrator(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.now = datetime.datetime.now().strftime('%a, %d.%b-%y')
        self.embed = Embed(color=Color.dark_purple())

        return

    #   Ban management
    @group(pass_context = True)
    @has_permissions(ban_members=True, administrator= True)
    async def ban(self, ctx):
        await self.CheckModChannel(ctx)
        await self.ClearMemory(ctx)

    async def list(self, ctx):
        """
            #   List of banned members
        """
        #   Initializing a list
        banned = []

        try:

            #   Iterating over the ctx.guild bans
           async for entry in ctx.guild.bans():

                dictionary = { "name": entry.user.name,
                                "discriminator": entry.user.discriminator,
                                "reason": entry.reason}

                banned.append(dictionary)

        except Exception as e : print(e)
        else:

            #   Prepare the ebeded message
            self.embed.title = 'List of banned server members'
            self.embed.description =' User name & discriminator | Reason'
            self.embed.color = Color.dark_red()

            if banned:
                for i in banned: self.embed.add_field(name= f'{i["name"]}#{i["discriminator"]}', value = f'{i["reason"]}', inline = True)

            else: self.embed.description = "Noone banned yet, Hurray :party:"

            self.embed.add_field(name= '== End of List ==', value = ':-)', inline = False)
            await ctx.send(embed=self.embed)

        #   Clear some space
        del banned, entry, dictionary

        return

    #   Prohbit a user to enter the channel again
    async def member(self, ctx, member:d.Member, *, reason=None):

        """
            #   Ban a server member
            #   Reason required
            #   Notify the user about the ban
            #   Cheeck for a moderationlog channel
            #   Log the ban

        """

        try :
        
            if reason == None: raise ValueError(f"Can not ban {member} with out a reason.")

            #   Checks after moderationlog channel
            ch = utils.get(ctx.guild.channels, name='moderationlog')

        except Exception as e :

            self.embed.color = Color.dark_red()
            self.embed.title =f"Tried to ban {member}"
            self.embed.description = f"{e}\n"
            await ctx.send(embed = self.embed)

        else:

            #   Log the ban
            self.embed.color = Color.dark_red()
            self.embed.description = f"due to {reason}"
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f'{member} has been banned by {ctx.author}'
            
            await ch.send(embed=self.embed)

            #   Notify the user about the ban & ban the member
            message = f'the Administrator Team has decided to probhid you for using  **{ctx.guild.name}** \n \n Due to :\n **{reason}**'
            await member.send(message)
            await member.ban(reason=reason)

        #   Clear some memory
        del reason, message
        del member, ch

        return

    #   Allows a user to enter the channel again
    async def unban(self, ctx, *, member:d.Member):

        #   Check if there is a channel called moderation log
        ch = utils.get(ctx.guild.channels, name='auditlog')

        try :
            if len(name) != 2: raise Exception("Did you forget the discriminator / name?")
            elif not ch : raise Exception("auditlog channel does not exits")

        except Exception as e:

            #   Prepare emed message
            self.embed.color = Color.dark_red()
            self.embed.title = f"An Exception Occured"
            self.description = f"{e}, try again"
            await ctx.send(embed = self.embed)

            del ch, member
            return

        else:
            name = str(member).split('#')

            #   Log the unban
            self.embed.color = Color.dark_red()
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f"{member[0]} has been unbanned by {ctx.author.name}"

            await ch.send(embed=self.embed)

            #  Unban the given member
            async for entry in ctx.guild.bans():
                user = entry.user
            
                if user.name == name[0] or user.discriminator == name[1]: await ctx.guild.unban(user)

        del member, name, ch

        return

    @ban.before_invoke
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

    @ban.after_invoke
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

