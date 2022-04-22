# Discord bot Adminral Von Snider

## Table of content

> [Introduction](#Introduction)
>> About the Developer
>>> Krigjo25
>>> Contact

> [About-AdminralVonSnider](#About-VonSnider)
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

### About the Maintainer

Goes by the name Kristoffer, born in 94, :flag_no:.<br>
maintaining Python & SQL projects<br>
otherwise just being a human.

### Project info

Information about the design can be found in the given links below
includes the text files below,

#### Status

    project start :<br>
        16.04-22

   Last Update :<br>
        15.04-22

    Current verison:<br>
        check changelog.md

    SQL Database:
        mariadb

## adminiralVonSnider

made as an pre moderator assistant bot for discord.<br> 
It is made with love, for the members, <br>
he prefix command used in<br>
in the bot  **@'**, e.g **'@help'**

### Feautures

#### Bot Member Utility:

##### Community-Module

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

#### Bot Pre Moderation Utility

##### Auto role-assignment

###### Member joins

When a member joins the server, the bot<br> 
will create a role called "@Members"<br>
the user will be added to the role.<br>


#### Bot Post Moderation Utility

Roles used in the project :

> Member        --  Automatic role assignment<br>
> sushed        --  Automatic role assignment <br>


##### Moderator-module

> *     Requires kick_members = True 
> **    Requires mute_members = True
> ***   Requires manage_channels = True

>   cls (channel name) (int)
>> Clearing the discord chat limit = 1000
>
>   crech (channel name) *
>>  Records the action in the moderationlog channel
>>  Create a new channel, by default it is only visible for roles and members with manage_channels

>   kick (member name) (reason) *
>> Kicks a member from the server, stores in a log in the modereationlog channel
>> records the action in the moderationlog channel
>
>   poll
>> Creates a poll
>
>   online
>>  Checks whom is online/offline
>
>   warn
>>  Manually warn a member
>> records the action in the moderationlog channel
>
>   sush *
>> Snooze a playyer manually for x seconds
>> records the action in the moderationlog channel

##### Administrator-module

> ban (member) (reason)
>> Ban a discord user from the server
>> records the action in the moderationlog channel
>
> banlist
>> View a list of banned server members
>                           
> unban (member)
>> Unban a discord user from the server
>> records the action in the moderationlog channel
>
>   setrole (member) (role)
>> Set a member's role
>
>   delRole (roleName)
>> Deletes a role from the server
>
>   announce (channel Name)
>> Creates an announcement in the given channel
>
>
> Software-Technician, Software-technician
>> Moderator commands
>> Admin commands

## What has been learned

*  Learned how to create some simple moderation tools to manage the server


### What makes krigjo25 unique

The bot is made with love for Python,<br> 
it will serve you as a humble bot


## Responsories

- discord.py [Rapptz](https://github.com/Rapptz/discord.py),  <br>
- ~~Anti-Spam [Skelmis](https://github.com/Skelmis/DPY-Anti-Spam/commits?author=Skelmis),~~<br>
- MariaDB [MariaDB Community](https://github.com/mariadb-corporation/mariadb-connector-python), <br>
- python_dotenv [Saurabh Kumar](https://github.com/motdotla/dotenv),<br>


 

## Credentials

### Disclaimers:

***The developer can only have the responsibility, for how the projects is created, how it is used,  is another story.***

### Contact Information

Discord : krigjo25#5588.<br>
~~website : krigjo25.com~~

Only One advice.<br>
« A human can maintain something, but never actually create something. The side effects of the maintained element are what has been created.

### References:

[ObjectOriented Discord Bot](https://nik.re/posts/2021-09-25/object_oriented_discord_bot), by Nikola Cucakovic,

***Books used while learning Python***

[learn Python with-in one day and learn it well, by Jamie Chan](https://learncodingfast.com/)<br>
[learn SQL with-in one day and learn it well, by Jamie Chan](https://learncodingfast.com/)