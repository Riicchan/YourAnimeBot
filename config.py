from discord import Color
from os import environ

TOKEN = None
INVITE = None

# URL Bases
ANILIST_BASE = "https://graphql.anilist.co"

# Colors
NORMAL_COLOR = Color.dark_theme()
ERROR_COLOR = Color.red()

# Emojis
YUI_SHY_EMOTE="<a:yui_shy:991749482763014184>"
ADULT_CONTENT_EMOTE="<:18_up:991930483309023352>"
BULLET_EMOTE="<:bullet:992560047978729512>"
DOT_EMOTE="<:dots:993535564835979357>"

def initialize_config_vars() -> str:
    global TOKEN, INVITE

    try:
        TOKEN = environ["TOKEN"]
        INVITE = environ["INVITE"]
    except Exception as e:
        return f"Error occurred while trying to cache Config Vars! \n{e}"
    else:
        return "Config Vars were cached successfully!"