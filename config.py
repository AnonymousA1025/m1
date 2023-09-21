import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 19500615))
API_HASH = getenv("7ee1d55d072add75a01e617fc0cef635")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("6566651050:AAGiliKDNZwFiG2WioSyA22LlkQMG5aAfD0")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://anonxmusic:anonxmusic@anonx.9v4i8.mongodb.net/?retryWrites=true&w=majority", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1001924383730))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6620707125))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/PyAaditya/ZenPlay",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ZenBotx")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/QuirkySquad")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION1","BAEpjkcAjFhXDyCGrlAx2A_FsbmllTL6NmjK9XHfrlRBY9pE-o8R0LP8-YQOE_xZlOQdRyPCNgIblylITKvU81ZT4zvDZu6TU0q21HUVQ4HE4NxrlvQCnD7S67lerjjUNoYJHrzgCF-i1uUKaDyZ-RqKpzGbA0rpQEvSdBSJtObJm6Yduk2NeKmvoNoZnvtc6IBBxUQwkvsRkN3LrI8JIrrfTxuZV9yNCYLUR1ACSL6UYbqaytcKAEE5IWjF4UxYnRlWI3ow1UX5s5XVV9pgxbu4RwOo7szmbP7jofVUCoYpPLzKxcwu2o6ZWi8wlpn9YAcKTWKrfdaPbXWKPaU87bffGb7zkwAAAAFnrAFGAA")
STRING2 = getenv("STRING_SESSION2", "AQEpjkcARSNhjNIluzgEVn-b0f57Rzngfow93lUN19LgDmWe_ZAX7Vyr1mWpN18r1BzEHYd2u8ICs27dSDmlzbwxY6roDK0tLK5S2nnr3rVRvWhUAP2fHzBsL5Cq7LtJ7AccwkxfSRVnPp7QKEUvU6yxW3F_O0lN3VRVr8Zt1TXRo0olUQvmVHmYurY_eDWlHA2fui1gdqe0jq6skQUGHdWZVDqy0qh8dpiIUJfIJl9XBWnmzcWVv27_lZFui-RYA0ob2l4bnrKJXYOidiTpfcLTsB4WYD36-eusnoAKTyPySHli0UynU77zglqU62ecbkF3CecMh0AbnMMqzvYPi5_yGwCCPQAAAAFPPjo-AA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/25efe6aa029c6baea73ea.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
