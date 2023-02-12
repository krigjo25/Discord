<h1 align="center"> PyMod Documentations</h1>

<h2 align="center">Table of content</h2>

### [Introduction](#introduction)
>   About the Maintainer
>   Contact

### [PyMod](#pymod)

> How to use the bot<br>
> Project Status<br>
> Available features<br>

### [Features](#features)

> Community Module<br>
> Moderation commands<br>
> Administrator commands<br>
> Updates

### [Responsories](#responsories)

### [Credentials](#credentials)

> PrivacyPolicy<br>
> Termsofusage<br>
> licence

### [Project Summary](#project-summary)

# Introduction

## About the Maintainer

Hey, my name is Kristoffer, I'm borin in 94, :norway:<br>
[Contact](https://github.com/krigjo25/contactinformation) me through discord, messenger or at my website.<br>
Bot developed by @krigjo25

[Terms of Use](), [Privacy Policy notice]()<br> 


#   Pymod

The bot is a discord moderator command assistant,<br>
Intention of the bot is to easy accsess discord moderation system.

## How to use the bot

As the bot has a prefixed command **?**<br>
You will have to type (eg. **?help**)

## available features

-   Community commands
-   Moderator commands
-   Administrator commands

## Project Status

Bot created at 15.04-22, and have a last update at 12.02-23<br>
The current version of the bot is v1


#   Features

## Bot Member Utility

<h3 align = "center"> Community module</h3>

Commands which is available for everyone.
> botinfo (optional parameter : log )<br>
> * Information about the bot
>
> meme<br>
> * Generates a random meme from Reddit
>
> members (optional parameters : off, on<br>
> * list of members in the server
>
> randint (integer one) (integer two)<br>
> * generate a random integer
>
> liro<br>
> * List the server roles
>
> poll
>  -    Creates a poll

## Bot Post Moderation Utility

<h3 align = "center"> Introduction</h3>

The bot has been coded to automate generate roles and channels

### Roles


>   Sushed<br>
>   - Is a role for muted members

### Channels
>   auditlog<br>
>   -   A channel log
<h2 align="center"> Moderation Module</h2>

###  **Moderators with manage_channels**

Commands which requires **manage_channels**
>   ch Clear (channel name) (int)
>  -    Clear the chat limit 100 lines each time the command is used
>
>   ch Create
>  -    Deletes a channel
>
>   ch Create
>  -   Creates a new channel
>  ~~ch Edit~~
>  -    ~~Modify a channel, permissions~~

###  **Moderators with manage_member**

Commands which requires **moderate_members**

>   sush* (memberName) (1s - 1 w) (reason)
>  -    Snoozes a member for given minute
>  -    Limitations : 1 w mute.    e.g : sush MemberName 1s / 1m / 1d / 1w reason
>
>   lift (memberName)
>   -   Removes the mute and the role.
>
>   Warn*
>  -    Manually warn a member

###   **Moderators with kick_members**

Commands which requires **kick_members**
>   kick* (member name) (reason)
>   -   Kicks a member from the server


###   **Moderators with manage_Roles**

Commands which requires **manage_roles**
>   role Create* (roleName)
>  - Pre made permissions,
>  - Customize your own permissions,
>  - Premade Colours
>  - Customize your own  colours
>
>   role Demote* (memberName)
>  -    Removes a member from the roles
>
>   role Set* (memberName) (role)
>  -   Set a member's role
>
>   role Delete* (roleName)
>  -   Deletes a role from the server

- "*" records the given command in the moderationlog channel

### **List of Premade Permissions**

>   Members
>   -   Full Membership Permissions
>   -   Chat previligies, Stream previliges & Voice Previliges
>   -   Chat Permissions only
>   -   permissions enabled :<br>Send_messages,<br> add_reactions,<br> external_emojis,<br> read_message_history & use_slash_commands<br>
>  StreamPermissions
>  -    permissions enabled :<br>Chat Permissions & stream
>
>   VoicePermissions
>   -   permissions enabled :<br> Chat Permissions,<br> speak, connect,<br> request_to_speak,<br> send_tts_messages,<br> use_voice_activation

>   Moderator
>
>   Guild Moderator
>   -   Manages the guilds with manage_guild permissions
>
>   Role Moderator
>   -  Can manage roles with mange_roles permissions
>
>   Voice Moderator
>   -   They're able to move, mute, deafen members. They have priority_speaker previliges
>
>   Member Moderator
>   -    They're able to manage nicknames & moderate members
>
>   ModerationMananger
>   -   Has every moderation possiblities the other moderation type + they're able to kick members


<h2 align="center"> Administrator module</h2>

>   ban* (member) (reason)
>  -   Ban a discord user from the server
>
>   banlist
>  -    View a list of banned server members
>                           
>   unban* (member)
>   -   Unban a discord user from the server
>
>   announce (channelName)
>  -   Creates an announcement in the given channel as the bot
> - **"*"** records the command in the channel auditlog

##  Credentials

### Responsories

-   discord.py by [Rapptz](https://github.com/Rapptz/discord.py),
-   ~~Anti-Spam by [Skelmis](https://github.com/Skelmis/DPY-Anti-Spam/commits?author=Skelmis)~~,
-   humanfriendly by [Peter Odding](https://github.com/xolox/python-humanfriendly),
-   MariaDB by [MariaDB Community](https://github.com/mariadb-corporation/mariadb-connector-python),
-   python_dotenv by [Saurabh Kumar](https://github.com/motdotla/dotenv),

### APIS

### Disclaimer

The developer can only have the responsibility,<br>
for how the projects is created, how it is used,<br>
is another story.