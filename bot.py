import discord
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Store processed message IDs to avoid duplicates
processed_messages = set()

@client.event
async def on_message(message):

    # Ignore bot messages
    if message.author.bot:
        return

    # Ignore webhook messages (n8n sends via webhook)
    if message.webhook_id:
        return

    # Ignore system messages
    if message.type != discord.MessageType.default:
        return

    # Prevent duplicate processing
    if message.id in processed_messages:
        return

    processed_messages.add(message.id)

    print("Processing message ID:", message.id)
    print("Message content:", message.content)

    data = {
        "message": message.content,
        "author": str(message.author),
        "channel": str(message.channel),
        "message_id": str(message.id)
    }

    try:
        response = requests.post(WEBHOOK_URL, json=data, timeout=5)
        print("Status Code:", response.status_code)
        print("Message sent to n8n Webhook!")
    except Exception as e:
        print("Failed to send to n8n:", e)

client.run(BOT_TOKEN)
