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
from tgEasy import Config


@app.command("start")
async def start(clinet, message):
    if message.chat.type == "supergroup":
        return await message.reply_text("Assistant Bot is Alive")
    else:
        text = Section(
            Link(label="tgEasy", url="https://github.com/jayantkageri/tgEasy"),
            "Assistant Robot for tgEasy",
            "",
            Link(label="Source Code",
                 url="https://github.com/DivideProjects/tgEasyAssistant")
        )
        return await message.reply_text(str(text), disable_web_page_preview=True)


@app.command("help")
async def help(client, message):
    text = Section(
        "Help.",
        Italic(
            f"Note: All commands can be used with the following: {Config.HANDLERS}"),
        SubSection(
            "Commands:",
            "/start - Starts the bot.",
            "/help - Shows this message.",
            "/donate - Shows information to Donate.",
            "/ban {handle/reply} - Bans the User - Admins Only.",
            "/unban {handle/reply} - UnBans the User - Admins Only.",
            "/mute {handle/reply} - Mutes the User - Admins Only.",
            "/unmute {handle/reply} - UnMutes the User - Admins Only.",
            "/kick {handle/reply} - Kicks the User - Admins Only.",
            "/kickme - Kicks the User who sent the Command.",
            "/info {handle/reply/none} - Shows Information about the User.",
            "/id - Shows the ID of Chat if not replied else the Replied User ID.",
            "/paste {reply to text/file} - Pastes the Content to Spacebin."
        ),
    )
    await message.reply_text(text)


@app.command("donate")
async def donate(clinet, message):
    text = f"""
Sorry, But Currently we aren't taking any Donations. Instead of Donating us you can donate to the Following Charities/Organizations

- {Link(url="https://donate.wikimedia.org/", label="Wikimedia Foundation")}
- {Link(url="https://donatenow.wfp.org/", label="World Food Programme")}
- {Link(url="https://help.unicef.org/", label="United Nations Children’s Fund")}
    """
    await message.reply_text(text, disable_web_page_preview=True)
