#   Python Responsory

#   Discord responsory

from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord import PermissionOverwrite
from discord.ext.commands import Cog, command

#   RSS responsory
from bs4 import BeautifulSoup
import feedparser

class CnnWorld(Cog):
    def __init__(self, bot) -> None:
        self.embed = Embed(color=Color.dark_blue())

    #   CNN World
    @command(name='cnnWorld')
    async def worldNews(self, ctx):

        x = 0

        #Creating a channel
        while x > 5:

            #   Creating the feed
            rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_world.rss')
            entry = rssNews.entries[x]
            
            srv = ctx.guild
            role = get(srv.roles, name='@Members')
            channel = get(srv.channels, name='newsFeed')
            
            # Create a channel
            if not channel:

            #   Creating channel permissions
                perms = {
                            
                            srv.default_role:PermissionOverwrite(read_messages=False),
                            role:PermissionOverwrite(view_channel=True, read_message_history = True),
                        }

                await srv.create_text_channel(f'{channel.name}', overwrites=perms)

            # Procsess the embed, and send it
            self.embed.title = f'{rssNews.feed.title}'
            self.embed.description = f'{rssNews.feed.description}'
            self.embed.add_field(name=f'{entry[x].title}\n {entry[x].link}', value=f'{entry[x].description}\n {entry[x].published}')

            x =+ 1
            if x == 5:
                self.embed = Embed(color=Color.dark_purple())
                channel.send(embed=self.embed)
                self.embed.clear_fields()

                break
        return

    #   CNN Europe
    @command(name='cnneuro')
    async def EuropeNews(self,ctx):
        pass
    

    @command(name='cnnafrica')
    async def AfricaNews(self,ctx):
        pass

    @command(name='cnnmeast')
    async def MiddleEastNews(self,ctx):
        pass

    @command(name='cnnasia')
    async def AsiaNews(self,ctx):
        pass

    @command(name='cnnAmerica')
    async def AmericaNews(self,ctx):
        pass

class CnnMisc(Cog):
    def __init__(self, bot) -> None:
        self.embed = Embed(color=Color.dark_blue())
    
        #   Top News
    @command(name='cnntop')
    async def topNews(self, ctx):

        #   Retrieve the guild information
        x = 0
        srv = ctx.guild
        role = get(srv.roles, name='@Members')
        ch = get(srv.channels, name='newsfeed')

        #   Create the channel
        if not ch:

        #   Creating channel permissions
            perms = {
                            
                        srv.default_role:PermissionOverwrite(read_messages=False),
                        #role:PermissionOverwrite(view_channel=True, read_message_history = True),
                    }

            await srv.create_text_channel(f'newsfeed', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition.rss')
        entries =  rssNews.entries[x]

        # looping through the RSS feed
        for article in entries:
            print(article)
            #   Calling the soupd module
            soup = BeautifulSoup(article.summary)
            thumbNail = soup.find('img')['src']
            print(thumbNail)
        '''    
            #   If image equal true:
            if thumbNail:
                pass
        #   Create the embed information

        self.embed.title = f'{rssNews.feed.title}'
        self.embed.description = f'{rssNews.feed.description}'
        self.embed.url = f'{rssNews.feed.link}' # Note : problems with description / summary 
        self.embed.add_field(name=f'{ent.title}', value=f'{entry.published}\n {entry.link} \n ')
        
        print(f' {entry} ')

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()
        '''       
        return



class CnnSports(Cog):
    def __init__(self, bot) -> None:
        self.embed = Embed(color=Color.dark_blue())