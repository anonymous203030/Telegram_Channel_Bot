import tracemalloc

tracemalloc.start()
BOT_TOKEN = input('input bot token:\n')
API_ID = input('input api_id:\n')
API_HASH = input('input api_hash:\n')
SESSION_STRING_CLIENT = 'client'
SESSION_STRING_BOT = 'bot'


'''
    Input channels from which you want to parce content
'''
count = int(input('Input the count of channels u want to parse content'))
SOURCE_CHANNEL = []
for x in range(count):
    SOURCE_CHANNEL.append(str(input(f'Input {count + 1} channel: \n')))

"""
    Input channel into what u want to include content
"""
TARGET_CHANNEL = str(input('Input the channel where u want to include parsed content'))


