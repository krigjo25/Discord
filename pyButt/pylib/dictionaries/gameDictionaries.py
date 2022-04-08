# System repososary
from os import getenv
from random import randrange, shuffle


# DotEnv Repososary
from dotenv import load_dotenv


load_dotenv()

class Dictionaries():
    def __init__(self):
        self.bot = getenv('BotName')

    #   After a game ends
    def CorrectAnswer():
        dictionary =  {
                        0:f'Congratulation you guessed correct',
                    }
        # Randomize the dictionary
        x = randrange(0,10)
        shuffle (dictionary)

        arg = dictionary.get(0)

        return arg

    def GameOver():
        dictionary = {
                        1:f'Game Over',
                    }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)
        shuffle (dictionary)

        arg = dictionary.get(x)
        return arg

    #   Game Errors    
    def DifficultyError():
        dictionary = {
                        1:f'let\'s fake it ',
                        2:f'difficulty mode IMPOSSIBLE enabled.',
                        3:f'bo, it looks like you wrote an unavailable mode, thanks',
                        4:f'This is an empty error string',
                        5:f'Created by @krigjo25',
                        6:f'Went looking for the selected mode couldn\'t solve the type issue',
                        7:f'Not mine mistake this time '
        }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)
        shuffle (dictionary)

        arg = dictionary.get(x)
        return arg

    #   AskQ dictionaries
    def PhiliosopicAnswer():
        dictionary = {
                    1:'What do you sense about it?',
                    2:'What would you do about it?',
                    3:'What are you really, deep down?',
                    4:'Just let it go, its not your issue.',
                    5:'Just let your self, experience the question',
                    6:'Visualize the question, and the answer will arrive.',
                    7:'If an human is a genious, then The best answers always comes from with-in, just believe in your self enough',
                    8:'As Socrets once said, you already know the answer of the question, since you had an idea of asking the question',
                    9:'Would you be able to let it go?',
                    10:'A Question does not arise with out it\'s answer, so place your attention on where the question has arised',
        }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)
        shuffle (dictionary)

        arg = dictionary.get(x)
        return arg

    def DumbFacts():
        dictionary = {
                    1:'The earth is oval',
                    2:'The gravity exists',
                    3:'life is why',
                    4:'it just is',
                    5:'The opposite sides of a die will always add up to seven.',
                    6:'The King of Hearts is the only king in a deck of cards without a mustache.',
                    7:'There exist no answers for your questions, if you look with-in you know its true',
                    8:'Alaska is the only state whose name is on one row on a keyboard.',
                    9:'A "jiffy" is about one trillionth of a second.',
                    10:'The ocean is blue',
                    11:'Mulan has the highest kill-count of any Disney character.',
                    12:'The infinity sign is called a lemniscate.'
                }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)
        shuffle (dictionary)

        arg = dictionary.get(x)
        return arg

    #   Reaction Game Dictionaries
    def RockScissorPaper():
        dictionary = {
                    1:'\U0001FAA8',       #  somewhat rock
                    2:'\U00002702',       #  ✂️
                    3: '\U0001F4C4'       #  📄

                }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)
        shuffle (dictionary)

        arg = dictionary.get(x)
        return arg


        return arg

    def TowTie():
        dictionary = {

                    1:f'Pybut draws a **tie**',
                    2:'Sir, lets **tie** a **tie**',
                    3:'What did the **tie** say to the **bowtie**? You\'re a weirdo',
                    4:f'Pybut **draw**ing a toe.',
                }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)
        shuffle (dictionary)

        arg = dictionary.get(x)
        return arg

Dictionaries.TowTie()