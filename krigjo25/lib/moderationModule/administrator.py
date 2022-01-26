import datetime
from discord import Member
from discord.utils import get

from discord.colour import Color
from discord import PermissionOverwrite
from discord.embeds import Embed, Colour
from discord.ext.commands.core import has_permissions
from discord.ext.commands import Cog, command,has_any_role

class Administrator(Cog, name='Admin-module'):
    def __init__(self, bot):
        self.bot = bot
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%d.%m - %Y')
        self.embed = Embed(color=Color.dark_purple())

    # Ban / Unban
    @command(name='banned')
    #@has_permission(ban_members=True)
    async def BannedList(self, ctx):
        
        #   Retrieve the list of banned members
        return

        # Prohbit a user to enter the channel again
    @command(name='Ban', help='prohbit a user to enter the channel again')
    @has_any_role('Admin', 'admin', 'Software-Technican')
    @has_permissions(ban_members= True)

    async def BanMember(self, ctx, member:Member, *, reason=None):

        if reason == None: # required a reason
            await ctx.send(f'Please provide me a reason to ban {member}')

        elif reason != None: # logs the reason in a given channel


            #   1:  Creating a message to send the user, so he get a notice of the ban, and ban the member
            message = f'the Administrator Team has decided to probhid you for using  **{ctx.guild.name}** \n \n Due to :\n **{reason}**'
            await member.send(message)
            await member.ban(reason=reason)

            #   2:  Check if there is a channel called moderation log
            srv = ctx.guild
            ch= get(srv, name='moderationlog')

            if not ch:
                pass

            #   3:  Log the ban
            self.embed = Embed(color=Color.dark_red())
            self.embed.title = f'{member} has been banned from {ctx.guild.name} by {ctx.author} due to {reason} '
            self.embed.description=''
            
            await ch.send(embed=self.embed)
            self.embed = Embed(color=Color.dark_purple())
        return


    #   allows a user to enter the channel again 
    @command(name='Unban', help='allow a user to enter the channel again')
    @has_any_role('Admin', 'admin', 'Software-Technican', 'Software-Technican')
    @has_permissions(administrator= True)

    async def UnBan(self, ctx, member:Member, reason=None):

        srv = ctx.guild

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
        BannedUsers= await ctx.guild.bans()
        MemberName, member_discriminator = member.split('#')

        for entry in BannedUsers:
            user = entry.user

            if (user.name, user.discriminator) == (MemberName, member_discriminator):
                await ctx.guild.unban(user)
            
                message = f'You have now been unbanned from  **{ctx.guild.name}**'
                await member.send(message)
                
        return

    #   Announcements
    @command(name='announce')
    @has_any_role('admin','Admin', 'Software-Technican')
    async def botSay(self, ctx, ch ):
        
        #   Prepare and send an embeded message
        self.embed.title = ''
        self.embed.description = 'What would you like to announce?'
        await ctx.send(embed=self.embed)

        #   Get the user's message and procsess it
        message = await self.bot.wait_for('message')
        message = str(message.content)

        # Find the given channel to send an announcement
        srv = ctx.guild
        channel = get(srv.channels, name=ch)
        await channel.send(f'{message} \n Sincerely, \n **{ctx.author}** \n Date : **{self.curTime}**')
        return

    #   Role Managements

    @command(name='createRole')
    @has_any_role('admin','Admin', 'Software-Technican')
    async def CreateRole(self, ctx, ch ):
        pass

    @command(name='setRole')
    @has_any_role('admin','Admin', 'Software-Technican')
    async def setRole(self, ctx, ch ):
        pass
    @command(name='remove')
    @has_any_role('admin','Admin', 'Software-Technican')
    async def removeMemberRole(self, ctx, ch ):
        pass
    
    @command(name='delRole')
    @has_any_role('admin','Admin', 'Software-Technican')
    async def removeRole(self, ctx, ch ):
        pass
 
 
 
 