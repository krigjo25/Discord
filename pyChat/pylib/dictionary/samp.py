
#   Python Responsories+
from pylib.dictionary.samplist import CommonGlitches, SAMPCommonIssues, CommonIssues

class SampFAQ():

    def __init__(self):
        pass

    def CommonSAMPErrors(question):

         #   Initializing lists

        faq = CommonIssues()
        error = SAMPCommonIssues()

        if question in faq:

            res = ''
            li = SAMPCommonIssues()

            for i in li:
                res += f":arrow_right:{i}\n"

            return question, res


        elif question in error:

            response = {

                        #   Client common issues
                        'San andreas not found':'SA:MP requires GTA:SA (v1 US/EN) to start. Versions greater than one / Steam / Direct2Drive / Microsoft Store version will not work with the multi-player functionallity',
                        'I can not see any servers in samp browser':'Ensure the procedure to install SA:MP has been followed, if the issue continues samp must be allowed to accsess through your firewall.\n \nUnfortuantely, i can not offer you some support for firewalls yet\ni suggest you google your firewall manufactor\n Ensure you have the latest SA:MP version (https:://www.sa-mp.com/downloads)',
                        'Single player loads insted of samp':'There is not supposed to be single player options ( New Game, Load game, etc.) - SA:MP loads by it self during the connection procses. If single player has loaded Its NOT SAN ANDREAS MULTIPLAYER.\nThe Single player might load for one of the following reasons which i listed below\n :arrow_right: SA:MP has been installed in the wrong folder, or the version of GTA:SA which is not compitable with SA:MP.\nIt is easy to fix, dont be afraid. You can downgrade the version to v1.\n:arrow_right: Sometimes the single-player menu might be shown, but SA:MP should have loaded properly.\nTo fix this you simply need to select an item on the menu then press esc until you\'re out of it, then SA:MP will proceed to load.',
                        'I get "unacceptable nickname" when connecting to a server':'When you get the **\' Unacceptable name\'** :arrow_right:You\'re either using characters which is not supported in SA:MP. (Characters which is allowed 0-9, a-z, A-Z, SpecialSymbols such as [],(), $, @,(./,), _ =) and max 20 characters in length\nYou may also get kicked out of some servers for \' Unacceptable name\' due to the server does not allow special characters in the nickname\ni recommend characters such as (a-z, A-Z, 0-9).\n:arrow_right: It could be coused when another player with the same nickname as you\n:arrow_right: might happend if you re-connect the same server very soon after timeout or crash\n:arrow_right: SA:MP server with a greater up time than 50days can couse this glitch.',
                        'Screen sticks at "connecting to ip:port..."':f'**{question}**\nIf you can not connected to the server, trubleshooting..\n:arrow_right: Server might be offline\n:arrow_right: If you are not able to connect to any SA:MP server. Disable your\'r firewall, and try again. If connection procsess works then you\'ll have to set up you\'r firewall properly.\n:arrow_right: else then server might not support the current SA:MP version. Download the correct version of samp(https://www.sa-mp.com/downloads).',
                        'The game crashes when a vehicle explodes':'There is three ways to solve the issue\n:arrow_right: Disable your 2dr monitor, while playing SA:MP.\n:arrow_right: Set your Visual FX quality to low. (Esc > Options > Display Setup > Advanced)\n:arrow_right: Rename the GTA San Andreas folder (e.g to *\'GTA SA2\'*)(Sometimes it might stop working, then you rename it to something else)',
                        'My mouse doesn\'t work after exiting the pause menu':'If your mouse seems to be frozen ingame while it works, in the pause menu. Disable multicore option in *\'sa-mp.cfg\' set multicore=0*.\n Continuously tapping Escape until the mouse responds again may also work, but it is not as neat a solution.',
                        'The file dinput8.dll is missing':'This might arise when DirectX is not properly installed.\n:arrow_right: re-install Directx & restart you\'r computer.\n :arrow_right: If the issue continues just go at C:\Windows\System32 and copy paste the dinput.dll file to the root directory of your GTA San Andreas. That would solve it.',
                        'I cannot see other player\'s nametags!':'*Be aware*: some servers may have disabled nametags globally.\n:arrow_right: the issue often occures for Intel HD integrated graphics processors. The cause is unkown, a long term solution would be to install a dedicated grapic card in your computer, if it is possible and allows it. ',
                        'I have a modified gta: san andreas and samp won\'t load':'If SA:MP does not load. It might be coused by a modification as it interfers with the SA-MP client & cousing it to crash.',
                        'When launching gta with samp it won\'t start':'Delete *\' gta_sa.set\'* from the folder, userfiles, then you remove any modifications from the game & try again',
                        
                        #   Server common issues
                        'Packet was modified':'`[hh:mm:ss] Packet was modified, sent by id: <id>, ip: <ip>:<port>`\nWhen a player times out or has connection issues',
                        'MSVCR___.dll/MSVCP___.dll not found':'Download the appriate Microsoft Visual C++ runtime libraries. **Note that the SA-MP server is 32 bit**',
                        'Warning: client exceeded ackslimit':'`Warning: client exceeded *\'ackslimit\'* <ip>:<port> (<count>) Limit: x/sec`\nhappens when acks limit exceeds',
                        'Warning: client exceeded messageholelimit':'`Warning: client exceeded *\'messageholelimit\'* (<type>) <ip>:<port> (<count>) Limit: x`\nhappens when message hole limit exceeds.',
                        'Warning: client exceeded messageslimit':'`Warning: client exceeded *\'messageslimit\'* (1) <ip>:<port> (<count>) Limit: x/sec`\nhappens when number of messages per second a client sends to the server exceeds.',
                        'Warning: Too many out-of-order messages':'`Warning: Too many out-of-order messages from player <ip>:<port> (<count>) Limit: x (messageholelimit)`\nhappens when *\'out of order messages`\'* reuses messageholelimit setting.',
                        'Players constantly getting "unacceptable nickname" error but it is valid':'ensure the name is acceptable, and the server is running on a Windows, 1. Change the compatibality for *\' samp-server.exe\'* to Windows 98, restart the server.\n 2. The issue might appear when the server is up 50+ days.',
                        'Server instantly crashes when started':'Commonly there is an error in your *\'server.cfg\'* file. Ud the reason is not located at the bottom of the file.check *\' crashinfo.txt\'* a better solution would be using the Crash detect plugin by Zeex (https://github.com/Zeex/samp-plugin-crashdetect) for more information',
                        'Server is not working - firewall is disabled':'You will need to forward your ports to allow players to join your server. You can forward your ports using the PF Port Checker. Download it from: (www.portforward.com) If the ports are not forwarded that means you have to open them in your router. You can check the router list at (http://portforward.com/english/routers/port_forwarding/routerindex.htm) for more information',
                        
                        #   Pawno common issues
                        'Failed to set data for ': 'Run pawno.exe as an administrator',
                        'Unable to execute compiler on windows vista/7': 'In the dictionary where pawno.exe is, there will be a file called settings.ini.\n :arrow_right: Open it in a text editor change \'FileAssoc\' from 1 to 0\n :arrow_right: Run pawno.exe as an administrator'
                        }       

            response = response[question]

            return question, response

        return


    def CommonSAMPGlitches(question):

        faq = CommonGlitches()
        #glitches = CommonGlitchesAnswer()

        if question in faq:

            res = ''
            li = CommonGlitches()

            for i in li:res += f":arrow_right:{i}\n"
            return question, res

        elif question in glitches:

            response = {}

            return question, response

        return