from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN","7576028028:AAFbSQFeStfHVdbAyLrMuMgFqh-FhFMEjcs")
BOT_NAME = getenv("BOT_NAME"," Plus Music Bot🚩")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQDkVxgAVByicTqSuqnkTwrIFXhJLvMJ2pGwpPBP41HKkZuctVup5H-qR-IKxTxmT8jzIlhBYn4WWM_ZdBmroWAKBXxGSxstT5aTqupiN4KbYPj389PgMml4jSdosEq-HKM5j7_1azHDzhIYqnGiwX33FMGOQIRTIcLRwfa5NzFF7OqNZeZKLrGcDvbVX4iu62AezsHt3jATF6mVCs5Me2Yscr5a9auRQJ26rZM__NyeSte82BwywUxD0KndBE_sHNZeTn-w3csdaKO5rhC61A5CaDe00zgbFHjha74w2atXi0jrSu7DrUJdz37N0NibLdG8W3bncfY-ekEVZjuV52dJwrc2_wAAAAHOQYzfAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1805019557 5122474448").split()))
