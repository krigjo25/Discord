#   RSS Responsory
import feedparser

#   Python Responsory

#   Discord Responsory

class   rssMisc(Cog):
    def __init__(self) -> None:
        self.embed = Embed(color=Color.dark_blue())

    #   Misc
    @command(name='rss')
    async def CustomRss(self, ctx, url):
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
        rssNews = feedparser.parse(f'{url}')
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
