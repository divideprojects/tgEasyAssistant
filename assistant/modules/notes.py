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
from kantex.html import *
from tgEasy.config import config


NOTES = {
    "CHAT_1001356758367": {
        "repo": "https://github.com/jayantkageri/tgEasy",
        "update": str(Code("pip install -U tgEasy")),
        "install": str(Code("pip install -U tgEasy")),
        "pypi": "https://pypi.org/project/tgEasy/",
        "pip": "https://pypi.org/project/tgEasy"
    }
}


async def get_note(chat_id, key):
    try:
        return NOTES.get(f"CHAT_{str(chat_id).replace('-', '')}").get(key)
    except (KeyError, ValueError, AttributeError):
        return None


@app.command("get")
async def get(client, message):
    reply_to = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    if not len(message.command) > 1:
        return await message.reply_text("Specify a Note to get.")
    if await get_note(message.chat.id, message.command[1]):
        return await message.reply_text(await get_note(message.chat.id, message.command[1].lower()), quote=True, disable_web_page_preview=True, reply_to_message_id=reply_to)
    return await message.reply_text("No such note found.")
