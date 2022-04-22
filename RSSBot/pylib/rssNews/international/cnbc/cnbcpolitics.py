
#   Discord Responsories
from asyncore import read
from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command
from discord.permissions import PermissionOverwrite

#   RSS Responsories used
import feedparser

class CNBCPolitics(Cog):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot
        self.channelName = 'rssfeed'
        self.embed = Embed(color = Color.dark_blue())

        return

    @command(name = 'cnbccom')
    async def Commentary(self, ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100370673'

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
        self.embed.description = f'{RSSNews.feed.image.link}\n{RSSNews.feed.description}'
        self.embed.url = f'{RSSNews.feed.link}'

        #   Looping throught the entries
        for nr, article in enumerate(entries):

            summary = article.get('summary', 'No data to be shown')
            updated = RSSNews.feed.get('updated', 'No data to be shown')

            if summary != 'No data to be shown':

                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information & reset embed
        await ch.send(embed=self.embed)
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()

        return

    # Local USA
    @command(name = 'cnbcpoli')
    async def Politicts(self, ctx):

        #   Initializing the variables
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000113'

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
        self.embed.description = f'{RSSNews.feed.image.link}\n{RSSNews.feed.description}'
        self.embed.url = f'{RSSNews.feed.link}'

        #   Looping throught the entries
        for nr, article in enumerate(entries):

            summary = article.get('summary', 'No data to be shown')
            updated = RSSNews.feed.get('updated', 'No data to be shown')

            if summary != 'No data to be shown':

                self.embed.add_field(name = f'{nr}. {article.title}', value = f'\n{summary}\n**{updated}**\n{article.link}\n')

            if nr == 5:
                break

        #   Send the information & reset embed
        await ch.send(embed=self.embed)
        self.embed = Embed(color=Color.dark_purple())
        self.embed.clear_fields()

        return