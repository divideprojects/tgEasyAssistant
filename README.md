# tgEasy Assistant

> The assistant bot that helps people with [tgEasy](//github.com/jayantkageri/tgEasy) directly on Telegram.

This repository contains the source code of [@tgEasyRobot](//t.me/tgEasyRobot) and the instructions for running a
copy yourself.
Feel free to explore the source code to
learn more about these topics.

## Requirements

- Python 3.8 or higher.
- A [Telegram API key](//docs.pyrogram.org/intro/setup#api-keys).
- A [Telegram bot token](//t.me/botfather).

## Run

1. `git clone https://github.com/DivideProjects/tgEasyAssistant`, to download the source code.
2. `cd tgEasyAssistant`, to enter the directory.
3. `python3 -m venv venv && . venv/bin/activate` to create and activate a virtual environment.
3. `pip install -U -r requirements.txt`, to install the requirements.
4. Create a new `.env` file, copy-paste the following and replace the values with your own:
   ```
   API_ID = 12345
   API_HASH = 0123456789abcdef0123456789abcdef
   BOT_TOKEN = 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
   ```
5. Run with `python -m assistant`.
6. Stop with <kbd>CTRL+C</kbd> and `deactivate` the virtual environment.

## License

GNU General Public Licence v3.0 Only, (C) 2021 [Jayant Hegde Kageri](//github.com/jayantkageri)