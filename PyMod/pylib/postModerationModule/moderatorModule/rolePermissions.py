#   Python Repositories


#   Discord Repositories
from discord.utils import get
from discord.colour import Color
from discord.abc import GuildChannel
from discord import PermissionOverwrite
from discord.embeds import Embed, Colour
from discord import Member, Permissions, utils
from discord.ext.commands.core import has_permissions

from discord.ext.commands import Cog, command

class ModerationChecks(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.curTime = self.now.strftime('%H:%M, %d.%b - %y')  
        self.embed = Embed(color=Colour.dark_purple(), description= '')

    async def CheckChannel(self, ctx, arg):

        srv = ctx.guild
        ch = utils.get(srv.channels, name=f'{arg}')

        if not ch:

            perms = { 
                        srv.default_role:PermissionOverwrite(
                                                                    view_channel=False
                                                                )
            }

            ch = await srv.create_text_channel(f'{arg}', overwrites=perms)
    
            if arg == 'auditlog':

                self.embed.color = Colour.dark_red()
                self.embed.title = 'Auto generated channel'
                self.embed.description = 'This channel is used to log every Moderation in this server, it is made to avoid abusage of the Moderation / administration commands'

                await ch.send(embed=self.embed)
                self.embed.clear_fields()
                self.embed.color = Colour.dark_purple()

        return ch

    async def CheckRole (self, ctx, role, *, reason= None):

        #   Initializing variables
        srv = ctx.guild
        role = get(srv.roles, name=f'{role}')


        #   Check if there is a role called auditlog
        ch = await ModerationChecks.CheckChannel(self, ctx, 'auditlog')

        #   Pre-role assignments
        if role != 'Sushed':

            #   Prepare & create the role
            role = 'Sushed'
            reason = f'Sushed is an automatically generated to mark muted members'
            perms = Permissions()
            await srv.create_role(name=f'{role}', permissions = perms, reason = reason)

            #   Prepare, send & Clean up embed
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Auto generated role {role}'
            self.embed.description = f'{reason}'

            await ch.send(embed=self.embed)

            self.embed.clear_fields()
            self.embed.color = Colour.dark_purple()

        else: pass

        return ch, role


class RolePermissions(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

        return

    #   User Roles
    async def BasicRolePermissions(self, role):

        perms = {

                    role:Permissions(
                                    #   UserRole

                                    #   Voice
                                    speak = True,
                                    connect = True,
                                    request_to_speak = True,
                                    send_tts_messages = True,
                                    use_voice_activations = True,

                                    #   Stream
                                    stream = True,

                                    # Text-Channels
                                    send_messages=True,
                                    add_reactions = True,
                                    external_emoji = True,
                                    read_message_history=True,

                                    #   Manage Permissions
                                    ban_members = False,
                                    kick_members = False,
                                    manage_guild = False, 
                                    manage_roles = False,
                                    manage_emojis = False,
                                    manage_messages = False,
                                    manage_channels = False,
                                    manage_nicknames = False,
                                    change_nickname = False,
                                    moderate_members = False,
                                    manage_webhooks = False,

                                    #   Voice permissions 
                                    move_members = False,
                                    mute_members = False,
                                    deafen_members = False,
                                    priority_speaker = False,  
    
                                    #   Server Settings permissions
                                    view_audit_log = False,
                                    view_guild_insights = False,
                                    create_instant_invite = False,)
        }

        return perms

    async def StreamPermissions(self, role):

        perms = {

                    role:Permissions(
                                    #   UserRole

                                    #   Voice
                                    speak = False,
                                    connect = False,
                                    request_to_speak = False,
                                    send_tts_messages = False,
                                    use_voice_activations = False,

                                    #   Stream
                                    stream = True,

                                    # Text-Channels
                                    send_messages=True,
                                    add_reactions = True,
                                    external_emoji = True,
                                    read_message_history=True,
                                    use_slash_commands = True,

                                    #   Manage Permissions
                                    ban_members = False,
                                    kick_members = False,
                                    manage_guild = False, 
                                    manage_roles = False,
                                    manage_emojis = False,
                                    manage_messages = False,
                                    manage_channels = False,
                                    manage_nicknames = False,
                                    change_nickname = False,
                                    moderate_members = False,
                                    manage_webhooks = False,

                                    #   Voice permissions 
                                    move_members = False,
                                    mute_members = False,
                                    deafen_members = False,
                                    priority_speaker = False,  
    
                                    #   Server Settings permissions
                                    view_audit_log = False,
                                    view_guild_insights = False,
                                    create_instant_invite = False,)
        }

        return perms

    async def VoicePermissions(self, role):

        perms = {

                    role:Permissions(
                                    #   UserRole
                                    speak = True,
                                    connect = True,
                                    request_to_speak = True,
                                    send_tts_messages = True,
                                    use_voice_activations = True,

                                    #   Stream
                                    stream = False,

                                    # Text-Channels
                                    send_messages=True,
                                    add_reactions = True,
                                    external_emoji = True,
                                    read_message_history=True,
                                    use_slash_commands = True,

                                    #   Manage Permissions
                                    ban_members = False,
                                    kick_members = False,
                                    manage_guild = False, 
                                    manage_roles = False,
                                    manage_emojis = False,
                                    manage_messages = False,
                                    manage_channels = False,
                                    manage_nicknames = False,
                                    change_nickname = False,
                                    moderate_members = False,
                                    manage_webhooks = False,

                                    #   Voice permissions 
                                    move_members = False,
                                    mute_members = False,
                                    deafen_members = False,
                                    priority_speaker = False,  
    
                                    #   Server Settings permissions
                                    view_audit_log = False,
                                    view_guild_insights = False,
                                    create_instant_invite = False,)
        }

        return perms

    async def ChatPermissions(self, role):

        perms = {

                    role:Permissions(

                                    #   UserRole
                                    #   Voice
                                    speak = False,
                                    connect = False,
                                    request_to_speak = False,
                                    send_tts_messages = False,
                                    use_voice_activations = False,

                                    #   Stream
                                    stream = False,

                                    # Text-Channels
                                    send_messages=True,
                                    add_reactions = True,
                                    external_emoji = True,
                                    read_message_history=True,
                                    use_slash_commands = True,


                                    #   Manage Permissions
                                    ban_members = False,
                                    kick_members = False,
                                    manage_guild = False, 
                                    manage_roles = False,
                                    manage_emojis = False,
                                    manage_messages = False,
                                    manage_channels = False,
                                    manage_nicknames = False,
                                    change_nickname = False,
                                    moderate_members = False,
                                    manage_webhooks = False,

                                    #   Voice permissions 
                                    move_members = False,
                                    mute_members = False,
                                    deafen_members = False,
                                    priority_speaker = False,  
    
                                    #   Server Settings permissions
                                    view_audit_log = False,
                                    view_guild_insights = False,
                                    create_instant_invite = False,)
        }

        return perms

    #   Moderation 
    async def ModerationGuild(self, role):

        perms = {
            role:Permissions(
                                #   UserRole
                                speak = True,
                                stream = True,
                                connect = True,
                                send_messages=True,
                                read_message_history=True,

                                #   Manage Permissions
                                ban_members = False,
                                kick_members = True,
                                manage_guild = True, 
                                manage_roles = False,
                                manage_emojis = False,
                                manage_messages = False,
                                manage_channels = False,
                                manage_nicknames = False,
                                change_nickname = False,
                                moderate_members = False,
                                manage_webhooks = False,

                                #   Voice permissions 
                                move_members = False,
                                mute_members = False,
                                deafen_members = False,
                                priority_speaker = False,  
  
                                #   Server Settings permissions
                                view_audit_log = False,
                                view_guild_insights = False,
                                create_instant_invite = False,)
                }

        return perms

    async def ModerationRole(self, role):

        perms = {
            role:Permissions(
                                #   UserRole
                                speak = True,
                                stream = True,
                                connect = True,
                                send_messages=True,
                                read_message_history=True,

                                #   Manage Permissions
                                ban_members = False,
                                kick_members = False,
                                manage_guild = False, 
                                manage_roles = True,
                                manage_emojis = False,
                                manage_messages = False,
                                manage_channels = False,
                                manage_nicknames = False,
                                change_nickname = False,
                                moderate_members = False,
                                manage_webhooks = False,

                                #   Voice permissions 
                                move_members = False,
                                mute_members = False,
                                deafen_members = False,
                                priority_speaker = False,  
  
                                #   Server Settings permissions
                                view_audit_log = False,
                                view_guild_insights = False,
                                create_instant_invite = False,)
                }

        return perms

    async def ModerationChannel(self, role):

        perms = {
            role:Permissions(
                                #   UserRole
                                speak = True,
                                stream = True,
                                connect = True,
                                send_messages=True,
                                read_message_history=True,

                                #   Manage Permissions
                                ban_members = False,
                                kick_members = True,
                                manage_guild = False, 
                                manage_roles = False,
                                manage_emojis = False,
                                manage_messages = False,
                                manage_channels = True,
                                manage_nicknames = True,
                                change_nickname = False,
                                moderate_members = False,
                                manage_webhooks = False,

                                #   Voice permissions 
                                move_members = False,
                                mute_members = False,
                                deafen_members = False,
                                priority_speaker = False,  
  
                                #   Server Settings permissions
                                view_audit_log = False,
                                view_guild_insights = False,
                                create_instant_invite = False,)
                }

        return perms

    async def ModerationGuild(self, role):

        perms = {
            role:Permissions(
                                #   UserRole
                                speak = True,
                                stream = True,
                                connect = True,
                                send_messages=True,
                                read_message_history=True,

                                #   Manage Permissions
                                ban_members = False,
                                kick_members = True,
                                manage_guild = True, 
                                manage_roles = True,
                                manage_emojis = True,
                                manage_messages = True,
                                manage_channels = True,
                                manage_nicknames = True,
                                change_nickname = False,
                                moderate_members = True,
                                manage_webhooks = True,

                                #   Voice permissions 
                                move_members = False,
                                mute_members = False,
                                deafen_members = False,
                                priority_speaker = False,  
  
                                #   Server Settings permissions
                                view_audit_log = False,
                                view_guild_insights = False,
                                create_instant_invite = False,)
                }

        return perms

    async def ModerationVoice(self, role):

        perms = {

                    role:Permissions(
                                    #   UserRole
                                    speak = True,
                                    stream = True,
                                    connect = True,
                                    send_messages=True,
                                    read_message_history=True,

                                    #   Manage Permissions
                                    ban_members = False,
                                    kick_members = False,
                                    manage_guild = False, 
                                    manage_roles = False,
                                    manage_emojis = False,
                                    manage_messages = False,
                                    manage_channels = False,
                                    manage_nicknames = False,
                                    change_nickname = False,
                                    moderate_members = False,
                                    manage_webhooks = False,

                                    #   Voice permissions 
                                    move_members = True,
                                    mute_members = True,
                                    deafen_members = True,
                                    priority_speaker = True,  
    
                                    #   Server Settings permissions
                                    view_audit_log = False,
                                    view_guild_insights = False,
                                    create_instant_invite = False,)
        }

        return perms

    async def ModerateMember(self, role):

        perms = {
            role:Permissions(

                                #   UserRole
                                speak = True,
                                stream = True,
                                connect = True,
                                send_messages=True,
                                read_message_history=True,

                                #   Manage Permissions
                                ban_members = False,
                                kick_members = True,
                                manage_guild = False, 
                                manage_roles = False,
                                manage_emojis = False,
                                manage_messages = False,
                                manage_channels = False,
                                manage_nicknames = True,
                                change_nickname = False,
                                moderate_members = True,
                                manage_webhooks = False,

                                #   Voice permissions 
                                move_members = False,
                                mute_members = False,
                                deafen_members = False,
                                priority_speaker = False,  
  
                                #   Server Settings permissions
                                view_audit_log = False,
                                view_guild_insights = False,
                                create_instant_invite = False,)
                }

        return perms

    async def ModerationMananger(self, role):

        perms = {
            role:Permissions(
                                #   UserRole
                                speak = True,
                                stream = True,
                                connect = True,
                                send_messages=True,
                                read_message_history=True,

                                #   Manage Permissions
                                ban_members = False,
                                kick_members = True,
                                manage_guild = True, 
                                manage_roles = True,
                                manage_emojis = True,
                                manage_messages = True,
                                manage_channels = True,
                                manage_nicknames = True,
                                change_nickname = True,
                                moderate_members = True,
                                manage_webhooks = True,

                                #   Voice permissions 
                                move_members = True,
                                mute_members = True,
                                deafen_members = True,
                                priority_speaker = True,  
  
                                #   Server Settings permissions
                                view_audit_log = True,
                                view_guild_insights = True,
                                create_instant_invite = True,)
                }

        return perms

    async def Administrator(self, role):

        perms = Permissions(
                                #   UserRole
                                speak = True,
                                stream = True,
                                connect = True,
                                send_messages=True,
                                read_message_history=True,
                                administrator = True
)


        return perms

    #   Custom
    async def CustomPermissions(self, ctx, role):

        #   1   Set a player's role
        sec = 60.0
        
        self.embed.title = f'Set the permissions for {role} '
        self.embed.description = 'Would you like to set the role\'s permissions?\n'
        await ctx.send(embed=self.embed)

        rolePerm = await self.bot.wait_for('message', timeout=sec)
        rolePerm = str(rolePerm.content).lower()

        self.embed.title = f' {role}\'s permissions'
        self.embed.description = 'Please type in one of the following selections '
        self.embed.add_field(name = 'Administrator', value = 'Basic user Role ')
        self.embed.add_field(name = 'Moderator', value = ' Moderator Role')
        self.embed.add_field(name = 'Member', value = ' Administrator role')
    
        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        role = await self.bot.wait_for('message', timeout=sec)
        role = str(voice.content).lower().replace(" ", "")

        if role == 'administrator':

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

        elif role == 'moderator':

            """

                manage_channels, manage_emojis, manage_guild, 
                manage_messages, manage_nicknames, manage_permissions, 
                manage_roles, manage_webhooks, change_nickname, 
                create_instant_invite, move_members, mute_members, 
                deafen_members, priority_speaker, view_audit_log, 
                view_guild_insights,

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

        elif role == 'member':

            """ 
                #   Voice channels
                speak, request_to_speak, connect, stream

                #   Text Channels
                send_messages,
                read_message_history / view_channels, send_tts_messages,

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
