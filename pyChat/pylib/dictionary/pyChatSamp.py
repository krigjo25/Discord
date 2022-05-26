
#   Python Responsories

class Samp():

    def __init__(self):
        pass

    def QuestionsRelatedToSamp(question):
        question = str(question)

        whs = [
                'Whats samp',  
                'What is samp',
                'What is sanandreasmultiplayer',
                'Whats is sanandreasmultiplayer',
                'What is san andreas multi player',
                'Whats is san andreas multi player',]

        dsamp = [
                    'Where can samp be downloaded',
                    'Where can i download samp',
                    'Can i download samp',]

        sampREQ = [
                'What is the requirements for downloading samp', 'Whats the requirements for downloading samp'
                'what is samp req', 'whats is samp req', 'whats samp requirements', 'what is samp requirements',
                'what is samp requirement', 'whats samp requirements' 'Samp requirements', 'Samp req',]

        v1 = [  'Can i downgrade samp', 'I have samp version 2 how can i downgrade', 'Ive samp version 2, can i downgrade',
                'Downgrade samp', 'Samp downgrade',]

        gm = ['Samp gamemodes', 'Gamemodes samp', 'Game mode samp', 'What is a game mode', 'samp game mode']

        response = {
                    0:'San Andreas Multiplayer (SA:MP) or (SA-MP) is a game modification for Grand Theft Auto San Andreas (GTA:SA) which enables it to be a multiplayer game. You can play over the internet (or through LAN) with up to 999 other users (limited to 1,000 players online at once). SA-MP requires GTA:SA PC game to play online.',
                    1:'Well lucky you, i did a swap search the SA:MP client can be downloaded using this mirror (https://bit.ly/3yYEGDa)',
                    2:'SA:MP requires GTA:SA v1.00 US/EU version. V2.00 Can be downgraded using third-party patch (http://files.sa-mp.com/gtasapatch.zip), The third-party patch does not support (Steam / Direct2Drive) versions.',
                    3:'Version two can be downgraded to verison one, using a third-party patch (http://files.sa-mp.com/gtasapatch.zip). The third-party patch does not support (Steam / Direct2Drive) versions.',
                    #'A Game mode is a distinct configuration that affects how game mechanics behave. A game with several modes will present different settings in each mode. ',
                    
        }

        if question in whs or question in dsamp or question in sampREQ or question in v1:

            if question in whs: response = response.get(0)
            elif question in dsamp: response = response.get(1)
            elif question in sampREQ:response = response.get(2)
            elif question in v1:response = response.get(3)
            #elif question in gm:response = response[4]

            print(f' SAMP Related Question :\n{question}\n')
            print(f'SAMP Related Answer :\n{response}\n')
            print('samp related response :\n', response)
            return question, response
        
        #else: return question


    def EastCoastRPG(Question):
        pass