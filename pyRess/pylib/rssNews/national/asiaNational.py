
#   Python Responsories

#   Discord Responsories

from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord import PermissionOverwrite
from discord.ext.commands import Cog, command

#   RSS Responsories
import feedparser

class SouthAsiaNational(Cog):

    def __init__(self, bot) -> None:

        self.channelName = 'rssfeed'
        self.embed = Embed(color=Color.dark_blue())

    #   CNN News
    @command(name = 'windia')
    async def IndiaNational(self,ctx):

            #   Retrieve the guild information
        srv = ctx.guild
        member = get(srv.roles, name='@Members')
        ch = get(srv.channels, name=f'{self.channelName}')
        rss = 'http://www.wionews.com/feeds/india-news/rss.xml'

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
            updated = rssNews.feed.get('updated', ' No date to be shown')
            author = article.get('author', 'Unknown') # Get the authors name
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

