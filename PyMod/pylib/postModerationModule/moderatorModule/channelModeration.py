#   Python Repositories
import datetime

#   Discord Repositories
import discord as d
from discord import utils
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
        self.embed = Embed()
        self.now = datetime.datetime.now().strftime('%H:%M, %d.%b - %y')

        return

    @group(pass_contex = True)
    @has_permissions(manage_channels = True)
    async def ch(self, ctx): return
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
        ch = utils.get(ctx.guild.channels, name = f"{ch}")
        chlog = utils.get(ctx.guild.channels, name = "auditlog")

        try :
            
            if ch: raise Exception(f"Channel \"{ch}\" already exists")
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

        arg = utils.get(ctx.guild.channels, name = f"{ch}")
        chlog = utils.get(ctx.guild.channels, name = "auditlog")

        try :
            #   If channel does not exist raise ValueError
            if not arg: raise Exception(f"Channel \"{ch}\" Does not Exists")
            elif not chlog : raise Exception("Channel auditlog does not exist yet")

        except Exception as e:

                self.embed.color = Colour.dark_red()
                self.embed.title = f"An Exception occured"
                self.embed.description = f"{e}\nTry another name."
                await ctx.send(embed=self.embed)

        #   Delete GuildChannel
        guild = GuildChannel
        await guild.delete(arg)

        self.embed.color = Colour.dark_red()
        self.embed.timestamp = datetime.datetime.now()
        self.embed.title = f"{ctx.author.name} has deleted {arg}"

        await chlog.send(embed=self.embed)

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

        arg = utils.get(ctx.guild.channels, name = ch)
        chlog = utils.get(ctx.guild.channels, name = "auditlog")

        try :

            if arg == None : raise Exception(f"Channel \"{ch}\" does not exist in the server")
            elif not chlog : raise Exception("Could not find the auditlog channel")

            if not str(x).isdigit(): raise Exception("You can not use alphabetical or ghlupical letters")
            elif int(x) < 0 or int(x) > 1000: raise Exception("Choose an integer between 1-1000")
            else : x = int(x)

        except Exception as e: 

            self.embed.color = Colour.dark_red()
            self.embed.title = f"An Exception Occured"
            self.embed.description = f'The channel {ch}, were not cleared as requested due to\n{e}'
            await ctx.send(embed = self.embed)

            del ch, chlog, x, arg
            return

        else:

            #   Prepare & send the embed message
            self.embed.color = Colour.dark_red()
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f"{ctx.author.name} has cleared {x} chat lines in {ch} channel."
            await chlog.send(embed = self.embed)

        #   Remove content from the channel
        await arg.purge(limit=x)

        #   Saving some memory
        del ch, chlog, x, arg

        return

    @ch.before_invoke
    async def CheckModChannel(self, ctx):

        #   Fetching the channel "auditlog"
        ch = utils.get(ctx.guild.channels, name = "auditlog")

        try :
            if ch: return True
        
        except TypeError as e: print(e)
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
        self.embed.clear_fields()
        self.embed.color = Colour.dark_purple()

        #   Clear some memory
        del perms, ch

        return

    #@ch.before_invoke
    #async def CheckRole(self, ctx):

        #   Fetching the channel "auditlog"
        ch = utils.get(ctx.guild.channels, name = "auditlog")
        role = utils.get(ctx.guild.roles, name = "Sushed")

        try :
            if role:
                #   Clear some memory
                del role, ch
                return True
        
        except TypeError as e: print(e)
        else:
            # Role Configurations
            perm = d.Permissions(send_messages = False, request_to_speak = False, send_tts_messages = False, use_voice_activations = False)
            await ctx.guild.create_role(name=f'{role}', permissions = perm, reason = f"Auto Generated - by Pymod")

            #   Prepare and send embeded message
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Auto Generated Role'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.description = f"Created to store sushed members"
            await ch.send(embed=self.embed)

        del role, perm, ch

        return

    @ch.after_invoke
    async def ClearMemory(self, ctx):

        #   Clear some Memory
        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.remove_thumbnail()
        self.embed.color = Colour.dark_purple()
        self.embed.description = ""

        return
