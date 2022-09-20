from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "7217645"))
API_HASH = getenv("API_HASH", "78ba6352dd5cdc166fdef5aa84ba7c67")
BOT_TOKEN = getenv("BOT_TOKEN", "2100096282:AAEWuPQVLGtcR_csGOG2oZZYriTH3jlFlzg")
BOT_NAME = getenv("BOT_NAME","Fantastic")
BOT_USERNAME = getenv("BOT_USERNAME", "fantasticfighterbot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Dushmanxronin")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "imperial_arena")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQC7YeVY_dfntSCNJaDQl0IZiep5IbEIaiQZ3SOxFDQw3tv-doVV8d89qzQn7oo1kM0n7C_CEC_H1UAko02i3w5vHqQtxDgctu70rczR7-WYoyjy7RiGayatWHpyDcTUmVDV94K1-CL3jnuNGKcNjtGcPibOgqf4C166SJ_UsDCNz69T9WfmTpNZc1GUiQS1TFzIAe3PkDZL-S48FJOWvDR8KfvtPqzE8X9FVXXmVNynEVRiu9NmiX9gy5tQ8_-IYhifCw_1fQdYhlwjeoogAejwmYf0P5fI6QwFeSIbyvnLoTXfVOqBrOxnKQFzAE7MgGjOHLbMd5sKJchjEnAMO2J7AAAAAS3VP2UA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1793699293").split()))
