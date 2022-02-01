import discord

from discord.utils import get
from discord.embeds import Embed
from discord import Color, Member
from discord.ext.commands import command, Cog
from discord.ext.commands.core import has_any_role

class HelpCommand(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')
#   Help-Module
    @command(name='help', pass_context=True)
    
    async def FrequentlyAskedQuestions(self, ctx, args=None):


        if args==None:

            self.embed.title='Frequently Asked Questions:question:'
            self.embed.description='Use ** ?help (Command/Category)**, for more details, sir.\n\n'
            self.embed.add_field(name=':handshake: Welcome', value='- when he came, he just left ', inline=True)
            self.embed.add_field(name=':people_holding_hands: Community', value='- Did you hear about the guy whom joined a community? \n he were never seen again. ', inline=True)
            self.embed.add_field(name=':people_wrestling: miniGames', value='- Gamers don\'t take hot showers, only steamy ones', inline=True)
            #self.embed.add_field(name=':x: Stream', value= '- ', inline=True)
            #self.embed.add_field(name=':x: :gear: Support', value= '- Im stuck, lets get\nchildsupport :exclamation:', inline=True)
            #self.embed.add_field(name=':x: Moderator', value= '- Post moderator module. ', inline=True)
            #self.embed.add_field(name=':x: Administrator', value= '- Post Administration ', inline=True)

            await ctx.send(embed=self.embed)

            self.embed.clear_fields()

        elif args != None:
            args =str(args)
            args = args.lower()
        #   Modules
            # Welcome - Module
            if args == 'welcome':
                
                self.embed.title=':handshake: Welcome-Module'
                self.embed.description='Use ** ?help (Command/Category)**, for more details, sir.\n\n'
                self.embed.add_field(name='Welcome message', value='- Over 100 Welcome messages and leave messages. In order for \n it to work, set a channel as\n"system message channel ', inline=True)
                self.embed.add_field(name='Force-readRules', value=' Customize a rule set and the person has to agree in order to get a role ', inline=True)
                
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
            
            #   Community - Module
            elif args == 'community':

                self.embed.title=':people_holding_hands: Community-Module'
                self.embed.description='Use ** ?help (Category)**, for more details, sir.\n\n'
                self.embed.add_field(name='?krigjo25 \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
                self.embed.add_field(name='?memberlist', value ='list of members', inline=True)
                self.embed.add_field(name='?dnd (message) ', value='- Busy, or going afk, notify your friends', inline=True)
                self.embed.add_field(name='?back ', value='- Welcome back', inline=True)
                self.embed.add_field(name='?meme', value='- What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)
                self.embed.add_field(name='/', value='- for built-ins ', inline=True)
                #self.embed.add_field(name=':x:*pre-mod', value='How does the pre-mod work')
                
                await ctx.send(embed=self.embed)
                
                self.embed.clear_fields()

            #   MiniGames Module
            elif args == 'minigames':

                self.embed.title=':people_wrestling: miniGames-Module'
                self.embed.description='Use ** ?help (Command/Category)**, for more details, sir.\n\n'
                self.embed.add_field(name='?rsp', value='- :rock:, :scissors:, :page_facing_up:', inline=True)
                self.embed.add_field(name=':question: ?jumble', value=' - unscrabble a jumble', inline=True)
                self.embed.add_field(name=':person_in_lotus_position: ?ask (Question)', value='- How can cops be the worst pool players?\n They always shoot the eight ball first', inline=True)
                self.embed.add_field(name=':seven:, :eight:, :nine: ?int (easiest / easy / normal / hard / kimpossible)', value='- How could the two four skip a meal?\n they already eight ', inline=True)
                await ctx.send(embed=self.embed)    
                self.embed.clear_fields()

            #   Stream module
            elif args == 'stream':

                self.embed.title=':woman_raising_hand: Stream-Module'
                self.embed.description='Use ** ?help (Command/Category)**, for more details, sir.\n\n'
                self.embed.add_field(name=':x:?youtube', value= '- to view the most important changes for current release', inline=True)
                self.embed.add_field(name=':x:?spotify ', value='- Would you like to hear a joke about parking tickets?\n Thats fine.', inline=True)
                self.embed.add_field(name=':x:?SoundCloud ', value='- Music never dies.', inline=True)
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
            
            #   Support-Module
            elif args == 'support':

                self.embed.title=':woman_raising_hand: Support-Module'
                self.embed.description='Use ** ?help (Command/Category)**, for more details, sir.\n\n'
                self.embed.add_field(name=':x:?changelog', value= '- to view the most important changes for current release', inline=True)
                self.embed.add_field(name=':x:?ticket (issue)', value='- Would you like to hear a joke about parking tickets?\n Thats fine.', inline=True)

                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

            #   Moderator-Module
            elif args == 'moderator' or args =='mod':

                self.embed.title='Moderator-Module'
                self.embed.description='Use ** ?help (Command/Category)**, for more details, sir.\n\n'
                self.embed.add_field(name=':bar_chart: ?poll', value='- Run a poll', inline=True)
                self.embed.add_field(name='?kick (member) (reason)', value='- Kicks a user off the server ', inline=True)
                self.embed.add_field(name='?crech (Channel Name)', value='- Create a new channel default : hidden ', inline=True)
                self.embed.add_field(name=':: ?cls (channel name) (int)', value= '- Clears the given channel Chat:bangbang:', inline=True)
                self.embed.add_field(name=':: ?online (on/off', value= '- Checks whom is online / offline', inline=True)


                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
            #   Administrator-Module
            elif args == 'admin' or args == 'administrator':
                
                self.embed.title=':customs: Administrator-Module'
                self.embed.description='Use ** ?help (Command/Category)**, for more details, sir.\n\n'
                self.embed.add_field(name=':bar_chart: ?banlist', value='-View banned members', inline=True)
                self.embed.add_field(name=':bar_chart: ?poll', value='-Run a poll', inline=True)
                self.embed.add_field(name='?unban (member Name)', value= '- unban a member ', inline=True)
                self.embed.add_field(name='?announce (channelName) (message)', value= '- Talk as the bot in a given channel', inline=True)
                self.embed.add_field(name='?cls (channel name) (int)', value= '- Clears the given channel Chat:bangbang:', inline=True)
                self.embed.add_field(name=':no_pedestrians: ?ban (member) (reason)', value='- Probhits a Discord user to enter your channel', inline=True)

                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

        #   Help Commands
            else:
                self.embed.title='Frequently Asked Questions:question:'
                self.embed.description='Use ** ?help (Command/ Category)**, for more details, sir.\n\n'
                self.embed.add_field(name=':handshake: Welcome', value='- when he came, he just left ', inline=True)
                self.embed.add_field(name=':people_holding_hands: Community', value='- Did you hear about the guy whom joined a community? \n he were never seen again. ', inline=True)
                self.embed.add_field(name=':people_wrestling: miniGames', value='- Gamers don\'t take hot showers, only steamy ones', inline=True)
                #self.embed.add_field(name=':x: Stream ', value= '- ', inline=True)
                #self.embed.add_field(name=':x: Moderator', value= '- Post moderator module. ', inline=True)
                #self.embed.add_field(name=':x: Administrator', value= '- Post Administration ', inline=True)
                #self.embed.add_field(name=':x: :gear: Support', value= '- Im stuck, lets get\nchildsupport :exclamation:', inline=True)

                await ctx.send(embed=self.embed)

                self.embed.clear_fields()

            return