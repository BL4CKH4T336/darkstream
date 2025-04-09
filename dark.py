# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import logging

# Your Telegram Bot Token
TOKEN = "8026705237:AAHIZvN-2k54QPTMVAGFnUDzZwk-ELde7lU"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat

    username = user.username or "N/A"
    first_name = user.first_name or ""
    last_name = user.last_name or ""
    full_name = (first_name + " " + last_name).strip()
    chat_id = chat.id

    message = (
        f"**User Details:**\n"
        f"Username: @{username}\n"
        f"Chat ID: `{chat_id}`\n"
        f"First Name: {first_name}\n"
        f"Last Name: {last_name}\n"
        f"Full Name: {full_name}"
    )

    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()
