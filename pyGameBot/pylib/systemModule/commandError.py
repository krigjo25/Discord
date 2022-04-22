
# Python Responsories

import sys
import traceback
from random import randrange

#   Asynico Responsories
from asyncio.exceptions import TimeoutError

#   Discord Responsories

from discord.colour import Color
from discord.embeds import Embed
from discord.ext.commands import Cog
from discord.ext.commands.errors import CheckFailure, CommandNotFound, MissingRequiredArgument, BadArgument, MemberNotFound, CommandInvokeError

class ErrorHandler(Cog):

    def __init__(self, bot):
        self.bot = bot

        self.embed = Embed(color=Color.dark_red())

        return

    @Cog.listener()

        #   Calls when there is an error
    async def on_command_error(self, ctx, error):
        '''
            The event triggered when an error is
            raised while invoking a command.Parameters

            ctx:    commands.Context
                The context used for command invocation.

            error:  commands.ErrorDictionary
                    The Exception which will be raised.

        '''

       #    Classes initialization
        BadArgs = BadArgument
        timeout = TimeoutError
        roleError = CheckFailure
        NotFound = MemberNotFound
        attribute = AttributeError
        cmdNotFound = CommandNotFound
        invokeError = CommandInvokeError
        cmdError = ErrorMessageDictionary
        misingargs = MissingRequiredArgument

        botDM = await self.bot.fetch_user(340540581174575107)
        botmsg = None

        #   Member not found 
        if isinstance(error, NotFound):

            #   Prepare & send the embed
            dictionary = cmdError.ErrorDescriptionDictionary(NotFound)
            self.embed.title = 'Member were not Found in the server'
            self.embed.description = f'{dictionary}'
            await ctx.send(embed=self.embed)

        #   Role not satisified
        elif isinstance(error, roleError):

            # Prepare & send the embed
            dictionary = cmdError.ErrorDescriptionDictionary(roleError)
            self.embed.title = 'Unauthorized Role'
            self.embed.description = f'{dictionary}'
            await ctx.send(embed=self.embed)

        #   MissingRequiredArgument
        elif isinstance(error, misingargs):

            """     Missing arguments

                Checking if there is any dictionary for the command.
                if a command is not listed send message to the bot maintainer.
                and notify the user, about the inconvinient

            """

            #   Initializing variables
            cmd = str(ctx.Command)
            errorModule = str(misingargs)

            #   Call Command list
            #   self.embed.title = cmdError.CommandList(cmd)
            #   await ctx.send(embed=self.embed)
            #   Community Module

            if cmd == 'Randint' or cmd == 'randint':
                self.embed.title = '*randint (integer one) (integer two)'

            #   Minigames Module
            elif cmd == 'Int' or cmd == 'int':
                self.embed.title = '*int (easiest / easy / normal / hard / kimpossible)'

            else:
                self.embed.title = 'Command Missing some required arguments'

            self.embed.description = cmdError.ErrorDescriptionDictionary(errorModule[36:59])
            await ctx.send(embed=self.embed)

        #   Command Not Found
        elif isinstance(error, cmdNotFound):

            #   Prepare and send the embed
            errorModule = str(cmdNotFound)

            self.embed.title = 'Command were not Found in the dictionary'
            self.embed.description = f'{cmdError.ErrorDescriptionDictionary(errorModule[36:51])}'
            await ctx.send(embed=self.embed)

        #   Non Discord errors
        elif isinstance(error, invokeError):

            #   Initializing variables

            if isinstance(error.original, timeout):
 
                #   Prepare & Send the message
                timeout = str(timeout)

                self.embed.title = 'The Game is over'
                self.embed.description = cmdError.ErrorDescriptionDictionary(timeout[27:39])
                await ctx.send(embed=self.embed)

            elif isinstance(error.original, attribute):

                #   Prepare and send the embed
                errorModule = str(attribute)

                self.embed.title = 'Attribute error'
                self.embed.description = cmdError.ErrorDescriptionDictionary(errorModule[8:22])
                await ctx.send(embed=self.embed)

                botmsg = f'Master, there is an error with an {errorModule[8:22]} Error were found. {error.original}'

            elif isinstance(error.original, BadArgs):

                #   Prepare & send the embed
                errorModule = str(BadArgs)
                botmsg = f'Master, There is some  {errorModule} Error were found. {error.original}'

                self.embed.title = 'You sent me a Bad Arguments'
                self.embed.description = cmdError.ErrorDescriptionDictionary(errorModule)
                await ctx.send(embed=self.embed)

                await self.bot.send(f'{botmsg}', tts = True)

        else:

            # If none of the above, print it in the terminal
            print('Ignoring exception in command {}:\n\n'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        if botmsg !=None: 
            await botDM.send(f'{botmsg}', tts = True)

        return

class ErrorMessageDictionary():
    def __init__(self) -> None:
        pass

    def ErrorDescriptionDictionary (errorModule, *cmd):

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
                            9:f'I have some good news, sir. Im a good boy. Command already executed {cmd}',
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
                            2:'Sir, Something went horribly wrong',
                            3:'I found out i didnt want to start after all',

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
