# Python Responsories
import sys
import traceback

#   Asynico Responsories
from asyncio.exceptions import TimeoutError

#   Discord Responsories
import discord as d
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
    async def on_command_error(self, ctx:d.ApplicationContext, error):

        '''
            #   Triggers when an error is raised while invoking a command.Parameters

            #   ctx:    commands.Context
            #   #   The context used for command invocation.

            #   commands.ErrorDictionary
            #   #   The Exception which will be raised.

        '''

       #    Classes initialization

        master = await self.bot.fetch_user(340540581174575107)
        botmsg = None

        #   Member not found 
        if isinstance(error, CommandNotFound):

            error = str(CommandNotFound)[36:51]
            try:
                self.embed.title = '404: Command Not Found'
            
            except (TypeError, Exception) as e : print(e)

            else :
                await ctx.send(embed=self.embed)

        #   Role not satisified
        elif isinstance(error, CheckFailure):

            try: 
                self.embed.title = '410:Unauthorized Role'

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
                self.embed.title = "405: Missing some Required Attributes"

            except Exception as e : print(e)

            else :
                await ctx.send(embed=self.embed)

        #   Command Not Found
        elif isinstance(error, CommandNotFound):

                self.embed.title = "404: Command were not found in the dictionary"
                self.embed.description = "Suggestion can be made though (github link)"
                await ctx.send(embed=self.embed)

        #   Non Discord errors
        elif isinstance(error, CommandInvokeError):

            if isinstance(error.original, TimeoutError):
 
                #   Prepare & Send the message
                try:
    
                    self.embed.title = "406: Timeout Error"
                    self.description = "Snail speed"
                except Exception as e : print(e)
                else :

                    await ctx.send(embed=self.embed)

            elif isinstance(error.original, AttributeError):

                    self.embed.title = "Attribute Error"
                    self.embed.description = f"The error has been reported to {master}"
                    botmsg = f"Greetings master.\n Unfortuantly the \"{ctx.command}\" sent an AttributeError {error.original}"
                    await ctx.send(embed=self.embed)

            elif isinstance(error.original, BadArgument):

                #   Prepare & send the embed
                try:
                    self.embed.title = "500: Recieved Bad Arguments"
                    self.embed.description = "Arguments Not accepted"

                except Exception as e: print(e)
                else:

                    botmsg = f"Greetings master.\n Unfortuantly the \"{ctx.command}\" sent some bad arguments {error.original}"
                    await ctx.send(embed=self.embed)

        else:

            #   Print the output in the terminal
            print(f"Ignoring exception in command {ctx.commands}:\n\n", file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        if botmsg != None: await master.dm(botmsg)

        #   Clear some memory
        del master, botmsg, error
        return