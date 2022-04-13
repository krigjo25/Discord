
#   Discord Repositories
from discord.utils import get
from discord import  Member, Colour
from discord.ext.commands import Cog
from discord.permissions import Permissions

#   System Repositories
from os import getenv
from random import shuffle,randrange

# pyLib Repositories
from pylib.systemModule.databasePython import MariaDB
from pylib.dictionaries.systemmessages import Dictionaries


class Welcome(Cog):
    def __init__(self, bot, *kwargs):
        self.bot = bot

#   When a member joins
    @Cog.listener()
    async def on_member_join(self, member:Member):


        #   Creating a new role for new members
        srv = member.guild
        ch = srv.system_channel
        memberRole = get(srv.roles, name='@Members')

        if not memberRole:
            overwrite = Permissions(    speak=True,
                                        send_messages=True,
                                        read_messages=True,
                                        view_channels=True)

            memberRole = await srv.create_role(name='@Members', permissions=overwrite, reason= 'Automatic Role assignment')
            await memberRole.edit(colour=Colour(0x567d46))
        else:
            await member.add_roles(memberRole)
        
        #   Sending a random Greetings message
        args = self.welcomeMember()

        await ch.send(f'{args}')

#   When a member leaves the channel
    @Cog.listener()
    async def on_member_remove(self, member:Member):

        #   Crating a random farewell message
        svr = member.guild
        ch = svr.system_channel

        emojiDict = {   0: ':sad:',
                        1:':sleepy:',
                        2:':sweat_smile:',
                        3:':fearful:',
                        4:':scream:',
                        5:':sob:',
                        6:':no_mouth:',
                        7:':imp:',
                        8:':broken_heart:',
                        9:':hankey:',
                        10:':-1:',
                        11:':skull:',
                        12:':fire:',
                        13:':imp:',
                        14:':ghost:',
                        15:':zZz:',
                    }
        animal = {  0:'cat',
                    1:'dog',
                    2:'squrrel',
                    3:'human',
                    4:'toad',
                    5:'fish',
                    6:'ant',
                    7:'gecko',
                    8:'fox',
                    9:'hare',
                    10:'leopard',
                    11:'tiger',
                    12:'crocodile',
                    13:'aye aye',
                    14:'shark',
                    15:'butterfly'

        }            

        shuffle(emojiDict)
        shuffle(animal)

        x = randrange(0,14)
        emoji = emojiDict.get(x)
        animal = animal.get(x)



        
        args = self.removeMember()
        #await ch.send(f'{args[x][2]}')

        return
 
    def welcomeMember(self):

        #   Configure database Connection
        db = MariaDB()
        database = getenv('databse1')
        query = 'SELECT welcomeMessages from table;'
        args = db.selectFromTable(database, query)

        #   Retrieve a number of rows in the guild
        x = db.RowCount(database, query)
        x = randrange(0,x)

        db.closeConnection()

        return args[x][1]

    
    def removeMember(self):

        #   Configure database Connection
        db = MariaDB()
        database = getenv('databse1')
        query = 'SELECT absenceMessages from table;'
        args = db.selectFromTable(database, query)

        #   Retrieve a number of rows in the guild
        x = db.RowCount(database, query)
        x = randrange(0,x)

        db.closeConnection()

        return args[x][2]