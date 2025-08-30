# ------------------------------ IMPORTS ---------------------------------
import logging
import os
from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client, filters as f

# --------------------------- LOGGING SETUP ------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("telegram").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# ---------------------------- CONSTANTS ---------------------------------
api_id = os.getenv("API_ID", "23212132")  # Fetch from environment variable
api_hash = os.getenv("API_HASH", "1c17efa86bdef8f806ed70e81b473c20")   # Fetch from environment variable

TOKEN = os.getenv("TOKEN" ,"7465073735:AAGOgUfMB5SALpbw1dWkb-swU8latLqK8zc")          # Fetch from environment variable

GLOG = os.getenv("GLOG", "moniclogs") # USERNAME ONLY
CHARA_CHANNEL_ID = os.getenv("CHARA_CHANNEL_ID", "moniclogs") #USERNAME ONLY
SUPPORT_CHAT_ID = os.getenv("SUPPORT_CHAT_ID", "moniclogs") #USERNAME ONLY

mongo_url = os.getenv("MONGO_URL", "mongodb+srv://ryumasgod:ryumasgod@cluster0.ojfkovp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Fetch from environment variable
PHOTO_URL = [
    os.getenv("PHOTO_URL_1", "https://files.catbox.moe/7ccoub.jpg"),
    os.getenv("PHOTO_URL_2", "https://files.catbox.moe/7ccoub.jpg")
]

SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/moniclogs")
UPDATE_CHAT = os.getenv("UPDATE_CHAT", "https://t.me/moniclogs")

SUDO = list(map(int, os.getenv("SUDO", "8429156335").split(',')))
OWNER_ID = int(os.getenv("OWNER_ID", "8429156335"))

# --------------------- TELEGRAM BOT CONFIGURATION -----------------------
command_filter = f.create(lambda _, __, message: message.text and message.text.startswith("/"))

application = Application.builder().token(TOKEN).build()
ZYRO = Client("Shivu", api_id=api_id, api_hash=api_hash, bot_token=TOKEN)

# -------------------------- DATABASE SETUP ------------------------------
ddw = AsyncIOMotorClient(mongo_url)
db = ddw['hinata_waifu']

# Collections
user_totals_collection = db['gaming_totals']
group_user_totals_collection = db['gaming_group_total']
top_global_groups_collection = db['gaming_global_groups']
pm_users = db['gaming_pm_users']
destination_collection = db['gamimg_user_collection']
destination_char = db['gaming_anime_characters']
# TEAMZYRO/__init__.py

char_power = {
    "Common": 10,
    "Rare": 25,
    "Epic": 50,
    "Legendary": 100,
    "Mythical": 200,
}

# -------------------------- GLOBAL VARIABLES ----------------------------
app = ZYRO
sudo_users = SUDO
collection = destination_char
user_collection = destination_collection

# --------------------------- STRIN ---------------------------------------
locks = {}
message_counters = {}
spam_counters = {}
last_characters = {}
sent_characters = {}
first_correct_guesses = {}
message_counts = {}
last_user = {}
warned_users = {}
user_cooldowns = {}
user_nguess_progress = {}
user_guess_progress = {}

# -------------------------- POWER SETUP --------------------------------
from TEAMZYRO.unit.zyro_ban import *
from TEAMZYRO.unit.zyro_sudo import *
from TEAMZYRO.unit.zyro_react import *
from TEAMZYRO.unit.zyro_log import *
from TEAMZYRO.unit.zyro_send_img import *
from TEAMZYRO.unit.zyro_rarity import *
# ------------------------------------------------------------------------

async def PLOG(text: str):
    await app.send_message(
       chat_id=GLOG,
       text=text
   )

# ---------------------------- END OF CODE ------------------------------
