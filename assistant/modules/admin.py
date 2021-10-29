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
from pyrogram.types.messages_and_media import message
from tgEasy import get_user, is_admin


@app.command("ban", group_only=True)
@app.adminsOnly(permission="can_restrict_members")
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
@app.adminsOnly(permission="can_restrict_members")
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
@app.adminsOnly(permission="can_restrict_members")
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
@app.adminsOnly(permission="can_restrict_members")
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
@app.adminsOnly(permission="can_restrict_members")
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
@app.adminsOnly(permission="can_promote_members")
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
@app.adminsOnly(permission="can_promote_members")
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


@app.command("del", group_only=True)
@app.adminsOnly(permission="can_delete_messages")
async def delete(client, message):
    try:
        await message.delete()
        if message.reply_to_message:
            await message.reply_to_message.delete()
    except:
        pass


@app.command("purge", group_only=True)
@app.adminsOnly(permission="can_delete_messages")
async def purge(client, message):
    spurge = False
    if len(message.command) > 1:
        if "-s".lower() in message.command[1].lower():
            spurge = True
    messageIds = []
    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to show me where to purge from.")
    for ids in range(message.reply_to_message.message_id, message.message_id):
        messageIds.append(ids)
        if len(messageIds) == 100:
            try:
                await client.delete_messages(message.chat.id, messageIds, revoke=True)
                messageIds = []
            except:
                pass

        if len(messageIds) > 0:
            try:
                await client.delete_messages(message.chat.id, messageIds, revoke=True)
            except Exception as e:
                print(e)
                pass
    if not spurge:
        await client.send_message(message.chat.id, "Purge Complete.")
        return await message.delete()
    await message.delete()


@app.command("pin", group_only=True)
@app.adminsOnly(permission="can_pin_messages")
async def pin(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to pin it.")
    await message.reply_to_message.pin()
    await message.reply_text("Pinned.")


@app.command("unpin", group_only=True)
@app.adminsOnly(permission="can_pin_messages")
async def unpin(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to unpin it.")
    await message.reply_to_message.unpin()
    await message.reply_text("Unpinned.")


@app.command("unpinall", group_only=True)
@app.adminsOnly("can_pin_messages")
async def unpinall(client, message):
    await client.unpin_all_chat_messages(message.chat.id)
    await message.reply_text("All pinned messages have been unpinned.")
