
#   Python Responsories+
from pylib.list.samplist import CommonGlitches, CommonIssues, CommonSAMPGlitches, CommonSAMPIssues

class SampFAQ():

    def __init__(self):
        pass

    def GeneralSAMPQuestions(Question):
        pass

    def CommonSAMPErrors(question):

         #   Initializing lists

        faq = CommonIssues()
        error = CommonSAMPIssues()

        if question in faq:

            res = ''
            faq = CommonSAMPIssues()

            for i in faq:
                title = '**Common SAMP bugs / Glitches listed below**\n\n'
                res += f":arrow_right:{i}\n"

            res = f'{title} {res}'

            return question, res

        elif question in error:

            response = {

                        #   Client common issues
                        'San andreas not found':' SA:MP requires GTA:SA Game (v1 US/EN) to start. Versions greater than one / Steam / Direct2Drive / Microsoft Store version will not work with the multi-player functionallity',
                        'I can not see any servers in samp browser':'Ensure the procedure to install SA:MP has been followed, if the issue continues samp must be allowed to accsess through your firewall.\n \nUnfortuantely, i can not offer you some support for firewalls yet\ni suggest you google your firewall manufactor\n Ensure you have the latest SA:MP version (https:://www.sa-mp.com/downloads)',
                        'Single player loads instead of samp':'There is not supposed to be single player options ( New Game, Load game, etc.) - SA:MP loads by it self during the connection procses. If single player has loaded Its NOT SAN ANDREAS MULTIPLAYER.\nThe Single player might load for one of the following reasons which i listed below\n :arrow_right: SA:MP has been installed in the wrong folder, or the version of GTA:SA which is not compitable with SA:MP.\nIt is easy to fix, dont be afraid. You can downgrade the version to v1.\n:arrow_right: Sometimes the single-player menu might be shown, but SA:MP should have loaded properly.\nTo fix this you simply need to select an item on the menu then press esc until you\'re out of it, then SA:MP will proceed to load.',
                        'I get "uacceptable nickname" when connecting to a server':'When you get the **\' Unacceptable name\'** :arrow_right:You\'re either using characters which is not supported in SA:MP. (Characters which is allowed 0-9, a-z, A-Z, SpecialSymbols such as [],(), $, @,(./,), _ =) and max 20 characters in length\nYou may also get kicked out of some servers for \' Unacceptable name\' due to the server does not allow special characters in the nickname\ni recommend characters such as (a-z, A-Z, 0-9).\n:arrow_right: It could be coused when another player with the same nickname as you\n:arrow_right: might happend if you re-connect the same server very soon after timeout or crash\n:arrow_right: SA:MP server with a greater up time than 50days can couse this glitch.',
                        'Screen sticks at "connecting to ip:port..."':f'**{question}**\nIf you can not connected to the server, trubleshooting..\n:arrow_right: Server might be offline\n:arrow_right: If you are not able to connect to any SA:MP server. Disable your\'r firewall, and try again. If connection procsess works then you\'ll have to set up you\'r firewall properly.\n:arrow_right: else then server might not support the current SA:MP version. Download the correct version of samp(https://www.sa-mp.com/downloads).',
                        'The game crashes when a vehicle explodes':'There is three ways to solve the issue\n:arrow_right: Disable your 2dr monitor, while playing SA:MP.\n:arrow_right: Set your Visual FX quality to low. (Esc > Options > Display Setup > Advanced)\n:arrow_right: Rename the GTA San Andreas folder (e.g to *\'GTA SA2\'*)(Sometimes it might stop working, then you rename it to something else)',
                        'My mouse doesn\'t work after exiting the pause menu':'If your mouse seems to be frozen ingame while it works, in the pause menu. Disable multicore option in *\'sa-mp.cfg\' set multicore=0*.\n Continuously tapping Escape until the mouse responds again may also work, but it is not as neat a solution.',
                        'The file dinput8.dll is missing':'This might arise when DirectX is not properly installed.\n:arrow_right: re-install Directx & restart you\'r computer.\n :arrow_right: If the issue continues just go at C:\Windows\System32 and copy paste the dinput.dll file to the root directory of your GTA San Andreas. That would solve it.',
                        'I can not see other player\'s nametags!':'*Be aware*: some servers may have disabled nametags globally.\n:arrow_right: the issue often occures for Intel HD integrated graphics processors. The cause is unkown, a long term solution would be to install a dedicated grapic card in your computer, if it is possible and allows it. ',
                        'I have a modified gta: san andreas and samp won\'t load':'If SA:MP does not load. It might be coused by a modification as it interfers with the SA-MP client & cousing it to crash.',
                        'When launching gta with samp it won\'t start':'Delete *\' gta_sa.set\'* from the folder, userfiles, then you remove any modifications from the game & try again',
                        
                        #   Server common issues
                        'Packet was modified':'`[hh:mm:ss] Packet was modified, sent by id: <id>, ip: <ip>:<port>`\nWhen a player times out or has connection issues',
                        'Msvcr___.dll/msvcp___.dll not found':'Download the appriate Microsoft Visual C++ runtime libraries. **Note that the SA-MP server is 32 bit**',
                        'Warning: client exceeded ackslimit':'`Warning: client exceeded *\'ackslimit\'* <ip>:<port> (<count>) Limit: x/sec`\nhappens when acks limit exceeds',
                        'Warning: client exceeded messageholelimit':'`Warning: client exceeded *\'messageholelimit\'* (<type>) <ip>:<port> (<count>) Limit: x`\nhappens when message hole limit exceeds.',
                        'Warning: client exceeded messageslimit':'`Warning: client exceeded *\'messageslimit\'* (1) <ip>:<port> (<count>) Limit: x/sec`\nhappens when number of messages per second a client sends to the server exceeds.',
                        'Warning: Too many out-of-order messages':'`Warning: Too many out-of-order messages from player <ip>:<port> (<count>) Limit: x (messageholelimit)`\nhappens when *\'out of order messages`\'* reuses messageholelimit setting.',
                        'Players constantly getting "unacceptable nickname" error but it is valid':'ensure the name is acceptable, and the server is running on a Windows, 1. Change the compatibality for *\' samp-server.exe\'* to Windows 98, restart the server.\n 2. The issue might appear when the server is up 50+ days.',
                        'Server instantly crashes when started':'Commonly there is an error in your *\'server.cfg\'* file. Ud the reason is not located at the bottom of the file.check *\' crashinfo.txt\'* a better solution would be using the Crash detect plugin by Zeex (https://github.com/Zeex/samp-plugin-crashdetect) for more information',
                        'Server is not working - firewall is disabled':'You will need to forward your ports to allow players to join your server. You can forward your ports using the PF Port Checker. Download it from: (www.portforward.com) If the ports are not forwarded that means you have to open them in your router. You can check the router list at (http://portforward.com/english/routers/port_forwarding/routerindex.htm) for more information',
                        
                        #   Pawno common issues
                        'Failed to set data for " "': 'Run pawno.exe as an administrator',
                        'Unable to execute compiler on windows vista/7': 'In the dictionary where pawno.exe is, there will be a file called settings.ini.\n :arrow_right: Open it in a text editor change \'FileAssoc\' from 1 to 0\n :arrow_right: Run pawno.exe as an administrator'
                        }       

            response = response[question]

            return question, response

        return

    def SAMPGlitches(question):

         #   Initializing lists

        glitchesList = CommonGlitches()
        sampBug = CommonSAMPGlitches()
    
        print(question)

        #   Returns a list of SAMP Glitches
        if question in glitchesList:

            res = ''
            title = '**Common SAMP Glitches listed below**\n\n**War glitches**\n'

            for i in sampBug:res += f":arrow_right: {i}\n"

            res = f'{title} {res}'

            return question, res



        #   Responses
        elif question in sampBug:

            link = {'C-bug':'https://www.youtube.com/watch?v=50AEMtm3rcw'}
            response = {

                        #   War glitches

                        'Two-shots':'**Two-Shots**\nIs a reload glitch where you skip the reload animation, by switching weapons fast.\n\n**Applies to weapon**\nShawn-off shotgun',
                        'Distance shots':'**Distance Shots**\nis a weapon glitch which allows you to shoot at greater distance than normal gameplay.\n\n:arrow_right: Shoot first,\n:arrow_right: aim to where the bullets should hit',
                        'Escaping':'**Escaping**\nWhile pressing \'menu button\' it will look like the player crashes due to internett connection, the character will do the same activity as it did right before the player did press the \'menu button\'',
                        'Fake-shots': '**Fake-Shots**\n (RPG infinite ammo). This glitch gives a player with RPG unlimited RPG shots, it has it\'s name due to the rocket is not visible for other players.\n:arrow_right: Press the \'Aiming button\' & the \'Fire button\' at once. ',
                        'Switch\'ing': '**Switch\'ing**\nSwitch weapons to avoid the reload animation.\nBy using \'Switch weapon\' button, you switch the current weapon with another.\n\n:arrow_right: Skips the reload animation\n:arrow_right:  Works with every reloadable weapons.\n:arrow_right: **Note : The weapon requires atleast one bullet round**.',
                        'Lite foot':'**Lite foot**\nProvides better movement speed after shooting, it is used in duel\n\n**How to**\n:arrow_right: Press A or D. (Depends on which side you\'d like to go)\n:arrow_right: Aim\n:arrow_right: Fire\n:arrow_right: Scroll ( You have to have thee fists as a weapon choice)\n:arrow_right: Crouch\n:arrow_right: Sprint\n\n**Applies to weapons**:\n:arrow_right:**Deagle**,\n:arrow_right:**Sniper rifle**,\n:arrow_right:**Shotgun**',
                        'Slide glitch':' **Slide\'ing**\nWhile using this bug you slide, either diagnolly or forward, when you\'re using certain weapons.\nIt mostly used when players want to move faster with a slow-running weapon.\n\n**How to **\n:arrow_right: Choose one of the following weapons (Deagle, AK47, Combat Shotgun).\n:arrow_right: Press the \'crounch button\'\n:arrow_right: press the \'Sprint button\', Choose between left or right.\n:arrow_right: When the character stands up, press the \' Aim button\'\n**Note : If the aim is released the sliding glitch will stop**.',
                        'Crouch glitch':'**Crounch Bug (C-Bug)**\nIs a glitch which cancels specific animations that temprorary delays movement after shooting, and can increase firing rate or movement in combats with specific weapons.\n\n**Basic C-bug**\nThe intentions for doing basic c-bug is to increase the firerate.\n **Applies for**\n:arrow_right:   Deagle,\n:arrow_right:  CombatShotgun,\n:arrow_right:  Shotgun,\n:arrow_right:  Sniper rifle,\n :arrow_right:  Rifle.\n\n**Basic C-bug procedure**:\n:arrow_right:  Aim\n:arrow_right:  Shoot.\n:arrow_right: (When the firearm sound arrives) Release the aim button, and press \'Crouching button\' Immediately.\n:arrow_right: Switch weapons back & fourth in order to cancel the reload animation.\n :repeat:\n\n**Advanced C-bug**\nThe intention for doing an Advanced C-bug is to increase character movement while fire\'ing. It\'s effective against Running weapons such as **Uzi**, **tc9**, **Shawn-off**.\n:arrow_right: The procedure is the same as the basic usage of C-bug, but the intetions is to increase movement, so it would be like (Shoot, move, shoot).',

                        #   Walk glitches
                        'Walking glitches':'**Floating man**\nThis glitch automatically makes the character to float.\n**Procedure for floating**:\n:arrow_right: Spam \'Crouching button\' & Switch weapon\n\n**Walking man**\nThis bug automatically makes the character walk forward, while doing something else\n**Procedure for Walking man**\nCrounch, Crounch, Walk, Switch weapons)\n\n:arrow_right: Press Crouching button twice,\n:arrow_right: Press the forward \'Walking button\'\n:arrow_right: Switch weapons.\n\n**Running man**\nThis glitch automatically makes the character run forward, while doing something else\n\n**Procedure for Running man**:\n(Crounch, Crounch, Walk, Sprint, Switch weapons)\n\n:arrow_right: Press Crouching button twice,\n:arrow_right: Press the forward \'walking button\'\n:arrow_right: Press the \'sprint button\'\n:arrow_right: Switch weapons.\n\n**Slow Walk**\nThis glitch slows down movement while switching weapons as the animation changes everytime.\n**Procedure for Slow walk **:\n:arrow_right: Walk forward, while switching weapons\n',


                        #   Interior glitches
                        #   Texture glitches
                        'The garver bridge glitch':'The Garver Bridge texture has a glitch where you can not reach the max vehicle speed w/o Nitro.\n Some parts of it can be used to be faster than other players.\n :arrow_right: https://youtu.be/F5ibXFR-jgo',
                        'other texture glitches':'https://youtu.be/xZ19UpHIg7Q',
                        #   Misc bugs
                        'Doherty glitch':'Gives you the adventage to hide inside the garage.\n :arrow_right: link: https://youtu.be/380l_4rvaiM',
                        'Parachute glitches':'**Parachute Glitch 1**\nIf the player falls down from a low height with a parachute, the result of the fall is the same as falling from great heights without maximum health or with a not-in-use parachute. This is more than likely a glitch. It is likely because the game thinks that Carl is falling from a great height when wearing a parachute, as the parachute is intended to be used at a great height.\n\n**Parachute Glitch 2**\nIf the player has a parachute but doesn\'t deploy it yet or is still doing the opening parachute animation when CJ hits the ground, the health bar will deplete instantly and CJ will be killed. Cheats, hacks, mods or trainers couldn\'t prevent it from happening. This is probably because the game consider the player are still \'falling\' when the opening parachute animation is triggered thus making this glitch.\n\n**Parachute Glitch 3**\nThe parachute can be used as a weapon to attack and even kill some invincible enemies during some missions. An example of this is Big Poppa in A Home in the Hills. Despite the player can attack him in the mansion, he is considered to be invicible. However, if reacting fast enough, the player can attack him with a parachute inside. He will receive damage and can be killed, but the mission will be stuck if this happens, since he is not programmed to die in the mansion.\n\n **Parachute Glitch 4**\n Using Parachute while murdering another character it register as \'fake kill\'',
                        }       

            response = response[question]

            return question, response

        return
