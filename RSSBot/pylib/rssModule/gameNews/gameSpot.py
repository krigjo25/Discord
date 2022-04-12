
#   Python Responsories

#   Discord Responsories
from discord.utils import get
from discord.embeds import Embed
from discord.colour import Color
from discord import PermissionOverwrite
from discord.ext.commands import Cog, command

#   RSS Responsories
import feedparser

class GameSpot(Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        self.channelName = 'rssfeedtest'
        self.embed = Embed(color=Color.dark_blue())

    @command('gsnews')
    async def GameNews(self, ctx):

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
        
        rssNews = feedparser.parse('https://www.gamespot.com/feeds/game-news')
        entries =  rssNews.entries

        #   Create the embed information

        self.embed.title = f'{rssNews.feed.title}'
        self.embed.description = f'{rssNews.feed.description}'
        self.embed.url = f'{rssNews.feed.link}'

        for artnr, article in enumerate(entries):

            #   Searching for selected list items
            summary = article.get('summary', 'There is no summary for this article')
            updated = rssNews.feed.get('updated', ' No Date to be shown')
            print(f'{artnr}. {article.title}\n{summary}\n**{updated}**\n{article.link}\n ')
            if summary != 'There is no summary for this article':

                self.embed.add_field(name=f'{artnr}. {article.title}', value=f'\n{summary[4:350]}\n**{updated}**\n{article.link}\n ')

            #   Drop the loop when the counter is reached
            if artnr == 4: 
                break

        #   Send the information, and reset embed
        await ch.send(embed=self.embed)
        self.embed.clear_fields()
