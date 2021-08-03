#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

# pip3 install telethon==1.22.0

from telethon import TelegramClient, events, utils
import re
import logging.config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    bot_id = 1232234

    # telegram api
    api_id = 123123
    api_hash = '213123213213213'

    client = TelegramClient('telegram', api_id=api_id, api_hash=api_hash).start()
    @client.on(events.NewMessage(incoming=True, outgoing=True, chats=[-1001308315775]))
    async def forward_messages_handler(event):
        if re.search('https\:\/\/open\.ani-download\.workers\.dev.*\.mp4', event.message.text):
            url = re.search('https\:\/\/open\.ani-download\.workers\.dev.*\.mp4', event.message.text).group(0)
            logger.info(url)
            await  client.send_message(int(bot_id), str(url))

    try:
        client.run_until_disconnected()
    finally:
        client.disconnect()
