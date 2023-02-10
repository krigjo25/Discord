#   Python Repositories

#   Discord Repositories
from discord import Member
from discord.utils import get
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, command
from discord.ext.commands.core import has_permissions

#   Pylib
from pylib.dictionaries.systemmessages import Dictionaries
from pylib.postModerationModule.moderatorModule.rolePermissions import RolePermissions
from pylib.postModerationModule.moderatorModule.moderator import ModerationChecks

class RoleModeration(Cog):

    """
        Commands which requires manage_roles

    """

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Colour.dark_purple())

        return

    #   Role Management

    #   Get a list of roles a member has
    @command(name='memro')
    @has_permissions(manage_roles = True)
    async def MemberRoleList(self, ctx, role, *, reason= None):

        """

            #   1   Create the role if not exist, if it exist send out a warning message
            #   2   Choose the permission of the role
            #   3   Choose the colour of the role with hexdecimals

        """

        #   Initializing classes
        dc = Dictionaries
        manager = RolePermissions

        #   Initializing variables
        srv = ctx.guild
        ch = get(srv.channels, name= 'auditlog')
        findRole = get(srv.roles, name = f'{role}')

        return

    #   Create role
    @command(name='crero')
    @has_permissions(manage_roles = True)
    async def CreateRole(self, ctx, role, *, reason= None):

        """

            #   1   Create the role if not exist, if it exist send out a warning message
            #   2   Choose the permission of the role
            #   3   Choose the colour of the role with hexdecimals

        """

        #   Initializing classes
        dc = Dictionaries
        manager = RolePermissions

        #   Initializing variables
        srv = ctx.guild
        ch = get(srv.channels, name= 'auditlog')
        findRole = get(srv.roles, name = f'{role}')

        if not ch:
            ch = await ModerationChecks.CheckChannel(self, ctx, 'auditlog')

        if not findRole:

            #   Prepare, Send & Clean up
            self.embed.title = f'Starting the process to create @{role}'
            self.embed.description = f'Would you like to create @{role} wih permission? type in a title or **x** to exit '
            self.embed.add_field(name = 'Member', value = 'Member user Role ')
            self.embed.add_field(name = 'Moderator', value = ' Moderator Role')
            self.embed.add_field(name = 'Admin', value = ' Administrator role')
            self.embed.add_field(name = 'Custom', value = 'Create a custom role')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            #   Waiting for response
            response = await self.bot.wait_for('message', timeout=30)
            rolePriviliges = str(response.content).lower().replace(" ", "")

            #   Checking respons issues 

            if rolePriviliges == 'member':

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
                answer = str(response.content).lower().replace(" ", "")

                #   List of mananger
                if answer == 'voice':perms = await manager.VoicePermissions(self, role)
                elif answer == 'stream':perms = await manager.StreamPermissions(self, role)
                elif answer == 'chat':perms = await manager.ChatPermissions(self, role)
                elif answer == 'member':perms = await manager.BasicRolePermissions(self, role)

            elif rolePriviliges == 'moderator':

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
                answer = str(response.content).lower().replace(" ", "")

                #   List of mananger
                if answer == 'guildmananger':perms = await manager.ModerationGuild(self, role)
                elif answer == 'rolemananger':perms = await manager.ModerationRole(self, role)
                elif answer == 'channelmananger':perms = await manager.ModerationChannel(self, role)
                elif answer == 'mananger':perms = await manager.ModerationMananger(self, role)
                elif answer == 'guildmananger':perms = await manager.ModerationGuild(self, role)

                #   Voice mananger
                elif answer == 'voice':perms = await manager.ModerationVoice(self, role)
                elif answer == 'membermoderation':perms = manager.ModerateMember(self, role)
                elif answer == 'managermananger':perms = manager.ModerationMananger(self, role)

            elif rolePriviliges == 'custom':perms = manager.CustomPermissions(self, role)
            elif rolePriviliges =='admin':perms = await manager.Administrator(self, role)
                


            self.embed.title = f'Choosing role Color'
            self.embed.description = f'Would you like to create @{role} wih colors? type in a title or **x** to exit '
            self.embed.add_field(name = 'Dark Purple', value = 'Dark Purple color for role ')
            self.embed.add_field(name = 'Purple', value = 'Purple color for role')
            self.embed.add_field(name = 'Dark Red', value = 'Dark red color for role')
            self.embed.add_field(name = 'Red', value = 'Red color for role')
            self.embed.add_field(name = 'Dark Blue', value = 'Dark Blue color for role')
            self.embed.add_field(name = 'Blue', value = 'Blue color for role')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            response = await self.bot.wait_for('message', timeout=30)
            answer = str(response.content).lower().replace(" ", "")

            if answer == 'darkpurple': color = dc.RoleColours(answer)
            else: color=Colour.default()

            print('test')
            await srv.create_role(name=f'{role}', permissions = perms, color = color, reason = f'{reason}')
            self.embed.title = f'@{role}'
            self.embed.description = f'has been succsessfully created with {answer} previliges and a colou'
            
        else:

            self.embed.title = f'{role} might exist'
            self.embed.description = f'?liro to check your server roles'

        #   Prepare, send, clean up & role creation
        
        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        return

    #   Delete Role
    @command(name='dero') # :X
    @has_permissions(manage_roles = True)
    async def DeleteRole(self, ctx, arg ):

        """
            1   Checking if there is any channels called 'moderationlog'
            2   Ask the user for comfirmation before removing the role

        """

        #   Initializing variables
        srv = ctx.guild
        role = get(srv.roles, name=f'{arg}')
        ch = get(srv.channels, name='auditlog')

        if not ch: pass
            #ch = await ModerationChecks.CheckChannel(self, ctx, 'auditlog')

        if role:

            #   Prepare, send & clean up the embed message
            self.embed.title = f'Removing {role} role'
            self.embed.description = f'Do you want to remove, @{role}?'

            await ctx.send(embed=self.embed)

            self.embed.clear_fields()

            #   Confirm the action
            confirmation = await self.bot.wait_for('message', timeout=60.0)
            confirmation = str(confirmation.content)

            if confirmation == 'yes' or confirmation == 'ye' or confirmation == 'y':

                #   Prepare the embed message and delete & role
                self.embed.title = f'{role} role, has been removed from the server'

                await role.delete()

            else:

                #   Prepare the embed message
                self.embed.title = f'Role removal cancelled'
        else:
            
            #   Prepare the embed message
            self.embed.title = f'{arg} Does not exist'

        #   Send & clean up the embed message
        self.embed.color = Colour.dark_red()
        self.embed.description = ''
        await ch.send(embed=self.embed)

        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return
 
    #   Remove role 
    @command(name='remro')
    @has_permissions(manage_roles = True)
    async def RemoveMemberRole(self, ctx, member:Member, role, *, reason=None ):

        """
            1   Checking if there is any channels called 'auditlog'
            2   When the command is invoked, ask the user for a confirmation
            3   Remove the user from the role

        """

        #   Initializing variables
        srv = ctx.guild
        role = get(srv.roles, name=f'{role}')
        ch = get(srv.channels, name='auditlog')

        if not ch:
            ch = await ModerationChecks.CheckChannel(self, ctx, 'auditlog')

        #   Prepare, Send & Clean up embed
        self.embed.color = Colour.dark_red()
        self.embed.title = f'removing {member} from {role}'
        self.embed.description = f'Are you sure you\'d like to remove {member} from {role}?'

        await ctx.send(embed=self.embed)

        #   Clean up
        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        #   Retrieve the confirmation from the user
        confirm = await self.bot.wait_for('message')
        confirm = str(confirm.content).lower()

        if confirm == 'yes' or confirm == 'ye' or confirm == 'y':

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

        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return self.embed

    #   Set Role
    @command(name='sero')
    @has_permissions(manage_roles = True)
    async def SetMemberRole(self, ctx, member:Member, role, *, reason= None):

        #   Initializing variables
        srv = ctx.guild
        role = get(srv.roles, name=f'{role}')
        ch = get(srv.channels, name='auditlog')

        if not ch:
            ch = await ModerationChecks.CheckChannel(self, ctx, 'auditlog')

        #   Prepare, Send & Clean up embed
        self.embed.color = Colour.dark_red()
        self.embed.title = f'removing {member} from {role}'
        self.embed.description = f'Are you sure you\'d like to remove {member} from {role}?'

        await ctx.send(embed=self.embed)

        #   Clean up
        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        #   Retrieve the confirmation from the user
        confirm = await self.bot.wait_for('message')
        confirm = str(confirm.content).lower()

        if confirm == 'yes' or confirm == 'ye' or confirm == 'y':

            #  Prepare, remove, send & Clean up
            self.embed.color = Colour.dark_red()
            self.embed.title = f'{member} has been added to {role} by {ctx.author} due to {reason} '

            await member.add_roles(role)


    #   Change Color for the role
    @command(name='colro')
    @has_permissions(manage_roles = True)
    async def SetRoleColor(self, ctx, role, *, reason= None):

        #   Initializing classes
        dc = Dictionaries
        manager = RolePermissions

        #   Initializing variables
        srv = ctx.guild
        ch = get(srv.channels, name= 'auditlog')
        findRole = get(srv.roles, name = f'{role}')

        if not ch:
            ch = await ModerationChecks.CheckChannel(self, ctx, 'auditlog')

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
        answer = str(response.content).lower().replace(" ", "")

        if answer == 'darkpurple': color = dc.RoleColours(answer)
        else: color=Colour.default()

        await srv.edit_role(name=f'{role}', color = color, reason = f'{reason}')
        self.embed.title = f'@{role}'
        self.embed.description = f'has been succsessfully changed color.'

        #   Prepare, send, clean up & role creation
        
        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        return