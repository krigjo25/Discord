
#   Python Responsories
from pylib.dictionary.list import SAMPClient, SAMPServer, SAMPErrors
class Samp():

    def __init__(self):
        pass

    def FrequentlyAskedQuestionsSAMP(question):


        client = SAMPClient(question)
        sampServer = SAMPServer(question) 
        sampErrors = SAMPErrors(question)

        if question in client  or question in sampServer or question in sampErrors:

            if question in client:

                indexCounter = client.index(question)
                minreq = '** The system requirements can be found in (https://team.sa-mp.com/wiki/Introduction.html#What_is_SA:MP.3F)'
                response = {

                            0:'''San Andreas Multiplayer (SA:MP) or (SA-MP) is an unoffical modification for Grand Theft Auto San Andreas (GTA:SA).
The modification grants us the ability to play GTA:SA over the internet (or through LAN) with up to 999 other users (limited to 1,000 players online at once).
SA-MP requires GTA:SA v1.00 PC game US / EN Version for the modification to work.''',
                            1:'Well the most recent SA:MP client can be downloaded using this mirror SA:MP team mirror :(https://bit.ly/3yYEGDa)',
                            2:f'''SA:MP requires GTA:SA v1.00 US/EU version. 
V2.00 Can be downgraded using third-party patch (http://files.sa-mp.com/gtasapatch.zip), 
The third-party patch does not support (Steam / Direct2Drive) versions.\n
System requirements for SA:MP:
SA:MP runs on any computers, which can run GTA:SA, with better performance, 
However the lower specs, the greater the chance for large servers might run slower.
Requirements can be found {minreq}''',
                            3:'Version two can be downgraded to verison one, using a third-party patch (http://files.sa-mp.com/gtasapatch.zip). The third-party patch does not support (Steam / Direct2Drive) versions.',
                            4:'''
SA:MP installation procedure(Windows):\n
1. Ensure you have a copy of GTA:SA installed on your computer (V.1) download the patcher(http://files.sa-mp.com/gtasapatch.zip) to downgrade the GTA:SA to v.1
2. Download SA:MP using this SA:MP team mirror :(https://bit.ly/3yYEGDa) and  install it where the gtasa.exe file is located. let the game pass through the firewall
3. Choose a nickName and connect to a server. '''
                }
                print (indexCounter)
                #   Checking if the condition is true
                if indexCounter >= 0 and indexCounter <= 6: response = response[0]
                elif indexCounter >= 7 and indexCounter <= 9: response = response[1]
                elif indexCounter >= 10 and indexCounter <= 20: response = response[2]
                elif indexCounter >= 21 and indexCounter <= 24: response  = response[3]


            elif question in sampServer:

                response = {

                            0:'',

                }
            elif question in sampErrors:

                response = {

                            0:'SA:MP requires GTA:SA v1 US/EN version in order to start. Versions such as Steam or Direct2Drive can not be used.',
                            1:'Ensure the procedure to install SA:MP has been followed, if the issue continues, ensure you have allowed SA:MP to accsess through your firewall.',
                            2:'The Single player loads for one of the reasons listed below \n SA:MP has been installed in the wrong folder, or the version of GTA:SA is not compitable with SA:MP.',
                            3:'When you get the **\' Unacceptable name\'** You\'re using characters which is not supported in SA:MP or names which might couse some glitch for the server, recommended characters is a-z, A-Z, 0-9.',
                            4:'The server might be offline. If it\'s not possible to connect any server. \n 1. Check if you have the newest version of SA:MP.\n2. deactivate your firewall, if the deactivation of the firewall works, you have to setup your firewall correctly.',
                            5:'If SA:MP does not load. It might be coused by a modification as it interfers with SA-MP client & cousing it to crash.',
                            6:'Delete *\' gta_sa.set\'* from the folder, userfiles, then you remove any modifications from the game & try again',
                            7:'Theis is a common issue with *\'server.cfg\'* check *\'server_log.txt\'* or *\'crashinfo.txt\'* in order to find out what couses the issue',
                            8:'The tranport has to be open, it can be opened with PFPC- software. (www.pfforward.com).\n If the port does not open, a port has to be open on the Internet router',
                            9:'ensure the name is acceptable, and the server is running on a Windows, 1. Change the compatibality for *\' samp-server.exe\'* to Windows 98, restart the server.\n 2. The issue might appear when the server is up 50+ days.'
                }

            print(f'SAMP Related Question :\n{question}\n')
            print(f'SAMP Related Answer :\n{response}\n')
            print('samp related response :\n', response)
            return question, response
        
        #else: return question


    def FrequentlyAskedQuestionsECRPG(question):

        ecrpg = [
                'Ecrpg ip',  
                'Ip of ecrpg',
                'Ecrpg server ip',
                'Server ip of ecrpg',
                ]

        pass