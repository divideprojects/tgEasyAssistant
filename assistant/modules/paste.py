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

import aiohttp
from pyrogram import Client, filters

from .. import app


@app.command("paste")
async def paste_bin(client, message):
    statusMsg = await message.reply_text("Pasting to Spacebin, Please wait for a while...")
    content = None
    extension = "txt"
    if len(message.command) > 1:
        # TODO: Make a way to get the extension
        if message.command[1].startswith("py"):
            extension = "python"
        if message.command[1].startswith("js"):
            extension = "javascript"
        if message.command[1].startswith("ts") or message.command[1].startswith("typescript"):
            extension = "typescript"
        if message.command[1].startswith("go"):
            extension = "go"
        if message.command[1].startswith("java"):
            extension = "java"
        if message.command[1].startswith("crystal") or message.command[1].startswith("cr"):
            extension = "crystal"
        if message.command[1].startswith("c") or message.command[1].startswith("objc"):
            extension = "c"
        if message.command[1].startswith("json") or message.command[1].startswith("yaml") or message.command[1].startswith("toml"):
            extension = "json"
        if message.command[1].startswith("markdown") or message.command[1].startswith("md"):
            extension = "markdown"
        if message.command[1].startswith("html") or message.command[1].startswith("css") or message.command[1].startswith("xml"):
            extension = "markup"
        if message.command[1].startswith("css"):
            extension = "css"
        if message.command[1].startswith("bash") or message.command[1].startswith("sh"):
            extension = "bash"
        if message.command[1].startswith("rust") or message.command[1].startswith("rs"):
            extension = "rust"
        if message.command[1].startswith("ruby") or message.command[1].startswith("rb"):
            extension = "ruby"
        if message.command[1].startswith("php"):
            extension = "php"

    if message.reply_to_message:
        if message.reply_to_message.document:
            if message.reply_to_message.document.file_size > 600000:
                return await statusMsg.edit_text("Max file size that can be pasted is 600KB.")
            uniqueId = f"paste_{message.from_user.id}_{message.message_id}"
            file_ = await message.reply_to_message.download(uniqueId)
            with open(file_, 'rb') as f:
                content = f.read().decode("UTF-8")
            os.remove(file_)
        else:
            try:
                content = message.reply_to_message.text.markdown
            except:
                pass

    if not content:
        return await statusMsg.edit_text("Reply to a Text or Document to Paste.")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://spaceb.in/api/v1/documents/",
                json={"content": content, "extension": extension},
                timeout=3
            ) as response:
                key = (await response.json())["payload"].get("id")
                url = f"Spacebin Denied the Paste \n{await response.json()}"
                if key:
                    url = f"https://spaceb.in/{key}"
    except Exception as e:
        return await statusMsg.edit_text(str(e))
    await statusMsg.edit_text(url, disable_web_page_preview=True)
