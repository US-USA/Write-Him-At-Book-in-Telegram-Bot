#import logging
import pyrogram
from pyrogram import Client, filters
                    
#Telegram Group: us7a5
# Set the bot token api_id api hash

app = Client(
        "BOTidSBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,

    )

# Telegram Group: us7a5
# start    
@app.on_message(pyrogram.filters.command("start"))
def start(client, message):
    first = message.from_user.first_name
    app.send_message(
        message.chat.id,
        text=f'''Hi {first},Send Text To Write Him At Book! \n\nGroup @us7a5 '''
        )

# Telegram Group: us7a5
# message
  
@app.on_message()
def get(client, message):
    client.send_message(
        message.chat.id,
        text="Wait Please."
    )

  
#Telegram Group: us7a5
#photo
  
    msg = message.text
    url = f'''http://apis.xditya.me/write?text={msg}'''
    client.send_photo(
        message.chat.id,
        url,
        caption="Done\n@us7a5"
    )

#//////////////////////#
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  
#level=logging.INFO)
#////////////////////#

  
#Telegram Group: us7a5
#print
  
print("done")

#Telegram Group: us7a5
#Run

app.run()
