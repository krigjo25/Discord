import datetime
from os import name

#   Discord library

from discord import Member
from discord.utils import get
from discord.embeds import Embed, Colour
from discord import PermissionOverwrite
from discord.ext.commands.core import has_permissions
from discord.ext.commands import Cog, command, has_role, has_any_role

class Moderator(Cog, name='Moderator-module'):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Colour.dark_purple(), description= '')
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%d.%m - %Y')      

        #Creating a channel
    @command(name="crech", help='Creating a channel')
    @has_any_role('Moderator', 'moderator', 'mod', 'Admin', 'admin', 'administrator', 'Administrator', 'Software-Technican')
    
    async def CreateChannel(self, ctx, chName):

        # Declaring variables
            svr = ctx.guild
            member = ctx.author
            role = get(svr.roles, name='Moderator')
            role2 = get(svr.roles, name='moderator')
            role3 = get(svr.roles, name='Mod')
            role4 = get(svr.roles, name='mod')

            overWrites = {
                            role:PermissionOverwrite(read_messages=True),
                            role2:PermissionOverwrite(read_messages=True),
                            role3:PermissionOverwrite(read_messages=True),
                            role4:PermissionOverwrite(read_messages=True),
                            member:PermissionOverwrite(read_messages = True),
                            #svr.default_role:PermissionOverwrite(read_messages=False)
                            
                        }
            ch = get(svr.channels, name=chName)

            # set permission to secret
            if not ch:
                await svr.create_text_channel(f'{chName}', overwrites=overWrites)
                await ctx.send(f'Sir, the channel, **{chName}** is created.')
            else :
                await ctx.send(f'the channel, **{chName}** already exists.')
        
        # Clearing all messages
    @command(name="cls",)
    @has_any_role('Moderator', 'moderator', 'mod', 'Admin', 'admin', 'administrator', 'Administrator', 'Software-Technican')

    async def ClearChat(self, ctx, chName, x):

            x = int(x)
            srv = ctx.guild
            channel = get(srv.channels, name=chName)

            if x <= 100:
                await channel.purge(limit=x)
                await ctx.send(f'Sir, i purged **{x}** lines, in **{channel}**')
            else:
                await ctx.send('Sir, the limit is 100 lines')

        # Kick a user from the server
    
    @command(name='kick', help='Kick a user from the channel')
    @has_any_role('Moderator', 'moderator', 'mod', 'Admin', 'admin', 'administrator', 'Administrator', 'Software-Technican')
    @has_permissions(kick_members= True)

    async def Kick(self, ctx, member:Member, *, reason=None):
        if reason == None:
            await ctx.send(f'Please provide me a reason to kick {member}')

        elif reason != None:
            # Creating a log 
            with open('krigjo25\lib\log\kick-log.log', 'a') as f:
                f.write(f'{member.name} has been kicked for {reason}, by {ctx.author.name} Date : {self.curTime}\n')
            
            # Creating a message to the user, send it to his DM, then kick
            message = f'the Administrator Team has decided to kick you out from  **{ctx.guild.name}** \n \n Due to :\n **{reason}**'
            await member.send(message)

            await member.kick(reason=reason)
            # Send to the member
            
    
    @command(name='poll', pass_context= True)
    @has_any_role('Moderator', 'moderator', 'mod', 'Admin', 'admin', 'administrator', 'Administrator', 'Software-Technican')
    #   creating a poll with default two values to choose from
    #   Using reaction to vote
    #   Title of the poll, how many options and Questions
    
    async def polls(self, ctx):


        # Emojis
        one = '1️⃣'
        two = '2️⃣'
        three = '3️⃣'
        four = '4️⃣'
        five = '5️⃣'

        # server        
        srv = ctx.guild

        # Creating an embed
        self.embed.title = ''
        self.embed.description = 'Type in a question or type \"q\" to quit '

        
        await ctx.send(embed=self.embed)
        
        def msgCheck(arg):

            author = ctx.author
            arg = str(arg.content)
            print(author, arg)
            return author != self.bot.user and arg

        arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
        quiz = str(arg.content)

        self.embed.title = f'{quiz}:question:,'
        self.embed.description = 'Thank you, please type in how many opinions you\'d like:question:'
        await ctx.send(embed=self.embed)

        arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
        x = int(arg.content)
        
        # Creating the Options
        if x == 2:
            #   First option
            self.embed.description = 'Name your first option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option = str(arg.content)

            #   Second option
            self.embed.description = 'Name your second option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option2 = str(arg.content)

            options = f':one:{option}\n:two: {option2}\n'
        
        elif x == 3:
            #   First option
            self.embed.description = 'Name your first option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option = str(arg.content)

            #   Second option
            self.embed.description = 'Name your second option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option2 = str(arg.content)

            #   Third option
            self.embed.description = 'Name your third option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option3 = str(arg.content)

            options = f':one:{option}\n:two: {option2}\n :three:{option3}'

        elif x == 4:
            #   First option
            self.embed.description = 'Name your first option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option = str(arg.content)

            #   Second option
            self.embed.description = 'Name your second option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option2 = str(arg.content)

            #   Third option
            self.embed.description = 'Name your third option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option3 = str(arg.content)
            
            #   Fourth option
            self.embed.description = 'Name your fourth option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option4 = str(arg.content)
            
            options = f':one:{option}\n:two: {option2}\n :three:{option3}\n :four:{option4}'

        elif x == 5:
            #   First option
            self.embed.description = 'Name your first option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option = str(arg.content)

            #   Second option
            self.embed.description = 'Name your second option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option2 = str(arg.content)

            #   Third option
            self.embed.description = 'Name your third option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option3 = str(arg.content)
            
            #   Fourth option
            self.embed.description = 'Name your fourth option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option4 = str(arg.content)
        
            #   fifth option
            self.embed.description = 'Name your fifth option'
            await ctx.send(embed=self.embed)

            arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
            option5 = str(arg.content)
            
            options = f':one:{option}\n:two: {option2}\n :three:{option3}\n :four:{option4}\n :five:{option5}'
        
        # Summuary for the question
        self.embed.title ='Summary'
        self.embed.description = f'Question : {quiz}\n Options :\n {options}\nWhich channel should the poll go in?'
        await ctx.send(embed=self.embed)

        #   Retrieve the channel name
        arg = await self.bot.wait_for('message', timeout=30.0, check=msgCheck)
        ch = str(arg.content)

        channel= get(srv.channels, name=ch)

        if not channel:  
            await srv.create_text_channel(f'{ch}')

        self.embed.title = f'{quiz}:question:'
        self.embed.description = f' Greetings fellas, its time for a poll, choose between \n {options}'
        r = await channel.send(embed=self.embed)

                # Add following reaction to the message
        

        if x==2:
            await r.add_reaction(one)
            await r.add_reaction(two)

        elif x==3:
            await r.add_reaction(one)
            await r.add_reaction(two)
            await r.add_reaction(three)

        elif x==4:
            await r.add_reaction(one)
            await r.add_reaction(two)
            await r.add_reaction(three)
            await r.add_reaction(four)

        elif x==5:
            await r.add_reaction(one)
            await r.add_reaction(two)
            await r.add_reaction(three)
            await r.add_reaction(four)
            await r.add_reaction(five)

        if quiz == 'q' or ch == 'q':
            return await ctx.send('The poll has ended')

#   Online members
    @command(name='online', pass_context=True)
    @has_any_role('Moderator', 'moderator', 'mod', 'Admin', 'admin', 'administrator', 'Administrator', 'Software-Technican')
    
    async def OnlineMembers(self, ctx, args=None):

        if args == None:
            
            #   Retriving the server
            svr = ctx.guild
            user = self.bot.user
            warn = ''
            self.embed.title = 'Server Members'
            self.embed.description = 'List of members'
            
            #   Fetching members
            for member in svr.members:

                #   Declare variables
                status = str(member.status)
                nick = str(member.nick)
                #   Add emoji to status
                if status == 'online':
                    status = ':heart_on_fire:'

                elif status == 'idle':
                    status = ':dash:'
                
                elif status == 'dnd':
                    status = ':technologist:'

                elif status == 'offline':
                    status = ':sleeping:'
                
                #   Fetch user nick
                if nick == 'None':
                    nick = ''
                else:
                    nick = f'Nick : {member.nick}\n'
                if member != user:
                    self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {warn}', inline=False)
            await ctx.send(embed = self.embed)
            self.embed.clear_fields()
        if args != None:
            args = str(args)
            args = args.capitalize()  

            if args == 'Online' or args == 'On':
                #   Retriving the server
                svr = ctx.guild
                off = True
                    
                warn = ''
                self.embed.title = 'Server Members'
                self.embed.description = 'List of members'
                
                #   Fetching members
                for member in svr.members:
                    
                    #   Declare variables
                    status = str(member.status)
                    nick = str(member.nick)
                    #   Add emoji to status
                    if status == 'online':
                        status = ':heart_on_fire:'

                    elif status == 'idle':
                        status = ':dash:'
                    
                    elif status == 'dnd':
                        status = ':technologist:'
                    
                    elif status == 'offline':
                        status = ':sleeping:'
                        off = False
                    
                    #   Fetch user nick
                    if nick == 'None':
                        nick = ''
                    else:
                        nick = f'Nick : {member.nick}\n'
                        
                    if off != False:
                        self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {warn}', inline=False)
                await ctx.send(embed = self.embed)
                self.embed.clear_fields()
            
            elif args == 'Off' or args == 'Offline':
                #   Retriving the server
                svr = ctx.guild
                off = True
                    
                warn = ''
                self.embed.title = 'Server Members'
                
                #   Fetching members
                for member in svr.members:
                    
                    #   Declare variables
                    status = str(member.status)
                    nick = str(member.nick)
                    
                    #   Add emoji to status
                    if status != 'Offline':
                        off = False
                    elif status == 'offline':
                         status = ':sleeping:'

                    #   Fetch user nick
                    if nick == 'None':
                        nick = ''
                    else:
                        nick = f'Nick : {member.nick}\n'

                    if off != False:
                        self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick}\n Status : {status}\n Warnings : {warn}', inline=False)
                self.embed.description = 'End of List'
                await ctx.send(embed = self.embed)
                self.embed.clear_fields()
