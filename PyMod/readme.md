# PyMod

## Table of content

### [About PyMod](#About-PyMod)

>> Project Status 
>> How to use the bot
>> Features
>> Updates

### [Responsories](#Responsories)

### [Credentials](#Credentials)
>> Disclaimers<br>
>> References

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

* Auto role-assignment

##### Member joins:

When a member joins the server, the bot will create a role called "@Members" and the user will be added to the role.<br>


### Bot Post Moderation Utility

Roles used in the project :

-   sushed  -Muted players

#### Moderator-module

#####   Moderators with kick_members privileges

> cls (channel name) (int)
>> Clear the chat limit 100 lines each time the command is used
>
> crech (channel name)*
>> Create a channel, by default it is only visible for admins & moderator roles
>
> kick (member name) (reason)*
>> Kicks a member from the server
>
> poll
>> Creates a poll
>
>   Online
>>  Checks whom is online/offline
>
>   Warn*
>>  Manually warn a member
>

#####   Moderators with mute_members privileges

>   sush
>>  Changes the member role into sushed with default permissions
>>  Requires the default permission to be set to "No channel views"

#####   Moderators with manage_channels privileges

> chdel
>> Deletes a channel
>
> chcre
>> Creates a new channel

#####   Moderators with manage_Roles privileges

> ?remove (memberName)
>> Removes a member from the roles
>
>  ?setRole (memberName) (role)
>> Set a member's role
>
> ?delRole (roleName)
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

- discord.py [Rapptz](https://github.com/Rapptz/discord.py),  <br>
- ~~Anti-Spam [Skelmis](https://github.com/Skelmis/DPY-Anti-Spam/commits?author=Skelmis),~~<br>
- MariaDB [MariaDB Community](https://github.com/mariadb-corporation/mariadb-connector-python), <br>
- python_dotenv [Saurabh Kumar](https://github.com/motdotla/dotenv),<br>


 

## Credentials

### Disclaimer

The developer can only have the responsibility,<br>
for how the project is created.
How the bot is used, is another story.

