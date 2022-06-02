
#   Python Responsories
from pylib.dictionary.samplist import SAMPClient, SAMPServerCommonIssues, SAMPErrors, SAMPCommonIssues, CommonIssues

class SampFAQ():

    def __init__(self):
        pass

    def CommonIssues(question):

        faq = CommonIssues()

        if question in faq:res = SAMPCommonIssues()

        return question, res

    def Client(question):

        """
            Frequently asked question about the client
        """

        #   Initializing lists
        client = SAMPClient()

        if question in client:

            indexCounter = client.index(question)

            response = {
                            0:'San Andreas Multiplayer (SA:MP) or (SA-MP) is an unoffical modification for Grand Theft Auto San Andreas (GTA:SA).\nThe modification grants us accsess to play GTA:SA over internet (or through LAN Network).\nWith a limitation to 1,000 players connected at once.\nSA-MP requires GTA:SA v1.00 PC game US/EN Version for the modification to work.',
                            1:'Well the most recent SA:MP client can be downloaded using this mirror SA:MP team mirror :(https://bit.ly/3yYEGDa)',
                            2:'SA:MP requires GTA:SA v1.00 US/EU version.\nV2.00 Can be downgraded using third-party patch (http://files.sa-mp.com/gtasapatch.zip).\nThe third-party patch does not support (Microsoft Store / Steam / Direct2Drive) versions.\n\n**System requirements for SA:MP:**\nSA:MP runs GTA:SA with better performence on any computer. \nHowever the lower specs, the greater the chance for large servers might run slower.\n\n**Minimum requirements**\n:arrow_right: 1 GHz Processor\n:arrow_right: Pentium 3 / Athlon or equivalent\n:arrow_right: 256MB RAM\n:arrow_right: Win 98/Me/2000/Xp/Vista\n:arrow_right: 64MB Graphics Card (DirectX 9 compatible)\n:arrow_right: Radeon 8500 / GeForce 3 or equivalent\n:arrow_right: 8X DVD-ROM Drive\n:arrow_right: 3.6GB free HD space\n:arrow_right: DirectX 9 compatible soundcard\n\n**What i would Recommended**\n:arrow_right: Intel pentium 4 HT 2,8 Ghz Processor Intel pentium D 3.0 GHZ / AMD Athlon X2 3800+\n:arrow_right: 1GB RAM\n:arrow_right: Win 98/Me/2000/Xp\n:arrow_right: PCIe 256MB Graphics Card (DirectX 9c compatible)\n:arrow_right: Radeon X800 / GeForce 6,7 or equivalent\n:arrow_right: 16X DVD-ROM Drive\n:arrow_right: 5.0GB free HD space\n:arrow_right: DirectX 9 compatible soundcard\n\n**SA:MP specifications**\n:arrow_right: In addition to the standard Single Player requirements, SA:MP needs the following:\n:arrow_right: 50MB free Hard Drive space\n:arrow_right: An Internet Connection (512k+ Broadband is highly recommended for smooth online play)\n:arrow_right: A copy of GTA San Andreas for PC - V1.0 *[NOT greater than v1,0. Neither versions from (Steam, Micrsoft Store, Direct2Drive)]*',
                            3:'Version two can be downgraded to verison one, using a third-party patch (http://files.sa-mp.com/gtasapatch.zip).\nUnless it is (Steam / Direct2Drive) versions.',
                            4:'SA:MP installation procedure(Windows):\n:arrow_right: Ensure you have a copy of GTA:SA (US/EN) (v1.00) installed on your computer (V.1) download the patcher(http://files.sa-mp.com/gtasapatch.zip) to downgrade the GTA:SA to v.1\n:arrow_right: Download SA:MP using this SA:MP team mirror :(https://bit.ly/3yYEGDa) and  install it where the gtasa.exe file is located. let the game pass through the firewall\n:arrow_right: Choose a custom Nickname ((a-z),(A-Z), (0-9) as some servers may be disallowing special characters) and connect to a server. ',

                        }

            #   Checking if the condition is true
            if indexCounter >= 0 and indexCounter <= 6: response = response[0]
            elif indexCounter >= 7 and indexCounter <= 9: response = response[1]
            elif indexCounter >= 10 and indexCounter <= 20: response = response[2]
            elif indexCounter >= 21 and indexCounter <= 24: response  = response[3]

            print(f'SAMP Related Question :\n{question}\n')
            print(f'SAMP Related Answer :\n{response}\n')

            return question, response
            
        return

    def Server(question):

         #   Initializing lists
        srv = SAMPServerCommonIssues() 

        if question in srv:

            indexCounter = srv.index(question)
            response = {
                        0:'commonly there is an error in your *\'server.cfg\'* file and the reason should be located at the bottom of the file.\nIf not check *\' crashinfo.txt\'* a better solution would be using the Crash detect plugin by Zeex (https://github.com/Zeex/samp-plugin-crashdetect) for more information',
                        1:'You will need to forward your ports to allow players to join your server. You can forward your ports using the PF Port Checker. Download it from: www.portforward.com If the ports are not forwarded that means you have to open them in your router. You can check the router list at (http://portforward.com/english/routers/port_forwarding/routerindex.htm) for more information',
                        2:'`[hh:mm:ss] Packet was modified, sent by id: <id>, ip: <ip>:<port>`\nWhen a player times out or has connection issues',
                        3:'`Warning: client exceeded *\'messageslimit\'* (1) <ip>:<port> (<count>) Limit: x/sec`\nhappens when number of messages per second a client sends to the server exceeds.',
                        4:'`Warning: client exceeded *\'ackslimit\'* <ip>:<port> (<count>) Limit: x/sec`\nhappens when acks limit exceeds',
                        5:'`Warning: client exceeded *\'messageholelimit\'* (<type>) <ip>:<port> (<count>) Limit: x`\nhappens when message hole limit exceeds.',
                        6:'`Warning: Too many out-of-order messages from player <ip>:<port> (<count>) Limit: x (messageholelimit)`\nhappens when *\'out of order messages`\'* reuses messageholelimit setting.',
                        7:':arrow_right: Try to change the compatibility option of the samp-server.exe to windows 98 & restart\n:arrow_right: a server rebot should resolve it',
                        8:'Download the appriate Microsoft Visual C++ runtime libraries. **Note that the SA-MP server is 32 bit**',
                        9:'Run pawno.exe as an administrator',
                        10:'In the dictionary where pawno.exe is, there will be a file called settings.ini.\n :arrow_right: Open it in a text editor change \'FileAssoc\' from 1 to 0\n :arrow_right: Run pawno.exe as an administrator'
                        }

            #   Checking if the condition is true
            if indexCounter >= 0 and indexCounter <= 6: response = response[0]
            elif indexCounter >= 7 and indexCounter <= 9: response = response[1]
            elif indexCounter >= 10 and indexCounter <= 20: response = response[2]
            elif indexCounter >= 21 and indexCounter <= 24: response  = response[3]

            print(f'SAMP Related Question :\n{question}\n')
            print(f'SAMP Related Answer :\n{response}\n')

            return question, response

        return

    def Error(question):

         #   Initializing lists
        sampErrors = SAMPErrors()

        if question in sampErrors:

            response = {

                        0:'SA:MP requires GTA:SA (v1 US/EN) to start. Versions greater than one / Steam / Direct2Drive / Microsoft Store version will not work with the multi-player functionallity',
                        1:'Ensure the procedure to install SA:MP has been followed, if the issue continues samp must be allowed to accsess through your firewall.\n \nUnfortuantely, i can not offer you some support for firewalls yet\ni suggest you google your firewall manufactor\n Ensure you have the latest SA:MP version (https:://www.sa-mp.com/downloads)',
                        2:'There is not supposed to be single player options ( New Game, Load game, etc.) - SA:MP loads by it self during the connection procses. If single player has loaded Its NOT SAN ANDREAS MULTIPLAYER.\nThe Single player might load for one of the following reasons which i listed below\n :arrow_right: SA:MP has been installed in the wrong folder, or the version of GTA:SA which is not compitable with SA:MP.\nIt is easy to fix, dont be afraid. You can downgrade the version to v1.\n:arrow_right: Sometimes the single-player menu might be shown, but SA:MP should have loaded properly.\nTo fix this you simply need to select an item on the menu then press esc until you\'re out of it, then SA:MP will proceed to load.',
                        3:'When you get the **\' Unacceptable name\'** :arrow_right:You\'re either using characters which is not supported in SA:MP. (Characters which is allowed 0-9, a-z, A-Z, SpecialSymbols such as [],(), $, @,(./,), _ =) and max 20 characters in length\nYou may also get kicked out of some servers for \' Unacceptable name\' due to the server does not allow special characters in the nickname\ni recommend characters such as (a-z, A-Z, 0-9).\n:arrow_right: It could be coused when another player with the same nickname as you\n:arrow_right: might happend if you re-connect the same server very soon after timeout or crash\n:arrow_right: SA:MP server with a greater up time than 50days can couse this glitch.',
                        4:f'**{question}**\nIf you can not connected to the server, trubleshooting..\n:arrow_right: Server might be offline\n:arrow_right: If you are not able to connect to any SA:MP server. Disable your\'r firewall, and try again. If connection procsess works then you\'ll have to set up you\'r firewall properly.\n:arrow_right: else then server might not support the current SA:MP version. Download the correct version of samp(https://www.sa-mp.com/downloads).',
                        5:'There is three ways to solve the issue\n:arrow_right: Disable your 2dr monitor, while playing SA:MP.\n:arrow_right: Set your Visual FX quality to low. (Esc > Options > Display Setup > Advanced)\n:arrow_right: Rename the GTA San Andreas folder (e.g to *\'GTA SA2\'*)(Sometimes it might stop working, then you rename it to something else)',
                        6:'If your mouse seems to be frozen ingame while it works, in the pause menu. Disable multicore option in *\'sa-mp.cfg\' set multicore=0*.\n Continuously tapping Escape until the mouse responds again may also work, but it is not as neat a solution.',
                        7:'This might arise when DirectX is not properly installed.\n:arrow_right: re-install Directx & restart you\'r computer.\n :arrow_right: If the issue continues just go at C:\Windows\System32 and copy paste the dinput.dll file to the root directory of your GTA San Andreas. That would solve it.',
                        8:'*Be aware*: some servers may have disabled nametags globally.\n:arrow_right: the issue often occures for Intel HD integrated graphics processors. The cause is unkown, a long term solution would be to install a dedicated grapic card in your computer, if it is possible and allows it. ',
                        9:'If SA:MP does not load. It might be coused by a modification as it interfers with the SA-MP client & cousing it to crash.',
                        10:'Delete *\' gta_sa.set\'* from the folder, userfiles, then you remove any modifications from the game & try again',
                        11:'Theis is a common issue with *\'server.cfg\'* check *\'server_log.txt\'* or *\'crashinfo.txt\'* in order to find out what couses the issue',
                        12:'The tranport has to be open, it can be opened with PFPC- software. (www.pfforward.com).\n If the port does not open, a port has to be open on the Internet router',
                        13:'ensure the name is acceptable, and the server is running on a Windows, 1. Change the compatibality for *\' samp-server.exe\'* to Windows 98, restart the server.\n 2. The issue might appear when the server is up 50+ days.'
                }

            print(f'SAMP Related Question :\n{question}\n')
            print(f'SAMP Related Answer :\n{response}\n')

            return question, response

        return
    