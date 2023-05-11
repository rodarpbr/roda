import os
from telegram import Bot

bot = Bot(token=os.environ.get('6094672033:AAGFGz1P2NtYz-lBlutjDXmOo5GEnu2Zyds'))
import logging
from telegram.ext import Updater, CommandHandler
from telegram import Update
from telegram.ext import CallbackContext


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='daniel, seu otário')

def main():
    updater = Updater(token='6094672033:AAGFGz1P2NtYz-lBlutjDXmOo5GEnu2Zyds', use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
