
#   Python Repositories
from os import getenv
from sys import api_version

#   dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord.message import Message
from discord.ext.commands import Bot

#   pylib Repositories
from pylib.systemModule.databasePython import MariaDB

load_dotenv()

class DiscordBot(Bot):

    """
        Connecting to preferably database in MariaDB

        >   Creation Date   : 01.01-23
        >   Last update     :

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
    def __init__(self, command_prefix='?', help_command=None, description=None, owner_id = 340540581174575107, **options):
        super().__init__(command_prefix, help_command=help_command, description=description, owner_id = owner_id, **options)

    async def on_ready(self):

        #   Initialize a list of guilds
        svr = [i for i in self.guilds]

        #   Print API name and version
        print(f'Py-cord.py v{api_version} has been loaded')

        for i in svr: print(f'{self.user.name} has establized an connection to {i}')

        return

        
    async def on_message(self, message:Message):

    #   Procsess commands
        await self.process_commands(message)

        return
