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
    async def create(self, ctx:d.ApplicationContext, channeltype:d.Option(str, "eg. (forum / text / voice / stage)", required = True), name:d.Option(str, "Name of the channel eg. (general-talk, general)", required = True), age_restricted:d.Option(bool, "Is the channel restricted for users below 18? (True / False)", default = False) , bitrate:d.Option(int, "bitrate (voic channel)", required = False, default = 0),  category:d.Option(str, "Name of the category. (GENERAL, GENERAL TALK)", required = False, default = None), delay: d.Option(int,"Slowmode counter(s)", default = 0), user_limit:d.Option(int,"User limitation for the channel (Voice channel parameter)", required = False, default = 0), perm:d.Option(str, "permissions (custom / member / moderator / admin)", required = False, default = "member"), *topic:d.Option(str, "Tell the users about the channel subject (general-talk, general)", required = False, default = None), **reason:d.Option(str, "Reason for creation of the channel", required = False, default = None)):

        """
            Creating a channel

            

            #   Checking the condtiions
            #   Create a channel
        """

        arg = [{ #  Initializing a list with the parameters
                "channeltype":channeltype, "channel_name": name, "category":category, "channel_permissions": perm,
                "slow_mode": delay,  "topic":reason.get("topic"), "reason":reason.get("reason"), # Text channels
                "nsfw": bool(age_restricted), "bitrate": bitrate, "user_limit": user_limit #  Voice and stage channels
                }]

        for i in arg:#   Fetch the channel from the guild
            chlog = utils.get(ctx.guild.channels, name = "auditlog")
            ch = utils.get(ctx.guild.channels, name = i["channel_name"])
            category = utils.get(ctx.guild.categories, name = i["category"])

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
                        
                if i["channel_permissions"] != None:
                    i["channel_permissions"] = ChannelPermissions().SelectPermissions(perm)
                    print( i["channel_permissions"])

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
                        try :await ctx.guild.create_text_channel(name = i["channel_name"], category = utils.get(ctx.guild.categories, name = i["category"]), nsfw = i["nsfw"], slowmode_delay = i["slow_mode"], topic = i["topic"], reason = i["reason"], overwrites = i["channel_permissions"])
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