#   Discord Repositories
import discord as d
from discord.colour import Colour


from discord.ext.commands import Cog


class ChannelPermissions(Cog):

    def __init__(self):

        self.embed = d.Embed(color=Colour.dark_purple())

        return

    async def SelectPermissions(self, arg):

        match str(arg).lower().replace(" ",""):
            case "member": return self.Member()


    def Member(self):

        perms = {d.PermissionOverwrite(#   Voice
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
                                                create_instant_invite = False)}

        return perms

"""
add_reactions
administrator
attach_files
ban_members
change_nickname
create_instant_invite
create_private_threads
create_public_threads
deafen_members
embed_links
external_stickers
kick_members
manage_channels
manage_emojis
manage_emojis_and_stickers
manage_events
manage_guild
manage_messages
manage_nicknames
manage_permissions
manage_roles
manage_threads
manage_webhooks
mention_everyone
move_members
mute_members
priority_speaker
send_messages_in_threads
start_embedded_activities
use_application_commands
use_external_emojis
use_external_stickers
use_slash_commands
value
view_audit_log
view_channel
view_guild_insights  """