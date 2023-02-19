#   Python Repositories
import datetime
import asyncio
import humanfriendly as hf

#   Discord Repositories
import discord as d
from discord import utils
from discord.embeds import Embed, Colour
from discord.ext.commands import  Cog

#   Modals
from  pylib.moderation.modal import Member

class ChannelModeration(Cog):

    """
        #  Author : Krigjo25
        #  Creation Date :  2.18-23
        #  last update :

        #   Create channels
        #   Delete channels
        #   modify channels
            Commands for Moderators with manage_channels & manage_messages
    """

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed()
        self.now = datetime.datetime.now().strftime('%H:%M, %d.%b - %y')

        return
    
    #   Slash command group
    channel = d.SlashCommandGroup(name = "channel", description = "Create something", default_member_permissions = d.Permissions(manage_channels = True))

    @channel.command()
    async def create(self, ctx : d.ApplicationContext, channeltype = "text", name = "test", age_restricted = False, bitrate = 0,  category = None, topic = None, delay = 0, reason = None, user_limit = 0, perm = None):

        """
            Creating a channel (forum / text / voice / category)

            #   Creating a single channel

            #   Checking the condtiions
            #   Create a channel
        """ 

        ch = utils.get(ctx.guild.channels, name = name)
        chlog = utils.get(ctx.guild.channels, name = "auditlog")

        try :#   Checking if the condition below is met, if the condition is met then raise exception

            if str(channeltype).isalpha() : 
                if str(channeltype) not in ["forum", "text", "voice", "stage", "category",  ]: raise Exception(" channeltype argument, has only five types, (forum / text / voice / stage or category)")
            else: raise ValueError("channeltype argument, can not be integers") #   Checking if the channelType contains integers

            if str(age_restricted).isalpha(): 
                if str(age_restricted).lower() == "false": age_restricted = False
                elif str(age_restricted).lower() == "true": age_restricted = True
                else: raise TypeError("age_restricted argument accepts only boolean values (\"**True**\" / \"**False**\")")
            else: raise TypeError("age_restricted argument accepts only boolean values (\"**True**\" / \"**False**\")")

            """
            if str(perm).isalpha():

                if str(perm).lower() in ["member", "moderator", "administrator", "everyone"]: perm = Discord.Permission(perm)
                elif str(perm).lower() in Discord.Permission(perm): perm =Discord.Permission(perm)
                else : raise Exception("You could either type in a permission or choose from one of the following \"member\", \"moderator\", \"administrator\"")
            else: raise TypeError("perm argument acceps only alphabetical characters.")
            """
            if str(bitrate).isnumeric():
                bitrate = int(bitrate)
                if bitrate < 0: raise ValueError("Bitrate argument has to be  equal (or grater) to 0")
            else: raise ValueError("bitrate argument accepts only integers")
            
            if str(delay).isnumeric():
                delay = int(delay)
                if delay < 0: raise ValueError("delay argument has to be greater than 0") 
            else: raise ValueError("delay argument accepts only integers")

            if ch : raise Exception(f"The channel {ch} already exits")  #   Checking if the channel already exits
            if not chlog : raise Exception("Channel auditlog does not exists")

        except (ValueError, TypeError, Exception) as e:#   If something goes wrong output a message

            self.embed.title = "An Exception Occured"
            self.embed.description = f"{e}"
            self.embed.color = Colour.dark_red()
            self.embed.timestamp = self.now
            await ctx.respond(embed = self.embed)

            return

        else:#   If everythings fine, continue 

            if perm == None: pass # Default permissions
        
            else: pass #    Else fetch permissions

            match str(channeltype).lower(): #   Matching the type of channel

                case "forum":

                    try: await ctx.guild.create_forum_channel(name = name, category = category, slowmode_delay = delay, nsfw = age_restricted, overwrites = perm, topic = topic, reason = reason)
                    except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                        self.embed.title = "An Exception Occured"
                        self.embed.description = f"{e}"
                        self.embed.color = Colour.dark_red()
                        ctx.respond(embed = self.embed)

                        return

                case "text":  
                    try :await ctx.guild.create_text_channel(name = name, category = category, slowmode_delay = delay, nsfw = age_restricted, topic = topic, reason = reason )
                    except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                        self.embed.title = "An Exception Occured"
                        self.embed.description = f"{e}"
                        self.embed.color = Colour.dark_red()
                        ctx.respond(embed = self.embed)

                        return

                case "voice":
                    try: await ctx.guild.create_voice_channel(name = name,  reason = reason, category = category, bitrate = bitrate,user_limit = user_limit, overwrites = perm, topic = topic, )
                    except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                        self.embed.title = "An Exception Occured"
                        self.embed.description = f"{e}"
                        self.embed.color = Colour.dark_red()
                        ctx.respond(embed = self.embed)

                        return

                case "stage":
                    try: await ctx.guild.create_stage_channel(name = name, category = category, overwrites = perm, topic = topic, reason = reason )
                    except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                        self.embed.title = "An Exception Occured"
                        self.embed.description = f"{e}"
                        self.embed.color = Colour.dark_red()
                        ctx.respond(embed = self.embed)

                        return

                case "category":  
                    try: await ctx.guild.create_category_channel(name = name, overwrites = perm, reason = reason )
                    except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                        self.embed.title = "An Exception Occured"
                        self.embed.description = f"{e}"
                        self.embed.color = Colour.dark_red()
                        ctx.respond(embed = self.embed)

                        return

            self.embed.color = Colour.dark_red()
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f"{ctx.author.name} has created a **{channeltype}**, **\"{name}\"**"

            await chlog.send(embed=self.embed)

        return

    @channel.command()  #   Delete the channel
    async def delete(self, ctx:d.ApplicationContext, channeltype, name, reason = None):

        await self.check_channel(ctx)
        """
                #   Delete a channel

                #   Fetch both channels
                #   Check if they exist
                #   Delete the channel
        """

        ch = utils.get(ctx.guild.channels, name = f"{name}")#   Fetch channel
        chlog = utils.get(ctx.guild.channels, name = "auditlog")#   Fetch channel

        try :   #  if channel does not exist raise Exception

            if not ch: raise d.NotFound(f"The channel \"{ch}\" Does not exists") #   if channel not found raise exception
            elif not chlog : raise d.NotFound("Channel auditlog does not exist yet") #  if the channel not found, raise exception NOt found

            if str(channeltype).isdigit() : raise ValueError("channeltype argument, can not be integers") #  if channeltype is digits, raise a valuerror
            elif str(channeltype) not in ["forum","text", "voice", "category", "stage" ]: raise Exception(" channeltype argument, has only five types, (forum / text / voice / stage or category)")

        except Exception as e:# Handle the exception

                self.embed.color = Colour.dark_red()
                self.embed.title = f"An Exception occured"
                self.embed.description = f"{e}\nTry another name."
                await ctx.respond(embed=self.embed)

        try:    #   Delete Channel

            await d.abc.GuildChannel.delete(ch, reason = reason)

        except (d.Forbidden, d.NotFound, d.HTTPException, ValueError, Exception) as e:
    
            self.embed.title = "An Exception Occured"
            self.embed.description = e
            await ctx.respond(embed = self.embed)

            return

        self.embed.color = Colour.dark_red()
        self.embed.timestamp = datetime.datetime.now()
        self.embed.title = f"{ctx.author.name} has deleted the channel\"**{name}**\""

        await chlog.send(embed=self.embed)

        #   Clear memory
        del ch, name, chlog
        del channeltype, reason

        await self.clear_memory(ctx)
        return 

    @channel.command()
    async def modify(self, ctx:d.ApplicationContext, channeltype, name, age_restricted = False, archived = False, category = None, delay = 0, locked = False, newname = None, overwrites = None, reason = None, region = None, require_tags = False, thread_slowmode = 0, topic = None, quality = None): #   Modify a channel

        ch = utils.get(ctx.guild.channels, name = name) #   Fetching the channel

        try :#  Checking for exceptions

            if str(channeltype).isdigit() : raise Exception("channeltype argument, can not be integers") #   Checking if the channelType contains integers
            elif str(channeltype) not in ["forum","text", "voice", "category", "stage" ]: raise Exception(" channeltype argument, has only four types, (forum / text / voice or category)")

            #   Boolean values
            if str(archived).isalpha():
                if str(archived) == "True": archived == True
                elif str(archived) == "False": archived == False
                else : raise TypeError("archived argument accepts only boolean expression \"True\" or \"False\"")
            else : raise TypeError("archived argument accepts only boolean expression \"True\" or \"False\" ")

            if str(age_restricted).isalpha():
                if str(age_restricted) == "True": age_restricted == True
                elif str(age_restricted) == "False": age_restricted == False
                else : raise TypeError("age_restricted argument accepts only boolean expression \"True\" or \"False\"") 
            else: raise TypeError("age_restricted accepts only boolean expression \"True\" or \"False\"")

            if str(locked).isalpha():
                if str(locked) == "True": locked == True
                elif str(locked) == "False": locked == False
                else : raise TypeError("locked argument accepts only boolean expression \"True\" or \"False\"") 
            else: raise TypeError("locked argument accepts only boolean expression \"True\" or \"False\"")

            if str(require_tags).isalpha():
                if str(require_tags) == "True": require_tags == True
                elif str(require_tags) == "False": require_tags == False
                else : raise TypeError("require_tags argument accepts only boolean expression \"True\" or \"False\"") 
            else: raise TypeError("require_tags argument accepts only boolean expression \"True\" or \"False\"")

            #   Integer values
            if str(thread_slowmode).isdigit(): 
                if int(thread_slowmode) < 0: raise ValueError("thread_slowmode argument accepts only integers greater or equal to zero")
            else: raise ValueError("thread_slowmode argument accepts only integers greater or equal to zero")

            if str(delay).isdigit(): 
                if int(delay) < 0: raise ValueError("delay argument accepts only integers greater or equal to zero")
            else: raise ValueError("delay argument accepts only integers greater or equal to zero")

            if not ch: raise Exception("Channel does not exist")
    
        except (ValueError, TypeError, Exception) as e :
            self.embed.title = "An Exception Occured"
            self.embed.description = f"{e}"
            self.embed.color = Colour.dark_red()
            ctx.respond(embed = self.embed)
            return


        arg = [{#   Adding values into a list
                "archived": archived,
                "category":category,
                "default_thread_slowmode": thread_slowmode,
                "locked":locked,
                "name":newname,
                "nsfw":age_restricted,
                "overwrites":overwrites,
                "require_tag": require_tags,
                "reason":reason,
                "region":region,
                "slow_mode": delay,
                "topic":topic,
                "video_quality":quality,
                

                }]
        
        for i in arg: # for each element in the dictionary, change values if None
            if i["name"] == None: i["name"] == ch.name 
            elif i["overwrites"] == None: i["overwrites"] == ch.overwrites
            elif i["topic"] == None: i["name"] == ch.topic
            elif i["category"] == None: i["category"] = ch.category
            elif i["region"] == None: i["region"] == ch.rtc_region  # Voice
            elif i["video_quality"] == None: i["video_quality"] == ch.video_quality_mode    #   Voice
            elif i["nsfw"] == False: i["nsfw"] == ch.nsfw # text
            elif i["slow_mode"] == 0: i["slow_mode"] == ch.slowmode_delay # text
            elif i["default_thread_slowmode"] == 0: i["default_thread_slowmode"] == ch.default_thread_slowmode_delay #text
            elif i["sync_permissions"] == False: i["sync_permissions"] == ch.permissions_synced
            elif i["require_tag"] == False: i["require_tag"] == ch.requires_tag

        #   Clear some memory
        del name, newname, topic
        del reason, category


        for i in arg:
            match channeltype:  #   Matching the type of channel
                case "forum": 
                    try : await ctx.channel.edit(reason = i["reason"], name = i["name"], nsfw = i["nsfw"], overwrites = i["overwrites"])
                    except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                        self.embed.title = "An Exception Occured"
                        self.embed.description = f"{e}"
                        self.embed.color = Colour.dark_red()
                        ctx.respond(embed = self.embed)

                        return

                case "text" : 
                    try : await ctx.channel.edit(reason = i["reason"], name = i["name"], topic = i["topic"], nsfw = i["nsfw"], sync_permissions = i["sync_permissions"], category = i["category"], slowmode_delay = i["slow_mode"], default_thread_slowmode_delay=i["default_thread_slowmode"], require_tag = i["require_tag"])
                    except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                        self.embed.title = "An Exception Occured"
                        self.embed.description = f"{e}"
                        self.embed.color = Colour.dark_red()
                        ctx.respond(embed = self.embed)

                        return

                case "voice" : 
                    try : await ctx.channel.edit(name = i["name"], topic = i["topic"], reason = i["reason"])
                    except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                        self.embed.title = "An Exception Occured"
                        self.embed.description = f"{e}"
                        self.embed.color = Colour.dark_red()
                        ctx.respond(embed = self.embed)

                        return

                case "stage" : 
                    try : await ctx.channel.edit(reason = i["reason"], name = i["name"], topic = i["topic"], nsfw = i["nsfw"], sync_permissions = i["sync_permissions"], category = i["category"], slowmode_delay = i["slow_mode"], default_thread_slowmode_delay=i["default_thread_slowmode"], require_tag = i["require_tag"])
                    except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                        self.embed.title = "An Exception Occured"
                        self.embed.description = f"{e}"
                        self.embed.color = Colour.dark_red()
                        ctx.respond(embed = self.embed)

                        return

                case "category": 
                    try: await ctx.channel.edit(name = name, archived = i["archived"], slowmode_delay=i["slow_mode"], reason = i["reason"])
                    except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                        self.embed.title = "An Exception Occured"
                        self.embed.description = f"{e}"
                        self.embed.color = Colour.dark_red()
                        ctx.respond(embed = self.embed)

                        return

        return

    async def clear(self, ctx, name, x):

        """
            #   Initializing the channels
            #   Checking wheter the values are correct or not
            #   Print a message
            #   Clearing a selected chat
        """

        ch = utils.get(ctx.guild.channels, name = name)#   Fetch channel
        chlog = utils.get(ctx.guild.channels, name = "auditlog")#   Fetch channel

        try :#   if channel does not exits

            if not ch : raise Exception(f"Channel \"{ch}\" does not exist in the server")
            elif not chlog : raise Exception("Could not find the auditlog channel")

            if str(x).isdigit():  
                x = int(x)
                if x < 0 or x > 1000: raise Exception("Choose an integer between 1-1000")
            else : raise Exception("You can not use alphabetical or ghlupical letters")


        except Exception as e: # Handle exceptions

            self.embed.color = Colour.dark_red()
            self.embed.title = f"An Exception Occured"
            self.embed.description = f'The channel {ch}, were not cleared as requested due to\n{e}'
            await ctx.send(embed = self.embed)

            del ch, chlog, x, name  #   Clear some memory
            return

        #   Prepare & send the embed message
        self.embed.color = Colour.dark_red()
        self.embed.timestamp = datetime.datetime.now()
        self.embed.title = f"{ctx.author.name} has cleared {x} chat lines in {ch} channel."
        await chlog.send(embed = self.embed)

        await ch.channel.purge(limit=x)#   Remove content from the channel
        del ch, chlog, x, name  #   Clear some memory

        return

    @channel.before_invoke  #   Invokes before channel command is executed
    async def check_channel(self, ctx: d.ApplicationContext):
        print("test check channel")
        channel = []
        ch = ["auditlog", "report", "support"]

        try :
            for i in ch:
                if utils.get(ctx.guild.text_channels, name = i): return 


        except TypeError as e: print(e)
        else:

            #   Creating a channel
            perms = {ctx.guild.default_role:d.PermissionOverwrite(view_channel=False)}

            for i in ch:

                #   Prepare and send embeded message
                self.embed.color = Colour.dark_red()
                self.embed.title = f'Auto Generated Channel'



                match i:

                    case "auditlog": 
                        self.embed.description = "Created to have easy accsess to bot commands used by admin / moderator"
                        i = await ctx.guild.create_text_channel(i, overwrites=perms)

                    case "report": 
                        self.embed.description = "Member report channel"
                        i = await ctx.guild.create_text_channel(i, overwrites=perms)

                    case "support": 
                        self.embed.description = "Member support channel"
                        i = await ctx.guild.create_text_channel(i, overwrites=perms)

                self.embed.timestamp = datetime.datetime.now()
                await i.send(embed=self.embed)
    
        #   Clear some memory
        del perms, ch, channel
        self.embed.description =""

        return

    @channel.after_invoke   #   Invokes after channel command is executed
    async def clear_memory(self, ctx: d.ApplicationContext):

        #   Clearing embeds
        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.remove_thumbnail()
        self.embed.color = Colour.dark_purple()
        self.embed.description = ""

        #await asyncio.sleep(1)

        del ctx
        return

class RoleModeration(Cog):

    """
        #  Author : krigjo25
        #  Date :   

        Commands for Moderators with manage_role

        #   Create a role
        #   Delete a role
        #   modify a role
    """

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed()
        self.now = datetime.datetime.now()

        return

    #   Slash command group
    role = d.SlashCommandGroup(name = "role", description = "Role mananger", default_member_permissions = d.Permissions(manage_roles = True))

    #   Create a role
    #   Delete a role
    #   role modify

    @role.before_invoke
    async def check_channel(self, ctx: d.ApplicationContext):

        channel = []
        ch = ["auditlog", "report", "support"]

        try :
            for i in ch:
                if utils.get(ctx.guild.text_channels, name = i): return 


        except TypeError as e: print(e)
        else:

            #   Creating a channel
            perms = {ctx.guild.default_role:d.PermissionOverwrite(view_channel=False)}

            for i in ch:

                #   Prepare and send embeded message
                self.embed.color = Colour.dark_red()
                self.embed.title = f'Auto Generated Channel'



                match i:

                    case "auditlog": 
                        self.embed.description = "Created to have easy accsess to bot commands used by admin / moderator"
                        i = await ctx.guild.create_text_channel(i, overwrites=perms)

                    case "report": 
                        self.embed.description = "Member report channel"
                        i = await ctx.guild.create_text_channel(i, overwrites=perms)

                    case "support": 
                        self.embed.description = "Member support channel"
                        i = await ctx.guild.create_text_channel(i, overwrites=perms)

                self.embed.timestamp = datetime.datetime.now()
                await i.send(embed=self.embed)
    
        #   Clear some memory
        del perms, ch, channel
        self.embed.description =""

        return

    @role.after_invoke
    async def clear_memory(self, ctx: d.ApplicationContext):

        #   Clear some Memory
        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.remove_thumbnail()
        self.embed.color = Colour.dark_purple()
        self.embed.description = ""

        #   Responding to discord
        await ctx.respond("Responding to a command")
        asyncio.sleep(1)
        await ctx.delete()
        return

class MiscModeration(Cog):

    """
        #  Author : krigjo25
        #  Date :   

        Miscerillious commands

        #   Create a role
        #   Delete a role
        #   modify a role
    """
        #   Channel moderation
        #   Commands for Moderators with manage_channels & manage_messages

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed()
        self.now = datetime.datetime.now().strftime('%H:%M, %d.%b - %y')

        return

    #   Slash command group
    misc = d.SlashCommandGroup(name = "misc", description = "misc moderator commands", default_member_permissions = d.Permissions(manage_channels = True))

    #   Announcements
    #   Auditlog
    #   polls

class MemberModeration(Cog):

    """
        #  Author : krigjo25
        #  Date :   

        Commands for Moderators with moderate members

        #   Warn a member
        #   Sush a member
        #   lift a member
        #   kick a member
    """
    def __init__(self, bot):

        self.bot = bot
        self.now = datetime.datetime.now().strftime("%a, %d.%b-%y")
        self.embed = Embed()

        return

    member = d.SlashCommandGroup(name = "member", description = "Member mananger", default_member_permissions = d.Permissions(moderate_members = True))

    #   Members
    #   Warn a member
    #   Timeout a member
    #   Lift a member
    #   Kick a member
    #   decorators

class Administrator(Cog):

    """
        #  Author : krigjo25
        #  Date :   

        Commands for Moderators with administrator

        #   Ban a member
        #   unban a member
        #   view the banlist
        #   view the auditlog
    """
    def __init__(self, bot):

        self.bot = bot
        self.now = datetime.datetime.now().strftime('%a, %d.%b-%y')
        self.embed = Embed(color=d.Colour.dark_red())

        return

    admin =d.SlashCommandGroup(name = "ban", description = "Server Administrator", default_member_permissions = d.Permissions(administrator = True))

    #   Ban Member
    #   Banlist
    #   unban a member