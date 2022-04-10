
#   Python Responsories

#   Discord Responsories
from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord import PermissionOverwrite
from discord.ext.commands import Cog, command

#   RSS Responsories
import feedparser

class CnnMisc(Cog):

    """     CnnMisc
            Class contains miscellaneouss news from CNN

    """

    def __init__(self, bot) -> None:
        self.bot = bot,
        self.channelName = 'rssfeed'
        self.embed = Embed(color=Color.dark_blue())
    
        #   Top News 10
    @command(name='ctop')
    async def TopNews(self, ctx):

        """              TopNews
            Retrieves the top 5 News in the world

        """
        #   Initializing variables
        srv = ctx.guild
        role = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')


        #   Create a channel
        if not ch:

            #   Creating channel permissions
            perms = {
    
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Scraping the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition.rss')
        entries =  rssNews.entries

        #   Create the embed information
        self.embed.title = f'{rssNews.feed.title}'
        self.embed.description = f'{rssNews.feed.image.link}\n{rssNews.feed.description}'
        self.embed.url = f'{rssNews.feed.link}'

        for artnr, article in enumerate(entries):

            #   Searching for selected list items
            summary = article.get('summary', 'There is no summary for this article')
            updated = rssNews.feed.get('updated', ' No Date to be shown')

            if summary != 'There is no summary for this article':

                self.embed.add_field(name=f'{artnr}. {article.title}', value=f'\n{summary}\n**{updated}**\n{article.link}\n ')

            #   Drop the loop when the counter is reached
            if artnr == 10: 
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return

    @command(name='cetn')
    async def EntertainmentNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        role = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_entertainment.rss')
        entries =  rssNews.entries

        #   Create the embed information
        self.embed.title = f'{rssNews.feed.title}'
        self.embed.description = f'{rssNews.feed.description}'
        self.embed.url = f'{rssNews.feed.link}'

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

    @command(name='css')
    async def SpaceAndScienceNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_space.rss')
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

    @command(name='ccash')
    async def MoneyNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/money_news_international.rss')
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

    @command(name='cvideo')
    async def VideoNews(self, ctx):
        #   Video		http://rss.cnn.com/rss/cnn_freevideo.rss
        ctx.send('under Development')

        return

    @command(name='cTravel')
    async def TravelNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_travel.rss')
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
        self.embed.clear_fields()

        return

    @command(name='ctech')
    async def TechnologiesNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_technology.rss')
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

    #   Bad Request too long
    @command(name='sdfsdsdfsdf')
    async def MostRecentNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        role = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')

        #   Create the channel
        if not ch:

            #   Creating channel permissions
            perms = {
                            
                    srv.default_role:PermissionOverwrite(read_messages=False),
                    role:PermissionOverwrite(view_channel=True, read_message_history = True),
                }

            await srv.create_text_channel(f'{self.channelName}', overwrites=perms)

        #   Creating the feed
        rssNews = feedparser.parse('http://rss.cnn.com/rss/cnn_latest.rss')
        entries =  rssNews.entries

        #   Create the embed information
        self.embed.title = f'{rssNews.feed.title}'
        self.embed.description = f'{rssNews.feed.description}'
        self.embed.url = f'{rssNews.feed.link}' # Note : problems with description / summary 

        #   looping through the RSS feed
        for artnr, article in enumerate(entries):
            print(artnr, article.title)
            #   Searching for selected list items
            summary = article.get('summary', 'There is no summary for this article')
            updated = rssNews.feed.get('updated', ' No Date to be shown')

            if summary != 'There is no summary for this article':
                self.embed.add_field(name=f'{artnr}. {article.title}', value=f'\n{summary}\n ')

            #   Drop the loop when the counter is reached
            if artnr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return
