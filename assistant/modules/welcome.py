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

import os
import re

from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified
from pyrogram.errors.exceptions.forbidden_403 import (ChatAdminRequired,
                                                      ChatWriteForbidden)
from pyrogram.methods.chats import get_chat_member
from pyrogram.types import ChatPermissions, Message
from pyrogram.types.messages_and_media import message
from tgEasy import handle_error, ikb, is_admin

from .. import app

WELCOME_TEXTS = {
    "CHAT_1001356758367": """
Welcome to the Support Group of [tgEasy](https://github.com/jayantkageri/tgEasy)

Important Rules:
    - No Spamming
    - No Promotions
    - No Spoonfeeding Users
    - No NSFW Contents

[GitHub](https://github.com/jayantkageri/tgEasy) | [PyPi](https://pypi.org/project/tgEasy/) | [Documentation](https://github.com/jayantkageri/tgEasy/wiki)
"""
}


async def chatWelcome(chatId: int):
    try:
        return WELCOME_TEXTS.get(f"CHAT_{str(chatId).replace('-', '')}")
    except:
        return None

@app.__client__.on_message(filters.new_chat_members)
async def welcome(client, message: Message):
    if not await is_admin(message.chat.id, (await client.get_me()).id, client):
        return
    for user in message.new_chat_members:
        if user.id == (await client.get_me()).id:
            return
        if user.is_bot:
            return
        try:
            if (await message.chat.get_member(user.id)).status == "restricted":
                return await message.reply_text(f"User {user.mention} was Restricted by admins and they tried to rejoin the chat.")
            replied = await message.reply_text(f"Hello {user.mention}! Please Click below Button to Confirm you are a Human", reply_markup=ikb([[["Confirm that you are a human", f"wlc_conf({user.id})"]]]))
            await message.chat.restrict_member(user.id, ChatPermissions())
        except ChatWriteForbidden:
            return await message.chat.leave()
        except (ChatAdminRequired, MessageNotModified):
            return await replied.delete()
        except BaseException as e:
            return await handle_error(e, message)


@app.callback("wlc_conf")
async def wlc_conf(client, cb):
    if not await is_admin(cb.message.chat.id, (await client.get_me()).id, client):
        return
    try:
        match = re.match(r"captcha\((.+?)\)", cb.data)
        if match:
            user_id = int(match.group(1))
            if not user_id == cb.from_user.id:
                if (await message.chat.get_member(cb.from_user.id)).status == "restricted":
                    return await cb.answer("You were Restricted by the admins, If you think this was a mistake then Contact the administrators.", show_alert=True)
                if (await message.chat.member(cb.from_user.id)).status in ["member", "administrator", "creator"]:
                    return await cb.answer("You can alredy talk freely, If you think you are smart then this Situation in handled.", show_alert=True)
        await cb.edit_message_reply_markup()
        if not await chatWelcome(cb.message.chat.id):
            await cb.message.chat.unban_member(cb.from_user.id)
            return await cb.message.delete()
        await cb.message.edit_text((await chatWelcome(cb.message.chat.id)), disable_web_page_preview=True, parse_mode="markdown")
        await cb.message.chat.unban_member(cb.from_user.id)
    except ChatWriteForbidden:
        return await cb.message.chat.leave()
    except (ChatAdminRequired, MessageNotModified):
        return await cb.message.delete()
    except Exception as e:
        try:
            await cb.edit_message_reply_markup()
        except:
            pass
        await cb.answer(f"{e}", show_alert=True)