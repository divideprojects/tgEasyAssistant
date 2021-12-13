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

from kantex.html import *
from tgEasy.helpers import get_user_adv, handle_error

from .. import app


@app.command("info")
async def info(client, message):
    try:
        user = await get_user_adv(message)
        if not user:
            return
        last_name = f" {user.last_name}" if user.last_name else ""
        name = user.first_name + last_name
        username = f"@{user.username}" if user.username else ""
        info = Section(
            "User Information",
            f"Name: {name}",
            f"Username: {username}",
            f"User ID: {Code(user.id)}",
            f"User Link: {user.mention('link')}",
        )
        text = str(f"{info}\n")
        text += "\nUser is a Bot." if user.is_bot else ""
        text += "\nUser has been flagged for Scam." if user.is_scam else ""
        text += "\nUser has been flagged for impersonation." if user.is_fake else ""
        text += "\nUser has been Verified by Telegram." if user.is_verified else ""
        text += "\nUser is a part of Telegram Support Team." if user.is_support else ""
        await message.reply_text(text, disable_web_page_preview=True)
    except Exception as e:
        return await handle_error(message, e)


@app.command("id")
async def id(client, message):
    if message.reply_to_message and not message.reply_to_message.sender_chat:
        return await message.reply_text(Code(message.reply_to_message.from_user.id))
    return await message.reply_text(Code(message.chat.id))
