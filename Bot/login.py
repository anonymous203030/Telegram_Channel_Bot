from telethon import TelegramClient
from telethon.sessions import StringSession
import config
with TelegramClient(StringSession(), config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN) as bot:
    print(bot.session.save())

with TelegramClient(StringSession(), config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN) as client:
    print(client.session.save())


# 1dc710c73f90ae85ee61b51c6f5e4bba39bbad75242a203d50bc2388e98418bf
# psql --dbname=d61nc0nbgsq65g --host=ec2-46-137-123-136.eu-west-1.compute.amazonaws.com --port=5432 -U yjqydwjrjcmydr -W
