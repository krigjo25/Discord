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

#   Dicitionary
from pylib.dictionaries.permissions import RolePermission
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
        self.now = datetime.datetime.now()

        return
    
    #   Slash command group
    channel = d.SlashCommandGroup(name = "channel", description = "Create something", default_member_permissions = d.Permissions(manage_channels = True))

    @channel.command
    async def test(self, ctx:d.ApplicationContext):
        print(ctx.guild.categories)
        return
    @channel.command()
    async def create(self, ctx:d.ApplicationContext, channeltype:d.Option(str, "eg. (forum / text / voice / stage)", required = True), name:d.Option(str, "Name of the channel eg. (general-talk, general)", required = True), age_restricted:d.Option(bool, "Is the channel restricted for users below 18? (True / False)", default = False) , bitrate:d.Option(int, "bitrate (voic channel)", required = False, default = 0),  category:d.Option(str, "Name of the category. (GENERAL, GENERAL TALK)", required = False, default = None), delay: d.Option(int,"Slowmode for the channel", default = 0), user_limit:d.Option(int,"User limitation for the channel (Voice channel parameter)", required = False, default = 0),perm:d.Option(str, "Permissions (custom / member / moderator / admin)", required = False, default = None), *topic:d.Option(str, "Tell the users about the channel subject (general-talk, general)", required = False, default = None), **reason:d.Option(str, "Reason for creation of the channel", required = False, default = None)):

        """
            Creating a channel

            
            #   Creating a single channel

            #   Checking the condtiions
            #   Create a channel
        """ 

        arg = [{ 
                "channeltype":channeltype, "Channelname": name, "category": str(category).upper(),"role_permissions": perm,
                "slow_mode": delay,  "topic":topic, "reason":reason, # Text channels
                "nsfw": age_restricted, "bitrate": bitrate, "user_limit": user_limit #  Voice and stage channels
                }]

        #   Clearing some space
        del name, bitrate, category
        del delay, user_limit, perm
        del topic, reason, age_restricted
        del channeltype

        for i in arg:#   Fetch the channel from the guild
            ch = utils.get(ctx.guild.channels, name = i["name"])
            chlog = utils.get(ctx.guild.channels, name = "auditlog")
            categories = utils.get(ctx.guild.categories, name = i["category"])

        try :#   Checking if the condition below is met, if the condition is met then raise exception
 
            if str(channeltype) not in ["forum", "text", "voice", "stage", "category",  ]: raise Exception(" channeltype argument, has only five types, (forum / text / voice / stage or category)")
            if ch : raise Exception(f"The channel {ch} already exits")  #   Checking if the channel already exits
            if not chlog : raise Exception("Channel auditlog does not exists")

            for i in arg:
                if i["delay"] < 0: raise ValueError("delay argument has to be greater than 0")
                if i["bitrate"] < 0: raise ValueError("Bitrate argument has to be  equal (or grater) to 0")
                 

        except (ValueError, TypeError, Exception) as e:#   If something goes wrong output a message

            self.embed.title = "An Exception Occured"
            self.embed.description = f"{e}"
            self.embed.color = Colour.dark_red()
            self.embed.timestamp = self.now
            await ctx.respond(embed = self.embed)

            return

        else:#   If everythings fine, continue 

            for i in arg:

                if i["category"] != None:#   Automatically creates a category if it does not exists
                    if not categories : await ctx.guild.create_category_channel(name = i["category"], reason = "User implied category, did not exist.")
                    else:
                        for j in ctx.guild.categories:
                            if category == j.name: i["category"] = j.id

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

                        try :await ctx.guild.create_text_channel(name = i["name"], category = i["category"])
                        except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                            self.embed.title = "An Exception Occured"
                            self.embed.description = f"{e}"
                            self.embed.color = Colour.dark_red()
                            ctx.respond(embed = self.embed)

                            return

                    case "voice":
                        try: await ctx.guild.create_voice_channel(name = name,  reason = reason, category = category, bitrate = bitrate, user_limit = user_limit, overwrites = perm, topic = topic, )
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

            self.embed.color = Colour.dark_red()
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f"{ctx.author.name} has created a **{channeltype}**, **\"{name}\"**"

            await chlog.send(embed=self.embed)

        return

    @channel.command()  #   Delete the channel
    async def delete(self, ctx:d.ApplicationContext, channeltype:d.Option(str, "eg. (forum / text / voice / stage)", required = True), name:d.Option(str, "Name of the chanel)", required = True), reason = None):

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

    @channel.command()
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

    #@role.commend()
    async def create(): pass

    @role.command() # delete a role
    async def delete(self, ctx, role ):

        """
            1   Checking if there is any channels called 'moderationlog'
            2   Ask the user for comfirmation before removing the role

        """

        #   Fetch role and channel
        role = utils.get(ctx.guild.roles, name= role)
        ch = utils.get(ctx.guild.channels, name='auditlog')

        try:
            if not role : raise Exception(f"\"{role}\" does not exists")
            elif not ch : raise Exception("audit channel does not exist")

        except Exception as e:

            self.embed.title = "An Exception Occured"
            self.embed.description = f'{e}, Try again...'
            await ctx.send(embed = self.embed)

            #   Clear some memory
            del role, ch
            return

        else:

            #   Prepare, send & clean up the embed message
            self.embed.title = f'Removing {role} role'
            self.embed.description = f'Sometimes we do not do what we do something stupid? type in the role to delete the role'

            await ctx.send(embed=self.embed)

            self.embed.clear_fields()

            #   Confirm the action
            response = await self.bot.wait_for('message', timeout=60.0)
            response = str(response.content)

            if response == role:
                #   Prepare the embed message and delete & role
                self.embed.title = f'{role} role, has been removed from the server'
                await response.delete()

            else: self.embed.title = f'Role removal cancelled'

        #   Send & clean up the embed message
        self.embed.color = Colour.dark_red()
        await ch.send(embed=self.embed)

        del role, ch, response

        return
 
    @role.command()# remove a member from a role
    async def demote(self, ctx, member:d.Member, role, *, reason=None ):

        """
            1   Checking if there is any channels called 'auditlog'
            2   When the command is invoked, ask the user for a confirmation
            3   Remove the user from the role

        """

        #   Initializing variables
        role = utils.get(ctx.guild.roles, name=f'{role}')
        ch = utils.get(ctx.guild.channels, name='auditlog')

        #   Prepare, Send & Clean up embed
        try: 
            if not role : raise Exception(f"Role \"{role}\" Not found")
        except Exception as e: 

            self.embed.color = Colour.dark_red()
            self.embed.title = 'An Exception Occured'
            self.embed.description = f"{e}, try again."
            await ctx.send(embed = self.embed)

        else:

            self.embed.color = Colour.dark_red()
            self.embed.title = f'removing {member} from {role}'
            self.embed.description = f'Type in the name if you really want to remove the person from the role.'

            await ctx.send(embed=self.embed)

        #   Retrieve the confirmation from the user
        response = await self.bot.wait_for('message')
        response = str(response.content).lower()

        if response in member:

            #  Prepare, remove, send & Clean up
            self.embed.color = Colour.dark_red()
            self.embed.title = f'{member} has been removed from {role} by {ctx.author} due to {reason} '

            await member.remove_roles(role)

        else:

            #   Prepare Send & Clean up
            self.embed = Embed(color=Colour.dark_red())
            self.embed.title = f'Role removal has been cancelled'

        self.embed.description=''
        await ch.send(embed=self.embed)


        return self.embed

    #   Set Role
    @role.command() # set a role
    async def set(self, ctx, member:d.Member, role, *, reason= None):

        #   Fetch roles and channel

        role = utils.get(ctx.guild.roles, name=f'{role}')
        ch = utils.get(ctx.guild.channels, name='auditlog')

        try :
            if not role: raise Exception("Role does not exist")
            elif not ch: raise Exception("auditlog channel does not exist")

        except Exception as e:

            self.embed.title = "An Exception Occured"
            self.embed.description = f"{e}, try again"
            await ctx.send(embed = self.embed)

            del role, ch
            return
        else:
            #   Prepare, Send & Clean up embed
            self.embed.color = Colour.dark_red()
            self.embed.title = f'removing {member} from {role}'
            self.embed.description = f'Type in **{member}** to set the member as {role}?'

            await ctx.send(embed=self.embed)

        #   Retrieve the confirmation from the user
        response = await self.bot.wait_for('message')
        response = str(response.content).lower()

        if response in member:

            #  Prepare, remove, send & Clean up
            self.embed.color = Colour.dark_red()
            self.embed.title = f'{member} has been added to {role} by {ctx.author}'
            self.embed.description = f"{reason}"

            await member.add_roles(role)


    #   Change Color for the role
    @role.command()
    async def modify(self, ctx, role, *, reason= None):

        #   Initializing classes
        perm = RolePermission

        #   Fetch channel and role
        ch = utils.get(ctx.guild.channels, name= 'auditlog')
        role = utils.get(ctx.guild.roles, name = f'{role}')
        color = ["Dark Purple", "Dark Red", "Dark Blue", "Purple", "Red", "Blue"]

        try:

            if not role: raise Exception("Role does not exists")
            if not ch: raise Exception("audit channel does not exists")

        except Exception as e:

            self.embed.color = Colour.dark_red()
            self.embed.title = 'An Exception Occured'
            self.embed.description = f'{e}, try again'
        
            await ctx.send(embed=self.embed)

            del ch, role, color, dc
            return

        else: 
            #   Prepare, send & Clean up
            self.embed.title = f'Choosing role Color'
            self.embed.description = f'Would you like to change colors of {role}? type in a title or **x** to exit '
            self.embed.add_field(name = 'Dark Purple', value = 'Dark Purple color for role ')
            self.embed.add_field(name = 'Purple', value = 'Purple color for role')
            self.embed.add_field(name = 'Dark Red', value = 'Dark red color for role')
            self.embed.add_field(name = 'Red', value = 'Red color for role')
            self.embed.add_field(name = 'Dark Blue', value = 'Dark Blue color for role')
            self.embed.add_field(name = 'Blue', value = 'Blue color for role')

            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            response = await self.bot.wait_for('message', timeout=30)
            response = str(response.content).lower().replace(" ", "")

            if response in color: color = dc.RoleColours(response)
            else: color=Colour.default()

            await ctx.guild.edit_role(name=f'{role}', color = color, reason = f'{reason}')
            
            self.embed.title = f"@{role}'s colour has changed into {response} by {ctx.author.name}"

            await ch.send(embed=self.embed)
            self.embed.clear_fields()

            #   Clear some memory
            del response, color, role
            del ch, dc
        return

    @role.before_invoke
    async def check_channel(self, ctx: d.ApplicationContext):

        channel = []
        ch = ["auditlog", "report", "support"]

        try :
            for i in ch:
                if utils.utils.get(ctx.guild.text_channels, name = i): return 


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

    @misc.command()
    async def polls(self, ctx, title, ch):

        """

            #   Creating a poll with default two values to choose from
            #   Using reaction to vote
            #   Title of the poll, how many options and Questions

        """

        pass

    @misc.command()
    async def serverbots(self, ctx):

        #   Fetching members
        for member in ctx.guild.members:

            #   Add emoji to status
            match member.status:
                case "idle": status = ":dash:"
                case "dnd": status = ":technologist:"
                case "Online": status = ":heart_on_fire:"
                case "offline": status = ":no:"

            #   Fetch user nick
            if str(member.nick) == None: nick = ''
            else: nick = f'Nick : {member.nick}\n'

            if member.bot == True: self.embed.add_field(name=f'{member.name} #{member.discriminator}',value=f'{nick}\n Status : {status}', inline=False)

        self.embed.title = 'Server Bots'
        self.embed.description = 'List of members'
        
        await ctx.send(embed = self.embed)
        
        self.embed.clear_fields()

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

    @member.command()
    async def warn(self, ctx, member:d.Member, *, reason=None):

        #   Fetch the channel log
        chlog = utils.utils.get(ctx.guild.channels, name='auditlog')

        try:
            if member == ctx.author: raise Exception("Can not warn your self")
            elif reason == None: raise Exception("Please provide a reason for the warn")

        except Exception as e :

            self.embed.color = Colour.dark_red()
            self.embed.title = "An Exception Occured"
            self.embed.description =f"{e}, Try again !"

            del chlog, member, reason

            return

        else:

            #   Prepare the embed message
            self.embed.color = Colour.dark_red()
            self.embed.description = f'*{reason}*.'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f'**{member}** has been warned by {ctx.author.name} Date: {self.now}'

            #   Message the user about the warn
            message = f'Greetings **{member}**.\n You recieve this Notification, because you have been warned by **{ctx.author}**.\n\n Due to :\n *{reason}*\n\nPlease read and follow the suggested guidelines for behavior in our disocrd channel'
            await member.send(message)

        await chlog.send(embed=self.embed)

        #   Clear some memory
        del message, reason, chlog
        del member

        return

   #   Mute Members
    @member.command()
    async def sush(self, ctx, member:d.Member, time=None, *, reason=None):

        """
            #   Fetch the channel
            #   Check if "time" argument is digits
            #   #   Set the time as int if it is a digit
            #   Check if the channel exists
            #   Check if there is a reason for unmute
            #   Check if the time is less than 1 week
            #   Check if the author is the member
            #   Calculate the time
            #   Prepare and messages
            #   timeout and send the message
        """

        #   Fetching the channel
        role = utils.get(ctx.guild.roles, name ='Sushed')
        ch = utils.get(ctx.guild.channels, name='auditlog')

        try:

            #   Checking if the selected member is the command invoker
            if member == ctx.author: raise Exception(f"Could not sush your self.")
            elif len(time) < 2: raise Exception(f"{time}s / m / h / d)")
            elif int(time[0]) > 604800: raise Exception(f' Could not sush **{member}** due to a limitation for 1w')
            elif not ch : raise Exception("Auditlog does not exists")
            elif reason == None: raise Exception(f" Could not sush **{member}** due to there were no reason to mute the member")

        except Exception as e: 

            self.embed.color = Colour.dark_red()
            self.embed.title = "An Exception Occured"
            self.embed.description = f"{e}"
            await ctx.send(embed = self.embed)

            #   Clear some memory
            del time, ch, reason, member

            return

        else:

            #   Calculating the time
            time = hf.parse_timespan(time)

            #   Prepare, send & Clean up embed
            self.embed.color = Colour.dark_red()
            self.embed.title = f"**{member.name}** has been sushed by {ctx.author.name} for {time} seconds. Date : {self.now}"
            self.embed.description = f"*{reason}*."
            await ch.send(embed=self.embed)

            #   Prepare and send the member, the message and sush the member
            await member.add_roles(role)
            await member.send(f"""Greetings, **{member.name}**.\nYou recieve this message, because server moderator {ctx.author.name} gave you an timeout for **{datetime.timedelta(seconds=time)}**.\nYou will not be able to use the {ctx.guild}'s channels, during this given time.\nThe reason for this intervention is\n*{reason}*""")
            await member.timeout(until = d.utils.utcnow() + datetime.timedelta(seconds=time), reason = reason)

        #   Clear some memory
        del member, reason, time
        del ch

        return

    @member.command()
    async def lift(self, ctx, member:d.Member):

        """
            #   Fetching the channel and role
            #   Checking for exceptions
            #   Remove the member role
            4   send the selected member a message
        """

        #   Fetch channel and role
        ch = utils.get(ctx.guild.channels, name='auditlog')
        role = utils.get(ctx.guild.roles, name ='Sushed')

        try :
            #   Check for exceptions
            if not ch: raise Exception("Auditlog channel does not exist")
            if not role: raise Exception("@Sushed role does not exit")

        except Exception as e:

            self.embed.description = f"{e}"
            self.embed.color = Colour.dark_red()
            self.embed.title = "An Exception Occured"
            await ctx.send(embed = self.embed)

            del ch, role
            return

        else:

            #   Prepare & send embed message
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Sush Lifted for {member}'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.description = f"by **{ctx.author.name}**\n Date: {self.now} User has been notified by a direct message."
        
        await ch.send(embed= self.embed)

        #   Removing role, timeout & Notify the user
        await member.remove_roles(role)
        await member.timeout(until=None, reason="unmuted")
        await member.send(f'Greetings **{member}**.\n\n The sush has been lifted you can now use {ctx.guild}')

        #   Clear some memory
        del role, ch, member
        return

    #   Kick Members
    @member.command()
    async def kick(self, ctx, member:d.Member, *, reason=None):

        """
            #   Fetching the auditlog channel
            #   Checks for exceptions
            #   Prepare the embed message
            #   Sending the member notification for the kick
            #   Kicking the member
        """

        #   Fetching the channel
        ch = utils.get(ctx.guild.channels, name='auditlog')

        try :

            if member == ctx.author: raise Exception("Can not kick your self")
            if reason == None: raise Exception(f"**{ctx.author.name}** Provide a reason to kick **{member.name}**")
            if not ch : raise Exception("There is no channel named auditlog")

        except Exception as e :

            self.embed.title = "An Exception Occured"
            self.embed.description = f"{e}, try again."
            self.embed.color = Colour.dark_red()
            await ctx.send(embed=self.embed)

            #   Clear some memory
            del ch, reason, member

        else:

            #   Prepare embed
            self.embed.color = Colour.dark_red()
            self.embed.description = f' *{reason}*.'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f'**{member}** has been kicked from the server by {ctx.author.name} Date : {self.now}'

            #   Creating a message to the user, send it to his DM, then kick
            await member.send(f"Greetings **{member}**.\nYou recieve this message, because moderator {ctx.author.name} kicked you from {ctx.guild.name}\nDue to :\n *{reason}*")
            await member.kick(reason=reason)

        #   Send & Clean up embed
        await ch.send(embed=self.embed)

        return

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

    ban =d.SlashCommandGroup(name = "ban", description = "Server Administrator", default_member_permissions = d.Permissions(administrator = True))

    #   Ban Member
    #   Banlist
    #   unban a member

    @ban.command()
    async def list(self, ctx:d.ApplicationContext):
        """
            #   List of banned members
        """
        #   Initializing a list
        banned = []

        try:

            #   Iterating over the ctx.guild bans
           async for entry in ctx.guild.bans():

                dictionary = { "name": entry.user.name,
                                "discriminator": entry.user.discriminator,
                                "reason": entry.reason}

                banned.append(dictionary)

        except Exception as e : print(e)
        else:

            #   Prepare the ebeded message
            self.embed.title = 'List of banned server members'
            self.embed.description =' User name & discriminator | Reason'
            self.embed.color = Colour.dark_red()

            if banned:

                for i in banned: self.embed.add_field(name= f'{i["name"]}#{i["discriminator"]}', value = f'{i["reason"]}', inline = True)

            else: self.embed.description = "Noone banned yet, Hurray :party:"

            self.embed.add_field(name= f'Total banned users {len(banned)}\n== End of List ==', value = ':-)', inline = False)
            await ctx.send(embed=self.embed)

        #   Clear some space
        del banned, entry, dictionary

        return

    @ban.command()    #   Prohbit a user to enter the channel again
    async def member(self, ctx:d.ApplicationContext, member:d.Member, *, reason=None):

        """
            #   Ban a server member
            #   Reason required
            #   Notify the user about the ban
            #   Cheeck for a moderationlog channel
            #   Log the ban

        """

        try :
        
            if reason == None: raise ValueError(f"Can not ban {member} with out a reason.")

            #   Checks after moderationlog channel
            ch = utils.get(ctx.guild.channels, name='moderationlog')

        except Exception as e :

            self.embed.color = Colour.dark_red()
            self.embed.title =f"Tried to ban {member}"
            self.embed.description = f"{e}\n"
            await ctx.send(embed = self.embed)

        else:

            #   Log the ban
            self.embed.color = Colour.dark_red()
            self.embed.description = f"due to {reason}"
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f'{member} has been banned by {ctx.author}'
            
            await ch.send(embed=self.embed)

            #   Notify the user about the ban & ban the member
            message = f'the Administrator Team has decided to probhid you for using  **{ctx.guild.name}** \n \n Due to :\n **{reason}**'
            await member.send(message)
            await member.ban(reason=reason)

        #   Clear some memory
        del reason, message
        del member, ch

        return

    @ban.command()#   Allows a user to enter the channel again
    async def unban(self, ctx:d.ApplicationContext, *, member:d.Member):

        #   Check if there is a channel called moderation log
        ch = utils.get(ctx.guild.channels, name='auditlog')

        try :
            if len(name) != 2: raise Exception("Did you forget the discriminator / name?")
            elif not ch : raise Exception("auditlog channel does not exits")

        except Exception as e:

            #   Prepare emed message
            self.embed.color = Colour.dark_red()
            self.embed.title = f"An Exception Occured"
            self.description = f"{e}, try again"
            await ctx.send(embed = self.embed)

            del ch, member
            return

        else:
            name = str(member).split('#')

            #   Log the unban
            self.embed.color = Colour.dark_red()
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f"{member[0]} has been unbanned by {ctx.author.name}"

            await ch.send(embed=self.embed)

            #  Unban the given member
            async for entry in ctx.guild.bans():
                user = entry.user
            
                if user.name == name[0] or user.discriminator == name[1]: await ctx.guild.unban(user)

        del member, name, ch

        return

    @ban.before_invoke
    async def CheckModChannel(self, ctx):

        #   Fetching the channel "auditlog"
        ch = utils.get(ctx.guild.channels, name = "auditlog")

        try :
            if ch: return True
        
        except TypeError as e: print(e)
        else:

            #   Creating a channel
            perms = {ctx.guild.default_role:d.PermissionOverwrite(view_channel=False)}
            ch = await ctx.guild.create_text_channel("auditlog", overwrites=perms)

            #   Prepare and send embeded message
            self.embed.color = Colour.dark_red()
            self.embed.title = f'Auto Generated Channel'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.description = f"Created to have easy accsess to bot commands used by admin / moderator"
            await ch.send(embed=self.embed)
    
        #   Clear some memory
        del perms, ch
        self.embed.description =""

        return

    @ban.after_invoke
    async def ClearMemory(self):

        #   Clear some Memory
        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.description = ""
        self.embed.remove_thumbnail()
        self.embed.color = Colour.dark_purple()

        return

    async def Announcement(self, ctx, ch):

        #   Fetch the channel
        ch = utils.get(ctx.guild.channels, name=ch)

        try:
            if not ch : raise Exception(f"Channel \"{ch}\" Not found")

        except Exception as e:

            self.embed.color = Colour.dark_purple()
            self.embed.title = "An Exception Occured"
            self.description = f"{e}, try again."
            ctx.send(embed = self.embed)

            return

        else:
            #   Prepare & send embeded message
            self.embed.title = 'Server Announcement'
            self.embed.description = 'What would you like to announce?'
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            #   Get the user's message and procsess it
            message = await self.bot.wait_for('message')
            message = str(message.content)

            #   Prepare & Send the embed message
            self.embed.description = message
            self.embed.title = 'Server News announcement'
            self.embed.timestamp = datetime.datetime.now()
            self.embed.set_author(name = f"By : {ctx.author.name}")
            
            await ch.send(embed=self.embed)

        del message, ch
        return

    async def Auditlog(self, ctx, limit = 3): pass