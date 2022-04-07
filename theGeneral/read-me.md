# Discord bot krigjo25

## Table of content

> [Introduction](#Introduction)
>> About the Developer
>>> Krigjo25
>>> Contact

> [About-krigjo25](#About-krigjo25)
>> project information 
>> How to use the bot
>> Features
>> Updates

> [Responsories](#Responsories)

> [Credentials](#Credentials)
>> Disclaimers
>> References

> [Project-Summary](#project-Summary)

## Introduction

### About the Developer

Kristoffer Gjøsund, born in 94, Norway, part the time goes to python, SQL
otherwise, Gym and living life as a human being.

### Project info

Information about the design can be found in the given links below
includes the text files below,

*   [GameBot](https://github.com/krigjo25/Discord/tree/main/gameBot/design/gameBot.md)


#### Status

    project start :<br>
        23.10-21

   Last Update :<br>
        12.02-22

    Current verison:<br>
    1.0.0
    SQL Database:
        mariaDB

### MajorArch

the MajorArch is made as an assistant for Discord bot<br>

## About-MajorArch
The bot is created as an moderator for the discord server

the prefix command used in the project  **?'**, e.g **'?help'**

## Feautures

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

> afk (message)
>> To notify other server members that you're going afk, 
>> a text-channel will be created, and a message will be sent there.
>> on mention the author recieves an afk message, and a error, that the person is not to be disturbed.
>
> back
>> Deletes the status update


### Bot Pre Moderation Utility

* Auto role-assignment

##### Member joins:

When a member joins the server, the bot will create a role called "@Members"<br>
the user will be added to the role.<br>

#### Member leveling System

~~Members will be able to level up to gain new roles~~<br>
~~Current max level is 100, roles+ changes every 25 level~~<br>



### Bot Post Moderation Utility

Roles used in the project :

> Member        --  Automatic role assignment<br>
> sushed        --  Muted players<br>
> Moderator,<br>
> Administrator,<br>

#### Moderator-module

> cls (channel name) (int)
>> Clear the chat limit 100 lines each time the command is used
>
> crech (channel name)
>> Create a channel, by default it is only visible for admins & moderator roles
>
> kick (member name) (reason)
>> Kicks a member from the server, stores in a log in the channel modereationlog
>> records the the kick in the channel moderationlog
>
> poll
>> Creates a poll
>
>   Online
>>  Checks whom is online/offline
>
>   Warn
>>  Manually warn a member
>> records the the warn in the channel moderationlog
>
>   sush
>>   Manually mutes the member for some seconds
>> records the the mute in the channel moderationlog

#### Administrator-module

> ban (member) (reason)
>> Ban a discord user from the server
>> records the the ban in the channel moderationlog
>
> banlist
>> View a list of banned server members
>                           
> unban (member)
>> Unban a discord user from the server
>> records the the unban in the channel moderationlog
>
> setRole (member) (role)
>> Set a member's role
>
> delRole (roleName)
>> Deletes a role from the server
>
>announce (channelName)
>> Creates an announcement in the given channel
>
>
> Software-Technician, Software-technician
>> Moderator commands
>> Admin commands

## What has been learned 


## What makes MajorArch unique

The bot serving you, as an humble assistant

## Responsories

- discord.py [Rapptz](https://github.com/Rapptz/discord.py),  <br>
- ~~Anti-Spam [Skelmis](https://github.com/Skelmis/DPY-Anti-Spam/commits?author=Skelmis),~~<br>
- MariaDB [MariaDB Community](https://github.com/mariadb-corporation/mariadb-connector-python), <br>
- python_dotenv [Saurabh Kumar](https://github.com/motdotla/dotenv),<br>


 

## Credentials

### Disclaimer

The developer can only have the responsibility,<br>
for how the projects is created, how it is used,<br>
is another story.

### Contact information


[ContactInformation](https://github.com/krigjo25/Discord/blob/main/krigjo25/read-me.md)

### References

[references](https://github.com/krigjo25/Discord/blob/main/krigjo25/read-me.md)

## Project Summary

