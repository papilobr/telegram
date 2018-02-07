import telepot
import json

LOCATION = 'credentials/telegram.json'

# Load Telegram Credentials from LOCATION
with open(LOCATION) as data_file:
    DATA = json.load(data_file)



bot = telepot.Bot(DATA['token'])

print bot.getMe()

res = bot.getUpdates()

print res