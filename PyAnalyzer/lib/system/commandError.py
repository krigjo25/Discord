# Python Responsories
import sys
import traceback
import random as r

#   Asynico Responsories
from asyncio.exceptions import TimeoutError

#   Discord Responsories
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog
from discord.ext.commands.errors import CheckFailure, CommandNotFound, MissingRequiredArgument, BadArgument, MemberNotFound, CommandInvokeError

class ErrorHandler(Cog):

    """
        #   raises when there is an error in the code.
    """

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_red())

        return

    #   Calls when there is an error
    @Cog.listener()
    async def on_command_error(self, ctx, error):

        '''
            #   Triggers when an error is raised while invoking a command.Parameters

            #   ctx:    commands.Context
            #   #   The context used for command invocation.

            #   commands.ErrorDictionary
            #   #   The Exception which will be raised.

        '''

       #    Classes initialization
        cmdError = ErrorMessageDictionary()

        botDM = await self.bot.fetch_user(340540581174575107)
        botmsg = None

        #   Member not found 
        if isinstance(error, CommandNotFound):

            error = str(CommandNotFound)[36:51]
            try:
                self.embed.title = '404: Command Not Found'
                self.embed.description = cmdError.ErrorDescriptionDictionary(error)
            
            except (TypeError, Exception) as e : print(e)

            else :
                await ctx.send(embed=self.embed)

        #   Role not satisified
        elif isinstance(error, CheckFailure):

            try: 
                self.embed.title = 'Unauthorized Role'
                self.embed.description = cmdError.ErrorDescriptionDictionary(str(CheckFailure))

            except Exception as e : print(e)

            else :
                await ctx.send(embed=self.embed)

        #   MissingRequiredArgument
        elif isinstance(error, MissingRequiredArgument):

            """
                #   Checking if there is any dictionary for the command.
                #   If a command is not listed send message to the bot maintainer.
                #   Notify the user, about the inconvinience
            """

            try: 
                self.embed.title = cmdError.CommandNameError(str(ctx.command).lower())
                self.embed.description = cmdError.ErrorDescriptionDictionary(str(MissingRequiredArgument)[36:59])

            except Exception as e : print(e)

            else :
                await ctx.send(embed=self.embed)

        #   Command Not Found
        elif isinstance(error, CommandNotFound):

            try: 
                self.embed.title = "404: Command were not found in the dictionary"
                self.embed.description = cmdError.ErrorDescriptionDictionary(str(CommandNotFound)[36:51])
                
            except Exception as e : print(e)

            else :
                await ctx.send(embed=self.embed)

        #   Non Discord errors
        elif isinstance(error, CommandInvokeError):

            if isinstance(error.original, TimeoutError):
 
                #   Prepare & Send the message
                try:
    
                    self.embed.title = "The Game is over"
                    self.embed.description = cmdError.ErrorDescriptionDictionary(str(TimeoutError)[27:39])
                except Exception as e : print(e)
                else :

                    await ctx.send(embed=self.embed)

            elif isinstance(error.original, AttributeError):

                try:
                    self.embed.title = "Attribute Error"
                    self.embed.description = cmdError.ErrorDescriptionDictionary(str(AttributeError)[8:22])
                
                except Exception as e: print(e)
                else:
                    botmsg = f"Master, there is an error with an {str(AttributeError)[8:22]} Error were found. {error.original}"
                    await ctx.send(embed=self.embed)

            elif isinstance(error.original, BadArgument):

                #   Prepare & send the embed
                try:
                    self.embed.title = "Recieved Bad Arguments"
                    self.embed.description = cmdError.ErrorDescriptionDictionary(str(BadArgument))

                except Exception as e: print(e)
                else:

                    botmsg = f"Master, There is some  {str(BadArgument)} Error were found. {error.original}"
                    await ctx.send(embed=self.embed)

        else:

            #   Print the output in the terminal
            print(f"Ignoring exception in command {ctx.commands}:\n\n", file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        if botmsg != None: await botDM.send(botmsg)

        #   Clear some memory
        del botDM, botmsg, error, cmdError
        return

class ErrorMessageDictionary():

    def __init__(self) -> None:
        pass

    def ErrorDescriptionDictionary (self, error, *cmd):
        errorm = [   "CommandNotFound", "MemberNotFound", "MissingRequiredArgument",
                    "AttributeError", "TimeoutError"] 
        try:

            if error not in errorm : raise Exception(error) 

        except Exception as e :
            print(f"Did not reconize the error :\n{e}")

            #   Clear some memory
            del errorm, error

            return

        else:

            match error:

                case "CommandNotFound":
                    dictionary = {
                                    1:'meep morp zeep :(',
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

                case "MemberNotFound":

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

                case "CheckFailure":

                    dictionary = {
                                    1:'meep, morp, zeep :(',
                                    2:'Role Authorication failed.',
                                }

                case "MissingRequiredArgument":

                    dictionary = {
                                    1:'meep, morp, meep :(\n',
                                    2:'Sir, i just executed the command with-out any arguments...',
                                    3:'Sir, should i just fake it?\n',
                                    4:'More infomation would do my job easier..',
                                    5:'Still missing some leads..',
                                    6:'We all do mistakes. You\'re missing some requred arguments ',
                                }

                case "AttributeError":

                    dictionary = {
                                    1:'meep, morp, zeep :(\n',
                                    2:'Sir, Something went horribly wrong',
                                    3:'I found out i didnt want to start after all',
                                }

                case "TimeoutError":

                    dictionary = {
                                    1:'meep, morp, zeep :(\n',
                                    2:'Sir, the BOENG 437 just left the airport',
                                    3:'Sir, do you need more time?',
                                    4:'The game is over',
                                    5:'Try again',
                                    6:'I decided to cancel the game.',
                                    7:'Never got a response in time',
                                }

            #   Clear some memory
            del error, errorm, cmd

        return dictionary.get(r.randrange(1, len(dictionary)))

    def CommandNameError(self, cmd):

        prefix = '?'

        dictionary = {
                        #   Community Module
                        'dnd':f'{prefix}{cmd} (message)',
                        'randint':f'{prefix}{cmd} (integer one) (integer two)',

                        #   Moderator module
                        'poll':f'{prefix}{cmd} (poll Name) (ChannelName)',
                        'online':f'{prefix}{cmd} optional (on/off)',
                        'kick':f'{prefix}{cmd} (MemberName) (reason)',
                        'member warn':f'{prefix}Member Warn (MemberName) (reason)',
                        'member sush':f'{prefix}Member Sush (MemberName) (1(s / m / d / w / y)) (reason)',
                        'member lift':f'{prefix}Member Lift (MemberName)',

                        #   Role Management
                        'role delete':f'{prefix}role Delete (RoleName)',
                        'role create':f'{prefix}role Create (RoleName)',
                        'role demoteremro':f'{prefix}{cmd} role Promote (MemberName) (RoleName)',
                        'sero':f'{prefix}{cmd} (MemberName) (roleName) optional (reason)',

                        #   Channel Management / message management
                        'ch zelete':f'{prefix}ch Delete (Channel Name)',
                        'ch create':f'{prefix}ch Create (Channel Name)',
                        'ch clear':f'{prefix}ch Clear (channelName) (x lines)',

                        #   Administrator module
                        'unban':f'{prefix}{cmd} (MemberName)',
                        'announce':f'{prefix}{cmd} (channelName)',
                        'ban':f'{prefix}{cmd} (MemberName) (reason)',
                    }
        return dictionary.get(cmd)
