#   Python Repositories
import datetime

#   Discord Repositories
from discord import Member, utils
from discord.colour import Color
from discord import PermissionOverwrite
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, command
from discord.ext.commands.core import has_permissions

class Administrator(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.now = datetime.datetime.now()
        self.curtime = self.now.strftime('%H:%M, %a, %d.%b - %y')
        self.embed = Embed(color=Color.dark_purple())

        return

    #   Ban management
    @command(name='banlist')
    @has_permissions(ban_members=True, administrator=True)
    async def BannedList(self, ctx):
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

            self.embed.add_field(name= ' End of List', value = ':-)', inline = False)

            await ctx.send(embed=self.embed)

        #   Clear some space
        del banned, entry, dictionary

        self.embed.clear_fields()

        return

    #   Prohbit a user to enter the channel again
    @command(name='ban')
    @has_permissions(ban_members=True, administrator=True)

    async def BanMember(self, ctx, member:Member, *, reason=None):

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

            if not ch:

                #   Requires a dictionary
                #perms = PermissionOverwrite(read_messages=False)
                await ctx.guild.create_text_channel(f"moderationlog")

                ch = utils.get(ctx.guild.channels, name='moderationlog')
                self.embed.color = Color.dark_red()
                self.embed.title = 'Auto generated channel'
                self.embed.description = 'This channel is used for every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'

                await ch.send(embed = self.embed)
                self.embed.clear_fields()
            
            #   Log the ban
            self.embed.color = Color.dark_red()
            self.embed.title = f'{member} has been banned by {ctx.author}'
            self.embed.description = f"due to {reason}\nDate:{self.curtime}"

            await ch.send(embed=self.embed)

            #   Notify the user about the ban & ban the member
            message = f'the Administrator Team has decided to probhid you for using  **{ctx.guild.name}** \n \n Due to :\n **{reason}**'
            await member.send(message)
            await member.ban(reason=reason)

        #   Clear some memory
        del reason, message
        del member, ch
        self.embed.clear_fields()
        self.embed.color = Color.dark_purple()

        return

    #   Allows a user to enter the channel again
    @command(name='unban')
    @has_permissions(ban_members=True, administrator= True)
    async def Unban(self, ctx, *, name):

        try :
            if len(name) != 2: raise ValueError("Did you forget the discriminator / name?")

        except Exception as e:

            #   Prepare emed message
            self.embed.color = Color.dark_red()
            self.embed.title = f"An exception occured"
            self.description = f"{e}"
            await ctx.send(embed = self.embed)

            self.embed.clear_fields()

        #######
        else:
            srv = ctx.guild
            name, discriminator = str(name).split('#')

        #   Check if there is a channel called moderation log
        ch = utils.get(srv.channels, name='moderationlog')

        if not ch:

            #   Requires a dictionary
            #perms = PermissionOverwrite(read_messages=False)
            await ctx.guild.create_text_channel(f"moderationlog")

            ch = utils.get(ctx.guild.channels, name='moderationlog')
            self.embed.color = Color.dark_red()
            self.embed.title = 'Auto generated channel'
            self.embed.description = 'This channel is used for every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'

            await ch.send(embed = self.embed)
            self.embed.clear_fields()

        #   Log the unban
        self.embed.color = Color.dark_red()
        self.embed.title = f"{member} unbanned"
        self.description = f"**{member}** has been Unbanned by **{ctx.author}**\nDate : **{self.curTime}**"

        await ch.send(embed=self.embed)

        self.embed = Embed(color=Colour.dark_purple(), description= '')

        #   3:  Unban the given member
        async for entry in ctx.guild.bans():
            user = entry.user
        
            if (user.name) == (memberName) or (user.discriminator) == (memberDiscriminator): await srv.unban(user)

        del member, memberName, memberDiscriminator

        return

    #   Announcements
    @command(name='announce')
    @has_permissions(administrator= True)
    async def botSay(self, ctx, ch):

        #   Prepare & send embeded message
        self.embed.title = ''
        self.embed.description = 'What would you like to announce?'
        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        #   Get the user's message and procsess it
        message = await self.bot.wait_for('message')
        message = str(message.content)

        # Find the given channel to send an announcement
        srv = ctx.guild
        channel = utils.get(srv.channels, name=ch)

        #   Prepare & Send the embed message
        self.embed.title = 'Server News announcement'
        self.embed.description = f'{message}\n\nSincerely,\n**{ctx.author.name}**\n\n ***published  {self.curTime}***'
        await channel.send(embed=self.embed)

        return
