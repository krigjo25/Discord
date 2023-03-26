# Python Repositories
import random as r

from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Custom libraries
from lib.system.databasePython import MariaDB
from lib.dictionary.tools import APITools

load_dotenv()

class Philosopher():

    """
        Dictionary for Eightball game

        >   Creation Date   : 12.01-23
        >   Last update     :

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Copyright (C) 2023  Kristoffer Gjøsund
    """

    def __init__(self):
        return

    #   AskQ dictionaries
    def Answer(self):

        dictionary = {
                    1:'What do you sense about it?',
                    2:'What can  you actually do about it?',
                    3:'What are you really, deep down?',
                    4:'Just let it go, its not your issue.',
                    5:'Just let your self, experience the question.',
                    6:'Visualize the question, and the answer will arrive.',
                    7:'If an human is a genious, then The best answers always comes from with-in, just believe in your self enough.',
                    8:'As Socrates once said, you already know the answer of the question, since you had the idea of asking the question.',
                    9:'Would you be able to let it go?',
                    10:'A Question does not arise with out it\'s answer, so place your attention on where the question has arised',
                    11:'From where does the question actually arise? Your mind or heart?',
                    12:'Life is just like one of the elements on earth, just flow with it',
                    13:'Einstein said once if the world were ending, and i had one hour to solve a problem " i would use 50 minutes to think about the issue, then use the 10 last minutes to solve the issue".',
                    14:'As the thought araises from with-in it can only be answered from with-in',
                    15:'Answers comes from with-in your self.'
}

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        return dictionary.get(x)

    def DumbFacts(self):

        dictionary = {
                        1:'Thoughts are like a librarynth, you will be lost',
                        2:'Dear lost boy, thoughts are like a labarynth you won\'t find the exit, when you take the wrong turn',
                        3:'When you search after an answer with why, it\'s like searching for something which doesn\'t exists.',
                        4:'life is why',
                        5:'Things tends to be what it is, neither less or more, but equal to what it is.',
                        6:'The opposite sides of a die will always add up to seven.',
                        7:'The King of Hearts is the only king in a deck of cards without a mustache.',
                        8:'There is always an answer with-in, just compenplate on it',
                        9:'Alaska is the only state whose name is on one row on a keyboard.',
                        10:'A "jiffy" is about one trillionth of a second.',
                        11:'The ocean is blue',
                        12:'Mulan has the highest kill-count of any Disney character.',
                        13:'The infinity sign is called a lemniscate.',
                        14:'why do you ask me?. '

}

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        return dictionary.get(x)

class ScrabbleGame():

    """
        Dictionary for Scrabble

        >   Creation Date   : 12.01-23
        >   Last update     :

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Copyright (C) 2023  Kristoffer Gjøsund
    """

    def ComputeScore(self, word):
        
        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Prompts the words for each player
            #   Calculating the score for both words
            #   Returning score from string

        '''

        #   Initializing variables
        result = 0
        word = str(word).lower()

        #   Initializing arrays
        alpha = [   'a', 'b', 'c', 'd',
                    'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x',
                    'y', 'z']

        POINTS = [  1, 3, 3, 2,
                    1, 4, 2, 4, 
                    1, 8, 5, 1,
                    3, 1, 1, 3,
                    10, 1, 1, 1,
                    1, 4, 4, 8,
                    4, 10 ]

        for i in word: 
            if i in alpha: result += POINTS[alpha.index(i)]

        return result

    def CheckWord(self, arg):

        if APITools().NinjaDefinition(arg): return True
        else: return False

class JumbleCategory():

    """
        Dictionary for Jumble Games

        >   Creation Date   : 12.01-23
        >   Last update     :

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Copyright (C) 2023  Kristoffer Gjøsund
    """

    def __init__(self) -> None: return


    def JumbleGenerator(self, jumble):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Shuffles the characters of the word
            #   Creating a new word with joining the elements of the iterator

        '''

        #   Shuffle the characters of the word
        jumble = r.sample(jumble, len(jumble))
    
        #   Join the elements of the iterator with particular character.
        jumble = ''.join(jumble)
        
        #   Returning the jumbled word
        return jumble

    def RetrieveCategory(self, category, sub):

        """
            #   Retrieve a category from the database,
            #   choose one of the selected values
        """

        category = str(category).lower().replace(" ", "")

        #   Initializing database connection
        db = MariaDB(database=getenv("db2"))

        try:

            word = db.SelectTable(category, sub)

            #   Counting the rows in the database
            print(len(word))
            x = db.RowCount(word)
            print(f" test :{x}")

        except Exception as e : print(e)
        else:

            x = r.randint(1, x)

        #   Closing the connection
        db.closeConnection()

        #   Clear some space
        del x
        del db

        return  word[x]

class GameOver():

    """
        Dictionary for Correct / incorrect answers

        >   Creation Date   : 12.01-23
        >   Last update     :

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Copyright (C) 2023  Kristoffer Gjøsund

    """


    def __init__(self):
        return

    #   When the answer is correct
    def CorrectAnswer(self, arg):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for game Won
        '''

        match str(arg):
            case 'integer':

                    dictionary = {
                                1:f'Thank you for the humble answer, sir ',
                                2:f'Well thats equal..',
                                3:'Thats a humble answer !' }

            case 'scrabble':
                dictionary = {
                                1:f'Congratulation, you gussed correct ',
                                2:f'Congratulation, genious'}

            case 'littleprofessor':
                dictionary = {
                                1:f'Congratulation, you gussed correct ',
                                2:f'Congratulation, genious'}

            case 'rockscissorpaper':#  Human winner

                if arg[1] == '\U0001FAA8':

                    dictionary = {
                                    1:f'The bot had the idea of using a {arg[2]} against your {arg[1]}',
                                    2:f'The bot thought the {arg[2]} were strong enough to cut thorugh your {arg[1]}, lets do a wii-match',
                                    3:f'You just had a {arg[1]}, while the bot had the thought of {arg[2]} would be a grate choice.',
                                    4:f'OH SNAP, you just scared the bot, he never returned to the battle field.',}

                elif arg == '\U0001F4C4':

                    dictionary = {
                                    1:f'The bot threw a {arg[1]} at you, but you grabbed it with a {arg[2]}, and wrapped it into a :package: \n you gave a :package: to the bot, how considerate of you !',
                                    2:f'You wrappend the bot\'s {arg[1]} into a :gift: and sent it to the North-Pole, Santa were stoned for the Christmas ',
                                    3:f'You made a mumified version of the bot',
                            }

                else:
                
                    dictionary = {
                                    1:f'Noone : \"\"\nthe bot : Oh snap',
                                    2:f'You succsessfully cut the {arg[1]} with a {arg[2]}',
                                    3:f'The bot ran from the battlefield',
                            }

            case 'jumble':
                dictionary = {
                                1:f'Congratulation, you gussed correct ',
                                2:f'Congratulation, genious'}

        x = r.randrange(1,len(dictionary))#   Randomize the dictionary
        return dictionary.get(x)#   Returning the value

    def IncorrectAnswer(self, *arg):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for game losses
        '''

        match str(arg[0]):
            case 'integer':

                if int(arg[1]) > int(arg[2]):#    If the prompted integer is greater than n

                    dictionary = {
                                    1:'Well, well you pride human, you think you\'re greater than?',
                                    2:f'{arg[1]} is not humble enough, try again.',
                                    3:f'{arg[1]} is greater than n',}

                elif int(arg[1]) < int(arg[2]):#  If the prompted integer is less than n

                    dictionary = {
                                    1:'You thought you were good enough, puh.',
                                    2:f'{arg[1]} is less than requested',
                                    3:f'{arg[1]} is less akward than :100:',
                                    4:'less is not humble',
                                    5:f'{arg[1]} is less humble ',}

            case 'littleprofessor':            
                dictionary = {
                                1:f'Incorrect Answer',
                                2:'EEE',}
            case 'scrabble':
                dictionary = {
                                1:f'Incorrect Answer',}
            case 'jumble':
                dictionary = {
                                1:f'Incorrect Answer',}
            case 'rockscissorspaper':#  If the bot win

                if arg == '\U0001FAA8':

                    dictionary = {
                                    1:f'That moment, when you realize :stone doesn\'t play along with :Scissors',
                                    2:f'Congratulations, this game were Rock Hard !',
                                    3:f'It were crushing days for the scissors',
                                    4:f'pyBot Says : look behind you. **running away **.'}
                elif arg == '\U0001F4C4':

                    dictionary = {
                                    1:f'The bot sent your stone to North-Korea !',
                                    2:f'You recieved a new stone as a christmas :gift:',
                                    3:f'You have been mumified by the bot',}
                else:
                
                    dictionary = {
                                    2:f'The paper were succsessfully cut in two by the bot ',
                                    3:f'The bot flexed with his scissors, you lost',
                                    4:f'The bot won '}
  

        x = r.randrange(1,len(dictionary))#   Randomize the dictionary
        return dictionary.get(x)#   Return the value

    def TowTie(self):

        """
            #   Dictionary for game draws
        """
        dictionary = {

                    1:f'The computer draws a tie',
                    2:'let\'s tie a tie',
                    3:'What did the tie say to the **bowtie**? You\'re a weirdo',
                    4:f'The cumputer drawing a toe.',
                }

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        return dictionary.get(x)
 
class MathDictionary():

    """
        Dictionary for Mathematical answers

        >   Creation Date   : 12.01-23
        >   Last update     :

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Copyright (C) 2023  Kristoffer Gjøsund
    """

    def Operators(self, arg = None):

        """
            The function accepts a parameter (+, -, / or *)
            and selects a choosen math operator.

        """
        dictionary = {  1:'+', 2:'-', 3:'/', 4:'*'}#, 5:'//', 6: '**', 7:'%'

        if str(arg) == "random":
            r.shuffle(dictionary) # Shuffle the dictionary
            return dictionary.get(r.randrange(1, len(dictionary)))
        else:
            return dictionary.get(arg)

class Madlibs():

    """
        Dictionary for madlibs

        >   Creation Date   : 12.01-23
        >   Last update     :

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Copyright (C) 2023  Kristoffer Gjøsund
    """
    def MadlibsOne(self, *args):
        print(args)