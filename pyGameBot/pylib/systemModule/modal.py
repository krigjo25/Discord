#   Python responsories
import regex as re
import sys
import datetime

#   Discord responsory
import discord as d
from discord import utils, Colour
from discord.ui import InputText, Modal
from pylib.dictionaries.gameDictionaries import Philosopher

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
