#   Python Repositories

import datetime

#   Discord Repositories
from discord import Member
from discord.utils import get
from discord.colour import Color
from discord import PermissionOverwrite
from discord.embeds import Embed, Colour
from discord.permissions import Permissions
from discord.ext.commands import Cog, command
from discord.ext.commands.core import has_permissions

class Administrator(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%d.%m - %Y')
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
    @has_permissions(administrator= True)
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
        self.embed.description = f'{message}\nSincerely {ctx.author}\n **{self.curDate}**'
        await channel.send(embed=self.embed)

        return

class RolePermissions(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.curTime = self.now.strftime('%d.%m - %Y')
        self.embed = Embed(color=Color.dark_purple())

        return

    async def Permissions(self, ctx, roleName):

        print(roleName)

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

class RoleManagement(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.curTime = self.now.strftime('%d.%m - %Y')
        self.embed = Embed(color=Color.dark_purple())

        return
    #   Role Management
    @command(name='createRole')
    @has_permissions(manage_roles = True)
    async def CreateRole(self, ctx, roleName):

        """

            #   1   Create the role if not exist, if it exist send out a warning message
            #   2   Choose the permission of the role
            #   3   Choose the colour of the role with hexdecimals

        """

        #   Initializing classes
        manager = RolePermissions

        #   Initializing variables

        srv = ctx.guild
        role = get(srv.roles, name=f'{roleName}')
        
        ch = get(srv.channels, name='moderationlog')

        if not role:

            self.embed.title = f'Starting the process to create {roleName}'
            self.embed.description = f'Would you like to create {roleName} with permissions? '
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            confirmation = await self.bot.wait_for('message')
            confirmation = str(confirmation.content).lower()

            if not ch:

                perms = PermissionOverwrite(read_messages=False)

                await srv.create_text_channel(f'{ch}', overwrites=perms)

                #   3:  Log the role Creation
                self.embed.title = 'Auto generated channel'
                self.embed.color = Embed(color=Colour.dark_red())
                self.embed.description = 'This channel is used to log every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'

                await ch.send(embed=self.embed)
                self.embed.clear_fields()


            if confirmation[0:4] == 'yes':

                #   Calling the roles Permission
                roleName = str(roleName)
                perms = manager.RolePermissions(roleName)

                """
                await srv.create_role(name=f'{roleName}', permissions = perms, reason='')

                #   Prepare embed
                self.embed.color = Embed(color=Colour.dark_red())
                self.embed.title = f'{ctx.author} created {roleName} as a with permissions '
                self.embed.description=f'{perms}'

                #   Send embed
                await ch.send(embed=self.embed)
                self.embed.clear_fields()
                """

            else:

                #   Prepare embed
                self.embed.color = Embed(color=Colour.dark_red())
                self.embed.title = f'{ctx.author} created {roleName} as a public role'
                self.embed.description=''

                #   Send embed
                await ch.send(embed=self.embed)
                self.embed.clear_fields()

                await srv.create_role(name=f'{roleName}', reason='')

        else:

            #   3:  Log the error
            self.embed.color = Embed(color=Colour.dark_red())
            self.embed.title = f'{ctx.author} tried to re-create {roleName}'
            self.embed.description='Role already exists'
            await ch.send(embed=self.embed)
            self.embed.clear_fields()

        self.embed.color = Embed(color=Colour.dark_purple())

        return

    @command(name='remove')
    @has_permissions(manage_roles = True)
    async def RemoveMemberRole(self, ctx, *, member:Member, role, reason=None ):

        """

            #   1 When the command is invoked, ask the user for a confirmation
            #   2 Remove the user from the role

        """

        srv=ctx.guild
        mRole = get(srv.roles, name=f'{role}')
        member.remove_roles(member, mRole)
        ch = get(srv.channels, name='moderationlog')

        self.embed.title = f'removing {member} from {role}'
        self.embed.description = f'Are you sure you\'d like to remove {member} from {role}'
        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        confirmation = await self.bot.wait_for('message')
        confirmation = str(confirmation.content).lower()

        if confirmation == 'yes':

            if not ch:

                perms = PermissionOverwrite(read_messages=False)

                await srv.create_text_channel(f'{ch}', overwrites=perms)

                self.embed = Embed(color=Colour.dark_red(), description= '')
                self.embed.title = 'Auto generated channel'
                self.embed.description = 'This channel is used to log every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'
                await ch.send(embed=self.embed)
                self.embed.clear_fields()

            #   3:  Log the ban
            self.embed = Embed(color=Color.dark_red())
            self.embed.title = f'{member} has been removed from {role} by {ctx.author} due to {reason} '
            self.embed.description=''

            await ch.send(embed=self.embed)
            self.embed.clear_fields()

        else:
            pass

        return

    @command(name='delRole')
    @has_permissions(manage_roles = True)
    async def removeRole(self, ctx, role ):
            """
                #   1   Ask the user for comfirmation before removing the role

            """
            
            self.embed.title = f'Removing {role}'
            self.embed.description = f'Do you want to remove the role?'
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            confirmation = await self.bot.wait_for('message', timeout=60.0)
            confirmation = str(confirmation.content)

            if confirmation == 'yes':

                srv = ctx.guild
                find = get(srv.roles, name=f'{role}')
                await find.delete()

                self.embed.title = f'{role} has been removed'
                self.embed.description = ''
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

            else:

                self.embed.title = f'Role removal canceled'
                self.embed.description = ''
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

            return
 
    @command(name='modifyRole')
    @has_permissions(manage_roles = True)
    async def ModifyRole(self, ctx, role ):

            """
                #   1   Ask the user for comfirmation before removing the role

            """

            return
