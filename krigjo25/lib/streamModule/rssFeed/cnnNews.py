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
    @command(name='cWorld')
    async def worldNews(self, ctx):
            #   Retrieve the guild information
        srv = ctx.guild
        role = get(srv.roles, name='@Members')
        chName = 'news'
        ch = get(srv.channels, name=f'{chName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    #role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{chName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_world.rss')
        entries =  rssNews.entries

        #   Create the embed information
        self.embed.title = f'{rssNews.feed.title}'
        self.embed.description = f'{rssNews.feed.description}'
        self.embed.url = f'{rssNews.feed.link}' # Note : problems with description / summary 

            #   looping through the RSS feed
        for artnr, article in enumerate(entries):
            #   Searching for selected list items
            summary = article.get('summary', 'There is no summary for this article')
            updated = rssNews.feed.get('updated', ' No Date to be shown')
            author = article.get('author', 'Unkown') # Get the authors name
            image = article.get('media_thumbnail', 'No images to be shown') # Get the image
            print(author)
            
            if summary != 'There is no summary for this article':
                self.embed.add_field(name=f'{artnr}. {article.title} {image}', value=f'\n{summary}\n{updated}\n{article.link}\n')
            
            #   Drop the loop when the counter is reached
            if artnr == 5:
                break
            
            #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()
     
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
    
        #   Top News 10
    @command(name='ctop')
    async def topNews(self, ctx):

            #   Retrieve the guild information
        srv = ctx.guild
        role = get(srv.roles, name='@Members')
        chName = 'rssfeed'
        ch = get(srv.channels, name=f'{chName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{chName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition.rss')
        entries =  rssNews.entries

        #   Create the embed information
        self.embed.title = f'{rssNews.feed.title}'
        self.embed.description = f'{rssNews.feed.description}'
        self.embed.url = f'{rssNews.feed.link}' # Note : problems with description / summary 

            #   looping through the RSS feed
        for artnr, article in enumerate(entries):
            #   Searching for selected list items
            summary = article.get('summary', 'There is no summary for this article')
            updated = rssNews.feed.get('updated', ' No Date to be shown')
            
            if summary != 'There is no summary for this article':
                self.embed.add_field(name=f'{artnr}. {article.title}', value=f'\n{summary}\n{updated}\n{article.link}\n ')
            
            #   Drop the loop when the counter is reached
            if artnr == 10:
                break
            
            #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()
     
        return



class CnnSports(Cog):
    def __init__(self, bot) -> None:
        self.embed = Embed(color=Color.dark_blue())