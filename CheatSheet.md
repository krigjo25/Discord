# Cheatsheets

## Intents

>   self.intents.dm_typing = # 
>   self.intents.dm_messages #
>    self.intents.dm_reactions #
>    self.intents.guild_typing #
>    self.intents.guild_messages
>    self.intents.guild_reactions #
>      self.intents.bans = #   Allows the bot to ban / unban members
>self.intents.guilds  #   Allows the bot to interect with guilds
>self.intents.members  #   Allows the bot to interact with members
>self.intents.messages #   Allows the bot to send messages Guild & DM
>self.intents.presences #   Allows the bot to track member activty
>self.intents.message_content #   Allows the bot to send embeded messages
>self.intents.emojis_and_stickers #   emoji, sticker related events
>self.intents.reactions #    shortcut for dm and guild reactions
>self.intents.invites #
>self.intents.value =
>self.intents.typing = # Whether guild and direct message typing related events >are enabled. Shortcut for  guild,dm typing.
>self.intents.Methods =
>self.intents.webhooks =
>self.intents.voice_states =
>self.intents.integrations =
>self.intents.scheduled_events =

##   Bot profile

###    Image

>       await client.edit_profile(password=None, username = avatar=pfp)
>       await client.edit_profile(password=None, username=)

###    About the bot
>    requests.patch(    url = f"https://discord.com/api/v9/users/@me", headers = {"authorization":getenv('PyModToken')}, json = {"bio": 'Botinfo'} )

>    r.patch(   url=f"https://discord.com/api/v9/users/@me", headers= {"authorization": getenv('PyMod')}, json = {"accent_color": ""} )

>   r.patch(url=f"https://discord.com/api/v9/users/@me", headers= {"authorization": getenv('PyMod')}, json = {"banner": ""} )

##   Presence

>         await self.change_presence(activity= Game())

