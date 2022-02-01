#   Discord Responsory
from discord import  Member
from discord.utils import get
from discord.ext.commands import Cog
from discord import PermissionOverwrite
from discord.permissions import Permissions

#   System Responsory
from random import shuffle,randrange

# Library Responsory
from lib.dictionaries.systemmessages import Dictionaries

class Welcome(Cog, name='Welcome module'):
    def __init__(self, bot, *kwargs):
        self.bot = bot

#   When a member joins
    @Cog.listener()
    async def on_member_join(self, member:Member):

        #   Creating a new role for new members
        srv = member.guild
        memberRole = get(srv.roles, name='@Members')

        if not memberRole:
            overwrite = Permissions(speak=True, send_messages=True, read_message_history=True, read_messages=True)
            memberRole = await srv.create_role(name='Member', permissions= overwrite, reason= 'Automatic Role assignment')
        else:
            await member.add_roles(memberRole)
        
        #   Sending a random Greetings message
        ch = srv.system_channel
        emoji = Dictionaries.EmojiDictionary()

        args = {    0:f' :boom: {member.mention} appeared. {emoji}',
                    1:f'Can you catch em all? {member.mention}. {emoji}',
                    2:f'finally a genious came {member.mention}. {emoji}',
                    3:f'we are pleased to meat you, {member.mention}. {emoji}',
                    4:f'noOne:\n  {member.mention}: just arrived. {emoji}',
                    5:f'a genious came {member.mention}. {emoji}',
                    6:f'{member.mention} Just threw a cupcake. {emoji}.',
                    7:f'oh dang, I just dropped a {member.mention}. {emoji}.',
                    8:f'Captn. {member.mention} Just appeared from nowhere {emoji}.',
                    9:f'Laugh more, worry less {member.mention}. {emoji}.',
                    10:f'I inveted a new {member.mention}. {emoji}.',
                    11:f'The server recieved a gift, after unwrapping it,  {member.mention}? {emoji}.',
                    12:f'A new Crazy {member.mention} arrived !',
                    13:f'I hope you brought a nut {member.mention}'
                    
        }

        # Ranomizing the message
        shuffle(args)
        x = randrange(0,13)

        await ch.send(f'{args[x]}')

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

        args = {    0:f' :dash: {member.mention} vanished.',
                    1:f'Swoosh, {member.mention} went  off the server {emoji}',
                    2:f'{member.mention} ghosted us. {emoji}',
                    3:f'I hope you find happyness anywhere else, {member.mention}. {emoji}',
                    4:f'noOne:\n  {member.mention}: just flew away. {emoji}',
                    5:f'Suddenly {member.mention} disapeared in the woods {emoji}',
                    6:f'{member.mention} Just got eaten by a {animal}.{emoji}.',
                    7:f'{member.mention} just became a lost boy {emoji}.',
                    8:f'{member.mention} went to work. {emoji}.',
                    9:f'{member.mention} blow up {emoji}.',
                    10:f'Farewell {member.mention}. {emoji}.',
                    11:f'{member.mention} Transformed into a {animal}. {emoji}.',
                    12:f'{member.mention} used one of his nuts, and disapeared into the jungle {emoji}',
                    13:f'{member.mention}, used a time machine back to 1800s',
                    14:f'{member} just dropped out',

                }
        
        #   Ranomizing the args
        shuffle(args)
        x = randrange(0,12)

        await ch.send(f'{args.get(x)}')