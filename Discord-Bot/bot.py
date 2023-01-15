import discord
import responses

def run_discord_bot():
    TOKEN = "MTA2NDA0OTI4NDA3MDI0ODUzOA.Gxsba1.myiCOMcq0tq2dsB4vRMIvb0S31xbbx7OD2ZP_U"
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said \"{user_message}\" ({channel})")
        
        #Takes the users message and slices the '?' from the beginning
        #For examples "?Help" => "Help"
        # if user_message[0] == "?":
        #     user_message = user_message[1:]   

    
    client.run(TOKEN)