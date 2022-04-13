# Discord library
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

# Python library
from random import shuffle,randrange, randint

from pylib.dictionaries.systemmessages import Dictionaries

# Asynico library
class GuessTheNumber(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')
        self.gameOver = Dictionaries.GameOver()
    
    @command(name='int')
    async def GuessTheNum(self, ctx, diff):
        
        # Difficulty
        diff = str(diff)
        diff.lower()
        
        self.embed.title = 'Attempts | < and >'

        # Lists / number of attempts
        atnum = 0
        lList = []
        gList = []
        
        if diff == 'easiest':

            #   Randomizing the given integer
            x = randint(0,10)
            i = randrange(0,2)


            value = 0
            sec = 10.0
            atNumMax = 4
            valueTwo = 10
            
            #   Sending and embeded message to the user with instructions
            self.embed.description = f' You\'ve choosen the **{diff} mode**, you have **{atNumMax}** attempts and **{sec}**, to guess. You can choose between **{value}** & **{valueTwo}** sir.\n'
            
            #   Send the given self.embed
            await ctx.send(embed=self.embed)

            while True:
                num = await self.bot.wait_for('message', timeout=sec)
                num = int(num.content)
                atnum += 1
                
                

                if num > x:
                    #   Adding choosen valuie to a list
                    lList.append(num)

                    #   Declare variable which contain the list 
                    lessOrGreater = f'< less than :**{lList}** > greater than **{gList}**\n'

                    #   Declare a list containing custom message
                    greater = {
                                0:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} Well well, we like the answer more humble than a greater answer',
                                1:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} The given number is not humble enough, try again.',
                                2:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} **{num}** is greater than the answer ',
                            }
                   
                    
                    #   Randomizing the dictionary
                    shuffle(greater)    

                    #   Get the key to the dictionary
                    greater = greater.get(i)

                    #   Prepare and send the embed message
                    self.embed.description = f'{greater}'
                    await ctx.send(embed=self.embed)
                    
               
                elif num < x:

                     #   Adding choosen valuie to a list
                    gList.append(num)

                    lessOrGreater = f'< less than **{gList}**  and > greater than **{lList}**\n'
                    
                    less = {
                                0:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less, we want more',
                                1:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less than i ask for',
                                2:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less akward than :100:',
                                }

                    #   Randomizing the dictionary
                    shuffle(less)

                    #   Retrive key to unlock Dictonary    
                    less = less.get(i)
                    
                    #   Prepare and send the embed message
                    self.embed.description = f'{less}'
                    await ctx.send(embed=self.embed)

                elif num == x:

                    #   Declare a variable which holds the custom answer
                    equal = {
                                0:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} Do you know why the equal sign are so humble? It were neither greater than or less than **{x}**',
                                1:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} Finally a humble answer !',
                                2:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{x}** = **{x}**',
                            }

                    #   Randomizing the dictionary
                    shuffle(equal)    

                    #   Retrieve the key
                    equal = equal.get(i)

                    # Prepare and send the embed message
                    self.embed.title = 'The game is over'
                    self.embed.description = f'{equal}'
                    await ctx.send(embed=self.embed)
                    break

                else:
                    await ctx.send(f'Something went wrong {num},  {x}')
                
                if atnum == atNumMax:

                    #   Prepare and send the embed message
                    self.embed.title = 'The Game is over'
                    self.embed.description = f'{self.gameOver}'
                    self.embed.add_field(name='Results', value=f'You guessed **{atnum}** of **{atNumMax}** times\n <{less} | {greater}> \n krigjo25\'s answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)

                    # Get out of the loop
                    break

        elif diff == 'easy':

            #   Randomizing the given integer
            x = randrange(0,100)
            i = randrange(0,2)
            
            value = 0
            sec = 10.0
            atNumMax = 4
            valueTwo = 100
            
            #   Sending and embeded message to the user with instructions
            self.embed.description = f' You\'ve choosen the **{diff} mode**, you have **{atNumMax}** attempts and **{sec}**, to guess.\n You can choose between **{value}** & **{valueTwo}** sir.\n'
            
            #   Send the given self.embed
            await ctx.send(embed=self.embed)

            while True:
                num = await self.bot.wait_for('message', timeout=sec)
                num = int(num.content)
                atnum += 1
                
                

                if num > x:
                    #   Adding choosen valuie to a list
                    lList.append(num)

                    #   Declare variable which contain the list 
                    lessOrGreater = f'< less than :**{lList}** > greater than **{gList}**\n'

                    #   Declare a list containing custom message
                    greater = {
                                0:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} Well well, we like the answer more humble than a greater answer',
                                1:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} The given number is not humble enough, try again.',
                                2:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} **{num}** is greater than the answer ',
                            }
                   
                    
                    #   Randomizing the dictionary
                    shuffle(greater)    

                    #   Get the key to the dictionary
                    greater = greater.get(i)

                    #   Prepare and send the embed message
                    self.embed.description = f'{greater}'
                    await ctx.send(embed=self.embed)
                    
               
                elif num < x:

                     #   Adding choosen valuie to a list
                    gList.append(num)

                    lessOrGreater = f'< less than **{gList}**  and > greater than **{lList}**\n'
                    
                    less = {
                                0:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less, we want more',
                                1:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less than i ask for',
                                2:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less akward than :100:',
                                }

                    #   Randomizing the dictionary
                    shuffle(less)

                    #   Retrive key to unlock Dictonary    
                    less = less.get(i)
                    
                    #   Prepare and send the embed message
                    self.embed.description = f'{less}'
                    await ctx.send(embed=self.embed)

                elif num == x:

                    #   Declare a variable which holds the custom answer
                    equal = {
                                0:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} Do you know why the equal sign are so humble? It were neither greater than or less than **{x}**',
                                1:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} Finally a humble answer !',
                                2:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{x}** = **{x}**',
                            }

                    #   Randomizing the dictionary
                    shuffle(equal)    

                    #   Retrieve the key
                    equal = equal.get(i)

                    # Prepare and send the embed message
                    self.embed.title = 'The game is over'
                    self.embed.description = f'{equal}'
                    await ctx.send(embed=self.embed)
                    break

                else:
                    await ctx.send(f'Something went wrong {num},  {x}')
                
                if atnum == atNumMax:

                    #   Prepare and send the embed message
                    self.embed.title = 'The Game is over'
                    self.embed.description = f'{self.gameOver}'
                    self.embed.add_field(name='Results', value=f'You guessed **{atnum}** of **{atNumMax}** times\n <{less} | {greater}> \n krigjo25\'s answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)

                    # Get out of the loop
                    break

        elif diff == 'normal':

            #   Number of attempts

            

            #   Randomizing the given integer
            x = randint(0,500)
            i = randrange(0,2)
            
            value = 0
            sec = 15.0
            atNumMax = 4
            valueTwo = 500
            
            #   Sending and embeded message to the user with instructions
            self.embed.description = f' You\'ve choosen the **{diff} mode**, you have **{atNumMax}** attempts and **{sec}**, to guess. You can choose between **{value}** & **{valueTwo}** sir.\n'
            
            #   Send the given self.embed
            await ctx.send(embed=self.embed)

            while True:
                num = await self.bot.wait_for('message', timeout=sec)
                num = int(num.content)
                atnum += 1
                
                

                if num > x:
                    #   Adding choosen valuie to a list
                    lList.append(num)

                    #   Declare variable which contain the list 
                    lessOrGreater = f'< less than :**{lList}** > greater than **{gList}**\n'

                    #   Declare a list containing custom message
                    greater = {
                                0:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} Well well, we like the answer more humble than a greater answer',
                                1:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} The given number is not humble enough, try again.',
                                2:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} **{num}** is greater than the answer ',
                            }
                   
                    
                    #   Randomizing the dictionary
                    shuffle(greater)    

                    #   Get the key to the dictionary
                    greater = greater.get(i)

                    #   Prepare and send the embed message
                    self.embed.description = f'{greater}'
                    await ctx.send(embed=self.embed)
                    
               
                elif num < x:

                     #   Adding choosen valuie to a list
                    gList.append(num)

                    lessOrGreater = f'< less than **{gList}**  and > greater than **{lList}**\n'
                    
                    less = {
                                0:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less, we want more',
                                1:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less than i ask for',
                                2:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less akward than :100:',
                                }

                    #   Randomizing the dictionary
                    shuffle(less)

                    #   Retrive key to unlock Dictonary    
                    less = less.get(i)
                    
                    #   Prepare and send the embed message
                    self.embed.description = f'{less}'
                    await ctx.send(embed=self.embed)

                elif num == x:

                    #   Declare a variable which holds the custom answer
                    equal = {
                                0:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} Do you know why the equal sign are so humble? It were neither greater than or less than **{x}**',
                                1:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} Finally a humble answer !',
                                2:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{x}** = **{x}**',
                            }

                    #   Randomizing the dictionary
                    shuffle(equal)    

                    #   Retrieve the key
                    equal = equal.get(i)

                    # Prepare and send the embed message
                    self.embed.title = 'The game is over'
                    self.embed.description = f'{equal}'
                    await ctx.send(embed=self.embed)
                    break

                else:
                    await ctx.send(f'Something went wrong {num},  {x}')
                
                if atnum == atNumMax:

                    #   Prepare and send the embed message
                    self.embed.title = 'The Game is over'
                    self.embed.description = f'{self.gameOver}'
                    self.embed.add_field(name='Results', value=f'You guessed **{atnum}** of **{atNumMax}** times\n <{less} | {greater}> \n krigjo25\'s answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)

                    # Get out of the loop
                    break

        elif diff == 'hard':

            #   Randomizing the given integer
            x = randint(-500,500)
            i = randrange(0,2)
            
            value = -500
            sec = 30.0
            atNumMax = 6
            valueTwo = 500
            
            #   Sending and embeded message to the user with instructions
            self.embed.description = f' You\'ve choosen the **{diff} mode**, you have **{atNumMax}** attempts and **{sec}**, to guess. You can choose between **{value}** & **{valueTwo}** sir.\n'
            
            #   Send the given self.embed
            await ctx.send(embed=self.embed)

            while True:
                num = await self.bot.wait_for('message', timeout=sec)
                num = int(num.content)
                atnum += 1
                
                

                if num > x:
                    #   Adding choosen valuie to a list
                    lList.append(num)

                    #   Declare variable which contain the list 
                    lessOrGreater = f'< less than :**{lList}** > greater than **{gList}**\n'

                    #   Declare a list containing custom message
                    greater = {
                                0:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} Well well, we like the answer more humble than a greater answer',
                                1:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} The given number is not humble enough, try again.',
                                2:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} **{num}** is greater than the answer ',
                            }
                   
                    
                    #   Randomizing the dictionary
                    shuffle(greater)    

                    #   Get the key to the dictionary
                    greater = greater.get(i)

                    #   Prepare and send the embed message
                    self.embed.description = f'{greater}'
                    await ctx.send(embed=self.embed)
                    
               
                elif num < x:

                     #   Adding choosen valuie to a list
                    gList.append(num)

                    lessOrGreater = f'< less than **{gList}**  and > greater than **{lList}**\n'
                    
                    less = {
                                0:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less, we want more',
                                1:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less than i ask for',
                                2:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less akward than :100:',
                                }

                    #   Randomizing the dictionary
                    shuffle(less)

                    #   Retrive key to unlock Dictonary    
                    less = less.get(i)
                    
                    #   Prepare and send the embed message
                    self.embed.description = f'{less}'
                    await ctx.send(embed=self.embed)

                elif num == x:

                    #   Declare a variable which holds the custom answer
                    equal = {
                                0:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} Do you know why the equal sign are so humble? It were neither greater than or less than **{x}**',
                                1:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} Finally a humble answer !',
                                2:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{x}** = **{x}**',
                            }

                    #   Randomizing the dictionary
                    shuffle(equal)    

                    #   Retrieve the key
                    equal = equal.get(i)

                    # Prepare and send the embed message
                    self.embed.title = 'The game is over'
                    self.embed.description = f'{equal}'
                    await ctx.send(embed=self.embed)
                    break

                else:
                    await ctx.send(f'Something went wrong {num},  {x}')
                
                if atnum == atNumMax:

                    #   Prepare and send the embed message
                    self.embed.description = f'{self.gameOver}'
                    self.embed.add_field(name='Results', value=f'You guessed **{atnum}** of **{atNumMax}** times\n <{less} | {greater}> \n krigjo25\'s answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)

                    # Get out of the loop
                    break
        
        elif diff ==  'kimpossible':
                

            #   Randomizing the given integer
            x = randint(-1000,1000)
            i = randrange(0,2)
            
            value = -1000
            sec = 30.0
            atNumMax = 4
            valueTwo = 1000
            
            #   Sending and embeded message to the user with instructions
            self.embed.description = f' You\'ve choosen the **{diff} mode**, you have **{atNumMax}** attempts and **{sec}**, to guess. You can choose between **{value}** & **{valueTwo}** sir.\n'
            
            #   Send the given self.embed
            await ctx.send(embed=self.embed)

            while True:
                num = await self.bot.wait_for('message', timeout=sec)
                num = int(num.content)
                atnum += 1
                
                

                if num > x:
                    #   Adding choosen valuie to a list
                    lList.append(num)

                    #   Declare variable which contain the list 
                    lessOrGreater = f'< less than :**{lList}** > greater than **{gList}**\n'

                    #   Declare a list containing custom message
                    greater = {
                                0:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} Well well, we like the answer more humble than a greater answer',
                                1:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} The given number is not humble enough, try again.',
                                2:f'**{atnum}** / **{atNumMax}**   | {lessOrGreater} **{num}** is greater than the answer ',
                            }
                   
                    
                    #   Randomizing the dictionary
                    shuffle(greater)    

                    #   Get the key to the dictionary
                    greater = greater.get(i)

                    #   Prepare and send the embed message
                    self.embed.description = f'{greater}'
                    await ctx.send(embed=self.embed)
                    
               
                elif num < x:

                     #   Adding choosen valuie to a list
                    gList.append(num)

                    lessOrGreater = f'< less than **{gList}**  and > greater than **{lList}**\n'
                    
                    less = {
                                0:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less, we want more',
                                1:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less than i ask for',
                                2:f'**{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{num}** is less akward than :100:',
                                }

                    #   Randomizing the dictionary
                    shuffle(less)

                    #   Retrive key to unlock Dictonary    
                    less = less.get(i)
                    
                    #   Prepare and send the embed message
                    self.embed.description = f'{less}'
                    await ctx.send(embed=self.embed)

                elif num == x:

                    #   Declare a variable which holds the custom answer
                    equal = {
                                0:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} Do you know why the equal sign are so humble? It were neither greater than or less than **{x}**',
                                1:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} Finally a humble answer !',
                                2:f'Attempts used **{atnum}** / **{atNumMax}**  |   {lessOrGreater} **{x}** = **{x}**',
                            }

                    #   Randomizing the dictionary
                    shuffle(equal)    

                    #   Retrieve the key
                    equal = equal.get(i)

                    # Prepare and send the embed message
                    self.embed.title = 'The game is over'
                    self.embed.description = f'{equal}'
                    await ctx.send(embed=self.embed)
                    break

                else:
                    await ctx.send(f'Something went wrong {num},  {x}')
                
                if atnum == atNumMax:

                    #   Prepare and send the embed message
                    self.embed.title = 'The Game is over'
                    self.embed.description = f'{self.gameOver}'
                    self.embed.add_field(name='Results', value=f'You guessed **{atnum}** of **{atNumMax}** times\n <{less} | {greater}> \n krigjo25\'s answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)

                    # Get out of the loop
                    break
        
        else:
            self.embed.title= 'The Game has not started yet'
            self.embed.description = f'lets fake it **{diff}**'
            await ctx.send(embed=self.embed)
