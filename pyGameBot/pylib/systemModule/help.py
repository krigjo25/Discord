from discord.embeds import Embed
from discord import Color
from discord.ext.commands import command, Cog


class HelpCommand(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

#   Frequently Asked Question

    @command(name='help', pass_context=True)
    async def FrequentlyAskedQuestions(self, ctx, args=None):
        print('test')
        if args == None:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.title = ' Usage ** ?help (Category)** for more details\n\n'
            self.embed.add_field(name=':people_holding_hands: Community-Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)
            self.embed.add_field(name=':people_wrestling: Game-Module', value='-Gamers does not take showers they do steamy once', inline=True)
                
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

        else:
            args = str(args)
            args.lower()

        #   Bot-Modules
        
        #   Community-Module
            if args == 'community' or args == 'community-module':

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
                #   self.embed.add_field(name='pyGames', value='- ServerInfo, stats etc', inline=True)
                #   self.embed.add_field(name='GameServer-Module', value='- ServerInfo, stats etc', inline=True)
                self.embed.add_field(name='miniGames-Module', value='- :rock:, :scissors:, :page_facing_up:', inline=True)

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

                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

            #return