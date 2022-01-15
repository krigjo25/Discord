# System repososary
from os import getenv
from random import randrange, shuffle


# DotEnv Repososary
from dotenv import load_dotenv


load_dotenv()

class Dictionaries():
    def __init__(self):
        self.bot = getenv('BotName')

    #   Emojies
    def EmojiDictionary ():
        
        #   Creating a dictionary for emojies
        dictionary = {
                    0: ':astonished',
                    1:':alien:',
                    2:':blush:',
                    3:':boom:',
                    4:':cold_sweat:',
                    5:':confounded:',
                    6:':no_mouth:',
                    7:':scream:',
                    8:':joy:',
                    9:':grin:',
                    10:':grinning:',
                    11:':grimacing:',
                    12:':smiley:',
                    13:':sparkles:',
                    14:':smile:',
                    15:':laughing:',
                    16:'smirk:',
                    17:':two_hearts:',
                    18:':+1:',
                    19:':muscle:',
                    20:':question:',
                    21:':see_no_evil:',
                    22:':fire:',
                }

        #   Randomize the dictionary
        shuffle(dictionary)
        x = randrange(0,10)
        arg = dictionary.get(x)

        return arg
    
    #   When the game is over due to to many attempts
    def GameOver():
        dictionary = {
                        0:f'Game Over',
                    }

        # Randomize the dictionary
        x = randrange(0,10)
        shuffle (dictionary)

        arg = dictionary.get(x)

        return arg

    #   Correct answer
    def CorrectAnswer():
        dictionary =  {
                        0:f'Congratulation you guessed correct',
                    }
        # Randomize the dictionary
        x = randrange(0,10)
        shuffle (dictionary)

        arg = dictionary.get(0)

        return arg

    #   Standard DificultyError    
    def DifficultyError():
        dictionary = {
                        0:f'let\'s fake it ',
                        1:f'difficulty mode IMPOSSIBLE enabled.',
                        2:f'bo, it looks like you wrote an unavailable mode, thanks',
                        3:f' Empty error string',
                        4:f'Created by @krigjo25',
                        5:f'Went looking for the selected mode couldn\'t solve the type issue',
                        6:f'Not mine mistake this time '
        }

        # Randomize the dictionary
        x = randrange(0,6)
        shuffle (dictionary)

        arg = dictionary.get(x)

        return arg

    #   AskQ dictionaries
    def PhiliosopicAnswer():
        dictionary = {
                    0:'What do you sense about it?',
                    1:'What would you do about it?',
                    2:'What are you really, deep down?',
                    3:'Just let it go, its not your issue.',
                    4:'Just let your self, experience the question',
                    5:'Visualize the question, and the answer will arrive.',
                    6:'If an human is a genious, then The best answers always comes from with-in, just believe in your self enough',
                    7:'As Socrets once said, you already know the answer of the question, since you had an idea of asking the question',
                    8:'Would you be able to let it go?',
        }

        # Randomize the dictionary
        x = randrange(0,8)
        shuffle (dictionary)

        arg = dictionary.get(x)

        return arg

    def DumbFacts():
        dictionary = {
                    0:'The earth is oval',
                    1:'The gravity exists',
                    2:'life is why',
                    3:'it just is',
                    4:'The opposite sides of a die will always add up to seven.',
                    5:'The King of Hearts is the only king in a deck of cards without a mustache.',
                    6:'There exist no answers for your questions, if you look with-in you know its true',
                    7:'Alaska is the only state whose name is on one row on a keyboard.',
                    8:'A "jiffy" is about one trillionth of a second.',
                    9:'The ocean is blue',
                    10:'Mulan has the highest kill-count of any Disney character.',
                    11:'The infinity sign is called a lemniscate.'
                }

        # Randomize the dictionary
        x = randrange(0,6)
        shuffle (dictionary)

        arg = dictionary.get(x)

        return arg

    #   Reaction Game
    def RockScissorPaper():
        dictionary = {
                    0:'\U0001FAA8',       #  somewhat rock
                    1:'\U00002702',       #  ✂️
                    2: '\U0001F4C4'       #  📄

                }

        #   Randomize the dictionary
        x = randrange(0,2)
        shuffle (dictionary)

        arg = dictionary.get(x)

        return arg

    #  Frequently Asked Questions