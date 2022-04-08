# System Repositories
from os import getenv
from random import randrange, shuffle


# DotEnv Repositories
from dotenv import load_dotenv


load_dotenv()

class Dictionaries():
    def __init__(self):
        self.bot = getenv('BotName')

    #   Emojies
    def EmojiDictionary ():
        
        #   Creating a dictionary for emojies
        dictionary = {
                    1: ':astonished',
                    2:':alien:',
                    3:':blush:',
                    4:':boom:',
                    5:':cold_sweat:',
                    6:':confounded:',
                    7:':no_mouth:',
                    8:':scream:',
                    9:':joy:',
                    10:':grin:',
                    11:':grinning:',
                    12:':grimacing:',
                    13:':smiley:',
                    14:':sparkles:',
                    15:':smile:',
                    16:':laughing:',
                    17:'smirk:',
                    18:':two_hearts:',
                    19:':+1:',
                    20:':muscle:',
                    21:':question:',
                    22:':see_no_evil:',
                    23:':fire:',
                }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)
        shuffle (dictionary)

        arg = dictionary.get(x)
        return arg