import discord
import responses


# send_message helper function
async def send_message(message, user_message):
    try:
        response = responses.handle_responses(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


# runs discord bot in main function
def run_discord_bot():
    TOKEN = "YOUR_TOKEN"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} starting...")

    @client.event
    async def on_message(message):
        # ensures Bot does not get stuck in infinite loop
        if message.author == client.user:
            return

        # assign the contents of the message to user_message
        user_message = str(message.content)

        await send_message(message, user_message)

    client.run(TOKEN)
