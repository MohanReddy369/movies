import re
from os import environ, getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#---------------------------------------------------------------
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '23398580'))
API_HASH = environ.get('API_HASH', 'b097227de20d589b49ed41d96d5bb29c')
BOT_TOKEN = environ.get('BOT_TOKEN', '8132314177:AAFTvL9OXlkv8-02ewCV_6jpahnM-hVbCgs')
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7660633418').split()]
USERNAME = environ.get('USERNAME', "https://t.me/@User_16437")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002393452878'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+dn2RdhYQUVA0Y2Q1')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', ' -1002456492253').split()]
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://jack:jack6231@jack.1dize.mongodb.net/?retryWrites=true&w=majority&appName=Jack")
DATABASE_NAME = environ.get('DATABASE_NAME', "Jack")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
#---------------------------------------------------------------
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-1002264665359'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/')
IS_VERIFY = is_enabled('IS_VERIFY', True)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")

#---------------------------------------------------------------
# Shortener links (Only keeping the second shortener active)
# SHORTENER_API = environ.get("SHORTENER_API", "4b97fdeb9fae9477d3050d7037085c0480bae4b4")
# SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'arolinks.com')
SHORTENER_API2 = environ.get("SHORTENER_API2", "4b97fdeb9fae9477d3050d7037085c0480bae4b4")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'arolinks.com')
# SHORTENER_API3 = environ.get("SHORTENER_API3", "")
# SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", '')

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

#---------------------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
STREAM_MODE = bool(environ.get('STREAM_MODE', True))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
ON_HEROKU = 'DYNO' in environ

SETTINGS = {
    'spell_check': SPELL_CHECK,
    'auto_filter': AUTO_FILTER,
    'file_secure': PROTECT_CONTENT,
    'auto_delete': AUTO_DELETE,
    'template': environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}'),
    'caption': environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}'),
    'tutorial': TUTORIAL,
    'shortner': SHORTENER_WEBSITE2,  # Only using the second shortener
    'api': SHORTENER_API2,  # Only using the second shortener
    'log': environ.get('LOG_VR_CHANNEL', '0'),
    'imdb': IMDB,
    'link': LINK_MODE,
    'is_verify': IS_VERIFY,
    'verify_time': TWO_VERIFY_GAP,
    'third_verify_time': THREE_VERIFY_GAP
}
