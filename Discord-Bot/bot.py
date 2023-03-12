import discord
import responses

async def send_message(message, user_message, is_private):
    
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
    

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
        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False) 
            
        if user_message[0] == "!":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)  
            
        #This sends the response the in the channel if there is no leading character to determine if the message needs to be private or not
        # else:
        #     await send_message(message, user_message, is_private=False)  
            

    
    client.run(TOKEN)