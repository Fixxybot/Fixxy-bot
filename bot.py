"""Telegram bot made for managing groups
   Made by Karlk and Gabriel"""

# IMPORTS
import logging
from telegram.ext import *

from lib import Db,handlers
from config import botconfig


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)
Db.main()


def error():
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    # Define the updater
    updater = Updater(token=botconfig.bot_token)
    # Add the dispatcher
    dp = updater.dispatcher
    # Handlers
    handlers.handlers(dp)
    # Start polling
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()