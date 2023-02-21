#   Discord Repositories
import discord as d
from discord.colour import Colour


from discord.ext.commands import Cog


class ChannelPermissions(Cog):

    """
        #  Author : Krigjo25
        #  Creation Date :  2.18-23
        #  last update :

        #   Create channels
        #   Delete channels
        #   modify channels
            Commands for Moderators with manage_channels & manage_messages
    """
    def __init__(self):

        self.embed = d.Embed(color=Colour.dark_purple())

        return

    async def SelectPermissions(self, ctx:d.ApplicationContext, arg, role = None):

        if role == None: role = ctx.guild.default_role
        match str(arg).lower().replace(" ",""):
            case "member": return self.Member()
            case "none": return self.hidden(role)

    def hidden(self, role): return {role :d.PermissionOverwrite(view_channel = False,)}

    def Member(self):

        perm = d.PermissionOverwrite(
                                                # Text-Channels
                                                send_messages=True,
                                                add_reactions = True,
                                                external_emojis = True,
                                                change_nickname = True,
                                                manage_messages = False,
                                                manage_webhooks = False,
                                                manage_channels = False,
                                                mention_everyone = False,
                                                read_message_history=True,
                                                create_instant_invite = False)

        return perm
"""perm = d.PermissionOverwrite(#   Voice
                                                speak = True,
                                                connect = True,
                                                request_to_speak = True,
                                                send_tts_messages = True,
                                                use_voice_activation = True,

                                                #   Stream
                                                stream = True,

                                                # Text-Channels
                                                send_messages=True,
                                                add_reactions = True,
                                                external_emojis = True,
                                                read_message_history=True,
                                                mention_everyone = False,

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
                                                create_instant_invite = False)"""