from random import shuffle, randrange


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
                        'Good day',]

        
        var = [
                'Bad', 'Not good',]
        ynm =[
                'Yes', 'No', 'Maybe', 'Might',]

        if question in greet or question in var or question in ynm:

            if question in greet:

                response = {
                            0:'Hello, how are you today?',
                            1:'Hey, how are you today?',
                            2:'Hi, how are you today?',
                            3:'Salutè, how are you today?',
                            4:'Good morning, how are your day going?',
                            5:'Good evening, how are your evening?',
                            6:'Howdy, how are you today?',
                            7:'Greetings, how can i be at service for you to day?',

            }
            elif question in var:

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
            x = len(response)
            x = randrange(0,x)

            response =  response.get(x)

            return question, response

        else:
            return question
