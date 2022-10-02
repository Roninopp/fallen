from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "7217645"))
API_HASH = getenv("API_HASH", "78ba6352dd5cdc166fdef5aa84ba7c67")
BOT_TOKEN = getenv("BOT_TOKEN", "2100096282:AAG2c-iWRPsqoxbRFrioHYnFc5hYzKzhkRY")
BOT_NAME = getenv("BOT_NAME","Fantastic")
BOT_USERNAME = getenv("BOT_USERNAME", "fantasticfighterbot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Dushmanxronin")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "imperial_arena")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQDDH_N6wtFNKnifc6DfYf6DVhpiMu_CsYoH60CmJ147z5irv-J4-jID869dUPvK3BWms3W7UFPq8tcOXmu_JiJjrI2ILNHnQdmRPD07saD6uWsqWwstUmTS7DpginZFRNT9UgmpplK9EHhNogaBkw5OgV2T10wcPxso4huqabL1g0mOIoqBUHMQ2REfmIQ4euuwISK-Yk_yB19snhcAJR65K8toG4ngaTURJT-BHQbNpRd8P1r06VrB1nx_fuDxEKuVFVgM6VxauxGFdiQHwko4ZQ4mkmR8XiAPl6nAPiBQcRZ0zNObv4ehOtRAvZ5sr2AFHD0IJdIa7MjmNuS7efv9AAAAAUIrqz8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1793699293").split()))
