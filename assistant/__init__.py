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

from pyrogram import Client
from tgEasy import tgClient
from tgEasy.config import config

client = Client(
    "assistant",
    api_id=config("API_ID"),
    api_hash=config("API_HASH"),
    bot_token=config("BOT_TOKEN"),
    plugins={"root": "assistant/modules"},
)
client.set_parse_mode("html")
app = tgClient(client)
