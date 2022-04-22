from random import sample
class Jumble():
    def __init__(self):
        pass

    #   Creating a function, to be the category picker

    def Jumble(word):

        #   Shuffle the characters of the word
        randomWord = sample(word, len(word))
    
        #   Join the elements of the iterator with particular character.
        jumbled = ''.join(randomWord)

        #   Returning the randomized characters
        return jumbled