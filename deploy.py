from pyrogram import Client

# Importer les variables de configuration depuis config.py
from config import API_ID, API_HASH, BOT_TOKEN

# Créer une instance du client Pyrogram
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Définir une fonction simple pour répondre à un message
@app.on_message()
def echo(client, message):
    message.reply_text(f"Vous avez dit : {message.text}")

# Lancer le bot
if __name__ == "__main__":
    print("Le bot est en cours d'exécution...")
    app.run()
