class Config(object):
    LOGGER = True
    
    API_ID = 25431765
    API_HASH = "f86261c85d80a06b9d5824f9186b7427"
    TOKEN = "7914858818:AAHAhVBtj0KHVmha7yK4ZdbntvWKfQMh904"  # Bot Token
    OWNER_ID = 123456789  # ← Apna Telegram user ID daal yahan
    
    SUPPORT_CHAT = "elivationn"  # Without @
    START_IMG = "https://telegra.ph/file/8a2395c0c5bc3e1797d1e.jpg"
    EVENT_LOGS = -1002598297381  # Log group
    
    MONGO_DB_URI = "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_URL = "postgresql://neondb_owner:npg_j6VxXRk2PiGq@ep-bold-frost-a10v7t7h-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"  # ElephantsQL or similar DB URI

    CASH_API_KEY = "cash_api_key_here"  # Can be from https://www.alphavantage.co
    TIME_API_KEY = "time_api_key_here"  # From https://timezonedb.com or similar
    
    BL_CHATS = [-1001234567890]  # Blacklisted groups
    DRAGONS = [123456789]  # High-level admins
    DEV_USERS = [123456789]  # Developer(s)
    DEMONS = []
    TIGERS = []
    WOLVES = []

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []  # List of modules to load
    NO_LOAD = []  # List of modules to skip
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
