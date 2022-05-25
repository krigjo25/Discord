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

    def Greetings(q):

        """

            When a member joins the community, we greet the member
        
        """
        Greetings = ['Good morning', 'Good Evening', 'Hi', 'Hello', 'Hey', 'Good morning', 'Good day',]
        var = ['Bad', 'Not good',]
        ynm = ['Yes', 'No', 'Maybe', 'Might',]

        if q in Greetings:

            response = {
                            0:'Hello, how are you today?',
                            1:'Hey, how are you today?',
                            2:'Hi, how are you today?',
                            3:'Salutè, how are you today?',
                            4:'Good morning, how are your day going?',
                            5:'Good evening, how are your evening?',
                            6:'Howdy, how are you today?',

            }

        elif q in var:

            response = {
                    1:'Then i suggest you, just let it go, its okay to have a bad day, isn\'t it?',
                    2:'Would you be able to let it go?',
                    3:'Well.. Its just life, like one of the elements on earth, just flow with it',
}

            #   Randomize the dictionary
            x = len(response)
            x = randrange(1,x)

            return q, response.get(x)

        elif q in ynm:

            response = {
                        0:'Thats great too, just be you. Nothing else i want you to be',
                        1:'Well, the time will heal.',
                        2:'Just be with the sensation',


            }

            #   Randomize the dictionary
            x = len(response)
            x = randrange(1,x)

            return q, response.get(x)