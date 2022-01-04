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


        # Prohbit a user to enter the channel again
    @command(name='Ban', help='prohbit a user to enter the channel again')
    @has_any_role('Admin', 'admin', 'Software-Technican')
    @has_permissions(ban_members= True)

    async def BanMember(self, ctx, member:Member, *, reason=None):

        if reason == None: # required a reason
            await ctx.send(f'Please provide me a reason to ban {member}')

        elif reason != None: # logs the reason
            #   1:  Logging the ban
            with open('krigjo25\\lib\\log\\ban-log.log', 'a') as f:
                f.write(f'{member} has been banned for {reason}, by {ctx.author.name} ban-date : {self.curTime}\n')

            #   2:  Creating a message to send the user, so he get a notice of the ban, and ban the member
            message = f'the Administrator Team has decided to probhid you for using  **{ctx.guild.name}** \n \n Due to :\n **{reason}**'
            await member.send(message)
            await member.ban(reason=reason)
        return


    #   allows a user to enter the channel again 
    @command(name='Unban', help='allow a user to enter the channel again')
    @has_any_role('Admin', 'admin', 'Software-Technican', 'Software-Technican')
    @has_permissions(administrator= True)

    async def UnBan(self, ctx, member:Member, reason=None):
        BannedUsers= await ctx.guild.bans()
        MemberName, member_discriminator = member.split('#')

        for entry in BannedUsers:
            user = entry.user

            if (user.name, user.discriminator) == (MemberName, member_discriminator):
                await ctx.guild.unban(user)
                
                message = f'the Administrator Team has decided to unban you out from  **{ctx.guild.name}**'
                await member.send(message)
                
            return
    #   Checking the logs
    @command(name='log', help='Read the ban or kick log')
    @has_any_role('Admin', 'admin', 'Software-Technican', 'Software-Technican')
    
    async def ReadClearLog(self, ctx, log, *args):

        log = str(log)
        args = str(args)
        if log == 'Ban':  # Opens and reads the ban log
            with open('krigjo25\\lib\\log\\ban-log.log', 'r') as f:
                self.embed.title = 'List of banned members'
                for i in f:
                    self.embed.description = f'`{i}`'
                    await ctx.send(embed=self.embed)

        elif log =='Kick': # Opens and reads the kick log
            with open('krigjo25\\lib\\log\\kick-log.log', 'r') as f:
                self.embed.title = 'List of Kicked members'
                for i in f:
                    self.embed.description = f'`{i}`'
                    await ctx.send(embed=self.embed)

        else:
            await ctx.send('Sir, the requested log could not be found !')

    @command(name= 'Clean', help= 'Cleans the log(s)')
    @has_any_role('Admin', 'admin', 'Software-Technican', 'Software-Technican')

    async def CleanLog(self, ctx, log):

            if log == 'Ban': # clearing the ban log

                with open('krigjo25\\lib\\log\\ban-log.log', 'w') as f:
                    f.write(f'Log has been cleared by {ctx.author.name}\n')
                await ctx.send(f'Sir, {ctx.author.name} i would like to notify you the ban log has been clared.')
        
            elif log == 'Kick': # clearing the kick log

                with open('krigjo25\\lib\\log\\kick-log.log', 'w') as f:
                    f.write(f'Ban log has been cleared by {ctx.author.name}\n')
                await ctx.send(f'Sir, {ctx.author.name} i would like to notify you the kick log has been clared.')

            elif log == 'Both': # Clears the both logs
                with open('krigjo25\\lib\\log\\kick-log.log', 'w') as f:
                    f.write(f'Cleared by {ctx.author.name}\n')

                with open('krigjo25\\lib\\log\\ban-log.log', 'w') as f:
                    f.write(f'Cleared by {ctx.author.name}')
                await ctx.send(f'Sir, {ctx.author.name} i would like to notify you the requested logs has been clared.')
            else:
                await ctx.send('Sir, the requested log could not be found !')

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

        await channel.send(message)

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
    
    @command(name='removeRole')
    @has_any_role('admin','Admin', 'Software-Technican')
    async def removeRole(self, ctx, ch ):
        pass
 
 
 
 