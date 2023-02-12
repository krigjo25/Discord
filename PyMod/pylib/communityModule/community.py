#   Python Repositories
import os
import random as r
from dotenv import load_dotenv

#   Discord Repositories
import aiohttp

from discord.utils import get
from discord.colour import Color
from discord.embeds import Embed
from discord.ext.commands import Cog, command

load_dotenv()

class CommunityModule(Cog, name='Community Module'):

    """
        #   Information about the bot
        #   Member list
        #   Reddit meme
    """

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())


    #   Bot Info
    @command(name="botinfo")
    async def BotInfo(self, ctx, arg=None):

        '''
            Retrive infomation about the bot
        '''

        botName = 'PyMod'

        if arg == "log":

            self.embed.title = 'Change log'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{botName}/changelog.md'
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

        await ctx.send(embed = self.embed)

        #   Clear some memory
        self.embed.clear_fields()

        del arg, botName

        return

    #   Online members
    @command(name='mlist', pass_context=True)
    async def MembersList(self, ctx, arg = None):

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
        self.embed.clear_fields()

        return

#   Random Meme
    @command(name='meme', pass_context= True)
    async def GetRedditMeme(self, ctx):

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

                self.embed.clear_fields()
                self.embed.set_image(url= '')
        
        #   Save some memories
        del response, post

        return

#   Random Number
    @command (name='randint')
    async def randomInt(self, ctx, *arg):

        """
            #   Generates a random integer 
            #   between arg and argTwo
        """

        try :

            print(arg)
            if len(arg) < 0 or len(arg > 2): raise ValueError("Value has to be max and minimum 2 integers")
            
            for i in arg: 
                if str(i).isalpha(): raise TypeError('Can not use characters')

        except Exception as e :

            self.embed.title = "An Error Occured.."
            self.embed.description = f"{e}"
            await ctx.send(embed = self.embed)

        else:
    
            self.embed.title = "Generating random integer"
            self.embed.description = f"{arg[r.randrange(int(arg[0]), int(arg[1]))]}"
            await ctx.send(embed = self.embed)

        #   Clear some memory
        del arg

        return

#   Random Yes / No / Maybe

    @command (name='yesnomaybe')
    async def YesNoMaybe(self, ctx):

        '''
            #   Randomly choosing between yes, no maybe
        '''

        #   Creating a list to keep the words in
        array = ['Yes', 'No', "Maybe"]

        #   Randomizing the words
        r.shuffle(array)

        #   Prepare and send the embed
        self.embed.title = f"{array[r.randrange(0,2)]}"
        await ctx.send(embed=self.embed)

        #   save some memory
        del array

        return 


    #   List Roles
    @command(name='liro')
    async def ListRoles(self, ctx):

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
        self.embed.clear_fields()

        return

class CommunityFunctions():


    def ReadChangelog(self):

        #   Opens the changelog
        try :

            with open("pymod/changelog.md", "r") as f:

                #   Read x bytes
                changelog = f.read(415)

        #   Closing the document
            f.close()

        except Exception as e : print(e)

        #   Clear some memory
        del f

        return changelog