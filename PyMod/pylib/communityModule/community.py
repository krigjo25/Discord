#   Python Repositories
import os
import aiohttp
import random as r

#   Discord Repositories
import discord as d
from discord import SlashCommandGroup, ApplicationContext
from discord.colour import Colour
from discord.embeds import Embed
from discord.ext.commands import Cog

#custom responsories
from pylib.moderation.modal import Member


class CommunityModule(Cog, name='Community Module'):

    """
        #   Author : krigjo25
        #   Date : 19.02-23
        #   last updated : 21.02-23

        Class contains community commands
        botinfo,        -   Information about the bot
        member,         -   A list of online / offline members
        meme,           -   Meme (optional args : reddit)
        report,         -   Reporting a server member using modals
        support,        -   Support ticket using modals
        roles           -   A list of server roles
    """

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Colour.dark_purple())

    community = SlashCommandGroup(name = "communitycommands", description = "Commands for the community")

    @community.command()#   Information about the bot :bug:
    async def botinfo(self, ctx: ApplicationContext, arg:d.Option(str, "Optional arguments (log / todo / bug)", required = False)):

        '''
            Information about the bot

            #   Arguments (log / todo / None)
            #   Changelog
            #   ToDo list
        '''

        if arg == "log":

            self.embed.title = f"{ctx.bot.user.name} change log"
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{ctx.bot.user.name}/changelog.md'
            self.embed.description = CommunityFunctions().Readlog(arg)

        elif arg == "todo":

            self.embed.title = f"{ctx.bot.user.name} todo"
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{ctx.bot.user.name}/todo.md'
            self.embed.description = CommunityFunctions().Readlog(arg)

        elif arg == "bug":
            modal = Community(title = "Bug Report")
            ctx.send_modal(modal)
        else:

            self.embed.title = f':notebook: About {ctx.bot.user.name}'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{ctx.bot.user.name}/readme.md'

            self.embed.add_field(name = ':rotating_light: Released', value = os.getenv('BotCreated'), inline=True)
            self.embed.add_field(name = ':new: Updated', value = os.getenv('PyModUpdated'), inline=True)
            self.embed.add_field(name = ':person_with_probing_cane: Current Version', value = os.getenv("Version"), inline=True)
            self.embed.add_field(name = ':toolbox: Responsory', value = os.getenv('Responsory'), inline=True)
            self.embed.add_field(name = ':cloud: Hosted', value = os.getenv('Hosted'), inline=True)
            self.embed.add_field(name = ':man: developed by', value = f'{ctx.bot.get_user(340540581174575107)} :flag_no:', inline=True)
            self.embed.add_field(name = ':arrows_counterclockwise: Server Counting', value = f'Watching **{len(ctx.bot.guilds)}** Discord Servers', inline=True)
            self.embed.add_field(name = "Bot's latency :", value = round(ctx.bot.latency * 1000), inline = True)

        await ctx.respond(embed = self.embed)

        del arg#   Clear some memory

        return

    @community.command()#  List of online members
    async def members(self, ctx: ApplicationContext, arg:d.Option(str, "Optional arguments (on / off / bot)", required = False)):

        """
            List of server members
        """

        self.embed.title = 'Server Members'

        #   Fetching members
        for member in ctx.guild.members:

            if arg == "on" and member.bot == False:

                if str(member.status) != "offline":

                    #   Add emoji to status
                    match str(member.status):
                        case "online" : status = ":heart_on_fire:"
                        case "idle" : status = ":dash:"
                        case "dnd": status = ":technologist:"

                if member.nick == None: self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'Status : {status} ', inline=False)
                else :self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'Nick {member.nick} Status : {status} ', inline=False)

            elif arg =="off" and member.bot == False:
            
                if str(member.status) == "offline":

                    if member.nick == None: self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'Status : {status} ', inline=False)
                    else: self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'Nick {member.nick}\nStatus : {status} ', inline=False) 

                else: self.embed.description = "Everyone is online"

            elif arg == "bot" and member.bot == True:

                self.embed.title = "Server bots"
                #   Add emoji to status
                match str(member.status):
                    case "online" : status = ":heart_on_fire:"
                    case "idle" : status = ":dash:"
                    case "dnd": status = ":technologist:"

                if member.nick == None: self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'Status : {status} ', inline=False)
                else :self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'Nick {member.nick} Status : {status} ', inline=False)

            else:

                if member.bot == False:

                    #   Add emoji to status
                    match str(member.status):
                        case "online" : status = ":heart_on_fire:"
                        case "idle" : status = ":dash:"
                        case "dnd": status = ":technologist:"
                        case "offline" : status =":sleeping:"

                    if member.nick == None: self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'Status : {status} ', inline=False)
                    else : self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'Nick {member.nick} Status : {status} ', inline=False)

        self.embed.add_field(name = "== End Of List ==", value=" ")
        await ctx.send(embed = self.embed)

        #   Clear some memories
        del member, status

        return

    @community.command()#   Memes
    async def meme(self, ctx: ApplicationContext, arg:d.Option(str, "Optional arguments (reddit)", required = False)):

        """
            Generates a random meme
        """

        meme = ["reddit"]
        if arg == None:arg = meme[r.randint(len(meme - 1))]

        match str(arg).lower():

            case "reddit":
                async with aiohttp.ClientSession() as cs:
                    async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as response:
                        response = await response.json()
                        post = response['data']['children'][r.randrange(0, 24)]
                        self.embed.title = post["data"]["title"]
                        self.embed.url = 'https://www.urbandictionary.com/define.php?term=Reddit'
                        self.embed.set_image(url=post['data']['url'])
                        self.embed.description = f'Hot meme porn from  {ctx.author.name}'
                        await ctx.respond(embed=self.embed)

                del response, post, cs, arg#   Clear some memory

        return

    @community.command()
    async def report(self, ctx:ApplicationContext):
        """
            Reporting a rule voilator by a modal
        """
        modal = Member(title = "Member Report")
        await ctx.send_modal(modal)
        #   Modual dialog

        return

    @community.command()
    async def support(self, ctx:ApplicationContext): 

        """
            Member Support
        """
        modal = Member(title = "Member Support")
        await ctx.send_modal(modal)
        #   Modual dialog
        #   Topics to choose from : Report a server member, contact the staff, Misc, report a bug
        return

    #   List Roles
    @community.command()
    async def roles(self, ctx:ApplicationContext):

        '''
            Retrieve a list of the server roles

            #   Initialize the variables
            #   Iterate through server roles
            #   respond to the command
        '''

        x = 1#   Initializing variable

        self.embed.title = 'Server roles'
        for role in ctx.guild.roles:#   for each role in guild.role 
            self.embed.add_field(name = f'Role No.{x}', value=f'{role.mention}')#   Adding a embed field.
            x += 1#   Increasing by one

        await ctx.respond(embed = self.embed)

        del x, role#   Clear some memory

        return

    @community.after_invoke
    async def clear_memory(self, ctx: d.ApplicationContext):

        #   Clearing embeds
        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.description = " "
        self.embed.remove_thumbnail()
        self.embed.color = Colour.dark_purple()

        del ctx #   Clearing some memory
        return

class CommunityFunctions():

    def Readlog(self, arg):

        match arg:
            case "log":
                try :#   Opens the changelog

                    with open("changelog.md", "r") as f:

                        log = f.read(415)#    Read x lines
                        f.close()#  Closing the document
                
                except Exception as e :

                    f.close()#  Closing the document
                    embed = Embed(title = "An Exception Occoured", description = e, color = d.Colour.dark_red()) 
                    return embed

            case "todo":
 
                try :#   Opens the changelog

                    with open("todo.md", "r") as f:

                        log = f.read(415)#    Read x lines
                        f.close()#  Closing the document

                except Exception as e :

                    f.close()#  Closing the document
                    embed = Embed(title = "An Exception Occoured", description = e, color = d.Colour.dark_red())

                    return embed

        del f#   Clear some memory

        return log