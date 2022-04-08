
#   Python Repositories
import sys
import traceback

from random import shuffle, randrange
#   Discord Repositories
import discord

from discord.embeds import Embed
from discord.ext.commands import Cog
from discord.errors import HTTPException 
from discord.ext.commands.help import HelpCommand
from discord.ext.commands.errors import CheckFailure, CommandNotFound, MissingRequiredArgument, BadArgument, MemberNotFound, CommandInvokeError

#   Asynico Repositories
from asyncio.exceptions import TimeoutError

class ErrorHandler(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.BadArgs = BadArgument
        self.timeOut = TimeoutError
        self.roleError = CheckFailure
        self.helpModule = HelpCommand
        self.NotFound = CommandNotFound
        self.attribute = AttributeError
        self.BadRequest = HTTPException
        self.invokeError = CommandInvokeError
        self.MemberNotFound = MemberNotFound
        self.misingargs = MissingRequiredArgument
        self.embed = Embed(color=discord.Colour.dark_purple())

    @Cog.listener()
        # Calls when there is an error
    async def on_command_error(self, ctx, error):
        '''
        The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.

        error: commands.CommandError
            The Exception raised.
        '''





        # Command Not Found
        if isinstance(error, self.NotFound):

                    # Dictionary for error messages to send insted of the "normal " one

            NotFound = {        0:'meep morp zeep :(\n',
                                1:'Tried to procsess your text, unfortuantly i couldn\'t understand you',
                                2:'Sir, you\'ve started the "Self destruction protocol", press "enter" to continue, press "esc" to stop.',
                                3:'Sir, im sorry, could you please repeat the command?',
                                4:'Sir The command has not been impleted in my software',
                                4:f'Sir where did you find the "{ctx.command}" ',
                                5:f'I have some good news, sir. Im a good boy, i didnt execute {ctx.command}',
                                6:f'We all do mistakes, sometimes.. There is no user with {ctx.author} name',
                                7: '0101010001101000011001010010000001100011011011110110110101101101011000010110111001100100001000000110010001101111011001010111001100100000011011100110111101110100001000000110010101111000011010010111001101110100'
                        }

            # Randomizing the dictonary, choose a random value and retrieve the value
            shuffle(NotFound)
            x = randrange(0,6)
            notFound = NotFound.get(x)

            # Send the message
            await ctx.send(f'{notFound}')
        
        # Role not satisified
        elif isinstance(error, self.roleError):

            # Dictionary for the error message to send insted of the normal one

            roleError = {   0:'meep, morp, meep :(\n',
                            1:f'lets do a rolePlay ',
                            2:'Unfortuantly you\'re not the right model we are looking for',
                            3:'Sir, im happy you love to play , I suggest you to do an audition.',
                            4:'010110010110111101110101001000000100010001101111001000000110111001101111011101000010000001101000011000010111011001100101001000000111010001101000011001010010000001110010011001010111000101110101011010010111001001100101011001000010000001110010011011110110110001100101'}

            # Randomizing the dictonary, choose a random value and retrieve the value
            shuffle(roleError)
            x = randrange(0,3)
            roleError = roleError.get(x)
            
            # Send the message
            await ctx.send(roleError)

        # MissingRequiredArgument
        elif isinstance(error, self.misingargs):
            
            cmd = str(ctx.command)
            
            # Dictionary for the error message to send insted of the normal one
            errorArguments = {  0:'meep, morp, meep :(\n',
                                1:'Sir, i just executed the command with-out any arguments...',
                                2:'Sir, should i just fake it?\n',
                                3:'More infomation would do my job easier..',
                                4:'Still missing some leads..',
                                5:'We all do mistakes. This time its not me, its you. ',
                            }

            # Randomizing the dictonary, choose a random value and retrieve the value
            shuffle(errorArguments)
            x = randrange(0,4)

            requiredArgs = errorArguments.get(x)

            
            # Checks which command is used

            #   Community

            if cmd == 'Randint' or cmd == 'randint':
                self.embed.title = '*randint (integer one) (integer two)'
                self.embed.description = requiredArgs
                await ctx.send(embed = self.embed)

            #   Minigames- Module
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


            #   Moderator-module
            elif cmd == 'Kick' or cmd == 'kick':

                self.embed.title = '*kick [member] [reason]'
                self.embed.url = 'https://www.dictionary.com/browse/kick#'
                self.embed.description = requiredArgs
                await ctx.send(embed = self.embed)

            elif cmd == 'Cls' or cmd == 'cls':
                self.embed.title = '*cls (channelid) (int)'
                self.embed.description = requiredArgs
                await ctx.send(embed=self.embed)
            
            elif cmd == 'Crech' or cmd == 'crech':
                self.embed.title = '*crech [ChannelName]'
                self.embed.description = requiredArgs
                await ctx.send(embed=self.embed)

            elif cmd ==  'Warn' or cmd == 'warn':
                self.embed.title = '*warn (name) (reason)'
                self.embed.description == requiredArgs
                await ctx.send(embed = self.embed)

            elif cmd ==  'Snooze' or cmd == 'snooze':
                self.embed.title = '*snooze (name) (sec) (reason)'
                self.embed.url = 'https://www.urbandictionary.com/define.php?term=snooze'
                self.embed.description == requiredArgs
                await ctx.send(embed = self.embed)
            
            #   Administrator module     
            elif cmd == 'Ban' or cmd == 'ban':
                self.embed.title = '*ban [member] [reason]'
                self.embed.url = 'https://www.dictionary.com/browse/ban'
                self.embed.description = requiredArgs
                await ctx.send(embed=self.embed)

            elif cmd == 'Announce' or cmd == 'announce':
                self.embed.title = '*announce (channelName)'
                self.embed.description = requiredArgs
                await ctx.send(embed = self.embed)

            elif cmd == 'Unban' or cmd == 'unban':
                self.embed.title = '*unban (Member Name)'
                self.embed.description = requiredArgs
                await ctx.send(embed = self.embed)
            
            else:
                # If the command is not listed 
                await ctx.send('Meep, Morp, Zeep')
        
        
        #The member is not found
        elif isinstance(error, self.MemberNotFound):

            # Dictionary for the error message to send insted of the normal one
            MemberMessage = {   0:'meep, morp, zeep :(\n',
                                1:'Sir, imagne the member where found\n',
                                2:'Sir, if the error continues, check your spelling \n',
                                3:'I regret to inform you, sir. the selected member does not exist, should i make one? \n',
                                4:'010110010110111101110101001000000100010001101111001000000110111001101111011101000010000001101000011000010111011001100101001000000111010001101000011001010010000001110010011001010111000101110101011010010111001001100101011001000010000001110010011011110110110001100101\n',
                                5:'I\'m the bot version for the 99th emoji !',
                                6:f'Just sent out an APB of {ctx.author}',
                                7:'We all do mistakes, this time the user doesn\'t exist',
                            }

            # Randomizing the dictonary, choose a random value and retrieve the value
            x = randrange(0,7)
            shuffle(MemberMessage)
            mError = MemberMessage.get(x)

            #   sends the message
            self.embed.title = 'Member were not Found in the server'
            self.embed.description = f'{mError}'
            await ctx.send(embed=self.embed)

        # Non Discord errors
        elif isinstance(error, self.invokeError):
            runTimeError = ' This time its my master\'s foulth. An issue report as been submitted, thank you for your patiency.'

           # Time-out
            if isinstance(error.original, self.timeOut):
                #   Dictionary for the error message to send insted of the normal one
                timeoutError =   {   
                                0:'meep, morp, zeep :(\n',
                                1:'Sir, the BOENG 437 just left the airport',
                                2:'Sir, do you need more time?',
                                3:f'The game is over, {ctx.author.mention} just ran out of time.',
                                4:'Try again',
                                5:'Decided to cancel the game.',
                                6:'Never got a response in time'
                                
                            }

                # Randomizing the dictonary, choose a random value and retrieve the value
                shuffle(timeoutError)
                x = randrange(0,5)
                timeout = timeoutError.get(x)
                

                # Send the message
                self.embed.title = 'The Game is over'
                self.embed.description = f'{timeout}'
                await ctx.send(embed=self.embed)

            elif isinstance(error.original, self.attribute):

                owner = self.bot.get_user(340540581174575107)
                await owner.send(f'Master, an attribute {self.attribute} error were found, in, {error.original}', tts = True)
                await ctx.send(f'{runTimeError}')
            
            elif isinstance(error.original, self.BadRequest):

                owner = self.bot.get_user(340540581174575107)
                await owner.send(f'Master, there were a bad request in, {error.original}', tts = True)
                await ctx.send(f'{runTimeError}')
            
            else:
                owner = self.bot.get_user(340540581174575107)
                await owner.send(f'Master, an undentified error were found, in, {error.original}', tts = True)
                await ctx.send(f'{runTimeError}')        
        else:
            # If none of the above, print it in the terminal
            print('Ignoring exception in command {}:\n'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)