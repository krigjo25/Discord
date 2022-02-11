from discord import Member
from discord.utils import get
from discord.colour import Color
from discord import PermissionOverwrite
from discord.embeds import Embed, Colour
from discord.permissions import Permissions
from discord.ext.commands.core import has_permissions
from discord.ext.commands import Cog, command,has_any_role


'''
class roleManagement(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.curTime = self.now.strftime('%d.%m - %Y')
        self.embed = Embed(color=Color.dark_purple())
        return
    
        #   Role Managements

    async def CreateRole(self, ctx, ch ):
        #   1   Create the role if not exist, if it exist send out a warning message

        #   2   Choose the permission of the role

        #   3   Choose the colour of the role with hexdecimals
        return

    async def RolePermissions(self, ctx, role):

        #   1   Set a player's role
        sec = 60.0'''
        '''
            add_reactions 
            administrator
            attach_files
            ban_members
            change_nickname
            connect
            create_instant_invite
            deafen_members
            embed_links
            external_emojis
            kick_members
            manage_channels
            manage_emojis
            manage_guild
            manage_messages
            manage_nicknames
            manage_permissions
            manage_roles
            manage_webhooks
            mention_everyone
            move_members
            mute_members
            priority_speaker
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
            view_audit_log
            view_guild_insights'''''''
        
        self.embed.title = f'{role} does not exist'
        self.embed.description = 'Would you like to create the role?\nYes / No'
        await ctx.send(embed=self.embed)

        role = await self.bot.wait_for('message', timeout=sec)
        role = str(role.content)

        if role == 'Yes' or role == 'yes':

                #   Voice permissions
                self.embed.title = f' {role}\'s permissions'
                self.embed.description = 'Please type "True" or "False" '
                self.embed.add_field(name='Voice permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

                voice = await self.bot.wait_for('message', timeout=sec)
                voice = str(voice.content)

                #   Send Messages permissions
                self.embed.title = f' {role}\'s permissions'
                self.embed.description = 'Please type "True" or "False" '
                self.embed.add_field(name='Send Messages permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                
                msg = await self.bot.wait_for('message', timeout=sec)
                msg = str(msg.content)

                #   Read History permissions
                self.embed.title = f' {role}\'s permissions'
                self.embed.description = 'Please type "True" or "False" '
                self.embed.add_field(name='View Channels', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                
                rm = await self.bot.wait_for('message', timeout=sec)
                rm = str(rm.content)

                #   Read History permissions
                self.embed.title = f' {role}\'s permissions'
                self.embed.description = 'Please type "True" or "False" '
                self.embed.add_field(name='Read entire history permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                
                rmh = await self.bot.wait_for('message', timeout=sec)
                rmh = str(rmh.content)
                overwrite = Permissions(
                                            speak=voice, 
                                            send_messages=msg, 
                                            read_message_history=rmh, 
                                            view_channels=rm)
            
        #memberRole = await srv.create_role(name=f'{ch}', permissions= overwrite, reason='Automatic Role assignment')
        #await memberRole.edit(colour=Colour(f'0x{colour}'))
        elif role == 'No' or role == 'no':
            self.embed.title = f'Procsess canceled'
            await ctx.send(embed=self.embed)

        return

    async def removeMemberRole(self, ctx, ch ):
        #   1   Simply remove a users role 
        return

    @command(name='delRole')
    @has_any_role('admin','Admin', 'Software-Technican')

    async def removeRole(self, ctx, ch ):
            #   1   Simply remove a role, ask for confirmation
        return

'''