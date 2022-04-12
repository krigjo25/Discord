
#   Python Responsories

#   Discord Responsories

from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord import PermissionOverwrite
from discord.ext.commands import Cog, command

#   RSS Responsories
import feedparser

class CnnWorld(Cog):
    def __init__(self, bot) -> None:
        self.channelName = 'rssfeedtest'
        self.embed = Embed(color=Color.dark_blue())

    #   CNN World
    @command(name='cnbcworld')
    async def WorldNews(self, ctx):

            #   Retrieve the guild information
        srv = ctx.guild
        role = get(srv.roles, name='@Members')
        
        ch = get(srv.channels, name=f'{self.channelName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    #role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100727362')
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
           #image = article.get('media_thumbnail', 'No images to be shown') # Get the image
            
            if summary != 'There is no summary for this article':
                self.embed.add_field(name=f'{artnr}. {article.title}', value=f'\n{summary}\n{updated}\n{article.link}\n written by: {author}')
            
            #   Drop the loop when the counter is reached
            if artnr == 10:
                break
            
            #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()
     
        return

    #   CNN Europe
    @command(name='cnbceurope')
    async def EuropeNews(self,ctx):
        
            #   Retrieve the guild information
        srv = ctx.guild
        role = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    #role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_europe.rss')
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
           #image = article.get('media_thumbnail', 'No images to be shown') # Get the image
            
            if summary != 'There is no summary for this article':
                self.embed.add_field(name=f'{artnr}. {article.title}', value=f'\n{summary}\n{updated}\n{article.link}\n written by: {author}')
            
            #   Drop the loop when the counter is reached
            if artnr == 10:
                break
            
            #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()
     
        return

    @command(name='cnbcasia')
    async def AsiaNews(self,ctx):
        
            #   Retrieve the guild information
        srv = ctx.guild
        role = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    #role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_asia.rss')
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
           #image = article.get('media_thumbnail', 'No images to be shown') # Get the image
            
            if summary != 'There is no summary for this article':
                self.embed.add_field(name=f'{artnr}. {article.title}', value=f'\n{summary}\n{updated}\n{article.link}\n written by: {author}')
            
            #   Drop the loop when the counter is reached
            if artnr == 5:
                break
            
            #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()
     
        return


        
            #   Retrieve the guild information
        srv = ctx.guild
        role = get(srv.roles, name='@Members')

        ch = get(srv.channels, name=f'{self.channelName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    #role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('')
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
           #image = article.get('media_thumbnail', 'No images to be shown') # Get the image
            
            if summary != 'There is no summary for this article':
                self.embed.add_field(name=f'{artnr}. {article.title}', value=f'\n{summary}\n{updated}\n{article.link}\n written by: {author}')
            
            #   Drop the loop when the counter is reached
            if artnr == 10:
                break
            
            #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()
     
        return