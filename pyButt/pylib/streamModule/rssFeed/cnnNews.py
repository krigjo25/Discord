#   Python Responsory

#   Discord responsory

from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord import PermissionOverwrite
from discord.ext.commands import Cog, command

#   RSS responsory
import feedparser

class CnnWorld(Cog):
    def __init__(self, bot) -> None:
        self.embed = Embed(color=Color.dark_blue())

    #   CNN World
    @command(name='cworld')
    async def worldNews(self, ctx):

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
           #image = article.get('media_thumbnail', 'No images to be shown') # Get the image
            
            if summary != 'There is no summary for this article':
                self.embed.add_field(name=f'{artnr}. {article.title}', value=f'\n{summary}\n{updated}\n{article.link}\n written by: {author}')
            
            #   Drop the loop when the counter is reached
            if artnr == 5:
                break
            
            #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()
     
        return

    #   CNN Europe
    @command(name='cEuro')
    async def EuropeNews(self,ctx):
        
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
            if artnr == 5:
                break
            
            #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()
     
        return
    

    @command(name='cafrica')
    async def AfricaNews(self,ctx):
        
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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_africa.rss')
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
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()
     
        return

    @command(name='cmeast')
    async def MiddleEastNews(self,ctx):
        
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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_meast.rss')
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
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()
     
        return

    @command(name='casia')
    async def AsiaNews(self,ctx):
        
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
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()
     
        return

    @command(name='camerica')
    async def AmericaNews(self,ctx):
        
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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_americas.rss')
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
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()
     
        return

    @command(name='cus')
    async def USNews(self,ctx):
        
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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_us.rss')
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
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()
     
        return

class CnnMisc(Cog):
    def __init__(self, bot) -> None:
        self.embed = Embed(color=Color.dark_blue())
    
        #   Top News 10
    @command(name='ctop')
    async def topNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
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
        self.embed.description = f'{rssNews.feed.image.link}\n{rssNews.feed.description}'
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

    @command(name='cetn')
    async def EntertainmentNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_entertainment.rss')
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

    @command(name='css')
    async def SpaceAndScienceNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
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
        pass

    @command(name='cmr')
    async def MostRecentNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/cnn_latest.rss')
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

    @command(name='ctravel')
    async def TravelNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
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
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()

        return

    @command(name='ctech')
    async def TechnologiesNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
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

class CnnSport(Cog):
    def __init__(self, bot) -> None:
        self.embed = Embed(color=Color.dark_blue())

    @command(name='cfootball')
    async def FootballNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
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
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()

        return

    @command(name='cgolf')
    async def GolfNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
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
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()

        return

    @command(name='cms')
    async def MotorSportNews(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
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

    @command(name='cworldsports')
    async def WorldsSports(self, ctx):

        #   Retrieve the guild information
        srv = ctx.guild
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
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
        rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_sports.rss')
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
        chName = 'rssfeed'
        role = get(srv.roles, name='@Members')
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