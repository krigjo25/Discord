
# Python Responsories

import sys
import traceback
from random import randint, randrange, shuffle

#   Asynico Responsories
from asyncio.exceptions import TimeoutError

#   Discord Responsories
import discord
from discord.embeds import Embed
from discord.ext.commands import Cog
from discord.ext.commands.errors import CheckFailure, CommandNotFound, MissingRequiredArgument, BadArgument, MemberNotFound, CommandInvokeError

class ErrorHandler(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=discord.Colour.dark_red())


    @Cog.listener()

        #   Calls when there is an error
    async def on_command_error(self, ctx, error):

        '''
            The event triggered when an error is raised while invoking a command.
            Parameters

            ctx:    commands.Context
                The context used for command invocation.

            error:  commands.ErrorDictionary
                The Exception raised.

        '''
       #    Classes initialization

        BadArgs = BadArgument
        timeout = TimeoutError
        roleError = CheckFailure
        NotFound = MemberNotFound
        attribute = AttributeError
        #HttpRequest = HTTPException
        cmdError = CommandDictionary
        cmdNotFound = CommandNotFound
        invokeError = CommandInvokeError
        misingargs = MissingRequiredArgument
 
        dmCreator = self.bot.get_user(340540581174575107)

            #   Member Not Found 
        if isinstance(error, NotFound):

                        # Prepare and send the embed
            dictionary = cmdError.ErrorDictionary(NotFound)

            self.embed.title = 'Member were not Found in the server'
            self.embed.description = f'{dictionary}'
            await ctx.send(embed=self.embed)
        
            #   Role not satisified
        elif isinstance(error, roleError):


            # Prepare and send the embed
            dictionary = cmdError.ErrorDictionary(roleError)

            self.embed.title = 'Unauthorized Role'
            self.embed.description = f'{dictionary}'
            await ctx.send(embed=self.embed)

        #   MissingRequiredArgument
        elif isinstance(error, misingargs):

            #   Initializing variables
            cmd = str(ctx.command)

            errorModule = str(misingargs)
            requiredArgs = cmdError.ErrorDictionary(errorModule[36:59], cmd)

            #   Checking which command its in the dictionary or not

            #   Community
            if cmd == 'Randint' or cmd == 'randint':
                self.embed.title = '*randint (integer one) (integer two)'
                self.embed.description = requiredArgs
                await ctx.send(embed = self.embed)

            #   Minigames Module
            elif cmd == 'Int' or cmd == 'int':
                self.embed.title = '*int (easiest / easy / normal / hard / kimpossible)'
                self.embed.description = requiredArgs
                await ctx.send(embed = self.embed)

            elif cmd == 'Ask' or cmd == 'ask':
                self.embed.title = '*ask (question)'
                self.embed.description = requiredArgs
                await ctx.send(embed = self.embed)
            
            elif cmd == 'Afk' or cmd == 'afk':
                self.embed.title = '*afk (Status update)'
                self.embed.description = requiredArgs
                await ctx.send(embed = self.embed)
            
            else:
                # If the command is not listed 
                await ctx.send('Meep, Morp, Zeep')
        
        
        #   Command Not Found
        elif isinstance(error, cmdNotFound):

            #   Prepare and send the embed
            cmd = str(ctx.command)
            errorModule = str(cmdNotFound)
            dictionary = cmdError.ErrorDictionary(errorModule[36:51], cmd)

            self.embed.title = 'Command were not Found in the dictionary'
            self.embed.description = f'{dictionary}'
            await ctx.send(embed=self.embed)

        #   Non Discord errors
        elif isinstance(error, invokeError):

           # Timeout
            if isinstance(error.original, timeout):
 
                #   Prepare & Send the message
                timeout = str(timeout)
                dictionary = cmdError.ErrorDictionary(timeout[27:39])

                self.embed.title = 'The Game is over'
                self.embed.description = f'{dictionary}'
                await ctx.send(embed=self.embed)

            elif isinstance(error.original, attribute):

                #   Prepare and send the embed
                errorModule = str(attribute)
                dictionary = cmdError.ErrorDictionary(errorModule[8:22])

                self.embed.title = 'Attribute error'
                self.embed.description = f'{dictionary}'
                await ctx.send(embed=self.embed)

                if dmCreator != None:
                    await dmCreator.send(f'Master, an attribute {attribute}. Error were found, in, {error.original}', tts = True)
                else:
                    print(dmCreator)

            elif isinstance(error.original, BadArgs):

                #   Prepare and send the embed
                BadArgs = str(BadArgs)
                dictionary = cmdError.ErrorDictionary(BadArgs)
                self.embed.title = 'You sent me a Bad Arguments'
                self.embed.description = f'{dictionary}'
                await ctx.send(embed=self.embed)
   
                if dmCreator != None:
                    await dmCreator.send(f'Master, Some Bad Arguments appeard {BadArgs}. Error were found, in, {error.original}', tts = True)
                else:
                    print(dmCreator)

            else:

                print(error.original)

                #   Prepare and send the embed
                #dictionary = cmdError.ErrorDictionary()
                #self.embed.title = 'Unkown Error appeared'
                #self.embed.description = f'{dictionary}'
                #await ctx.send(embed=self.embed)

                if dmCreator != None:
                    await dmCreator.send(f'Master, an Unknown Error appeard. Error were found in, {error.original}', tts = True)
                else:
                    print(dmCreator)

        else:

            # If none of the above, print it in the terminal
            print('Ignoring exception in command {}:\n\n'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

class CommandDictionary():
    def __init__(self) -> None:
        pass

    def ErrorDictionary (errorModule, *cmd):

        if errorModule == 'CommandNotFound':

            dictionary = {
                            1:'meep morp zeep :(\n',
                            2:'Given command does not exists',
                            3:'Sir, have you drunken to much?',
                            4:'We all do mistakes, sometimes...',
                            5:f'Sir where did you find the "{cmd}" ',
                            6:'Sir, im sorry, could you please repeat the command?',
                            7:'Sir The command has not been impleted in my software',
                            8:'Command Executed, if you see this message, check your spelling.',
                            9:'I have some good news, sir. Im a good boy. Command already executed {cmd}',
                            10:f'Sir, an error has emerged \"{cmd}\" were not found in bot command dictionary',
                            11:'Sir, you\'ve started the "Self destruction protocol", press "enter" to continue, press "esc" to stop.',
                            12:'0101010001101000011001010010000001100011011011110110110101101101011000010110111001100100001000000110010001101111011001010111001100100000011011100110111101110100001000000110010101111000011010010111001101110100',
}

        elif errorModule == 'MemberNotFound':

            dictionary = {
                            1:'meep, morp, zeep :(\n',
                            2:'Sir, imagne the member where found\n',
                            3:'Sir, if the error continues, check your spelling \n',
                            4:'I regret to inform you, sir. the selected member can not be found in the dictionary, should i make one? \n',
                            5:'010110010110111101110101001000000100010001101111001000000110111001101111011101000010000001101000011000010111011001100101001000000111010001101000011001010010000001110010011001010111000101110101011010010111001001100101011001000010000001110010011011110110110001100101\n',
                            6:'I\'m the bot version for the 99th emoji !',
                            7:f'Just sent out an APB.',
                            8:'We all do mistakes, this time the user doesn\'t exist',
}

        elif errorModule == 'CheckFailure':

            dictionary = {
                            1:'meep, morp, zeep :(\n',
                            2:'Role access Denied.',
}
                            

        elif errorModule == 'MissingRequiredArgument':

            dictionary = {
                            1:'meep, morp, meep :(\n',
                            2:'Sir, i just executed the command with-out any arguments...',
                            3:'Sir, should i just fake it?\n',
                            4:'More infomation would do my job easier..',
                            5:'Still missing some leads..',
                            6:'We all do mistakes. You\'re missing some requred arguments ',
}

        elif errorModule == 'AttributeError':

            dictionary = {
                            1:'meep, morp, zeep :(\n',
                            2:'Sir, the BOENG 437 just left the airport',
                            3:'Sir, do you need more time?',
                            4:'The game is over',
                            5:'Try again',
                            6:'I decided to cancel the game.',
                            7:'Never got a response in time',
}



        elif errorModule == 'TimeoutError':

            dictionary = {
                            1:'meep, morp, zeep :(\n',
                            2:'Sir, the BOENG 437 just left the airport',
                            3:'Sir, do you need more time?',
                            4:'The game is over',
                            5:'Try again',
                            6:'I decided to cancel the game.',
                            7:'Never got a response in time',
}

        else:
            print(errorModule)
            dictionary = {
                            1:f'Something went wrong with {errorModule}',
                            2:'The content has a False value',
}

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1, x)


        return dictionary.get(x)