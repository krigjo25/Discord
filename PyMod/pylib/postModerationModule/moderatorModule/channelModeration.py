#   Python Repositories
import datetime

#   Discord Repositories
import discord as d
from discord.utils import get
from discord.abc import GuildChannel
from discord.embeds import Embed, Colour
from discord.ext.commands import Cog, before_invoke, group, after_invoke, has_permissions

class ChannelModeration(Cog):

    '''
        #   Channel moderation
        #   Commands for Moderators with manage_channels & manage_messages
    '''

    def __init__(self, bot):

        self.bot = bot
        self.warn = 0
        self.now = datetime.datetime.now()
        self.curTime = self.now.strftime('%H:%M, %d.%b - %y')
        self.embed = Embed()

        return

    @before_invoke("ch")
    async def CheckModChannel(self, ctx):

        #   Fetching the channel "auditlog"
        ch = get(ctx.guild.channels, name = "auditlog")

        try :
            if ch: return True
        
        except Exception as e: pass
        else:

            perms = { 
                        ctx.guild.default_role:d.PermissionOverwrite(view_channel=False)
                    }

            ch = await ctx.guild.create_text_channel("auditlog", overwrites=perms)

            #   Prepare and send embeded message
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Auto Generated Channel'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.description = f"Created to have easy accsess to bot commands used by admin / moderator"
            await ch.send(embed=self.embed)
    
        #   Clear some memory
        del ch, perms
        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        return

    @after_invoke("ch")
    async def ClearMemory(self, ctx):

        #   Clear some Memory
        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.remove_thumbnail()
        self.embed.color = Colour.dark_purple()

        return

    @group(pass_contex = True)
    @has_permissions(manage_channels = True)
    async def ch(self, ctx):

        #   Calling a command to invoke first
        await self.CheckModChannel(ctx)
        await self.ClearMemory(ctx)

    #   Create a channel
    @ch.command()
    async def Create(self, ctx, ch):

        """
            #   Fetch given channel
            #   Fetch the auditlog
            #   Check if both exist
            #   If both does not raise any errors create a new Channel
        """
        #   Fetch channel
        arg = ch
        ch = get(ctx.guild.channels, name = f"{ch}")
        chlog = get(ctx.guild.channels, name = "auditlog")

        try :
            
            if ch: raise ValueError(f"Channel \"{ch}\" already exists")
            if not chlog : raise Exception("Channel auditlog does not exist yet")

        except Exception as e:

            self.embed.color = Colour.dark_red()
            self.embed.title = f"An Exception Occured"
            self.embed.description = f"{e} Try another name."

            await ctx.send(embed=self.embed)

            #   Clear some memory
            del ch, arg, chlog

            return

        else :

            perms = { 
                            ctx.guild.default_role:d.PermissionOverwrite(view_channel=False)
                    }

            ch = await ctx.guild.create_text_channel(f'{arg}', overwrites=perms)

            #   Prepare and send embeded message
            self.embed.color = Colour.dark_red()
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f'{ctx.author.name} Created the channel : \"{ch}\"'
            await chlog.send(embed=self.embed)

        #   Clear some memory
        del ch, arg, chlog

        return 

    #   Delete a channel
    @ch.command()
    async def Delete(self, ctx, ch):

        """
                #   Fetch both channels
                #   Check if they exist
                #   Delete the channel
        """

        #   Fetch channel

        arg = get(ctx.guild.channels, name = f"{ch}")
        ch = get(ctx.guild.channels, name = "auditlog")

        try :
            #   If channel does not exist raise ValueError
            if not arg: raise ValueError(f"Channel \"{ch}\" Does not Exists")
            elif not ch : raise Exception("Channel auditlog does not exist yet")

        except Exception as e:

                self.embed.color = Colour.dark_red()
                self.embed.title = f"An Exception occured"
                self.embed.description = f"{e}\nTry another name."
                await ch.send(embed=self.embed)
        else :
            #   Delete GuildChannel
            guild = GuildChannel
            await guild.delete(arg)

        self.embed.color = Colour.dark_red()
        self.embed.timestamp = datetime.datetime.now()
        self.embed.title = f"{ctx.author.name} has deleted {arg}"

        await ch.send(embed=self.embed)

        #   Clear memory
        del ch, arg, guild
        return 

    #   Clearing all messages
    @ch.command()
    async def Clear(self, ctx, ch, x):

        """
            #   Initializing the channels
            #   Checking wheter the values are correct or not
            #   Print a message
            #   Clearing a selected chat
        """

        #   Initializing Channels

        ch = get(ctx.guild.channels, name = ch)
        chlog = get(ctx.guild.channels, name = "auditlog")

        try :

            if not str(x).isdigit(): raise ValueError("You can not use alphabetical or ghlupical letters")
            elif int(x) < 0 or int(x) > 1000: raise ValueError("Choose an integer between 1-1000")
            else : x = int(x)

            if not ch : raise TypeError("Channel does not exist in the server")
            elif not chlog : raise TypeError("Could not find the auditlog channel")

        except Exception as e: 

            self.embed.color = Colour.dark_red()
            self.embed.title = f"An Exception Occured"
            self.embed.description = f'The channel {ch}, were not cleared as requested due to\n{e}'
            await ch.send(embed = self.embed)

        else:

            #   Prepare & send the embed message
            self.embed.color = Colour.dark_red()
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f"{ctx.author.name} has cleared {x} chat lines in {ch} channel."
            await chlog.send(embed = self.embed)

        #   Remove content from the channel
        x = await ch.purge(limit=x)

        #   Saving some memory
        del ch, chlog, x

        return

