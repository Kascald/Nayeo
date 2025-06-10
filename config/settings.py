import os


def get_token() -> str:
    """Return the Discord bot token from the environment."""
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN environment variable not set")
    return token


def get_channel_id() -> str | None:
    """Return the text channel ID the bot listens to, if set."""
    return os.getenv("CHANNEL_ID")


def get_model_path() -> str | None:
    """Return the ONNX model path for TTS, if set."""
    return os.getenv("MODEL_PATH")
