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

Kristoffer Gjøsund, born in 94, Norway,<br>
 1/3 of the times goes to python, SQL<br>
otherwise, Gym and living life as a human being.

### Project info

Information about the design for each modules<br>
can be found in the given links below includes<br>
the text files below,

* [theGeneral](https://github.com/krigjo25/Discord/tree/main/theGeneral/design/theGeneral.md)


#### Status

    project start :<br>
        15.04-22

   Last Update :<br>


    Current verison:<br>
        0.0.1 beta

    SQL Database:
        mariaDB

## About-Krigjo25
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


## What makes theGeneral unique

Its made with love, for pyhon and he serves you as a humble servant

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

