
#   Discord Responsories
from asyncore import read
from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command
from discord.permissions import PermissionOverwrite

#   RSS Responsories used
import feedparser

class CNBCMiscellaneous(Cog):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot
        self.channelName = 'rssfeed'
        self.embed = Embed(color = Color.dark_blue())

        return

    @command(name = 'cnbcbus')
    async def Business(self, ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10001147'

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

    @command(name='cnbcsbus')
    async def SmallBusiness(self, ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10001147'

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

    @command(name = 'cnbcstate')
    async def RealEstate(self, ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000115'

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

    @command(name = 'cnbctech')
    async def Technologies(self, ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19854910'

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
                print(article)
                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return


    @command(name = 'cnbccare')
    async def HealthCare(self, ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000108'

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

    @command(name = 'cnbcenergy')
    async def Energy(self, ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19836768'

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

    @command(name = 'cnbctravel')
    async def Travel(self, ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000739'

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

    @command(name = 'cnbcsmedia')
    async def SocialMedia(self, ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000110'


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
                print(article)
                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()

        return


    @command(name = 'cnbcsports')
    async def Sports(self, ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000101'

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

