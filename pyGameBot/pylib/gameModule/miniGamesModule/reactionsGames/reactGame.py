# Discord library

from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

# Python library
from random import shuffle,randrange

from lib.dictionaries.systemmessages import Dictionaries


class RockScissorPaper(Cog, name='miniGames module'):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')

    @command(name='rsp')
    #   Send a messge to the user, with embed to
    #   User reacts on the message with the given emoji¨
    #   User recieves an botChoice based on the chosen emoji

    async def ReactionGame(self, ctx,):

        rock = '\U0001FAA8'       #somewhat rock
        scissor = '\U00002702'    #✂️
        paper =  '\U0001F4C4'     #📄

        bot = self.bot.user

        # the Bot's choice
        botChoice = Dictionaries.RockScissorPaper()

        # Sending the reactions, game
        self.embed.title = ' Reaction Game'
        self.embed.description = 'Choose one of the following reaction'

        message = await ctx.send(embed=self.embed)
        await message.add_reaction(rock)
        await message.add_reaction(scissor)
        await message.add_reaction(paper)


        # Checks if there is an emoji, and a user
        def emojiCheck(reaction, member):
            reaction = str(reaction)
            member == ctx.author.name 
            return member !=self.bot.user and reaction

                                                          #           Timer               Check
        reaction, member = await self.bot.wait_for('reaction_add', timeout=30.0, check=emojiCheck)
            
        # Dictionaries
             
        # Tie
        tie = { 
                    0:f'{bot} draws a **tie** for {member}',
                    1:'Sir, lets **tie** a **tie**',
                    2:'What did the **tie** say to the bowtie? You\'re a weirdo',
                    3:'lets have a wii-match',
                }

        # Reaction : Paper
            
        memberPaper = {
                            0:f'{bot} threw {botChoice} at {member}, but {member} grabbed it with his {reaction}, and wrapped it into a :package: \n you gave a :package: to {bot}, how considerate of you !',
                            1:f'You wrappend {bot}\'s {botChoice} into a :gift: and sent it to the North-Pole, Santa were stoned for the Christmas ',
                            2:f'You made a mumified version of {bot}',
                        }
        # Reaction : Rock
        memberRock = {
                        0:f'{bot} had the idea of using a {botChoice} against your {reaction}, {bot} thought the {botChoice} were strong enough to cut thorugh your {reaction}, lets do a wii-match',
                        1:f'{member} congratulations, lets do it again',
                        2:f'{member} just had a {reaction}, while {bot} had the thought of {botChoice} would be a grate choice.',
                        3:f'OH SNAP, you just scared {bot}, he never returned to the battle field.',
                    }
                 # Reaction Scissors
        memberScissors = {  
                            0:f'Noone : \'\'\n{bot} : Oh snap',
                            1:f'You succsessfully cut the {botChoice} with a {reaction}',
                            2:f'{member} showed of with his :scissors: which he thought were a knife, but the goal were reached, {bot} ran.',
                            3:f'you won '
                        }
    
            # Bot arguments

        botPaper = {
                        0:f'{member} threw a {reaction} at {bot}, but {bot} grabbed it with his {botChoice}, and wrapped it into a :package: \n you have recieved a new :package: !',
                        1:f'{bot} wrappend {member}\'s {reaction} into a :gift: and sent it to the North-Pole, Santa were stoned for the Christmas ',
                        2:f'You have been mumified by {bot}',
                    }

        botRock = {
                    0:f'This moment, when you realize you did a mistaken {reaction}, :scissors: doesn\'t play along with a rock',
                    1:f'{member} congratulated bot this time !',
                    2:f'{member} you just thought it would be a good idea to throw a {reaction}, while {bot} had the thought of {botChoice} would be a great choice.',
                    3:f'look behind you, then he never returned to the battle field.',
                    }
        botScissors = {
                        0:f'Noone : \'\'\n{bot} : Oh snap',
                        1:f'You succsessfully cut the {reaction} with a {botChoice}',
                        2:f'{member} showed of with his :scissors: which he thought were a knife, but the goal were reached, {bot} ran.',
                        3:f'i won '
                        }
        
        # Randomize the dictionaries
        shuffle(tie)
        shuffle(botRock)
        shuffle(botPaper)
        shuffle(memberRock)
        shuffle(memberPaper)
        shuffle(botScissors)
        shuffle(memberScissors)
   
        x = randrange(0,3)
            
        # If the situation is a draw / tie
        if str(reaction) == botChoice:

            tie= tie.get(x)
            self.embed.description = tie
            await ctx.send(embed = self.embed)

        elif str(reaction) != botChoice:

            if str(reaction) == '\U0001F4C4':
                if botChoice =='\U0001FAA8':     # annswer = rock
                    
                    # Get the string
                    argsDict = memberPaper.get(x)

                    #Creating the embed description
                    self.embed.description = argsDict
                    await ctx.send(embed = self.embed)
                    
                elif botChoice == '\U0001F4CC': # botChoice = Scissors
                    
                    Argsdict = botScissors.get(x)
    
                    #Creating the self.embed description
                    self.embed.description = Argsdict
                    await ctx.send(embed = self.embed)
                    
            elif str(reaction) == '\U00002702':
                if botChoice =='\U0001FAA8':     # botChoice = rock
                        
                    # retrieve  botChoice
                    argsDict = botRock.get(x)

                    # Creating the embed.description
                    self.embed.description = argsDict
                    await ctx.send(embed = self.embed)
                    
                if botChoice == '\U0001F4C4': # botChoice = Paper
                        
                    # Randomizing the dictonary
                    argsDict = memberScissors.get(x)
                        
                    # Creating the embed.description
                    self.embed.description = argsDict
                    await ctx.send(embed = self.embed)
                
            elif str(reaction) == '\U0001FAA8': # Rock hard
                if botChoice =='\U0001F4CC':     # botChoice = Scissors

                    #   Randomizing the dictonary
                    x = randrange(0,3)
                    argsDict = memberRock.get(x)

                    # Creating the embed.description
                    self.embed.description = argsDict
                    await ctx.send(embed = self.embed)
                
                if botChoice == '\U0001F4C4': # botChoice = Paper

                    # Randomizing the dictonary
                    x = randrange(0,3)
                    argsDict = botPaper.get(x)
                    
                    # Creating the embed.description
                    self.embed.description = argsDict
                    await ctx.send(embed = self.embed)