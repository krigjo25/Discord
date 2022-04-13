'''
# Name 
   CommandError.py

#  About
        Handling errors

# Author
    krigjo25

'''
import sys
import discord
import traceback

from discord.embeds import Embed
from discord.ext.commands import Cog
from discord.errors import HTTPException
from discord.ext.commands.errors import CheckFailure, CommandNotFound, MissingRequiredArgument, BadArgument, MemberNotFound, CommandInvokeError

from random import shuffle, randrange
from asyncio.exceptions import TimeoutError

class ErrorHandler(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=discord.Colour.dark_red())

    @Cog.listener()
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

        #   Initializing classes
        badboy = BadArgument()
        badReq = HTTPException()
        timeout = TimeoutError()
        cmdError = ErrorMessage()
        cmd404 = CommandNotFound()
        checkError = CheckFailure()
        #helpModule = HelpCommand ()
        member404 = MemberNotFound()
        attribute = AttributeError()
        
        req = MissingRequiredArgument()
        invokeError = CommandInvokeError()

        #   Initializing variables
        maintainer = self.bot.get_user(340540581174575107)

        if isinstance(error, cmd404):

            """
                Command Not found
            """

            #   Prepare & send embed message
            self.embed.title = 'Command Not found in the command dictionary'
            self.embed.description = cmdError.ErrorArguments(cmd404)
            await ctx.send(embed = self.embed)

        elif isinstance(error, checkError):

            """
                Check Failure
                when a role is not satisified for the command
            """

            #   Prepare & send embed message
            self.embed.title = 'Authorization failure'
            self.embed.description = cmdError.ErrorArguments(checkError)
            await ctx.send(embed = self.embed)

        elif isinstance(error, req):

            """         MissingRequiredArguments
                when you miss some arguments which is required.

            """

            cmd = str(ctx.command)

            #   Prepare & send the embed
            self.embed = cmdError.ErrorArguments(cmd)
            await ctx.send(embed = self.embed)

        #The member is not found
        elif isinstance(error, member404):

            #   Prepare & send embed message
            self.embed.title = '404 Member Not Found'
            self.embed.description = cmdError.ErrorArguments(member404)
            await ctx.send(embed = self.embed)

        # Non Discord errors
        elif isinstance(error, invokeError):

            """     RunTimeError

                Executes an error which takes place while
                a member is executing a command

            """

            runTimeError = ' This time its my master\'s foulth. An issue report as been submitted, thank you for your patiency.'

           # Time-out
            if isinstance(error.original, timeout):

                #   Prepare & send embed message
                self.embed.title = 'Had to long response time -.-'
                self.embed.description = cmdError.ErrorArguments(timeout)
                await ctx.send(embed = self.embed)

            elif isinstance(error.original, attribute):

                #   Prepare & send embed
                self.embed.title = 'Woups, seems like you found a badboy'
                self.embed.description = cmdError.ErrorArguments(badboy)
                await ctx.send(embed = self.embed)

                #   Prepare a report to the maintainer
                await maintainer.send(f'Master, an attribute {self.attribute} error were found, in, {error.original}', tts = True)
                await ctx.send(f'{runTimeError}')
            
            elif isinstance(error.original, badReq):

                #   Prepare & send embed
                self.embed.title = 'Woups, seems like you found a badboy'
                self.embed.description = cmdError.ErrorArguments(badReq)
                await ctx.send(embed = self.embed)

                #   Prepare a report to the maintainer
                await maintainer.send(f'Master, there were a bad request in, {error.original}', tts = True)

            elif isinstance(error.original, badboy):

                #   Prepare & send embed
                self.embed.title = 'Woups, seems like you found a badboy'
                self.embed.description = cmdError.ErrorArguments(badboy)
                await ctx.send(embed = self.embed)

                #   Prepare a report to the maintainer
                await maintainer.send(f'Master, there were a bad request in, {error.original}', tts = True)

            
            else:

                await maintainer.send(f'Master, an undentified error were found, in, {error.original}', tts = True)
                await ctx.send(f'{runTimeError}')        
        else:
            # If none of the above, print it in the terminal
            print('Ignoring exception in command {}:\n'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        return

class ErrorMessage(Cog):

    def __init__(self) -> None:
        self.embed = Embed()

    def ErrorArguments(self, ctx, errorModule, *cmd):

        if errorModule == 'CommandNotFound':

            dictionary = { 
                            1:'meep morp zeep :(\n',
                            2:'Tried to procsess your text, unfortuantly i couldn\'t understand you',
                            3:'Sir, you\'ve started the "Self destruction protocol", press "enter" to continue, press "esc" to stop.',
                            4:'Sir, im sorry, could you please repeat the command?',
                            5:'Sir The command has not been impleted in my software',
                            6:f'Sir, did you search the dumpster after the command..?',
                            7:f'I have some good news, sir. Im a good boy, i didnt execute {cmd}',
                            8:f'We all do mistakes, sometimes.. There is no user with {cmd} name',
                            9:'0101010001101000011001010010000001100011011011110110110101101101011000010110111001100100001000000110010001101111011001010111001100100000011011100110111101110100001000000110010101111000011010010111001101110100',
}

        elif errorModule == 'CheckFailure':

            dictionary = { 
                            0:'meep, morp, meep :(\n',
                            1:f'Authorization failure ',
                            2:'Unfortuantly you\'re not the right model we are looking for',
                            3:'Sir, im happy you love to play , I suggest you to do an audition.',
                            4:'010110010110111101110101001000000100010001101111001000000110111001101111011101000010000001101000011000010111011001100101001000000111010001101000011001010010000001110010011001010111000101110101011010010111001001100101011001000010000001110010011011110110110001100101',
}

        elif errorModule == 'MissingRequiredArument':

            dictionary = {  1:'meep, morp, meep :(\n',
                            2:'Sir, i just executed the command with-out any arguments...',
                            3:'Sir, should i just fake it?\n',
                            4:'More infomation would do my job easier..',
                            5:'Still missing some leads..',
                            6:'We all do mistakes. This time its not me, its you. ',
}

        elif errorModule == 'MemberNotFound':

            dictionary = {
                            1:'meep, morp, zeep :(\n',
                            2:'Sir, imagne the member where found\n',
                            3:'Sir, if the error continues, check your spelling \n',
                            4:'I regret to inform you, sir. the selected member does not exist, should i make one? \n',
                            5:'010110010110111101110101001000000100010001101111001000000110111001101111011101000010000001101000011000010111011001100101001000000111010001101000011001010010000001110010011001010111000101110101011010010111001001100101011001000010000001110010011011110110110001100101\n',
                            6:'I guess the member ghosted you',
                            7:f'Just sent out an APB of {ctx.author}',
                            8:'We all do mistakes, this time the user doesn\'t exist',
}

        elif errorModule =='TimeOutException':

            dictionary = {

                            1:'meep, morp, zeep :(\n',
                            2:'Sir, the BOENG 437 just left the airport',
                            3:'Sir, do you need more time?',
                            4:f'The game is over, {ctx.author.mention} just ran out of time.',
                            5:'Try again',
                            6:'Decided to cancel the game.',
                            7:'Never got a response..'
}

        x = len(dictionary)
        x = randrange(1,x)
        self.embed.description = dictionary.get(x)

        return self.embed.description

    def RequiredArguments(self, cmd):

        #   Community
        if cmd == 'Randint' or cmd == 'randint':self.embed.title = '*randint (integer one) (integer two)'

        #   Minigames- Module
        elif cmd == 'Int' or cmd == 'int':self.embed.title = '*int (easiest / easy / normal / hard / kimpossible)'
        elif cmd == 'Ask' or cmd == 'ask':self.embed.title = '*ask (question)'
        elif cmd == 'Afk' or cmd == 'afk':self.embed.title = '*afk (Status update)'

        #   Moderator-module
        elif cmd == 'Kick' or cmd == 'kick':

            self.embed.title = '*kick [member] [reason]'
            self.embed.url = 'https://www.dictionary.com/browse/kick#'

        elif cmd == 'Cls' or cmd == 'cls':self.embed.title = '*cls (channelid) (int)'
            
        elif cmd == 'Crech' or cmd == 'crech':self.embed.title = '*crech [ChannelName]'

        elif cmd ==  'Warn' or cmd == 'warn':self.embed.title = '*warn (name) (reason)'

        elif cmd ==  'Sush' or cmd == 'sush':
            self.embed.title = '*sush (name) (sec) (reason)'
            self.embed.url = 'https://www.urbandictionary.com/define.php?term=snooze'
            
        #   Administrator module     
        elif cmd == 'Ban' or cmd == 'ban':
            self.embed.title = '*ban [member] [reason]'
            self.embed.url = 'https://www.dictionary.com/browse/ban'

        elif cmd == 'Announce' or cmd == 'announce':self.embed.title = '*announce (channelName)'

        elif cmd == 'Unban' or cmd == 'unban':self.embed.title = '*unban (Member Name)'


        else:
            self.embed.title = 'Missing some important notes !'
            self.embed.url = 'https://www.merriam-webster.com/dictionary/attribute'

        dictionary = {  1:'meep, morp, meep :(\n',
                        2:'Sir, i just executed the command with-out any arguments...',
                        3:'Sir, should i just fake it?\n',
                        4:'More infomation would do my job easier..',
                        5:'Still missing some leads..',
                        6:'We all do mistakes. This time its not me, its you. ',
}

        x = len(dictionary)
        x = randrange(1,x)
        self.embed.description = dictionary.get(x)

        return self.embed
