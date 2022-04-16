
#   Python Responsories

#   Discord Responsories

from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord import PermissionOverwrite
from discord.ext.commands import Cog, command

#   RSS Responsories
import feedparser

class CNNWorld(Cog):
    def __init__(self, bot) -> None:
        self.channelName = 'rssfeed'
        self.embed = Embed(color=Color.dark_blue())

        return

    #   CNN World
    @command(name='cworld')
    async def WorldNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        rss = 'http://rss.cnn.com/rss/edition_world.rss'
        
        ch = get(srv.channels, name=f'{self.channelName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    member:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse(f'{rss}')
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
    @command(name='ceurope')
    async def EuropeNews(self,ctx):
        
        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'http://rss.cnn.com/rss/edition_europe.rss'

        #   Creating the channel if it does not exists
        if not ch:

            #   Inserting the channel permissions
            perms = {
                        srv.default_role:PermissionOverwrite(read_messages=False),
                        member:PermissionOverwrite(view=True, read_channel_history=True)
}

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the RSS 
        RSSNews = feedparser.parse(f'{rss}')
        entries = RSSNews.entries

        #   Prepareing the embed
        self.embed.title = f'{RSSNews.feed.title}'
        self.embed.description = f'{RSSNews.feed.description}'
        self.embed.url = f'{RSSNews.feed.link}'

        #   Looping throught the entries
        for nr, article in enumerate(entries):
            summary = article.get('summary', 'There is no summary for this article')
            updated = RSSNews.feed.get('updated', 'There is no summary for this article')

            if summary != 'There is no summary for this article':

                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return

    @command(name='cafrica')
    async def AfricaNews(self,ctx):
        
        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'http://rss.cnn.com/rss/edition_africa.rss'

        #   Creating the channel if it does not exists
        if not ch:

            #   Inserting the channel permissions
            perms = {
                        srv.default_role:PermissionOverwrite(read_messages=False),
                        member:PermissionOverwrite(view=True, read_channel_history=True)
}

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the RSS 
        RSSNews = feedparser.parse(f'{rss}')
        entries = RSSNews.entries

        #   Prepareing the embed
        self.embed.title = f'{RSSNews.feed.title}'
        self.embed.description = f'{RSSNews.feed.description}'
        self.embed.url = f'{RSSNews.feed.link}'

        #   Looping throught the entries
        for nr, article in enumerate(entries):
            summary = article.get('summary', 'There is no summary for this article')
            updated = RSSNews.feed.get('updated', 'There is no summary for this article')

            if summary != 'There is no summary for this article':

                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return

    @command(name='cmeast')
    async def MiddleEastNews(self,ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'http://rss.cnn.com/rss/edition_meast.rss'

        #   Creating the channel if it does not exists
        if not ch:

            #   Inserting the channel permissions
            perms = {
                        srv.default_role:PermissionOverwrite(read_messages=False),
                        member:PermissionOverwrite(view=True, read_channel_history=True)
}

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the RSS 
        RSSNews = feedparser.parse(f'{rss}')
        entries = RSSNews.entries

        #   Prepareing the embed
        self.embed.title = f'{RSSNews.feed.title}'
        self.embed.description = f'{RSSNews.feed.description}'
        self.embed.url = f'{RSSNews.feed.link}'

        #   Looping throught the entries
        for nr, article in enumerate(entries):
            summary = article.get('summary', 'There is no summary for this article')
            updated = RSSNews.feed.get('updated', 'There is no summary for this article')

            if summary != 'There is no summary for this article':

                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return

    @command(name='casia')
    async def AsiaNews(self,ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'http://rss.cnn.com/rss/edition_asia.rss'

        #   Creating the channel if it does not exists
        if not ch:

            #   Inserting the channel permissions
            perms = {
                        srv.default_role:PermissionOverwrite(read_messages=False),
                        member:PermissionOverwrite(view=True, read_channel_history=True)
}

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the RSS 
        RSSNews = feedparser.parse(f'{rss}')
        entries = RSSNews.entries

        #   Prepareing the embed
        self.embed.title = f'{RSSNews.feed.title}'
        self.embed.description = f'{RSSNews.feed.description}'
        self.embed.url = f'{RSSNews.feed.link}'

        #   Looping throught the entries
        for nr, article in enumerate(entries):
            summary = article.get('summary', 'There is no summary for this article')
            updated = RSSNews.feed.get('updated', 'There is no summary for this article')

            if summary != 'There is no summary for this article':

                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return

    @command(name='camerica')
    async def AmericaNews(self,ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'http://rss.cnn.com/rss/edition_americas.rss'

        #   Creating the channel if it does not exists
        if not ch:

            #   Inserting the channel permissions
            perms = {
                        srv.default_role:PermissionOverwrite(read_messages=False),
                        member:PermissionOverwrite(view=True, read_channel_history=True)
}

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the RSS 
        RSSNews = feedparser.parse(f'{rss}')
        entries = RSSNews.entries

        #   Prepareing the embed
        self.embed.title = f'{RSSNews.feed.title}'
        self.embed.description = f'{RSSNews.feed.description}'
        self.embed.url = f'{RSSNews.feed.link}'

        #   Looping throught the entries
        for nr, article in enumerate(entries):
            summary = article.get('summary', 'There is no summary for this article')
            updated = RSSNews.feed.get('updated', 'There is no summary for this article')

            if summary != 'There is no summary for this article':

                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return
