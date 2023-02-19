#   Python Repositories
import os
import aiohttp
import random as r

#   Discord Repositories
from discord import SlashCommandGroup,ApplicationContext
from discord.colour import Colour
from discord.embeds import Embed
from discord.ext.commands import Cog


class CommunityModule(Cog, name='Community Module'):

    """
        #   Information about the bot
        #   Member list
        #   Reddit meme
    """

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Colour.dark_purple())

    community = SlashCommandGroup(name = "communitycommands", description = "Commands for the community")

    #   Bot Info
    @community.command()    #   Information about the bot
    async def botinfo(self, ctx: ApplicationContext, arg=None):

        '''
            Retrive infomation about the bot
        '''

        botName = 'PyMod'

        if arg == "log":

            self.embed.title = 'Change log'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{botName}/changelog.md'
            self.embed.description = CommunityFunctions().ReadChangelog()

        elif arg == "todo":

            self.embed.title = 'Pymod todo'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{botName}/todo.md'
            self.embed.description = CommunityFunctions().ReadChangelog()

        else:

            self.embed.title = f':notebook: About {botName}'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{botName}/readme.md'

            self.embed.add_field(name = ':rotating_light: Released', value=os.getenv('BotCreated'), inline=True)
            self.embed.add_field(name = ':new: Updated', value=os.getenv('PyModUpdated'), inline=True)
            self.embed.add_field(name = ':person_with_probing_cane: Current Version', value= os.getenv('PyModV'), inline=True)
            self.embed.add_field(name = ':toolbox: Responsory', value=os.getenv('Responsory'), inline=True)
            self.embed.add_field(name = ':cloud: Hosted', value=os.getenv('Hosted'), inline=True)
            self.embed.add_field(name = ':man: Master', value=f'{self.bot.get_user(340540581174575107)} :flag_no:', inline=True)
            self.embed.add_field(name = ':arrows_counterclockwise: Server Counting', value=f'Watching **{len(self.bot.guilds)}** Discord Servers', inline=True)
            self.embed.add_field(name = ':thought_balloon: To do list', value = '[Future projects](https://github.com/krigjo25/Discord/projects/1)', inline=True)
            self.embed.add_field(name = "Bot's latency :", value = round(self.bot.latency * 1000), inline = True)

        await ctx.respond(embed = self.embed)

        #   Clear some memory
        del arg, botName

        return

    #   Online members
    @community.command() #  List of online members
    async def list(self, ctx, arg = None):

        """
            #   Retrive List of server members
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
        await self.ClearMemory()

        return

#   Random Meme
    @community.command()    #   Memes
    async def reedditmeme(self, ctx):

        """
            #   Generates a random meme from reddit
        """

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as response:
                response = await response.json()
                post = response['data']['children'][r.randrange(0, 24)]
                self.embed.title = post["data"]["title"]
                self.embed.url = 'https://www.urbandictionary.com/define.php?term=Reddit'
                #self.embed.set_author(name = "")
                self.embed.set_image(url=post['data']['url'])
                self.embed.description = f'Hot meme porn from  {ctx.author.name}'
                await ctx.send(embed=self.embed)

                await self.ClearMemory()
        
        #   Save some memories
        del response, post

        return

#   Random Number
    @community.command()
    async def random(self, ctx, arg1, arg2):

        """
            #   Generates a random integer 
            #   between arg and argTwo
        """
        arg = []
        arg.append(arg1)
        arg.append(arg2)

        try :

            if len(arg) < 2 or len(arg > 2): raise Exception("You have to insert exact two integers")
            for i in arg:
                print(i)
                for j in i:
                    print(j)
            if not str(arg).isdigit(): raise Exception('Can not use characters')
        

        except Exception as e :

            self.embed.title = "An Error Occured.."
            self.embed.description = f"{e}"
            await ctx.send(embed = self.embed)

        else:
    
            self.embed.title = "Generating random integer"
            self.embed.description = f"{r.randrange(int(arg[0]), int(arg[1]))}"
            await ctx.send(embed = self.embed)

        #   Clear some memory
        del arg, arg1, arg2
        #await self.ClearMemory()

        return

    @community.command()
    async def report(self, ctx): 
        #   Modual dialog
        #   Topics to choose from : Report a server member, contact the staff, Misc, report a bug
        return

    #   List Roles
    @community.command()
    async def roles(self, ctx):

        '''
            #   Retrieve the roles
            2 :x:   Check if its a member or bot role (only member roles)
            3 :x:  Mentioned
            4   send embed into the channel
        '''

        #   Initializing variables
        x = 1

        #   Iteration over the ctx guild roles
        print(ctx.guild.roles)
        for role in ctx.guild.roles:

            #   Adding a embed field.
            self.embed.add_field(name = f'Role No.{x}', value=f'{role.mention}')

            #   Increasing by one
            x += 1

        #   Prepare & Send embed message
        self.embed.title = 'Server roles'
        await ctx.send(embed=self.embed)

        #   Clear some memory
        del x
        await self.ClearMemory()

        return

class CommunityFunctions():


    def ReadChangelog(self):

        #   Opens the changelog
        try :

            with open("changelog.md", "r") as f:

                #   Read x bytes
                changelog = f.read(415)

        #   Closing the document
            f.close()

        except Exception as e : print(e)

        #   Clear some memory
        del f

        return changelog