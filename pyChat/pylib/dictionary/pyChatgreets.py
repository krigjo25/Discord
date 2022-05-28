from random import randint, shuffle, randrange


class GreetMember():

    def __init__(self):
        pass

    def UserInputs(msg):

        """

            When a member joins the community, we greet the member
        
        """
        liste = [
            'Hi', 'Hello', 'Hey', 'Good morning', 'Good day', 
            'Good evening'

        ]
        
        for msg in liste:
            return liste

        return

    def Greetings(question):

        """

            When a member joins the community, we greet the member
        
        """
        greet = [
                        'Good morning', 
                        'Good Evening', 
                        'Hi', 
                        'Hello', 
                        'Hey', 
                        'Good morning', 
                        'Good day',
                        'Hey There you are',]

        
        negative = ['Bad', 'Not good',]

        positive = ['Fine', 'Good', 'Never been better', 'Never better',
                    'Great',]
        ynm =[
                'Yes', 'No', 'Maybe', 'Might',]

        if question in greet or question in negative or question in positive or question in ynm:

            if question in greet:


                dictionary = {
                                0:'how are you?',
                                1:'what\'s new?',
                                2:'what\'s the good word for today?'
                }
                shuffle(dictionary)

                response = {
                            0:f'Hello, {dictionary.get(randrange(0,len(dictionary)-1))}',
                            1:f'Hey, {dictionary.get(randrange(0,len(dictionary)-1))}',
                            2:f'Hi, {dictionary.get(randrange(0,len(dictionary)-1))}',
                            3:f'Salutè, {dictionary.get(randrange(0,len(dictionary)-1))}',
                            4:f'Good morning, {dictionary.get(randrange(0,len(dictionary)-1))}',
                            5:f'Good evening, {dictionary.get(randrange(0,len(dictionary)-1))}',
                            6:f'Howdy, {dictionary.get(randrange(0,len(dictionary)-1))}',
                            7:f'Greetings, how can i be at service for you to day?',
                            8:f'I\'m Happy to see you !',

            }
            elif question in negative:

                response = {
                            0:'Just let it go, man its okay to have a bad day, isn\'t it?',
                            1:'Would you be able to let it go?',
                            2:'Well.. Its just life, like one of the elements on earth, just flow with it',
                }

            elif question in ynm:

                response = {
                            0:'Thats great too, just be you. Nothing else i want you to be',
                            1:'Well, the time will heal.',
                            2:'Just be with the sensation',
            }

            #   Randomize the dictionary
            shuffle(response)
            x = len(response)
            x = randrange(0,x)

            response =  response.get(x)

            return question, response
