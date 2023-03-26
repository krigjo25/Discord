#   Python responsories
import regex as re
import datetime

#   Discord responsory
import discord as d
from discord import utils
from discord.ui import InputText, Modal
from lib.dictionary.game import Philosopher

class Socrates(Modal):

    """
        Discord UI modal

        >   Creation Date   : 21.02-23
        >   Last update     : 26.02-23

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Copyright (C) 2023  Kristoffer Gjøsund
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.embed = d.Embed()
        self.kwargs = [kwargs]

        for i in self.kwargs:
            match i['title']:
                case "Ask Socrates": self.socrates()

        return

    def socrates(self):

        self.add_item(InputText(label = "Ask Socrates", placeholder = "Your question", style = d.InputTextStyle.short, required = True))
        self.embed.colour = d.Colour.dark_purple()

        return

    async def callback(self, interaction:d.Interaction):

        for i in self.kwargs:

            match i['title']:
                case 'Ask Socrates':

                    array = [".", ",", "-", "'", ""]

                    quiz = self.children[0].value.lower()# Initializing the results
                    

                    try : # Looking for any characters which is not alphabetical
                        if not re.search(r'([A-Za-z\s\,\.\'\?\!])', quiz):raise Exception(" The answer can not contain any numberic or glyptic answers")

                    except Exception as e :
                        self.embed.title = f'Socrates Answers on your question "*{quiz}*"'
                        self.embed.description = f'{e}'
                        await interaction.response.send_message(embed = self.embed)
                        return

                    #   Checking for certain words in prompted message.
                    if quiz.startswith('how') or quiz.startswith("what") : prompt = Philosopher().Answer()
                    else: prompt = Philosopher().DumbFacts() 

                    #   Prepare and send the embed
                    self.embed.title = f'Socrates Answers your question "*{quiz}*"'
                    self.embed.description = f'{prompt}'
                    await interaction.response.send_message(embed=self.embed)

                    del quiz, prompt #  Clear some memory
        return

class Member(Modal):

    """
        Copyright (C) 2023  Kristoffer Gjøsund

        Collection of Community Commands

        >   Creation Date   : 21.02-23
        >   Last update     : 22.02-23

        Discord UI, reporting / supporting members

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Member modals

    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.embed = d.Embed()
        self.kwargs = [kwargs]

        for i in self.kwargs:

            match i['title']:
                case "Member Report": self.report()
                case "Member Support": self.support()

        return

    def report(self):

        self.add_item(InputText(label = "Member", placeholder= "Member Name"))
        self.add_item(InputText(label = "Uniform Resource Locator", style=d.InputTextStyle.long, required= True, placeholder= "https://google.com"))
        self.add_item(InputText(label = "Reason", style=d.InputTextStyle.long, required= False, placeholder= ""))
        self.embed.colour = d.Colour.dark_red()

        return

    def support(self):

        self.add_item(InputText(label = "Title Of The Document", placeholder= "eg. How To Use Commands", style=d.InputTextStyle.short))
        self.add_item(InputText(label = "Image", placeholder= "Member", style=d.InputTextStyle.short))
        self.add_item(InputText(label = "Challange", placeholder= "What do you need help with ?", style=d.InputTextStyle.long))
        self.embed.colour = d.Colour.dark_red()
        return

    async def callback(self, interaction:d.Interaction):

        for i in self.kwargs:

            match i['title']:
                case "Member Report": ch = utils.get(interaction.guild.text_channels, name = "report")
                case "Member Support":ch = utils.get(interaction.guild.text_channels, name = "support")


        try:

            if not ch: raise Exception(f"{ch} does not exists")

        except Exception as e:
     
            ch = utils.get(interaction.guild.channels, name = "auditlog")

             #   Prepare the embed message
            self.embed.description = f" {e}"
            self.embed.title = "An Exception Occured"
            self.embed.timestamp = datetime.datetime.now() 

            await ch.send(embed= self.embed)    #   Send the modal response

        else:

            #   Prepare the embed message
            self.embed.title = self.title
            self.embed.timestamp = datetime.datetime.now() 
            self.embed.set_author(name = f"Author: {interaction.user.name}")


            #   Prepare the user mode
            for i in range(len(self.children)): self.embed.add_field(name = self.children[i].label, value = self.children[i].value, inline= False)

            await interaction.response.defer()  #   Save the modal response
            await ch.send(embed= self.embed)    #   Send the modal response

        del ch, interaction
        return

class Channel(Modal):

    """
        Channel modals

        #   Author : krigjo25
        #   Date :   21.02-23
        #   Last update: 22.02-23

        #   Server announcements
        #   Create multiply channels
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.embed = d.Embed()
        self.kwargs = [kwargs]

        for i in self.kwargs:

            match i["title"]:
                case "Channel Announcement": self.announcement()
                case "Channel Creation": self.channel()

        return

    def announcement(self):

        self.add_item(InputText(label = "channel name", placeholder = "eg. announcement", style= d.InputTextStyle.short))
        self.add_item(InputText(label = "title", placeholder = "eg. announcement", style = d.InputTextStyle.short))
        self.add_item(InputText(label = "url", placeholder = "url", style = d.InputTextStyle.short, required = False,))
        self.add_item(InputText(label = "What would you like to announce?", placeholder = "Some text you would like to announce", style = d.InputTextStyle.long))

        return

    async def callback(self, interaction:d.Interaction):

        match self.title:
            case "Channel Announcement":

                modal = [{
                            "channel_name":self.children[0].value.lower(),
                            "announcement_title":self.children[1].value.capitalize(),
                            "announcement_url":self.children[2].value.lower(),
                            "announcement_message":self.children[3].value}]

                ch = utils.get(interaction.guild.channels, name = self.children[0].value)   #   Fetch the channel

                try:
                    if not ch: raise Exception("Channel does not exits")

                except Exception as e:

                    self.embed.title = "An Exception Occured"
                    self.embed.description = e

                    await interaction.response.send_message(embed=self.embed)
                    return

                else:
                    for i in modal:

                        self.embed.title = i["announcement_title"]
                        self.embed.set_author(name = f"by {interaction.user.name}")
                        if i["announcement_url"] != None: self.embed.url = i["announcement_url"]
                        self.embed.description = i["announcement_message"]
                    await ch.send(embed = self.embed)
                    await interaction.response.send_message("Message responded", delete_after=0.1)

                    return

        del interaction, modal#   Clearing some memory
        self.embed.clear_fields()
        self.embed.description = ""
        self.embed.remove_author()
        return

class Role(Modal):

    """
        Role modals

        #   Date :   21.02-23
        #   Last update: 22.02-23

        #   Create multiple roles
        #   Create multiply channels
        #   Role Deletion Confirmation 
    """