<h1 align="center"> PyMod Documentations</h1>

<h2 align="center">Table of content</h2>

### [Introduction](#introduction)
>   About the Maintainer

### [PyMod](#pymod)

> About the bot<br>
> Project Status<br>
> How to use the bot<br>
> Features<br>

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

goes by the name Kristoffer, born in 94, :flag_no:.<br>
maintaining Python & SQL projects<br>
otherwise just being a human.

<h1 align="center"> About Pymod</h1>

Pymod is a discord moderator command assistant,<br>
Intention of the bot is to easy accsess discord moderation.

## How to use the bot

Command prefix for the bot **?**, e.g **?help** 

-   Moderator's privileges required **kick**
-   Administrator's privileges required **Administrator**

## Project Status

Bot created at 15.04-22, and have a last update at 11.05-22


<h2 align="center"> Features</h2>

## Bot Member Utility

### Community-Module

Commands which is available for everyone.
> botinfo (optional: log )
>> Information about the bot
>
> meme
>> Generates a random meme from Reddit
>
> memberlist
>> list of members in the server
>
> randint (integer one) (integer two)
>> generate a random integer
>
> liro
>> List the server roles

## Bot Post Moderation Utility

Automated roles in the project :

>   Sushed  - Muted members

<h2 align="center"> Moderation Module</h2>

##   General Moderator commands

These commands does not required any spesific permissions but requires the role moderator

>   cls (channel name) (int)
>  -    Clear the chat limit 100 lines each time the command is used
>
>   poll
>  -    Creates a poll
>
>   Online
>  -    Checks whom is online/offline
>
>   Warn*
>  -    Manually warn a member

##   Moderators with kick_members privileges

Commands which requires **kick_members**
>   kick* (member name) (reason)
>   -   Kicks a member from the server

##   Moderators with moderate_members privileges

Commands which requires **moderate_members**

>   sush* (memberName) (1s - 1 w) (reason)
>  -    Snoozes a member for given minute
>  -    Limitations : 1 w mute.    e.g : sush MemberName 1s / 1m / 1d / 1w reason
>
>   lift (memberName)
>   -   Removes the mute and the role.


##   Moderators with manage_channels & manage_threads privileges

Commands which requires **manage_channels**
Commands which requires **manage_threads**

>  ~~chedit~~
>>  ~~Modify a channel, permissions~~

>   chdel
>  -    Deletes a channel
>
>   chcre
>  -   Creates a new channel

##   Moderators with manage_Roles privileges

Commands which requires **manage_roles**
>   crero* (roleName)
>  - Pre made permissions,
>  - Customize your own permissions,
>  - Premade Colours
>  - Customize your own  colours
>
>   remro* (memberName)
>  -    Removes a member from the roles
>
>   sero* (memberName) (role)
>  -   Set a member's role
>
>   dero* (roleName)
>  -   Deletes a role from the server

- "*" records the given command in the moderationlog channel

## List of Premade Permissions

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
>
>   Moderator
>
>>  GuildModerator<br>
>>  manage_guild
>
>> Role Moderator
>> -   manage_roles
>
>> Voice Moderator
>> -    They're able to move, mute, deafen members. They have priority_speaker previliges
>
>> Member Moderator
>> -    They're able to manage nicknames & moderate members
>
>>  ModerationMananger
>>   -   Has every moderation possiblities the other moderation type + they're able to kick members

## List of premade Colours


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

### API

-   [NAPI Ninjas](https://api-ninjas.com/)<br>

### Disclaimer

The developer can only have the responsibility,<br>
for how the projects is created, how it is used,<br>
is another story.

### Contact information

[ContactInformation](https://github.com/krigjo25/contactinformation)
 
# Bot Summary

-   Created some basic commands for members
-   Moderation module
    *   kick_members previliges
    *   moderate_members previliges 
    *   manage_channels previliges
    *   manage_role previliges
        *   Created some roles permissions
        *   Created some role Colours


Bot developed by @krigjo25

[Terms of Use]() <br>
[Privacy Policy notice]()<br> 
