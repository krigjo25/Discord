
# Discord library
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   pylib Responsories
from pylib.dictionaries.gameDictionaries import ReactionGame

class RockScissorPaper(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')

    @command(name='rsp')
    async def ReactionGame(self, ctx):
        """
            #   Send a messge to the user, with embed to
            #   User reacts on the message with the given emoji¨
            #   User recieves an botChoice based on the chosen emoji
        """

        # Initializing Classes
        r = ReactionGame()

        #   Prepare & Send the embed
        rock = '\U0001FAA8'       #somewhat rock
        scissor = '\U00002702'    #✂️
        paper =  '\U0001F4C4'     #📄

        self.embed.title = ' Rock Scissors & Paper Game'
        self.embed.description = 'Choose one of the following reaction'

        #   Retrieve reactions from the bot
        message = await ctx.send(embed=self.embed)
        await message.add_reaction(rock)
        await message.add_reaction(scissor)
        await message.add_reaction(paper)

        #   the Bot's choice
        botChoice = r.RockScissorPaper()

        # Checks if there is an emoji, and a user
        def emojiCheck(reaction, member):
            reaction = str(reaction)
            member == ctx.author.name 
            return member !=self.bot.user and reaction

                                                          #           Timer               Check
        reaction, member = await self.bot.wait_for('reaction_add', timeout=30.0, check=emojiCheck)

        #   Checking whom is the winner
        playerChoice = str(reaction)

        if playerChoice == botChoice:

            #   Prepare and send the embed
            self.embed.description = r.Tie()
            await ctx.send(embed = self.embed)

        elif playerChoice != botChoice:

            if playerChoice == '\U0001F4C4' and botChoice =='\U0001FAA8':

                    self.embed.description = r.memberWin(reaction, botChoice)
                    await ctx.send(embed = self.embed)
                    
            elif playerChoice == '\U00002702' and botChoice == '\U0001F4C4':

                    #   Prepare and send the embed
                    self.embed.description = r.memberWin(reaction, botChoice)

                    await ctx.send(embed = self.embed)

            elif playerChoice == '\U0001FAA8' and botChoice =='\U0001F4CC': # Rock hard

                    #   Prepare and send the embed
                    self.embed.description = r.memberWin(reaction, botChoice)
                    await ctx.send(embed = self.embed)

            elif botChoice == '\U0001F4CC' and playerChoice == '\U0001F4C4':

                    #   Prepare and send the embed
                    self.embed.description =  r.BotWin(botChoice)
                    await ctx.send(embed = self.embed)

            elif botChoice =='\U0001FAA8' and playerChoice == '\U00002702':     # botChoice = rock

                    #   Prepare and send the embed
                    self.embed.description =  r.BotWin(botChoice)
                    await ctx.send(embed = self.embed)
                    
            elif botChoice == '\U0001F4C4' and playerChoice == '\U0001FAA8':

                    #   Prepare and send the embed
                    self.embed.description =  r.BotWin(botChoice)
                    await ctx.send(embed = self.embed)