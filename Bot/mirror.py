import os

from telethon.sessions import StringSession, SQLiteSession
from telethon.sync import TelegramClient
import config
from telethon import events


bot = TelegramClient(StringSession(), config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN)
client = TelegramClient(SQLiteSession(config.SESSION_STRING_CLIENT), config.API_ID, config.API_HASH)

all = []
file_path = os.path.abspath(Bot)
file_name = os.path.basename(file_path)
print('Starting Parsing:')
for channel in config.SOURCE_CHANNEL:
    @client.on(events.NewMessage(chats=channel, incoming=True))
    async def handler_new_message(event):
        global f
        try:
            print(event)
            print('\n\n\n\nStarting Parsing New Messages...\n...\n...\n.......\n')
            if event.message.message != None:
                #Sendind Parsed Message
                try:
                    f = await client.download_media(message=event.message)
                    await bot.send_message(config.TARGET_CHANNEL, event.message.message, file=f)
                except:
                    await bot.send_message(config.TARGET_CHANNEL, event.message.message)
            else:
                await bot.send_file(config.TARGET_CHANNEL, f)
            print('\n\n\nNEW MESSAGE SENT\n\n\n'
                  'WAITING FOR ANOTHER MESSAGE!\n')

        except Exception as e:
            print(e)

if __name__ == '__main__':
    bot.start()
    client.start()
    client.connect()
    bot.run_until_disconnected()
    client.run_until_disconnected()
