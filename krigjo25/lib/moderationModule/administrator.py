import datetime
from discord import Member
from discord.colour import Color
from discord.embeds import Embed
from discord.ext.commands.core import has_permissions
from discord.utils import get
from discord.ext.commands import Cog, command, has_role, has_any_role

class Administrator(Cog, name='Admin-module'):
    def __init__(self, bot):
        self.bot = bot
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%d.%m - %Y')
        self.embed = Embed(color=Color.dark_purple())

    # Ban / Unban

        # Prohbit a user to enter the channel again
    @command(name='Ban', help='prohbit a user to enter the channel again')
    @has_any_role('Admin', 'admin', 'Software-Technican')
    @has_permissions(ban_members= True)

    async def BanMember(self, ctx, member:Member, *, reason=None):

        if reason == None: # required a reason
            await ctx.send(f'Please provide me a reason to ban {member}')

        elif reason != None: # logs the reason in a given channel

            #   1:  Check if there is a channel called moderation log
            #   2:  Log the ban

            #   3:  Creating a message to send the user, so he get a notice of the ban, and ban the member
            message = f'the Administrator Team has decided to probhid you for using  **{ctx.guild.name}** \n \n Due to :\n **{reason}**'
            await member.send(message)
            await member.ban(reason=reason)
        return


    #   allows a user to enter the channel again 
    @command(name='Unban', help='allow a user to enter the channel again')
    @has_any_role('Admin', 'admin', 'Software-Technican', 'Software-Technican')
    @has_permissions(administrator= True)

    async def UnBan(self, ctx, member:Member, reason=None):

        
        #   1:  Check if there is a channel called moderation log
        #   2:  Log the unban

        #   3:  Unban the given member
        BannedUsers= await ctx.guild.bans()
        MemberName, member_discriminator = member.split('#')

        for entry in BannedUsers:
            user = entry.user

            if (user.name, user.discriminator) == (MemberName, member_discriminator):
                await ctx.guild.unban(user)
                
                message = f'the Administrator Team has decided to unban you from  **{ctx.guild.name}**'
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
 
 
 
 