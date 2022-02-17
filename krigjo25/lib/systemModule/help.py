import discord

from discord.utils import get
from discord.embeds import Embed
from discord import Color, Member
from discord.ext.commands import command, Cog
from discord.ext.commands.core import has_any_role

class HelpCommand(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

#   Frequently Asked Question

    @command(name='help', pass_context=True)
    async def FrequentlyAskedQuestions(self,ctx, args=None):

        if args == None:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.title = ' Usage ** ?help (Category)** for more details\n\n'
            self.embed.add_field(name=':handshake: Welcome-Module', value='This is our new home', inline=True)
            self.embed.add_field(name=':people_holding_hands: Community-Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)
            self.embed.add_field(name=':people_wrestling: Game-Module', value='-Gamers does not take showers they do steamy once', inline=True)
            self.embed.add_field(name=':tv: Stream-Module',value='An Irishman arrived at J.F.K. Airport and wandered around the terminal with tears streaming down his cheeks...', inline=True)
            #self.embed.add_field(name=':gear: Suport-Module', value='Erectile disfunction support group has been cancelled', inline=True)
            if ctx.author.guild_permissions.kick_members:
                self.embed.add_field(name='Moderator-Module', value = 'A joke here', inline=True)

            if ctx.author.guild_permissions.administrator:
                self.embed.add_field(name='Administrator-Module', value='A joke here', inline=True)
                
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

        else:
            args = str(args)
            args.lower()

        #   Bot-Modules

        #   Welcome Module
            if args == 'welcome' or args == 'welcome-module':

                self.embed.title=':handshake: Welcome-Module'
                self.embed.description='Use ** ?help (Command)**, for more details, sir.\n\n'
                self.embed.add_field(name='On member join / leave ', value='- Over 100 Welcome messages and leave messages. In order for \n it to work, set a channel as\n"system message channel ', inline=True)
                self.embed.add_field(name='Force-readRules', value=' Customize a rule set and the person has to agree in order to get a role / be able to view other channels', inline=True)
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
        
        #   Community-Module
            elif args == 'community' or args == 'community-module':

                self.embed.title=':people_holding_hands: Community-Module'
                self.embed.description='Use ** ?help (Command)**, for more details, sir.\n\n'
                self.embed.add_field(name='?botinfo \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
                self.embed.add_field(name='?memberlist', value ='list of members', inline=True)
                self.embed.add_field(name='?dnd (message) ', value='- Busy, or going afk, notify your friends that you have a life', inline=True)
                self.embed.add_field(name='?back ', value='- Shows that you\'re a no lifer again', inline=True)
                self.embed.add_field(name='?meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)
                self.embed.add_field(name='/', value='- for built-ins ', inline=True)
                self.embed.add_field(name=':x:?pre-mod', value='How does the pre-mod work')
                
                await ctx.send(embed=self.embed)
                
                self.embed.clear_fields()

        #   Games-Module
            elif args == 'game' or args == 'game-module':

                self.embed.title=':people_wrestling: Games-Module'
                self.embed.description='Use ** ?help (Command/Category)**, for more details, sir.\n\n'
                self.embed.add_field(name='miniGames-Module', value='- :rock:, :scissors:, :page_facing_up:', inline=True)
                #self.embed.add_field(name='discordGames', value='- ServerInfo, stats etc', inline=True)
                await ctx.send(embed=self.embed)    
                self.embed.clear_fields()
            
            elif args == 'minigames' or args == 'minigames-module':

                self.embed.title = 'Minigames Module'
                self.embed.add_field(name='?rsp', value='- :rock:, :scissors:, :page_facing_up:', inline=True)
                self.embed.add_field(name=':question: ?jumble', value=' - unscrabble a jumble', inline=True)
                self.embed.add_field(name=':person_in_lotus_position: ?ask (Question)', value='- How can cops be the worst pool players?\n They always shoot the eight ball first', inline=True)
                self.embed.add_field(name=':seven:, :eight:, :nine: ?int (easiest / easy / normal / hard / kimpossible)', value='- How could the two four skip a meal?\n they already eight ', inline=True)
                await ctx.send(embed=self.embed)    
                self.embed.clear_fields()

        #   Stream-Module    
            elif args == 'stream'  or args == 'stream-module':

                self.embed.title=':woman_raising_hand: Stream Module'
                self.embed.add_field(name='RSS-Feeds', value='Summury for blogs, news etc.')
                #self.embed.add_field(name=':x:?youtube', value= '- to view the most important changes for current release', inline=True)
                #self.embed.add_field(name=':x:?spotify ', value='- Would you like to hear a joke about parking tickets?\n Thats fine.', inline=True)
                #self.embed.add_field(name=':x:?SoundCloud ', value='- Music never dies.', inline=True)
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
            
            elif args == 'rss' or args == 'rss-feeds':
                self.embed.title = 'RSS-Module'
                self.embed.add_field(name='CNN-News', value = 'Cnn RSS feeds')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

            elif args == 'cnn' or args == 'cnn-news':
                self.embed.title = 'CNN News'
                self.embed.add_field(name ='World', value ='Cnn World News')
                self.embed.add_field(name ='CNN-Misc', value ='Cnn Misc News')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

            elif args == 'cnnworld' or args == 'cnn-world':
                self.embed.title = 'CNN World News'
                self.embed.add_field(name ='World', value ='Cnn World News')
                self.embed.add_field(name ='CNN-Misc', value ='Cnn Misc News')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

            elif args == 'cworld' or args == 'cnn-news':
                self.embed.title = 'CNN News'
                self.embed.add_field(name ='?cworld', value ='Cnn World News')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

            elif args == 'cnnmisc' or args == 'cnn-news':
                self.embed.title = 'CNN Misc News'
                self.embed.add_field(name ='?cnntop', value ='Top 5 Cnn News')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

        #   Support-Module
            elif args == 'support'  or args == 'support-module':

                self.embed.title = 'Support Module'
                #self.embed.add_field(name=':x:?report', value= '- to view the most important changes for current release', inline=True)
                #self.embed.add_field(name=':x:?ticket (issue)', value='- Would you like to hear a joke about parking tickets?\n Thats fine.', inline=True)
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

        #   Moderator-Module
            elif args == 'moderator'  or args == 'moderator-module':

                self.embed.title = 'Moderator Module'
                self.embed.add_field(name=':bar_chart: ?poll', value='- Run a poll', inline=True)
                self.embed.add_field(name='?kick (member) (reason)', value='- Kicks a user off the server ', inline=True)
                self.embed.add_field(name='?crech (Channel Name)', value='- Create a new channel default : hidden ', inline=True)
                self.embed.add_field(name='?cls (channel name) (1-100)', value= '- Clears the given channel Chat:bangbang:', inline=True)
                self.embed.add_field(name='?online (on/off)', value= '- Checks whom is online / offline', inline=True)
                self.embed.add_field(name='?warn (MemberName) (Reason)', value= '- Manually Warn a member for their behavior', inline=True)
                self.embed.add_field(name='?sush (MemberName) (sec) (reason)', value= '- Shush a member for a number of sec', inline=True)

                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

        #   Administrator-Module
            elif args == 'administrator'  or args == 'administrator-module':

                self.embed.title = 'Administrator Module'
                self.embed.add_field(name=':bar_chart: ?banlist', value='-View banned members', inline=True)
                self.embed.add_field(name=':bar_chart: ?poll', value='-Run a poll', inline=True)
                self.embed.add_field(name='?unban (member Name)', value= '- unban a member ', inline=True)
                self.embed.add_field(name=':no_pedestrians: ?ban (member) (reason)', value='- Probhits a Discord user to enter your channel', inline=True)
                self.embed.add_field(name='?announce (channelName) (message)', value= '- Talk as the bot in a given channel', inline=True)
                self.embed.add_field(name='?demote (name)', value='- Demote a person from the role', inline=True)
                self.embed.add_field(name=':x:?promote (name)', value='- Promotes a regular user to given role', inline=True)
                self.embed.add_field(name=':x:?roleCreate (name))', value='- Creates a role in the server', inline=True)
                self.embed.add_field(name='?delRole (Name)', value='- Deletes a role from the server', inline=True)
            

                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
            return