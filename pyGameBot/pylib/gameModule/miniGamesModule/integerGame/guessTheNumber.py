
# Python Responsories
from random import randrange, randint

# Discord Responsories
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

# pylib Responsories
from pylib.dictionaries.gameDictionaries import GameDictionary, GameError


class GuessTheNumber(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')
    
    @command(name='int')
    async def GuessTheNum(self, ctx, diff):
    
        #   Initializing Classes
        d = GameError()
        gd = GameDictionary()

        # Difficulty
        diff = str(diff)
        diff.lower()
        
        self.embed.title = 'Attempts | < and >'

        # Lists / number of attempts
        attempt = 0
        lList = []
        gList = []
        
        if diff == 'easiest':

            #   Game Configurations
            value = 0
            sec = 10.0
            limited = 4
            valueTwo = 10

            #   Randomizing the given integer
            x = randint(0,10)

            #   Prepare & Send the embed
            self.embed.description = f' You\'ve choosen the **{diff} mode**, you have **{limited}** attempts and **{sec} sec**, to guess. You can choose between **{value}** & **{valueTwo}** sir.\n'
            await ctx.send(embed=self.embed)

            while True:

                num = await self.bot.wait_for('message', timeout=sec)
                num = int(num.content)

                if num > x:

                    #   Adding choosen valuie to a list
                    gList.append(num)

                    #   Declare variable which contain the list 
                    lessOrGreater = f'less than :**{lList}** greater than **{gList}**\n'

                    #   Prepare and send the embed message
                    self.embed.title = f'**{attempt}** / **{limited}**   | {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)
                    
               
                elif num < x:

                     #   Adding choosen valuie to a list
                    lList.append(num)

                    lessOrGreater = f'less than **{lList}**  and greater than **{gList}**\n'

                    #   Prepare and send the embed message
                    self.embed.title = f'**{attempt}** / **{limited}**  |   {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)

                else:

                    # Prepare and send the embed message
                    self.embed.title = f'Attempts used **{attempt}** / **{limited}**  |   {lessOrGreater}'
                    self.embed.description = d.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)
                    break

                if attempt == limited:

                    #   Prepare and send the embed message
                    self.embed.title = 'The Game is over'
                    self.embed.description = f'{gd.GameOver}'
                    self.embed.add_field(name='**Game Summary**', value=f'You guessed **{attempt}** of **{limited}** times\n <{lList} | {gList}> \n krigjo25\'s answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)

                    # Get out of the loop
                    break

            attempt += 1

        elif diff == 'easy':

            #   Game Configurations
            value = 0
            sec = 10.0
            limited = 4
            valueTwo = 100

            #   Randomizing the given integer
            x = randrange(0,100)

            #   Sending and embeded message to the user with instructions
            self.embed.description = f' You\'ve choosen the **{diff} mode**, you have **{limited}** attempts and **{sec}**, to guess. You can choose between **{value}** & **{valueTwo}** sir.\n'
            
            #   Send the given self.embed
            await ctx.send(embed=self.embed)

            while True:

                num = await self.bot.wait_for('message', timeout=sec)
                num = int(num.content)

                if num > x:
                    #   Adding choosen valuie to a list
                    gList.append(num)

                    #   Declare variable which contain the list 
                    lessOrGreater = f'less than :**{lList}** greater than **{gList}**\n'

                    #   Prepare and send the embed message
                    self.embed.title = f'**{attempt}** / **{limited}**   | {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)
                    
               
                elif num < x:

                     #   Adding choosen valuie to a list
                    lList.append(num)

                    lessOrGreater = f'less than **{lList}**  and greater than **{gList}**\n'

                    #   Prepare and send the embed message
                    self.embed.title = f'**{attempt}** / **{limited}**  |   {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)

                else:

                    # Prepare and send the embed message
                    self.embed.title = f'Attempts used **{attempt}** / **{limited}**  |   {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)
                    break

                if attempt == limited:

                    #   Prepare and send the embed message
                    self.embed.title = 'The Game is over'
                    self.embed.description = f'{gd.GameOver}'
                    self.embed.add_field(name='**Game Summary**', value=f'You guessed **{attempt}** of **{limited}** times\n <{lList} | {gList}> \n krigjo25\'s answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)

                    # Get out of the loop
                    break

            attempt += 1

        elif diff == 'normal':

            #   Game Configuration
            value = 0
            sec = 15.0
            limited = 4
            valueTwo = 500

            #   Randomizing the given integer
            x = randrange(0,500)

            #   Sending and embeded message to the user with instructions
            self.embed.description = f' You\'ve choosen the **{diff} mode**, you have **{limited}** attempts and **{sec}**, to guess. You can choose between **{value}** & **{valueTwo}** sir.\n'
            
            #   Send the given self.embed
            await ctx.send(embed=self.embed)

            while True:

                num = await self.bot.wait_for('message', timeout=sec)
                num = int(num.content)

                if num > x:
                    #   Adding choosen valuie to a list
                    gList.append(num)

                    #   Declare variable which contain the list 
                    lessOrGreater = f'less than :**{lList}** greater than **{gList}**\n'

                    #   Prepare and send the embed message
                    self.embed.title = f'**{attempt}** / **{limited}**   | {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)
                    
               
                elif num < x:

                     #   Adding choosen valuie to a list
                    lList.append(num)

                    lessOrGreater = f'less than **{lList}**  and greater than **{gList}**\n'

                    #   Prepare and send the embed message
                    self.embed.title = f'**{attempt}** / **{limited}**  |   {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)

                else:

                    # Prepare and send the embed message
                    self.embed.title = f'Attempts used **{attempt}** / **{limited}**  |   {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)
                    break

                if attempt == limited:

                    #   Prepare and send the embed message
                    self.embed.title = 'The Game is over'
                    self.embed.description = f'{gd.GameOver}'
                    self.embed.add_field(name='**Game Summary**', value=f'You guessed **{attempt}** of **{limited}** times\n <{lList} | {gList}> \n krigjo25\'s answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)

                    # Get out of the loop
                    break

        elif diff == 'hard':

            #   Game Configurations
            sec = 30.0
            limited = 6
            value = -500
            valueTwo = 500

            #   Randomizing the given integer
            x = randint(-500,500)

            #   Sending and embeded message to the user with instructions
            self.embed.description = f' You\'ve choosen the **{diff} mode**, you have **{limited}** attempts and **{sec}**, to guess. You can choose between **{value}** & **{valueTwo}** sir.\n'
            
            #   Send the given self.embed
            await ctx.send(embed=self.embed)

            while True:

                num = await self.bot.wait_for('message', timeout=sec)
                num = int(num.content)

                if num > x:
                    #   Adding choosen valuie to a list
                    gList.append(num)

                    #   Declare variable which contain the list 
                    lessOrGreater = f'less than :**{lList}** greater than **{gList}**\n'

                    #   Prepare and send the embed message
                    self.embed.title = f'**{attempt}** / **{limited}**   | {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)
                    
               
                elif num < x:

                     #   Adding choosen valuie to a list
                    lList.append(num)

                    lessOrGreater = f'less than **{lList}**  and greater than **{gList}**\n'

                    #   Prepare and send the embed message
                    self.embed.title = f'**{attempt}** / **{limited}**  |   {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)

                else:

                    # Prepare and send the embed message
                    self.embed.title = f'Attempts used **{attempt}** / **{limited}**  |   {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)
                    break

                if attempt == limited:

                    #   Prepare and send the embed message
                    self.embed.title = 'The Game is over'
                    self.embed.description = f'{gd.GameOver}'
                    self.embed.add_field(name='**Game Summary**', value=f'You guessed **{attempt}** of **{limited}** times\n <{lList} | {gList}> \n krigjo25\'s answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)

                    # Get out of the loop
                    break

        elif diff ==  'kimpossible':

            #   Game Configurations
            sec = 30.0
            limited = 10
            value = -1000
            valueTwo = 1000

            #   Randomizing the given integer
            x = randint(-1000,1000)

            #   Sending and embeded message to the user with instructions
            self.embed.description = f' You\'ve choosen the **{diff} mode**, you have **{limited}** attempts and **{sec}**, to guess. You can choose between **{value}** & **{valueTwo}** sir.\n'
            
            #   Send the given self.embed
            await ctx.send(embed=self.embed)

            while True:

                num = await self.bot.wait_for('message', timeout=sec)
                num = int(num.content)

                if num > x:
                    #   Adding choosen valuie to a list
                    gList.append(num)

                    #   Declare variable which contain the list 
                    lessOrGreater = f'less than :**{lList}** greater than **{gList}**\n'

                    #   Prepare and send the embed message
                    self.embed.title = f'**{attempt}** / **{limited}**   | {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)
                    
               
                elif num < x:

                     #   Adding choosen valuie to a list
                    lList.append(num)

                    lessOrGreater = f'less than **{lList}**  and greater than **{gList}**\n'

                    #   Prepare and send the embed message
                    self.embed.title = f'**{attempt}** / **{limited}**  |   {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)

                else:

                    # Prepare and send the embed message
                    self.embed.title = f'Attempts used **{attempt}** / **{limited}**  |   {lessOrGreater}'
                    self.embed.description = gd.CustomAnswer(num, x)
                    await ctx.send(embed=self.embed)
                    break

                if attempt == limited:

                    #   Prepare and send the embed message
                    self.embed.title = 'The Game is over'
                    self.embed.description = f'{gd.GameOver}'
                    self.embed.add_field(name='**Game Summary**', value=f'You guessed **{attempt}** of **{limited}** times\n <{lList} | {gList}> \n krigjo25\'s answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)

                    # Get out of the loop
                    break
        
        else:
            self.embed.title= 'The Game has not started yet'
            self.embed.description = d.DifficultyError(diff)
            await ctx.send(embed=self.embed)
