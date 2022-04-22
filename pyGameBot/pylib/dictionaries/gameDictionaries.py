
# Python Repositories
from os import getenv
from random import randrange, shuffle


#   Dotenv Repositories
from dotenv import load_dotenv


load_dotenv()

class GameDictionary():

    def __init__(self):
        return

    """
        Dictionary for the gameModule
    """

    #   After a game ends
    def CorrectAnswer(self):

        """
            #   When a player has won a game
        """
        dictionary =  {
                        1:'Congratulation you guessed correct',
                        2:'',
                    }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)

        return dictionary.get(x)

    def GameOver(self):

        """
            When a player has lost a game
        """

        dictionary = {
                        1:f'Game Over',
                        2:'',
                    }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)

        return dictionary.get(x)

    def CustomAnswer(self, num, x):

        if num > x:

            dictionary = {
                            1:'Well well, we like the answer more humble than a greater answer',
                            2:'The given number is not humble enough, try again.',
                            3:'is greater than the answer ',1:'Do you know why the equal sign are so humble? neither were less or greater !',
                            }

        elif num < x:

            dictionary = {
                            1:f'**{num}** is less, we want more',
                            2:f'**{num}** is less than i ask for',
                            3:f'**{num}** is less akward than :100:',
                            4:f'**{num}** is less humble',
                            }

        else:

            dictionary = {
                            1:f'Thank you for the humble answer, sir ',
                            2:f'Well thats equal..'
                           }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)

        return dictionary.get(x)

class GameError():

    def __init__(self):
        return

        #   Game Errors    
    def DifficultyError(self, diff):

        """

        #   Difficulty doesnt not exist
        #   looping Through difficulties available

        """
        diff = str(diff)

        dictionary = {
                        1:f'let\'s fake it ',
                        2:f'difficulty mode IMPOSSIBLE enabled.',
                        3:f'bo, it looks like you wrote an unavailable mode, thanks',
                        4:f'This is an empty error arg',
                        5:f'Created by @krigjo25',
                        6:f'Went looking for the selected Difficulty couldn\'t solve the type issue',
                        7:f'Sometimes this happends.',
}

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)

        return dictionary.get(x)

class PhiliosopicAnswer():

    def __init__(self):
        return

    #   AskQ dictionaries
    def PhiliosopicAnswer(self):

        dictionary = {
                    1:'What do you sense about it?',
                    2:'What can  you actually do about it?',
                    3:'What are you really, deep down?',
                    4:'Just let it go, its not your issue.',
                    5:'Just let your self, experience the question.',
                    6:'Visualize the question, and the answer will arrive.',
                    7:'If an human is a genious, then The best answers always comes from with-in, just believe in your self enough.',
                    8:'As Socrets once said, you already know the answer of the question, since you had an idea of asking the question.',
                    9:'Would you be able to let it go?',
                    10:'A Question does not arise with out it\'s answer, so place your attention on where the question has arised',
                    11:'From where does the question actually answer?',
                    12:'Life is just like one of the elements on earth, just flow with it',
                    13:'Einstein said once if the world were ending, and i had one hour to solve a problem " i would use 50 minutes to think about the issue, then use the 10 last minutes to solve the issue".',
                    14:'As the thought araises from with-in it can only be answered from with-in',

}

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)
        print(dictionary.get(x))

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
        x = len(dictionary)
        x = randrange(1,x)

        return dictionary.get(x)

class ReactionGame():
    #   arg Game Dictionaries
    def RockScissorPaper(self):

        dictionary = {
                        1:'\U0001FAA8',          #  somewhat rock
                        2:'\U00002702',          #  ✂️
                        3:'\U0001F4C4'           #  📄
}

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)

        return dictionary.get(x)

    def TowTie(self):

        dictionary = {

                    1:f'Pybut draws a **tie**',
                    2:'Sir, lets **tie** a **tie**',
                    3:'What did the **tie** say to the **bowtie**? You\'re a weirdo',
                    4:f'Pybut **draw**ing a toe.',
                }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)

        return dictionary.get(x)
    
    def BotWin(self, arg):

        #   Initializing variables
        bot = getenv('botName')
        
        if arg == '\U0001FAA8':

            dictionary = {
                            1:f'That moment, when you realize :stone doesn\'t play along with :Scissors',
                            2:f'Congratulations, this game were Rock Hard !',
                            3:f'It were crushing days for the scissors',
                            4:f'pyBot Says : look behind you. **running away **.',
}

        elif arg == '\U0001F4C4':

            dictionary = {
                            1:f'{bot} sent your stone to North-Korea !',
                            2:f'You recieved a new stone as a christmas :gift:',
                            3:f'You have been mumified by {bot}',
}

        else:
        
            dictionary = {
                            1:f'Noone : \'\'\n{bot} : Oh snap',
                            2:f'The paper were succsessfully cut in two by {bot} ',
                            3:f'{bot} flexed with his scissors, you lost',
                            4:f'i won '
}

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)

        return dictionary.get(x)

    def MemberWin(self, arg, arg1):

        #   Initializing variables
        bot = getenv('botName')

        if arg == '\U0001FAA8':

            dictionary = {
                            0:f'{bot} had the idea of using a {arg1} against your {arg}, {bot} thought the {arg1} were strong enough to cut thorugh your {arg}, lets do a wii-match',
                            1:f'Congratulations, lets do it again',
                            2:f'You just had a {arg}, while {bot} had the thought of {arg1} would be a grate choice.',
                            3:f'OH SNAP, you just scared {bot}, he never returned to the battle field.',
                    }

        elif arg == '\U0001F4C4':

            dictionary = {
                            0:f'{bot} threw {arg1} at you, but you grabbed it with his {arg}, and wrapped it into a :package: \n you gave a :package: to {bot}, how considerate of you !',
                            1:f'You wrappend {bot}\'s {arg1} into a :gift: and sent it to the North-Pole, Santa were stoned for the Christmas ',
                            2:f'You made a mumified version of {bot}',
                    }

        else:
        
            dictionary = {
                            0:f'Noone : \'\'\n{bot} : Oh snap',
                            1:f'You succsessfully cut the {arg1} with a {arg}',
                            2:f'you showed of with his :scissors: which he thought were a knife, but the goal were reached, {bot} ran.',
                            3:f'you won '
                    }

        #   Randomize the dictionary
        x = len(dictionary)
        x = randrange(1,x)

        return dictionary.get(x)

class JumbleCategory():

    def __init__(self) -> None:
        pass

    def Titles(self):

        category = [
                    ['Random Jumbles', 'selecting a random jumble category\n'],
                    ['Walt Disney', '- Animation,\n- Characters,\n- Roles,\n'],
                    ['Animal kingdom', '- flyingCreatures \n- Cats\n'],
                    ]

        return category

    def SubTitle(self, sub):

        sub = str(sub).lower()

        if sub == 'walt disney':

            category = ['- Characters\n- Animations,\n- Roles']

        elif sub == 'animal kingdom':

            category = ['- flyingCreatures \n- Cats,\n- Dogs']
        else:
            category = ['An unexpected error']

        for sub in category:

            return sub
