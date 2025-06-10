# Nayeo

This repository contains a simple Discord Text-To-Speech bot skeleton using [discord.py](https://discordpy.readthedocs.io/en/stable/).
Currently it only implements a `/ping` slash command that replies with `Pong!`.
The code is organised into the following folders:

- `config` – configuration helpers
- `commands/general` – general-purpose bot commands (e.g. `ping`)
- `tts` – TTS engine stubs

## Requirements

- Python 3.9+
- `ffmpeg` installed and accessible in the `PATH`
- Discord bot token with `message_content` intent enabled

Python dependencies are listed in `requirements.txt`.

## Running locally

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set the required environment variable and start the bot:

```bash
export DISCORD_TOKEN=YOUR_TOKEN
python bot.py
```

## Docker

You can build and run the bot using Docker:

```bash
docker build -t nayeo-bot .
docker run -e DISCORD_TOKEN=YOUR_TOKEN nayeo-bot
```

`ffmpeg` is installed in the container image.
