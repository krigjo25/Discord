#   Python Repositories
import datetime

#   Discord Repositories
from discord import utils
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, before_invoke, group, after_invoke, has_permissions


class InvokeBefore(): pass

class MiscModeration(Cog):

    def __init__(self, bot) -> None:
        self.embed = Embed()
        self.bot = bot

    @group(pass_contex = True)
    @has_permissions(manage_channels = True)
    async def misc(self, ctx): pass

    @misc.command()
    async def polls(self, ctx, title, ch):

        """

            #   Creating a poll with default two values to choose from
            #   Using reaction to vote
            #   Title of the poll, how many options and Questions

        """

        pass

    @misc.command()
    async def ServerBots(self, ctx):

        #   Fetching members
        for member in ctx.guild.members:

            #   Add emoji to status
            match member.status:
                case "idle": status = ":dash:"
                case "dnd": status = ":technologist:"
                case "Online": status = ":heart_on_fire:"
                case "offline": status = ":no:"

            #   Fetch user nick
            if str(member.nick) == None: nick = ''
            else: nick = f'Nick : {member.nick}\n'

            if member.bot == True: self.embed.add_field(name=f'{member.name} #{member.discriminator}',value=f'{nick}\n Status : {status}', inline=False)

        self.embed.title = 'Server Bots'
        self.embed.description = 'List of members'
        
        await ctx.send(embed = self.embed)
        
        self.embed.clear_fields()

    #   Announcements
    #   Modual dialog
    @misc.command()
    @has_permissions(administrator= True)
    async def Announcement(self, ctx, ch):

        #   Fetch the channel
        ch = utils.get(ctx.guild.channels, name=ch)

        try:
            if not ch : raise Exception(f"Channel \"{ch}\" Not found")

        except Exception as e:

            self.embed.color = Colour.dark_purple()
            self.embed.title = "An Exception Occured"
            self.description = f"{e}, try again."
            ctx.send(embed = self.embed)

            return

        else:
            #   Prepare & send embeded message
            self.embed.title = 'Server Announcement'
            self.embed.description = 'What would you like to announce?'
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            #   Get the user's message and procsess it
            message = await self.bot.wait_for('message')
            message = str(message.content)

            #   Prepare & Send the embed message
            self.embed.description = message
            self.embed.title = 'Server News announcement'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.set_author(name = f"By : {ctx.author.name}")
            
            await ch.send(embed=self.embed)

        del message, ch
        return

    @misc.command() #:x:
    @has_permissions(view_audit_log = True)
    async def Auditlog(self, ctx, limit = 3):
        
        #   Initializing variables


        t = 'test Kick'
        ch = utils.get(ctx.guild.channels, name='auditlog')
        array = []
        '''
            with open (f'audit_logs_{srv.name}') as f:
            async for entry in srv.audit_logs(limit=limit):
                f.write(f'{entry.user} did {entry.action} to{ entry.target} reason {entry.reason}')
        '''

        async for entry in ctx.guild.audit_logs(limit = limit):

            entries = { "AuditlogEntry":entry.id,
                        "AuditAction": entry.action,
                        "UserName": entry.user.name,
                        "UserDiscriminator": entry.user.discriminator,
                        "TargetName": entry.target.name,
                        "TargetDiscriminator": entry.target.discriminator,
                        "Reason": entry.reason,
                        "ExtraInformation": entry.extra,
                        "Nick": entry.category,
                        "Member Count": 3,}
            array.append(entries)

            #self.embed.add_field(name = f'{entry.user} did {entry.action}', value = f'{entry.target} reason {entry.reason} ')
        for i in array:

            print(i["Nick"],i["AuditlogEntry"], i["UserName"], i["UserDiscriminator"], i["AuditAction"], i["TargetName"], i["TargetDiscriminator"], i["ExtraInformation"], i["Reason"])

        del entries, array
        return