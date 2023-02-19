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

The bot uses Slash command, "/"
You will have to type (eg. **/community help**)

## available features

-   Community commands
-   Moderator commands
-   Administrator commands

## Project Status

Bot created at 15.04-22, as a prefixed command and have a last update at 25.02-23<br>
The current version of the bot is v1


#   Features

## Bot Member Utility

<h3 align = "center"> Community module</h3>

Commands which is available for everyone.
> /community botinfo (optional parameter : log )<br>
> * Information about the bot
>
> /community meme (optional parameter : reddit<br>
> * Generates a random meme from Reddit
>
> /community members (optional parameters : off, on<br>
> * list of members in the server
>
> /community random (integer one) (integer two)<br>
> * generate a random integer
>
> /community roles<br>
> * List the server roles
>
> /community poll
>  -    Creates a poll
>
> /community report
>   -   Reporting a member for his / her behavior
>
> /community support
>   -   Creating a post in the support channel
## Bot Post Moderation Utility

<h3 align = "center"> Introduction</h3>

The bot has been coded to automate generate roles and channels

### Roles


>   Sushed<br>
>   - Is a role for muted members

### Channels
>   auditlog<br>
>   -   A channel log
>
>   support<br>
>   -   Generates a new post in help and support
>
>   report<br>
>   -   Reporting a members behavior

<h2 align="center"> Moderation Module</h2>

###  **Moderators with manage_channels**

Commands which requires **manage_channels**
>   /misc clear (channel name) (int)
>  -    Clear the chat limit 100 lines each time the command is used
>   -   Does not create duplicated channels due to deletion error.
>
>   /create channel (channel name)
>  -    Creates a new channel as default hidden
>
>   /delete channel (channel name)
>   -   Deletes a channel if it exists

###  **Moderators with manage_member**

Commands which requires **moderate_members**

###   **Moderators with kick_members**

Commands which requires **kick_members**


###   **Moderators with manage_Roles**

Commands which requires **manage_roles**

>   /role delete* (roleName)
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

-   pycord.py by [Pycord Development](https://github.com/Pycord-Development/pycord),
-   ~~Anti-Spam by [Skelmis](https://github.com/Skelmis/DPY-Anti-Spam/commits?author=Skelmis)~~,
-   humanfriendly by [Peter Odding](https://github.com/xolox/python-humanfriendly),
-   MariaDB by [MariaDB Community](https://github.com/mariadb-corporation/mariadb-connector-python),
-   python_dotenv by [Saurabh Kumar](https://github.com/motdotla/dotenv),

### APIS

no apis used in the project

### Disclaimer

The developer can only have the responsibility,<br>
for how the projects is created, how it is used,<br>
is another story.