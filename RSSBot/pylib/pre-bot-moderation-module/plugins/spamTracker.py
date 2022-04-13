"""Our subclass of AntiSpamTracker"""
import asyncio
import datetime
import typing
from copy import deepcopy

from discord.utils import get
from discord import Permissions, Member, Message

from antispam.dataclasses import Guild
from antispam.plugins import AntiSpamTracker
from antispam import MemberNotFound, GuildNotFound, MemberAddonNotFound

# noinspection DuplicatedCode
class SpamTracker(AntiSpamTracker):
    async def update_cache(self, message:Message, data: dict) -> None:
        """Override this so we can add a custom field to the stored user"""    

        member_id = message.author.id
        guild_id = message.guild.id
        timestamp = datetime.datetime.now(datetime.timezone.utc)

        try:
            member_data = await self.member_tracking.get_member_data(
                member_id, guild_id
            )
        except (MemberNotFound, GuildNotFound, MemberAddonNotFound):
            member_data = {"has_been_muted": False, "timestamps": []}

        member_data["timestamps"].append(timestamp)
        await self.member_tracking.set_member_data(member_id, guild_id, member_data)

    async def get_user_has_been_muted(self, message:Message) -> bool:
        """
        Returns if the user for the associated message
        has been muted yet or not.
        Parameters
        ----------
        message : Message
            The message from which to extract user
        Returns
        -------
        bool
            True if the user has been muted
            before else False
        Raises
        ------
        UserNotFound
            The User for the ``message`` could not be found
        """
        member_id = message.author.id
        guild_id = message.guild.id

        try:
            member_data = await self.member_tracking.get_member_data(
                member_id, guild_id
            )
        except GuildNotFound as e:
            raise MemberNotFound from e

        return member_data["has_been_muted"]

    async def do_punishment(self, message:Message, *args, **kwargs) -> None:
        """
        We do the punishment by checking ``self.is_spamming``.
        The first punishment is a mute, followed
        by the next punishment being removal from the guild
        Parameters
        ----------
        message : Message
            The message to get the attached user from
        Notes
        -----
        Simply does nothing if the member isn't found
        """
        if message.author.id == self.anti_spam_handler.bot.user.id:
            return None

        member = message.author
        svr = message.guild
        ch = message.channel
        member_id = message.author.id
        guild_id = message.guild.id
        try:
            Muted = await self.get_user_has_been_muted(message=message)
            member_data = await self.member_tracking.get_member_data(
                member_id, guild_id
            )
        except (GuildNotFound, MemberNotFound):
            return None

        if Muted:
            # User has been muted before, time to kick em
            await ch.send(f"{member.mention}, will be kicked from the server. ")
            await asyncio.sleep(2.5)
            await svr.kick(member, reason="Kicked for spam.")
            # cleanup on the assumption they won't 'just come back'
            await self.remove_punishments(message)

        elif await self.is_spamming(message=message):

            member_data["has_been_muted"] = True
            mutedRole = get(svr.roles, name='@Muted')
            memberRole = get(svr.roles, name='@Members')

            await self.member_tracking.set_member_data(member_id, guild_id, member_data)
            await ch.send(f"Greetings {member.mention}, you will be muted for 5 min.")

            if not mutedRole:
                overwrite = Permissions()
                overwrite.send_messages = False
                overwrite.speak = True
                overwrite.connect = True
                overwrite.read_messages=False
                overwrite.read_message_history = True
                Muted = await svr.create_role(name ='@Muted', permissions=overwrite)

            await member.add_roles(mutedRole, reason="Temp-muted for spam.")
            await member.remove_roles(memberRole)
            await asyncio.sleep(30)  # Mute for 5 minutes
            await member.add_roles(memberRole)
            await member.remove_roles(mutedRole, reason="Automatic un-mute.")
            # Dm a person
            await ch.send(
                f"Hey {member.mention}, the time has been passed, you will be unmuted, next consequence will be kick."
            )

    async def clean_cache(self) -> None:
        """Override this so if the has_been_muted field exists we don't remove them"""
        cache: typing.AsyncIterable[
            Guild
        ] = await self.anti_spam_handler.cache.get_all_guilds()

        async for guild in cache:
            for member in guild.members.values():
                await self.remove_outdated_timestamps(
                    member.addons[super().__class__.__name__],
                    member_id=member.id,
                    guild_id=guild.id,
                )

                member_data = await self.member_tracking.get_member_data(
                    member_id=member.id, guild_id=guild.id
                )
                if (
                    len(member_data["timestamps"]) == 0
                    and not member_data["has_been_muted"]
                ):
                    member.addons.pop(super().__class__.__name__)
                    await self.anti_spam_handler.cache.set_member(member)

    async def get_user_count(self, message: Message) -> int:
        if not isinstance(message, Message):
            raise TypeError("Expected message of type: Message")

        if not message.guild:
            raise MemberNotFound("Can't find user's from dm's")

        member_id = message.author.id
        guild_id = message.guild.id

        try:
            member_data = await self.member_tracking.get_member_data(
                member_id, guild_id
            )
        except (MemberNotFound, GuildNotFound):
            raise MemberNotFound from None

        await self.remove_outdated_timestamps(
            guild_id=guild_id, member_id=member_id, data=member_data["timestamps"]
        )

        member_data = await self.member_tracking.get_member_data(member_id, guild_id)

        return len(member_data["timestamps"])

    async def remove_outdated_timestamps(
        self, data: typing.List, member_id: int, guild_id: int
    ):
        current_time = datetime.datetime.now(datetime.timezone.utc)

        async def _is_still_valid(timestamp):
            difference = current_time - timestamp
            offset = datetime.timedelta(
                milliseconds=await self._get_guild_valid_interval(guild_id=guild_id)
            )

            if difference >= offset:
                return False
            return True

        current_timestamps = []

        member_data = await self.member_tracking.get_member_data(member_id, guild_id)

        for timestamp in member_data["timestamps"]:
            if await _is_still_valid(timestamp):
                current_timestamps.append(timestamp)

        member_data["timestamps"] = deepcopy(current_timestamps)
        await self.member_tracking.set_member_data(member_id, guild_id, member_data)