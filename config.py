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
SESSION_NAME = getenv("SESSION_NAME", "BQAPFt3O_5Y6VUo_1o9CeWMZVq0X14NSv8pCFbW6WoS8cY7g7lNcWT0CcMruwO03qHRoNM1SnntQN2xF_o-bkE8Csy1xpHeQZB7vTVNV6RqwUy5dtSl6fdE6LEfGC2xgBU03QPooBENnGBrWYhaAB2CeElJ6Se9aiv2CMcq3LNbi4zbmwo4EQEnlWsPYrqjlnKbnsnNBC1fNKEn1lEFV_PpWRuOxZ0Mwm0_3Cwx8rCEEUef35j1SEhKSPVdzih-dyUF2XorUdJTLuuUaiuJ-usVJbLZsukEroDjSgen_2HNyFxBJi4-PVyXoXje4chsiYV_rTfpou_akI-Qsn0t9EmWtAAAAAS3VP2UA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1793699293").split()))
