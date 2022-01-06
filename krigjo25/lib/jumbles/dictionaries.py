from random import randrange, shuffle
class Dictionaries():
    def __init__(self):
        pass

    def jumbleOver():
        gameOver = {
                        0:f'Jamie\'s answer were',
                    }
        x = 0 #randrange(0,6)
        gameOver = gameOver.get(x)
        return gameOver 

    def CorrectAnswer():
        answer =  {
                        0:f'Congratulation you guessed correct',
                    }
        x = 0 #randrange(0,6)     
        CorrectAnswer = answer.get(x)
        return CorrectAnswer

    def DifficultyError():
        modeError = {
                        0:f'let\'s fake it ',
                        1:f'difficulty mode IMPOSSIBLE enabled.',
                        2:f'bo, it looks like you wrote an unavailable mode, thanks',
                        3:f' Empty error string',
                        4:f'Created by @krigjo25',
                        5:f'Went looking for the selected mode couldn\'t solve the type issue',
                        6:f'Not mine mistake this time '
        }
        x = randrange(0,6)
        modeError = modeError.get(x)
        return modeError