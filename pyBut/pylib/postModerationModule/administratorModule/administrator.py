#   Python Repositories

import datetime

#   Discord Repositories
from discord import Member
from discord.utils import get
from discord.colour import Color
from discord import PermissionOverwrite
from discord.embeds import Embed, Colour
from discord.permissions import Permissions
from discord.ext.commands.core import has_permissions
from discord.ext.commands import Cog, command,has_any_role

#   pyLib Repositories
#from permissionModule import roleManagement
class Administrator(Cog, name='Admin-module'):
    def __init__(self, bot):
        self.bot = bot
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%d.%m - %Y')
        self.embed = Embed(color=Color.dark_purple())

    #   Ban management
    @command(name='banlist')
    @has_permissions(ban_members=True)
    async def BannedList(self, ctx):
        
        srv = ctx.guild
        bannedList=[]

        bannedUsers= await srv.bans()
        
        for entry in bannedUsers:
            bannedList.append(entry.user.name)
            bannedList.append(entry.user.discriminator)
            bannedList.append(entry.reason)

        self.embed.title = 'List of banned server members'
        self.embed.description ='No-one banned yet, Hurray :party:'

        if bool(bannedList) == True:
            self.embed.description =' User name | User discriminator | Reason'
            self.embed.add_field(name= f'{bannedList[0]}, {bannedList[1]}', value = f'{bannedList[2]}')
        
        self.embed.add_field(name= ' End of List', value = ':-)')
        await ctx.send(embed=self.embed)
        self.embed.clear_fields()    
            
        # Prohbit a user to enter the channel again
    @command(name='ban')
    @has_any_role('Admin', 'admin', 'Software-Technican')
    @has_permissions(ban_members= True)

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


    #   allows a user to enter the channel again
 
    @command(name='unban')
    @has_any_role('Admin', 'admin', 'Software-Technican', 'Software-Technican')
    @has_permissions(administrator= True)

    async def UnBan(self, ctx, *, member):

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

        
            if (user.name) == (memberName) or (user.name,  user.discriminator) == (memberName, memberDiscriminator):
                await srv.unban(user)
                
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
        
        #   1   Create the role if not exist, if it exist send out a warning message

        #   2   Choose the permission of the role

        #   3   Choose the colour of the role with hexdecimals
        pass

    @command(name='setRole')
    @has_any_role('admin','Admin', 'Software-Technican')
    async def setRole(self, ctx, member:Member, role):
            # Not finished
        srv = ctx.guild
        memberRole = get(srv.roles, name=f'{role}')

        if not memberRole:
            
            return #roleManagement.RolePermissions

        else:

            await member.add_roles(memberRole)
        return

    @command(name='setPermission')
    @has_any_role('admin','Admin', 'Software-Technican')
    async def setRole(self, ctx, member:Member, role):
            # Not finished
        pass
        return

    @command(name='remove')
    @has_any_role('admin','Admin', 'Software-Technican')
    async def removeMemberRole(self, ctx, *, member:Member, role, reason=None ):

        srv=ctx.guild
        mRole = get(srv.roles, name=f'{role}')
        member.remove_roles(member, mRole)
        ch = get(srv.channels, name='moderationlog')

        

        #   1   Creating a confirmation to remove a member from a role
        self.embed.title = f'removing {member} from {role}'
        self.embed.description = f'Are you sure you\'d like to remove {member} from {role}'
        await ctx.send(embed=self.embed)

        submit = await self.bot.wait_for('message')
        submit = str(submit.content)


        #   2   Simply remove a users role
        if submit == 'Yes' or 'yes':

            if not ch:
                perms = PermissionOverwrite(read_messages=False)

                await srv.create_text_channel(f'{ch}', overwrites=perms)

                self.embed = Embed(color=Colour.dark_red(), description= '')
                self.embed.title = 'Auto generated channel'
                self.embed.description = 'This channel is used to log every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'
                await ch.send(embed=self.embed)

            #   3:  Log the ban
            self.embed = Embed(color=Color.dark_red())
            self.embed.title = f'{member} has been removed from {role} by {ctx.author} due to {reason} '
            self.embed.description=''
            
            await ch.send(embed=self.embed)


        else:

            if not ch:
                perms = PermissionOverwrite(read_messages=False)

                await srv.create_text_channel(f'{ch}', overwrites=perms)

                self.embed = Embed(color=Colour.dark_red(), description= '')
                self.embed.title = 'Auto generated channel'
                self.embed.description = 'This channel is used to log every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'
                await ch.send(embed=self.embed)

            #   3:  Log the ban
            self.embed = Embed(color=Color.dark_red())
            self.embed.title = f'{member} has been removed from {role} by {ctx.author} due to {reason} '
            self.embed.description=''
            
            await ch.send(embed=self.embed)

        return
    
    @command(name='delRole')
    @has_any_role('admin','Admin', 'Software-Technican')

    async def removeRole(self, ctx, role ):
            #   1   Simply remove a role, ask for confirmation
            self.embed.title = f'Removing {role}'
            self.embed.description = f'Do you want to remove the role? True / False'
            await ctx.send(embed=self.embed)

            answer = await self.bot.wait_for('message', timeout=60.0)
            answer = answer.content


            if answer == 'True' or answer == 'true':
                srv = ctx.guild
                findRole = get(srv.roles, name=f'{role}')
                await findRole.delete()

                self.embed.title = f'{role} has been removed'
                self.embed.description = ''
                await ctx.send(embed=self.embed)

            else:
                self.embed.title = f'Role removal canceled'
                self.embed.description = ''
                await ctx.send(embed=self.embed)
            return
 
