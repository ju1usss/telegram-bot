from telethon import TelegramClient, events
import re

api_id = 32122247
api_hash = "84e806980060e887c670f85b079a6903"

source_channel = "cnfansfindglobal"
target_channel = "@UsFansdrip"

affiliate_link = "https://www.usfans.com/register?ref=CKNBKZ"

client = TelegramClient("session", api_id, api_hash)

def polish_text(text):
    if not text:
        text = "🔥 Nowa okazja"

    text = re.sub(r"https?://\S+", affiliate_link, text)

    return f"""🔥 OKAZJA

{text}

💸 Link: {affiliate_link}
⏳ Sprawdź szybko!
"""

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    msg = event.message
    text = polish_text(msg.text)

    if msg.photo:
        await client.send_file(target_channel, msg.photo, caption=text)
    else:
        await client.send_message(target_channel, text)

print("Bot działa...")
client.start()
client.run_until_disconnected()
