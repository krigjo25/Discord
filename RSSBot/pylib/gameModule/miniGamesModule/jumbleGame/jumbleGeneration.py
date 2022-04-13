from random import sample

class Jumbles():
    def __init__(self):
        pass

    def GenerateJumble(word):

        """         GenerateJumble
                Jumbles the words randomly 
        """

        #   Shuffle the characters of the word
        randomize = sample(word, len(word))
    
        #   Join the elements of the iterator with particular character.
        jumble = ''.join(randomize)

        return jumble