# PyMod

## Table of content

### [About PyMod](#About-PyMod)

> Project Status<br>
> How to use the bot<br>
> Features<br>
> Updates

### [Features](#Features)

> Community Module<br>
> Moderation commands<br>
> Administrator commands<br>
> Updates

### [Responsories](#Responsories)

### [Credentials](#Credentials)

> Disclaimers<br>
> References

### [Project-Summary](#project-Summary)

## About-PyMod

I'm your discord moderator command assistant, 
My intention is just to assist you in your discord server

### How to

Command prefix for the bot **?**, e.g **?help** 

-   Moderator's privileges required **kick**
-   Administrator's privileges required **Administrator**

### Project Status

project name:
PyMod

project start :<br>
15.04-22

Last Update :<br>
11.05-22

Project version:
?botinfo

## Features

### Bot Member Utility

#### Community-Module

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

### Bot Pre Moderation Utility


### Bot Post Moderation Utility

Roles used in the project :

-   sushed  - Muted players

#### Moderator-module

#####   General Moderator commands

These commands does not required any spesific permissions

> cls (channel name) (int)
>> Clear the chat limit 100 lines each time the command is used
>
> poll
>> Creates a poll
>
>   Online
>>  Checks whom is online/offline
>
>   Warn*
>>  Manually warn a member

#####   Moderators with kick_members privileges

Commands which requires **kick_members**
> kick (member name) (reason)*
>> Kicks a member from the server

#####   Moderators with moderate_members privileges

Commands which requires **moderate_members**
>   sush (memberName) (sec) (reason)

>>  Changes the member role into sushed, to time the member out
>>  limitations : 1week mute.    e.g : sush MemberName 1s / 1m / 1d / 1w / 1y reason
>
>   lift (memberName)
>>  Removes the mute and the role.


#####   Moderators with manage_channels privileges

Commands which requires **manage_channels**
Commands which requires **manage_threads**
> chedit
>> Modify a channel, permissions

> chdel
>> Deletes a channel
>
> chcre
>> Creates a new channel

#####   Moderators with manage_Roles privileges

Commands which requires **manage_Roles**
> remove (memberName)
>> Removes a member from the roles
>
> setRole (memberName) (role)
>> Set a member's role
>
> delRole (roleName)
>> Deletes a role from the server

> editRole (roleName) //
>> Deletes a role from the server

- "*" records the given command in the moderationlog channel

#### Administrator-module

> ban (member) (reason)*
>> Ban a discord user from the server
>
> banlist
>> View a list of banned server members
>                           
> unban (member)*
>> Unban a discord user from the server
>
> announce (channelName)
>> Creates an announcement in the given channel as the bot
>> - "*" records the the unban in the channel moderationlog


## Responsories

-   discord.py [Rapptz](https://github.com/Rapptz/discord.py),  <br>
-   humanfriendly [Peter Odding](https://github.com/xolox/python-humanfriendly)<br>
-   ~~Anti-Spam [Skelmis](https://github.com/Skelmis/DPY-Anti-Spam/commits?author=Skelmis),~~<br>
-   MariaDB [MariaDB Community](https://github.com/mariadb-corporation/mariadb-connector-python), <br>
-   python_dotenv [Saurabh Kumar](https://github.com/motdotla/dotenv),<br>


 

## Credentials

### Disclaimer

The developer can only have the responsibility,<br>
for how the project is created.
How the bot is used, is another story.

