from telethon import TelegramClient
import os
import re

api_id = int(os.getenv(32122247)
api_hash = os.getenv(84e806980060e887c670f85b079a6903
affiliate_link = os.getenv(https://www.usfans.com/register?ref=CKNBKZ

source_channel = "cnfansfindglobal"
target_channel = "@UsFansdrip"

client = TelegramClient("session", api_id, api_hash)


def format_text(text):
    if not text:
        text = "🔥 Nowa okazja"

    text = re.sub(r"https?://\S+", affiliate_link, text)

    return f"""🔥 OKAZJA

{text}

👉 {affiliate_link}
"""


async def main():
    await client.start()

    messages = await client.get_messages(source_channel, limit=5)

    for msg in messages:
        text = format_text(msg.text)

        if msg.photo:
            await client.send_file(target_channel, msg.photo, caption=text)
        else:
            await client.send_message(target_channel, text)

    print("DONE")


with client:
    client.loop.run_until_complete(main())
