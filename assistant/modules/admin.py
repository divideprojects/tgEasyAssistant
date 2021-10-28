# tgEasy Assistant, Assistant Bot and Example Bot from tgEasy
# Copyright (C) 2021 Jayant Hegde Kageri <https://github.com/jayantkageri/>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from assistant import app
from pyrogram.types import ChatPermissions
from tgEasy import get_user, is_admin


@app.command("ban", group_only=True)
async def ban(client, message):
    user = await get_user(message)
    if not user:
        return
    if await is_admin(message.chat.id, user.id, client):
        return
    try:
        await message.chat.kick_member(user.id)
        return await message.reply_text(f"{user.mention} has been Banned")
    except:
        return


@app.command("unban", group_only=True)
async def unban(client, message):
    user = await get_user(message)
    if not user:
        return
    if await is_admin(message.chat.id, message.from_user.id, client):
        return
    try:
        await message.chat.unban_member(user.id)
        return await message.reply_text(f"{user.mention} has been UnBanned")
    except:
        return


@app.command("kick", group_only=True)
async def kick(client, message):
    user = await get_user(message)
    if not user:
        return
    if await is_admin(message.chat.id, user.id, client):
        return
    try:
        await message.chat.kick_member(user.id)
        await message.chat.unban_member(user.id)
        await message.reply_text(f"{user.mention} has been Kicked")
    except:
        return


@app.command("mute", group_only=True)
async def mute(client, message):
    user = await get_user(message)
    if not user:
        return
    if await is_admin(message.chat.id, user.id, client):
        return
    try:
        await message.chat.restrict_member(user.id, ChatPermissions())
        await message.reply_text(f"{user.mention} has been Muted")
    except:
        return


@app.command("unmute", group_only=True)
async def unmute(client, message):
    user = await get_user(message)
    if not user:
        return
    if await is_admin(message.chat.id, user.id, client):
        return
    try:
        await message.chat.unban_member(user.id)
        await message.reply_text(f"{user.mention} has been UnMuted")
    except:
        return


@app.command("promote", group_only=True)
async def promote(client, message):
    user = await get_user(message)
    if not user:
        return
    if await is_admin(message.chat.id, user.id, client):
        return
    try:
        await message.chat.promote_member(
            user.id,
            can_change_info=True,
            can_restrict_members=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_promote_members=False
        )
        await message.reply_text(f"{user.mention} has been Promoted")
    except:
        return


@app.command("demote", group_only=True)
async def demote(client, message):
    user = await get_user(message)
    if not user:
        return
    if not await is_admin(message.chat.id, user.id, client):
        return
    try:
        await message.chat.demote_member(user.id)
        await message.reply_text(f"{user.mention} has been Demoted")
    except:
        pass


@app.command("kickme", group_only=True)
async def kickme(client, message):
    if await is_admin(message.chat.id, message.from_user.id, client):
        return
    try:
        await message.chat.kick_member(message.from_user.id)
        await message.chat.unban_member(message.from_user.id)
        await message.reply_text(f"As per the Wish of {message.from_user.mention}, They have been kicked.")
    except:
        return
