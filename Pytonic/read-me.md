# Discord Pytonic

## Table of content

## [Introduction](#introduction)<br>
> [the Maintainer](#the-maintainer)<br>
> [project information](#project-info)<br>

## [PyGame](#pygame)<br>
> [How to use the bot](#how-to-use-the-bot))<br>

## [Features](#feautures)<br>
>  [available games](#available-games)<br>
>  [Eightball](#eightball)<br>
>  [Jumble Game](#jumblegame)<br>
>  [Scrabble](#scrabble)<br>
>  [Little Proffessor](#little-proffessor)<br>
> [Guess The Number](#guess-the-number)<br>

## [Credentials](#credentials)<br>
> [Responsories](#responsories)<br>
> [APIs](#api)<br>
> [Disclaimers](#disclaimer)<br>
>  [licence](#licence)<br>
>  [contact](#contact-information)

## Introduction

### The Maintainer

My name is Kristoffer, most calls me for Kriss. I'm born in 94, Kristoffer using most oof his spare time to develop & improve the programming skills. Otherwise i live the life as a human would do.

### Project infomation

> Project start :<br>
>   26.03-23
>
>   Last update :<br>
>
>
>   SQL Database:<br>
>   mariadb

## PyGame

This project "Pytonic" Kriss had a thought to develop a bot containing some childhood games, for Discord.
It is made with love, for the community, <br>

### How to use the bot

The bot uses Slash command, "/" (eg. **/help frequentlyaskedquestions**)

## Feautures

### Moderation

### Bot Post Moderation Utility

<h2 align = "center"> Introduction</h3>

The bot has been coded to automatically generate roles and channels.

### Channels
>   log<br>
>   -   A category to store the listed text channels.
>   auditlog<br>
>   -   A channel log
>
>   member-support<br>
>   -   Generates a new post in help and support
>
>   member-report<br>
>   -   Reporting a members behavior


### <h2 align="center"> Moderation Module</h2>

Note : Most of the commands is recorded in the auditlog channel

Note : The targeted member will be notified if commands such as warn, sush, lift, kick, ban is used, the member will get a clear understanding for the left brain thought "why" it has happend

####  **Moderators with manage_channels**

Commands which requires **manage_channels**
>   /channel clear (channel name) (int)
>  -    Clear the chat limit 100 lines each time the command is used
>   -   Limited to channel duplicates, due to an deletion error.
>
>   /channel create (channel type), (name), (age_restricted), (bitrate), (category), (delay), (user_limit), (perm), *(topic), (**reason)
>   -   Channel_type, is required to contain either (text / forum / voice, stage or category). So the program knows what type of channel the user would like to create.
>   -   name, is required to type in, so the program knows what you would like to call the channel.
>   -   age_restricted has a default value of False, if you would like to restrict the channels for adults add True as value.
>   -   category, has a default value to None, if you would like to select a category for the channel, type in the name of the category.
>   -   delay has a default value of 0, if you would like slow peoples posts set it to a desired number, can not be less than 0.
>   -   user_limit, limits how many users can be at once in a VOICE channel.
>   -   perm, overwrites whom can view the channel, default to hidden.
>   -   topic, notify moderators / admins what the channel is used for
>   -   Reason to add to the auditlog
>
>   /channel delete (channel name)
>   -   Deletes a channel if it exists<br>
>
>   /channel clear (channel name)
####  **Moderators with manage_member**

Commands which requires **moderate_members**
>   /member warn (member name), (reason)<br>
>   /member sush (member name), (time), (reason)<br>
>   /member lift (member name)<br>

Commands which requires **kick_members**
> /member kick (member name), (reason)


####  **Moderators with manage_Roles**

Commands which requires **manage_roles**

>   /role delete* (roleName)
>   ~~/role create~~
>   /role modify
>   /role add


#### **List of Premade Permissions**

>   Members ()
>   -   Full Membership Permissions
>   -   Chat previligies, Stream previliges & Voice Previliges
>   -   Chat Permissions only
>   -   permissions enabled :<br>Send_messages,<br> add_reactions,<br> external_emojis,<br> read_message_history & use_slash_commands<br>

>  StreamPermissions
>  -    permissions enabled : stream
>
>   VoicePermissions
>   -   permissions enabled :<br> speak, connect,<br> request_to_speak,<br> send_tts_messages,<br> use_voice_activation

>   Moderator
>
>   Server Moderator
>   -   Manages the guilds with manage_guild, and other  permissions for moderators.
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
>   Headmoderator
>   -   Has every moderation possiblities the other moderation type + they're able to kick members


<h2 align="center"> Administrator module</h2>

>   /ban member (member) (reason)
>  -   Ban a discord user from the server
>
>   /ban list
>  -    View a list of banned server members
>
>   /ban unban* (member)
>   -   Unban a discord user from the server
>
>   /misc announce (channelName)
>  -   Opens a modal, where you can create a announcement in the given channel as the bot. The author will be the member whom invoked the commannd.


### Available games

-   WordGames
*   -   JumbleGame
*   -   Scrabble
*   -   Eightball

-   Math Games
*   -   Little Proffesor
*   -   Guess the number

-   Reaction Games
*   -   Rock Scissor paper

### WordGames

#### Socrates

Socrates is a inspired  by (Magic 8ball, by Albert C. Carter), and Dr. David R. Hawkings teachings. 

Socrates is designed to reflect on your own questions, and determind your own answers, as according to Dr.David R. Hawkings, and other philiosophers, that the questioneer must have the answer, as the questioneer has formulated the question, and the question can not be formulated with out an answer

The limitations of the game:

*      If the question contains any ghlypts or digits an exception will rise ( except ?.,)
*      Language supported : English

#### JumbleGame

1 player

JumbleGame where you unscrabble a given word, from a choosen caetgory, which is saved in a Mariadb database except randomized words, random words is provided by [API-Ninja](https://api-ninjas.com/)

Game limitations <br>
-   If the user does write any characters which is not alphabetical an exception occurs. 
-   Language supported : English

#### Scrabble

Scrabble is a known word game, where you gain points for each letter in the word, if the word does "exist" in an dictionary

The program will do a word validation check, throught the provided api by [API-Ninja](https://api-ninjas.com/)

If there is less than two players the player only plays with the bot which provide a random word.

-   If the word does not exists, the player will recieve zero points for the word
-   Language supported : English

### Math Games

#### Little Proffessor

Little Professor is a math game, which generates integers to (add, substract, devide / reminder / power of / module of )
based on the player level.

Exceptions may occure when a player inserts an alphabetical character or a Glypth as an answer

#### Guess the number

As the title implies. The intetion for the game is to guess a number between given integers.
the games ia automated with a level system

An Exception may occure:<br>

-   if user inputs any character which is non-integers.
-   if the user uses more than x seconds to answer.

### Reaction Games

####    Rock Scissors and Paper

As the name implies the bot adds three types of reaction, where the player can select one of the reactions<br>
to choose which type of hand the player wants to play.

Then the bot will select a reaction and print an answer

### Community Functions

-   botinfo (optional argument : log)
-   meme (optional argument : reddit)
-   Members (optional argument: online / offline)
-   roles
-   termsofusage

####    Botinfo

Botinfo provides some information about the bot and changelog

####    Meme

Generates a meme, from choosen disbrutor 

####    roles

See server roles

#####   termsofusage

show the program's terms of usage.

## Credentials

### Responsories

-   pycord.py [Pycord Development](https://github.com/Pycord-Development/pycord),  <br>
-   python_dotenv [Saurabh Kumar](https://github.com/motdotla/dotenv),<br>
-   requests [Kenneth Reitz](https://requests.readthedocs.io/en/latest/)<nt>

### API

-   [NAPI Ninjas](https://api-ninjas.com/)<br>

### Disclaimer

The developer can only have the responsibility,<br>
for how the projects is created, how it is used,<br>
is another story. 

[Terms of Use](https://www.termsfeed.com/live/4c7f1718-578b-4e89-8bb4-aa2a5500981d), [Privacy Policy notice]()<br> 

### [Licence](https://github.com/krigjo25/Discord/blob/main/licence)

### Contact information

-   Discord : krigjo25#5588<br>
-   Messenger : krigjo25<br>
-   website :