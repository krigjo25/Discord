#   Python Repositories
import datetime
import asyncio
import humanfriendly as hf

#   Discord Repositories
import discord as d
from discord import utils
from discord.embeds import Embed, Colour
from discord.ext.commands import  Cog, Bot

#   Dicitionary
from pylib.dictionaries.permissions import ChannelPermissions
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
    @channel.command()
    async def test(self, ctx:d.ApplicationContext, text = None):
        print(ctx.guild.categories)
        return

    @channel.command()
    async def create(self, ctx:d.ApplicationContext, channeltype:d.Option(str, "eg. (forum / text / voice / stage)", required = True), name:d.Option(str, "Name of the channel eg. (general-talk, general)", required = True), age_restricted:d.Option(bool, "Is the channel restricted for users below 18? (True / False)", default = False) , bitrate:d.Option(int, "bitrate (voic channel)", required = False, default = 0),  category:d.Option(str, "Name of the category. (GENERAL, GENERAL TALK)", required = False, default = None), delay: d.Option(int,"Slowmode counter(s)", default = 0), user_limit:d.Option(int,"User limitation for the channel (Voice channel parameter)", required = False, default = 0), perm:d.Option(str, "permissions (custom / member / moderator / admin)", required = False, default = None), role:d.Option(str, "Server role name", required = False), *topic:d.Option(str, "Tell the users about the channel subject (general-talk, general)", required = False, default = None), **reason:d.Option(str, "Reason for creation of the channel", required = False, default = None)):

        """
            Creating a channel

            

            #   Checking the condtiions
            #   Create a channel
        """

        arg = [{ #  Initializing a list with the parameters
                "channeltype":channeltype, "channel_name": name, "category":category, "channel_permissions": perm,
                "slow_mode": delay,  "topic":reason.get("topic"), "reason":reason.get("reason"), # Text channels
                "nsfw": bool(age_restricted), "bitrate": bitrate, "user_limit": user_limit, "channel_roles":role #  Voice and stage channels
                }]

        for i in arg:#   Fetch the channel from the guild
            chlog = utils.get(ctx.guild.channels, name = "auditlog")
            ch = utils.get(ctx.guild.channels, name = i["channel_name"])
            category = utils.get(ctx.guild.categories, name = i["category"])
            role = utils.get(ctx.guild.roles, name = i["channel_roles"])

        try :#   Checking if the condition below is met, if the condition is met then raise exception
 
            if str(channeltype) not in ["forum", "text", "voice", "stage",  ]: raise Exception(" channeltype argument, has only four types, (forum / text / voice or stage )")
            if not chlog : raise Exception("Channel auditlog does not exists")

            for i in arg:
                if i["slow_mode"] < 0: raise ValueError("**delay** argument has to be greater than 0")
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
                    if not category :await ctx.guild.create_category_channel(name = i["category"], reason = "User implied category, did not exist.")
                    else:
                        for j in ctx.guild.categories:
                            if category == j.name: i["category"] = int(j.id)

                if i["channel_permissions"] == None: i["channel_permissions"] = await ChannelPermissions().SelectPermissions(ctx, i["channel_permissions"])
                else:i["channel_permissions"] = await ChannelPermissions().SelectPermissions(i["channel_permissions"], role)

                match str(i["channeltype"]).lower(): #   Matching the type of channel

                    case "forum":

                        try: await ctx.guild.create_forum_channel(name = i["channel_name"], category = utils.get(ctx.guild.categories, name = i["category"]), snsfw = i["nsfw"], slowmode_delay = i["slow_mode"], topic = i["topic"], reason = i["reason"], overwrites = dict(i["channel_permissions"]))
                        except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                            self.embed.title = "An Exception Occured"
                            self.embed.description = f"{e}"
                            self.embed.color = Colour.dark_red()
                            ctx.respond(embed = self.embed)

                            return

                    case "text":
                        try :await ctx.guild.create_text_channel(name = i["channel_name"], category = utils.get(ctx.guild.categories, name = i["category"]), nsfw = i["nsfw"], slowmode_delay = i["slow_mode"], topic = i["topic"], reason = i["reason"], overwrites = dict(i["channel_permissions"]))
                        except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                            self.embed.title = "An Exception Occured"
                            self.embed.description = f"{e}"
                            self.embed.color = Colour.dark_red()
                            await ctx.respond(embed = self.embed)

                            return

                    case "voice":
                        try: await ctx.guild.create_voice_channel(name = i["channel_name"], category = utils.get(ctx.guild.categories, name = i["category"]),bitrate = i["bitrate"], user_limit = i["user_limit"], topic = i["topic"], reason = i["reason"], overwrites = i["channel_permissions"])
                        except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                            self.embed.title = "An Exception Occured"
                            self.embed.description = f"{e}"
                            self.embed.color = Colour.dark_red()
                            ctx.respond(embed = self.embed)

                            return

                    case "stage":
                        try: await ctx.guild.create_stage_channel(name = i["channel_name"], category = utils.get(ctx.guild.categories, name = i["category"]), topic = i["topic"], reason = i["channel_permissions"])
                        except (d.Forbidden, d.HTTPException, d.InvalidArgument) as e: 

                            self.embed.title = "An Exception Occured"
                            self.embed.description = f"{e}"
                            self.embed.color = Colour.dark_red()
                            ctx.respond(embed = self.embed)

                            return

            self.embed.color = Colour.dark_red()
            self.embed.timestamp = datetime.datetime.now()
            self.embed.title = f"{ctx.author.name} has created a  {str(channeltype).capitalize()} Channel, called **\"{name}\"**"

            await chlog.send(embed=self.embed)

        #   Clearing some space
        del name, bitrate, category
        del delay, user_limit, role
        del topic, reason, age_restricted
        del channeltype, chlog, ch, arg

        return

    @channel.command()
    async def delete(self, ctx:d.ApplicationContext, ch:d.Option(str, "Channel name", required = True)):

        """
            #   Delete a channel

            #   Fetch both channels
            #   Check if they exist
            #   Delete the channel
        """

        #   Fetch channels
        ch = utils.get(ctx.guild.channels, name = ch)
        chlog = utils.get(ctx.guild.channels, name = "auditlog")

        try:   # If one of the channels does not exist raise exception
            if not chlog: raise Exception(f"Channel \"{chlog}\" does not exists")
            if not ch: raise Exception(f"Channel \"{chlog}\" does not exists")

        except Exception as e: 
            self.embed.title = "An Exception Occured"
            self.embed.description = e
            ctx.send(emed = self.embed)
            return

        self.embed.color = Colour.dark_red()
        self.embed.timestamp = datetime.datetime.now()
        self.embed.title = f"{ctx.author.name} has deleted the channel\"**{ch}**\""

        await chlog.send(embed=self.embed)

        ctx.send_response
        await ctx.channel.delete()
        del ch, chlog # Clear memory
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
                "archived": archived, "category":category,
                "default_thread_slowmode": thread_slowmode,
                "locked":locked, "name":newname,"nsfw":age_restricted,
                "overwrites":overwrites,"require_tag": require_tags,
                "reason":reason, "region":region, "slow_mode": delay,
                "topic":topic,"video_quality":quality,
                

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
    async def clear(self, ctx:d.ApplicationContext, name, x):

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

        await ctx.channel.purge(limit=x)#   Remove content from the channel
        del ch, chlog, x, name  #   Clear some memory

        return

    @channel.before_invoke
    async def check_channels(self, ctx:d.ApplicationContext):

        print("test")
        ch = ["auditlog", "member-reports", "member-support"]

        category = utils.get(ctx.guild.categories, name = "log")

        if not category:
            category = utils.get(ctx.guild.categories, name = "log")
            await ctx.guild.create_category(name = "log", reason = "")

        for i in ch:
            i = utils.get(ctx.guild.channels, name = i)#  Fetch channel
            if not i: await ctx.channel.create_text_channel(name = i, category = category, reason = "Auto generated channel")

        del ch, i, ctx  #   Clear some memory
        del category

        return

    @channel.after_invoke
    async def clear_memory(self, ctx: d.ApplicationContext):

        #   Clearing embeds
        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.description = ""
        self.embed.remove_thumbnail()
        self.embed.color = Colour.dark_purple()
        

        del ctx
        return

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
    async def member(self, ctx:d.ApplicationContext, member:d.Member, *, reason:d.Option(str, "Reason for the ban", required = True)):

        """
            #   Ban a server member
            #   Reason required
            #   Notify the user about the ban
            #   Cheeck for a moderationlog channel
            #   Log the ban

        """

        ch = utils.get(ctx.guild.channels, name='auditlog') #   Fetch channel
        try :
            if not ch : raise Exception(f"Could not find \"**{ch}**\"")
            

        except Exception as e :

            self.embed.color = Colour.dark_red()
            self.embed.title =f"An Exception Occured "
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

        ch = utils.get(ctx.guild.channels, name='auditlog') #   Fetch channel

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
            
                if user.name == name[0] or user.discriminator == name[1]: 
                    await ctx.guild.unban(user)
                    await member.send(f"Greetings, {member}, the administrator team has decided to unban you from {ctx.guild}\n You are now welcome back to the server.")

        del member, name, ch, user

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
