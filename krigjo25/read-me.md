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

***About the Developer***

kristoffer Gjøsund, born in 94, Norway, part the time goes to python, SQL otherwise, Gym and living life as a human

**Project info**

The idea for the discord bot is just for fun, and a learning progress how to use the documentation, and how to code Python



***The bot***

krigjo25 made for Discord, intentionally<br>
helping out as a Discord administrator, miniGames mananger and Server configuriations for games

## About-Krigjo25

***Project Information***<br>

Project started: <br>
**23.10-21.**<br>

Last update: <br>
**12.02-22.**<br>

Current verison:<br>
**1.0.0 RC 1**

SQL Language Used :<br>
**MariaDB**

**How to**

The bot is there to help you to manage your server, with the given tasks which is available to be used, and for other members to have fun with-in discord,
the prefix command used in the project  **?'**, e.g **'?help'**

***Feautures***

***Bot Member Utility:***

**Community-module**

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

**miniGames-module**

> 8ball <br>
> jumble <br>
> guess The Number<br>
> reaction game (Rock, Scissor & paper)<br>

new games added in the feauture

***Bot Pre Moderation Utility***

**Auto role-assignment**

*Member joins:*

When a member joins the server, the bot will create a role called "@Members"<br>
the user will be added to the role.<br>

*Member leveling System*

~~Members will be able to level up to gain new roles~~<br>
~~Current max level is 100, roles+ changes every 25 level~~<br>



***Bot Post Moderation Utility***

Roles used in the project :

> Member        --  Automatic role assignment<br>
> sushed        --  Muted players<br>
> Moderator,<br>
> Administrator,<br>

*Moderator-module*

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

*Administrator-module*

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

***What has been learned***

- function

*What makes krigjo25 unique*

The bot serving you, as a humble bot

## Responsories

- discord.py, [Rapptz](https://github.com/Rapptz/discord.py),  <br>
- ~~Anti-Spam, [Skelmis](https://github.com/Skelmis/DPY-Anti-Spam/commits?author=Skelmis),~~<br>
- MariaDB, [MariaDB Community](https://github.com/mariadb-corporation/mariadb-connector-python), <br>
- python_dotenv, [Saurabh Kumar](https://github.com/motdotla/dotenv),<br>

 

## Credentials

***Disclaimers:***<br>

***The developer can only have the responsibility, for how the projects is created, how it is used,  is another story.***

***Contact Information***

Discord : krigjo25#5588.<br>
~~website : krigjo25.com~~

Only One advice.<br>
« Everything is perfect as it is.

***References:***

[ObjectOriented Discord Bot](https://nik.re/posts/2021-09-25/object_oriented_discord_bot), by Nikola Cucakovic,

***Books used while learning Python***

[learn Python with-in one day and learn it well, by Jamie Chan](https://learncodingfast.com/)<br>
[learn SQL with-in one day and learn it well, by Jamie Chan](https://learncodingfast.com/)

## Project Summary

   
*   Since i do not have any particular experience in Phyton or SQL language then i did have a lot of challanges<br> 
    regarding connecting to a database, creating a reaction based game, working with the different modules in the<br>
    python library, finding ways to protect the database inputs, creating an advanced command handler to have some<br>
    control over the different parts of the bot.