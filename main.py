from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


TOKEN: Final = '7647463833:AAFYUM42F4TOJlaJiU-cQEzpGmKKYSYv3kI'
BOT_USERNAME: Final = '@neakhubb_bot'

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am Neakhubb Bot. How can I assist you today?') # type: ignore

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am Neakhubb Bot. I can help you with various tasks. Just let me know how I can assist you!') # type: ignore

async def custom_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!') # type: ignore

# responces 
def handle_response(text: str) -> str:
    text = text.lower()

    if 'hello' in text:
        return 'Hello there! How can I help you?'
    elif 'how are you' in text:
        return 'I am just a bot, but I am doing great! Thanks for asking.'
    else:
        return 'Sorry, I did not understand that. Can you please rephrase?'
    

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text: str = str(update.message.text).lower()

    print(f'User: {update.message.chat.id} - {text}') 
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
        else:
            return 
        
    else:        
        response = handle_response(text)
        
    print(f'Bot: {response}')
    await update.message.reply_text(response) # type: ignore

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler('start', start_cmd))
    app.add_handler(CommandHandler('help', help_cmd))
    app.add_handler(CommandHandler('custom', custom_cmd))

    # Message handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handler
    app.add_error_handler(error)

    print('Bot is running...')
    app.run_polling(poll_interval=3)