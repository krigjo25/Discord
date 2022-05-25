
#   Python Responsories
from random import Random

class Samp():

    def __init__(self):
        pass

    def QuestionsRelatedToSamp(question):

        faq = [
                'W', 'What is samp?', 'what is samp', 'what\'s samp?',

                'Where can samp be downloaded?','Where can i download samp?',
                'where can i download samp?', 'Can i download samp?',
                'Where can samp be downloaded','Where can i download samp',
                'where can i download samp', 'Can i download samp',
                
            ]

        if question in faq:

            x = faq.index(question)
            response = {

            0:'San Andreas Multiplayer (SA:MP) is a modification for Grand Theft Auto: San Andreas which turns it into a multiplayer game. You can play over the internet (or LAN) with up to 999 other people (having up to 1,000 players online at once). You need the original Grand Theft Auto: San Andreas PC game to play San Andreas Multiplayer.',
            1:'It can be downloaded at samp.com',
            

                    }
            return question, response.get(x)
        else:
            question = ''
            response = ''
            return question, response

