#   Discord Repositories
import discord as d
from discord.utils import get
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, group, after_invoke, before_invoke, has_permissions

#   Custom library
from pylib.dictionaries.systemmessages import Dictionaries
from pylib.postModerationModule.moderatorModule.rolePermissions import RolePermissions

class RoleModeration(Cog):

    """
        Commands which requires manage_roles

    """

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Colour.dark_purple())

        return

    @before_invoke("role")
    async def CheckModChannel(self, ctx):

        #   Fetching the channel "auditlog"
        ch = get(ctx.guild.channels, name = "auditlog")

        try :
            if ch: return True
        
        except TypeError as e: print(e)
        else:

            perms = { 
                        ctx.guild.default_role:d.PermissionOverwrite(view_channel=False)
                    }

            ch = await ctx.guild.create_text_channel("auditlog", overwrites=perms)

            #   Prepare and send embeded message
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Auto Generated Channel'
            self.embed.description = f"Created to have easy accsess to bot commands used by admin / moderator"
            await ch.send(embed=self.embed)
    
        #   Clear some memory
        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        #   Clear some memory
        del perms, ch

        return

    @before_invoke("role")
    async def CheckRole(self, ctx):

        #   Fetching the channel "auditlog"
        ch = get(ctx.guild.channels, name = "auditlog")
        role = get(ctx.guild.roles, name = "Sushed")

        try :
            if role:
                #   Clear some memory
                del role, ch
                return True
        
        except TypeError as e: print(e)
        else:
            # Role Configurations
            perm = d.Permissions(send_messages = False, request_to_speak = False, send_tts_messages = False, use_voice_activations = False)
            await ctx.guild.create_role(name=f'{role}', permissions = perm, reason = f"Auto Generated - by Pymod")

            #   Prepare and send embeded message
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Auto Generated Role'
            self.embed.description = f"Created to store sushed members"
            await ch.send(embed=self.embed)

        del role, perm, ch

        return

    @after_invoke("role")
    async def ClearMemory(self, ctx):

        #   Clear some Memory
        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.remove_thumbnail()
        self.embed.color = Colour.dark_purple()

        return

    #   Role Management
    @group(pass_context = True)
    @has_permissions(manage_roles = True)
    async def role(self, ctx):

        await self.CheckModChannel(ctx)
        await self.CheckRole(ctx)
        await self.ClearMemory(ctx)

    #   Create role
    @role.command()
    async def Create(self, ctx, role, *, reason= None):

        """

            #   1   Create the role if not exist, if it exist send out a warning message
            #   2   Choose the permission of the role
            #   3   Choose the colour of the role with hexdecimals

        """

        #   Initializing classes
        dc = Dictionaries
        manager = RolePermissions
        color = ["Dark Purple", "Dark Red", "Dark Blue",
                    "Purple", "Red", "Blue"]

        #   Initializing variables

        ch = get(ctx.guildchannels, name= 'auditlog')
        role = get(ctx.guildroles, name = f'{role}')

        try:
            if not ch: raise Exception("Channel auditlog does not exist")
            elif role: raise Exception("Role already exists")

        except Exception as e: print(e)
        else:

            #   Prepare, Send
            self.embed.title = f'Configure @{role}'
            self.embed.description = f'Would you like to create @{role} wih permission? type in a title or **x** to exit '
            self.embed.add_field(name = 'Member', value = 'Member user Role ')
            self.embed.add_field(name = 'Moderator', value = ' Moderator Role')
            self.embed.add_field(name = 'Admin', value = ' Administrator role')
            self.embed.add_field(name = 'Custom', value = 'Create a custom role')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            #   Waiting for response
            response = await self.bot.wait_for('message', timeout=30)
            response = str(response.content).lower().replace(" ", "")

            #   Checking respons issues 
            match response:
                case "member":

                    #   Prepare, Send & Clean up
                    self.embed.title = f'Creating moderation permissions for **@{role}**, role'
                    self.embed.description = f'Would you like to create @{role} with previliges? type one of the tiles below or **x** to exit '

                    self.embed.add_field(name = 'Voice ', value = 'Chat & speak')
                    self.embed.add_field(name = 'Stream', value = 'Chat & Stream')
                    self.embed.add_field(name = 'Chat', value = ' Can only Chat')
                    self.embed.add_field(name = 'Member', value = 'Can do everything like a regular user')

                    await ctx.send(embed=self.embed)
                    self.embed.clear_fields()

                    #   Waiting for response
                    response = await self.bot.wait_for('message', timeout=30)
                    response = str(response.content).lower().replace(" ", "")

                    #   List of mananger
                    match response:
                        case "chat": perm = await manager.ChatPermissions(self, role)
                        case "voice": perm = await manager.VoicePermissions(self, role)
                        case "stream": perm = await manager.StreamPermissions(self, role)
                        case "member": perm = await manager.BasicRolePermissions(self, role)
                case "moderator":

                    #   Prepare, Send & Clean up
                    self.embed.title = f'Creating moderation permissions for **@{role}**, role'
                    self.embed.description = f'Would you like to create @{role} with previliges? type one of the tiles below or **x** to exit '

                    self.embed.add_field(name = 'Voice Mananger', value = 'Manages Voice ')
                    self.embed.add_field(name = 'Role Manager', value = ' Mananges only roles')
                    self.embed.add_field(name = 'Guild Manager', value = ' Manages only Guild')
                    self.embed.add_field(name = 'Channel Manager', value = 'Manages only channels')
                    self.embed.add_field(name = 'Mananger', value = ' Manages Guild, Channel, Role, Voice & Members')
                    self.embed.add_field(name = 'Member Moderator', value = 'Moderates Members')

                    await ctx.send(embed=self.embed)
                    self.embed.clear_fields()

                    #   Waiting for response
                    response = await self.bot.wait_for('message', timeout=30)
                    response = str(response.content).lower().replace(" ", "")

                    #   Mananger list
                    match response:
                        case "guildmananger":perm = await manager.ModerationGuild(self, role)
                        case "rolemananger": perm = await manager.ModerationRole(self, role)
                        case "channelmanager": perm = await manager.ModerationChannel(self, role)
                        case "mananger": perm = await manager.ModerationMananger(self, role)
                        case "voice":perm = await manager.ModerationVoice(self, role)
                        case "membermoderation": perm = manager.ModerateMember(self, role)
                        case "manangermananger":perm = manager.ModerationMananger(self, role)
                case "custom": perm = manager.CustomPermissions(self, role)
                case "admin": perm = await manager.Administrator(self, role)

            self.embed.title = f'Choosing role Color'
            self.embed.description = f'Would you like to create @{role} wih colors? type in a title or **x** to exit '
            self.embed.add_field(name = 'Dark Purple', value = 'Dark Purple color for role ')
            self.embed.add_field(name = 'Purple', value = 'Purple color for role')
            self.embed.add_field(name = 'Dark Red', value = 'Dark red color for role')
            self.embed.add_field(name = 'Red', value = 'Red color for role')
            self.embed.add_field(name = 'Dark Blue', value = 'Dark Blue color for role')
            self.embed.add_field(name = 'Blue', value = 'Blue color for role')
            self.embed.add_field(name = 'Default', value = 'Blue color for role')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            response = await self.bot.wait_for('message', timeout=30)
            response = str(response.content).lower().replace(" ", "")

            if response in color: color = dc.RoleColours(response)
            else : color = Colour.default()

            await ctx.guild.create_role(name=f'{role}', permissions = perm, color = color, reason = f'{reason}')
            self.embed.title = f'@{role}'
            self.embed.description = f'has been succsessfully created with {response} previliges and a colou'
            await ctx.send(embed = self.embed)
        #   Clear some memory
        del ch, role, response
        del dc, manager, color
        return

    #   Delete Role
    @role.command()
    async def Delete(self, ctx, role ):

        """
            1   Checking if there is any channels called 'moderationlog'
            2   Ask the user for comfirmation before removing the role

        """

        #   Fetch role and channel
        role = get(ctx.guild.roles, name= role)
        ch = get(ctx.guild.channels, name='auditlog')

        try:
            if not role : raise Exception(f"\"{role}\" does not exists")
            elif not ch : raise Exception("audit channel does not exist")

        except Exception as e:

            self.embed.title = "An Exception Occured"
            self.embed.description = f'{e}, Try again...'
            await ctx.send(embed = self.embed)

            #   Clear some memory
            del role, ch
            return

        else:

            #   Prepare, send & clean up the embed message
            self.embed.title = f'Removing {role} role'
            self.embed.description = f'Sometimes we do not do what we do something stupid? type in the role to delete the role'

            await ctx.send(embed=self.embed)

            self.embed.clear_fields()

            #   Confirm the action
            response = await self.bot.wait_for('message', timeout=60.0)
            response = str(response.content)

            if response == role:
                #   Prepare the embed message and delete & role
                self.embed.title = f'{role} role, has been removed from the server'
                await response.delete()

            else: self.embed.title = f'Role removal cancelled'

        #   Send & clean up the embed message
        self.embed.color = Colour.dark_red()
        await ch.send(embed=self.embed)

        del role, ch, response

        return
 
    #   Remove role 
    @role.command()
    async def Demote(self, ctx, member:d.Member, role, *, reason=None ):

        """
            1   Checking if there is any channels called 'auditlog'
            2   When the command is invoked, ask the user for a confirmation
            3   Remove the user from the role

        """

        #   Initializing variables
        role = get(ctx.guild.roles, name=f'{role}')
        ch = get(ctx.guild.channels, name='auditlog')

        #   Prepare, Send & Clean up embed
        try: 
            if not role : raise Exception(f"Role \"{role}\" Not found")
        except Exception as e: 

            self.embed.color = Colour.dark_red()
            self.embed.title = 'An Exception Occured'
            self.embed.description = f"{e}, try again."
            await ctx.send(embed = self.embed)

        else:

            self.embed.color = Colour.dark_red()
            self.embed.title = f'removing {member} from {role}'
            self.embed.description = f'Type in the name if you really want to remove the person from the role.'

            await ctx.send(embed=self.embed)

        #   Retrieve the confirmation from the user
        response = await self.bot.wait_for('message')
        response = str(response.content).lower()

        if response in member:

            #  Prepare, remove, send & Clean up
            self.embed.color = Colour.dark_red()
            self.embed.title = f'{member} has been removed from {role} by {ctx.author} due to {reason} '

            await member.remove_roles(role)

        else:

            #   Prepare Send & Clean up
            self.embed = Embed(color=Colour.dark_red())
            self.embed.title = f'Role removal has been cancelled'

        self.embed.description=''
        await ch.send(embed=self.embed)


        return self.embed

    #   Set Role
    @role.command()
    async def Set(self, ctx, member:d.Member, role, *, reason= None):

        #   Fetch roles and channel

        role = get(ctx.guild.roles, name=f'{role}')
        ch = get(ctx.guild.channels, name='auditlog')

        try :
            if not role: raise Exception("Role does not exist")
            elif not ch: raise Exception("auditlog channel does not exist")

        except Exception as e:

            self.embed.title = "An Exception Occured"
            self.embed.description = f"{e}, try again"
            await ctx.send(embed = self.embed)

            del role, ch
            return
        else:
            #   Prepare, Send & Clean up embed
            self.embed.color = Colour.dark_red()
            self.embed.title = f'removing {member} from {role}'
            self.embed.description = f'Type in **{member}** to set the member as {role}?'

            await ctx.send(embed=self.embed)

        #   Retrieve the confirmation from the user
        response = await self.bot.wait_for('message')
        response = str(response.content).lower()

        if response in member:

            #  Prepare, remove, send & Clean up
            self.embed.color = Colour.dark_red()
            self.embed.title = f'{member} has been added to {role} by {ctx.author}'
            self.embed.description = f"{reason}"

            await member.add_roles(role)


    #   Change Color for the role
    @role.command()
    async def Color(self, ctx, role, *, reason= None):

        #   Initializing classes
        dc = Dictionaries

        #   Fetch channel and role
        ch = get(ctx.guild.channels, name= 'auditlog')
        role = get(ctx.guild.roles, name = f'{role}')
        color = ["Dark Purple", "Dark Red", "Dark Blue", "Purple", "Red", "Blue"]

        try:

            if not role: raise Exception("Role does not exists")
            if not ch: raise Exception("audit channel does not exists")

        except Exception as e:

            self.embed.color = Colour.dark_red()
            self.embed.title = 'An Exception Occured'
            self.embed.description = f'{e}, try again'
        
            await ctx.send(embed=self.embed)

            del ch, role, color, dc
            return

        else: 
            #   Prepare, send & Clean up
            self.embed.title = f'Choosing role Color'
            self.embed.description = f'Would you like to change colors of {role}? type in a title or **x** to exit '
            self.embed.add_field(name = 'Dark Purple', value = 'Dark Purple color for role ')
            self.embed.add_field(name = 'Purple', value = 'Purple color for role')
            self.embed.add_field(name = 'Dark Red', value = 'Dark red color for role')
            self.embed.add_field(name = 'Red', value = 'Red color for role')
            self.embed.add_field(name = 'Dark Blue', value = 'Dark Blue color for role')
            self.embed.add_field(name = 'Blue', value = 'Blue color for role')

            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            response = await self.bot.wait_for('message', timeout=30)
            response = str(response.content).lower().replace(" ", "")

            if response in color: color = dc.RoleColours(response)
            else: color=Colour.default()

            await ctx.guild.edit_role(name=f'{role}', color = color, reason = f'{reason}')
            
            self.embed.title = f"@{role}'s colour has changed into {response} by {ctx.author.name}"

            await ch.send(embed=self.embed)
            self.embed.clear_fields()

            #   Clear some memory
            del response, color, role
            del ch, dc
        return
