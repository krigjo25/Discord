#   Python Repositories
import datetime

#   Discord Repositories
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, before_invoke, group, after_invoke, has_permissions


class InvokeBefore(): pass
class ModerationChecks(Cog):

    def __init__(self, bot):

        self.bot = bot
        self.now= datetime.datetime.strftime('%H:%M, %d.%b - %y')  
        self.embed = Embed(color=Colour.dark_purple(), description= '')

class miscModeration(Cog):

    def __init__(self) -> None:
        self.embed = Embed()

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

    #   Checking wheter whom is offline and online
    @misc.command()
    async def Members(self, ctx, args=None):

        array = ["None", "on", "off"]

        try:

            if args != None:str(args).lower()
            
            if args not in array: raise Exception("Available parameters \"on\", \"off\"")
            elif str(args).isdigit(): raise ValueError("The value can not consist of digits")

        except Exception as e :

            self.embed.title = "An exception arised"
            self.embed.description = f"{e}"
            ctx.send(embed = self.embed)

            # Clear some memory
            del args, array, e

            self.embed.clear_fields()
            self.embed.colour = Colour.dark_purple()

        else :

            if args == "None":

                #   Fetching members
                for member in ctx.guild.members:
                        
                    #   Add emoji to status
                    match str(member.status):

                        case "dnd": status = ":technologist:"
                        case "idle": status = ":dash:"
                        case "online": status = ":heart_on_fire:"
                        case "offline": status = ":sleeping:"

                    #   Fetch user nick
                    if member.nick == None: nick = ''
                    else: nick = f'Nick : {member.nick}\n'

                    if member.bot == False: 
                        self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {self.warn}', inline=False)

            elif args == "on":

                #   Fetching members
                for member in ctx.guild.members:

                    #   Add emoji to status
                    match member.status:
                        case "offline" : off = False
                        case "idle" : status = ":dash:"
                        case "dnd" : status = ":technologist:"
                        case "online" : status = ":heart_on_fire:"

                    #   Fetch user nick
                    if member.nick == None: nick = ''
                    else: nick = f'Nick : {member.nick}\n'

                    if off != False & member.bot == False: self.embed.add_field(name=f'{member.name}, #{member.discriminator}',value=f'{nick}\n Status : {status}', inline=False)

            elif args == 'off':

                #   Fetching members
                for member in ctx.guild.members:

                    #   Add emoji to status
                    if member.status == 'offline': 

                            status = ":sleeping:"
                            off = True
                    else : off = False

                    #   Fetch user nick
                    if member.nick == None :nick = ''
                    else: nick = f'Nick : {member.nick}\n'

                    if off == True and member.bot == False: self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick}\n Status : {status}', inline=False)

            self.embed.title = 'Server Members'
            self.embed.description = 'List of members'
            await ctx.send(embed = self.embed)

        #   Clear memory
        del args, array, nick
        del status

        return

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
