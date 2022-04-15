
#   Python Responsories

#   Discord Responsories

from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord import PermissionOverwrite
from discord.ext.commands import Cog, command

#   RSS Responsories
import feedparser

class UKNational(Cog):

    def __init__(self, bot) -> None:
        self.channelName = 'rssfeed'
        self.embed = Embed(color=Color.dark_blue())

        return

    #   BBC News
    @command(name = 'bbcuk')
    async def BBCNational(self,ctx):

            #   Retrieve the guild information
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = ''

        #   Create the channel
        if not ch:

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
            if artnr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return


    #   SKY News
    @command(name = 'skyuk')
    async def SkyNewsNational(self,ctx):

            #   Retrieve the guild information
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = ''

        #   Create the channel
        if not ch:

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
            if artnr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return

class FranceNational(Cog):

    def __init__(self, bot) -> None:
        self.channelName = 'rssfeedtest'
        self.embed = Embed(color=Color.dark_blue())

    @command(name='frfr')
    async def FranceNational(self, ctx):

            #   Retrieve the guild information
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://www.france24.com/en/france/rss'

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

        #   Prepare the embed
        self.embed.title = f'France 24 National'
        self.embed.description = f''
        #self.embed.url = f'{RSSNews.feed.link}'

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
