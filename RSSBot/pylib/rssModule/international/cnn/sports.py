
#   Python Responsories

#   Discord Responsories

from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord import PermissionOverwrite
from discord.ext.commands import Cog, command

#   RSS Responsories
import feedparser



class CnnSport(Cog):

    def __init__(self, bot) -> None:
        self.channelName = 'rssfeed'
        self.embed = Embed(color=Color.dark_blue())

    @command(name='cfootball')
    async def FootballNews(self, ctx):

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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_football.rss')
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

    @command(name='cgolf')
    async def GolfNews(self, ctx):

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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_golf.rss')
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

    @command(name='cms')
    async def MotorSportNews(self, ctx):

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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_motorsport.rss')
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

    @command(name='ctennis')
    async def TennisNews(self, ctx):

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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_tennis.rss')
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

#   Attribute error
    @command(name='cwsport')
    async def WorldsSports(self, ctx):

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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_sport.rss')
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

