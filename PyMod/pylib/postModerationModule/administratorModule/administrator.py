#   Python Repositories

import datetime

#   Discord Repositories
from discord import Member
from discord.utils import get
from discord.colour import Color
from discord import PermissionOverwrite
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, command
from discord.ext.commands.core import has_permissions

class Administrator(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%H:%M, %a, %d.%b - %y')
        self.embed = Embed(color=Color.dark_purple())

        return

    #   Ban management
    @command(name='banlist')
    @has_permissions(ban_members=True, administrator=True)
    async def BannedList(self, ctx):

        #   Initializing variables
        srv = ctx.guild
        bannedList=[]
        bannedUsers = await srv.bans()

        for entry in bannedUsers:

            bannedList.append(entry.user.name)
            bannedList.append(entry.user.discriminator)
            bannedList.append(entry.reason)

        self.embed.title = 'List of banned server members'

        if bool(bannedList) == True:
            self.embed.description =' User name | User discriminator | Reason'
            self.embed.add_field(name= f'{bannedList[0]}, {bannedList[1]}', value = f'{bannedList[2]}')

        else: self.embed.description = self.embed.description ='Noone banned yet, Hurray :party:'
        self.embed.add_field(name= ' End of List', value = ':-)')
        await ctx.send(embed=self.embed)
        self.embed.clear_fields()    

    #   Prohbit a user to enter the channel again
    @command(name='ban')
    @has_permissions(ban_members=True, administrator=True)

    async def BanMember(self, ctx, member:Member, *, reason=None):

        if reason == None: # required a reason
            await ctx.send(f'We do not ban, {member} for No-reason, provide one')

        elif reason != None: # logs the reason in a given channel

            #   1:  Creating a message to send the user, so he get a notice of the ban, and ban the member
            message = f'the Administrator Team has decided to probhid you for using  **{ctx.guild.name}** \n \n Due to :\n **{reason}**'
            await member.send(message)
            await member.ban(reason=reason)

            #   2:  Check if there is a channel called moderation log

            srv = ctx.guild
            ch = get(srv.channels, name='moderationlog')

            if not ch:
                perms = PermissionOverwrite(read_messages=False)

                await srv.create_text_channel(f'{ch}', overwrites=perms)

                self.embed = Embed(color=Colour.dark_red(), description= '')
                self.embed.title = 'Auto generated channel'
                self.embed.description = 'This channel is used for every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'
                await ch.send(embed=self.embed)

            #   3:  Log the ban
            self.embed = Embed(color=Color.dark_red())
            self.embed.title = f'{member} has been banned from {ctx.guild.name} by {ctx.author} due to {reason} '
            self.embed.description=''

            await ch.send(embed=self.embed)
            self.embed = Embed(color=Color.dark_purple())

        return

    #   Allows a user to enter the channel again
    @command(name='unban')
    @has_permissions(ban_members=True, administrator= True)
    async def Unban(self, ctx, *, member):

        srv = ctx.guild
        memberName, memberDiscriminator = member.split('#')

        #   1:  Check if there is a channel called moderation log
        ch = get(srv.channels, name='moderationlog')

        #   Create a new channel if not found
        if not ch:

            #   Creating channel permissions
            perms = PermissionOverwrite(read_messages=False)

            await srv.create_text_channel(f'{ch}', overwrites=perms)

            self.embed = Embed(color=Colour.dark_red(), description= '')
            self.embed.title = 'Auto generated channel'
            self.embed.description = 'This channel is used for every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'
            await ch.send(embed=self.embed)

        #   2:  Log the unban
        self.embed = Embed(color=Colour.dark_red(), description= '')
        self.embed.title = f'**{member}** has been Unbanned by **{ctx.author}** Date : **{self.curTime}**'
        self.embed.description = ''
        await ch.send(embed=self.embed)

        self.embed = Embed(color=Colour.dark_purple(), description= '')

        #   3:  Unban the given member
        BannedUsers= await srv.bans()

        for entry in BannedUsers:
            user = entry.user
        
            if (user.name) == (memberName) or (user.name,  user.discriminator) == (memberName, memberDiscriminator):await srv.unban(user)

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
        channel = get(srv.channels, name=ch)

        #   Prepare & Send the embed message
        self.embed.title = 'Server News announcement'
        self.embed.description = f'{message}\n\nSincerely,\n**{ctx.author.name}**\n\n ***published  {self.curTime}***'
        await channel.send(embed=self.embed)

        return
