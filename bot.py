"""Telegram bot made for managing groups
   Made by Karlk and Gabriel"""

# IMPORTS
import logging
from peewee import *
from telegram.ext import *

from lib import Admin, commands
from config import botconfig

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)
db = SqliteDatabase('bot.db')
db.connect()
db.create_tables([Admin.Admin], safe=True)

def error():
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    # Define the updater
    updater = Updater(token=botconfig.bot_token)
    # Define the dispatcher
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("r", commands.restart))
    dp.add_handler(CommandHandler("start", commands.start))
    dp.add_handler(CommandHandler("id", commands.id))
    dp.add_handler(CommandHandler("roms", commands.aosip))
    dp.add_handler(CallbackQueryHandler(commands.callback))
    dp.add_handler(CommandHandler("rr", commands.rr))
    dp.add_handler(CommandHandler("cat", commands.cat))
    dp.add_handler(RegexHandler("Hola", commands.hola))
    dp.add_handler(CommandHandler("gapps", commands.gapps))
    dp.add_handler(CommandHandler("notificaciones", commands.notificaciones))
    dp.add_handler(CommandHandler("grupos", commands.grupos))
    dp.add_handler(CommandHandler("gcam", commands.gcam))
    dp.add_handler(CommandHandler("selinux", commands.selinux))
    dp.add_handler(CommandHandler("tuto", commands.roms))
    dp.add_handler(CommandHandler("logcat", commands.logcat))
    dp.add_handler(CommandHandler("magisk", commands.magisk))
    dp.add_handler(CommandHandler("twrp", commands.twrp))
    dp.add_handler(CommandHandler("scam", commands.scam))
    dp.add_handler(MessageHandler(Filters.entity("url"), commands.efbot))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, commands.new_user))
    dp.add_handler(CommandHandler("pin", commands.ancla))
    dp.add_handler(CommandHandler("di", commands.di))
    dp.add_handler(CommandHandler("ban", commands.ban))
    dp.add_handler(CommandHandler("kick", commands.kick))
    dp.add_handler(CommandHandler("unban", commands.unban))
    dp.add_handler(CommandHandler("del", commands.delete))
    dp.add_handler(CommandHandler("broadcast", commands.broadcast))
    dp.add_handler(CommandHandler("actualizar", commands.pull))
    dp.add_handler(MessageHandler(Filters.all, commands.puto))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()