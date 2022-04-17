
#   Discord Responsories
from discord.utils import get
from discord.colour import Color
from discord import PermissionOverwrite
from discord.embeds import Embed, Colour
from discord.permissions import Permissions
from discord.ext.commands import Cog, command,has_any_role



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
        self.embed.description = 'Please type in ModeratorRole Administrator Role or User Role '

        role = await self.bot.wait_for('message', timeout=sec)
        role = str(voice.content).lower().replace(" ", "")

        if role == 'administratorrole':
            """
                administrator
                ban_members
                mention_everyone
                kick_members
                manage_channels
                manage_emojis
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
                deafen_members
                priority_speaker
                view_audit_log
                view_guild_insights
            """
        if role == 'moderatorrole':
            """
            kick_members
            manage_channels
            manage_emojis
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
            deafen_members
            priority_speaker
            view_audit_log
            view_guild_insights
            """

        if role == 'userrole':

            """ 
                add_reactions 
                attach_files
                connect
                embed_links
                external_emojis
                read_message_history
                request_to_speak
                send_messages
                send_tts_messages
                speak
                stream
                use_external_emojis
                use_slash_commands
                use_voice_activation
                value
            """

            #   Voice permissions
            self.embed.description = f'You selected {role} permissions'
            self.embed.add_field(name='Voice permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            voice = await self.bot.wait_for('message', timeout=sec)
            voice = str(voice.content)

            #   Send Messages permissions
            self.embed.add_field(name='Send Messages permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            msg = await self.bot.wait_for('message', timeout=sec)
            msg = str(msg.content)

            #   Read History permissions

            self.embed.add_field(name='View Channels', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            rm = await self.bot.wait_for('message', timeout=sec)
            rm = str(rm.content)

            #   Read History permissions

            self.embed.add_field(name='Read entire history permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            rmh = await self.bot.wait_for('message', timeout=sec)
            rmh = str(rmh.content)

            perm = Permissions(
                                            speak=voice, 
                                            send_messages=msg, 
                                            read_message_history=rmh, 
                                            view_channels=rm)

        else:

            self.embed.title = f'Procsess canceled'
            await ctx.send(embed=self.embed)
            perm = ''

        return perm

class RoleColour(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.curTime = self.now.strftime('%d.%m - %Y')
        self.embed = Embed(color=Color.dark_purple())

        return