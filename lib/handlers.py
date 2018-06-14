""""Bot handlers"""

from telegram.ext import *
from lib import commands, resources


def handlers(dp):
    dp.add_handler(CommandHandler("r", commands.restart))
    dp.add_handler(CommandHandler("start", commands.start))
    dp.add_handler(CommandHandler("id", commands.id))
    dp.add_handler(CommandHandler("roms", resources.aosip))
    dp.add_handler(CallbackQueryHandler(resources.callback))
    dp.add_handler(CommandHandler("cat", commands.cat))
    dp.add_handler(RegexHandler("Hola", commands.hola))
    dp.add_handler(CommandHandler("gapps", commands.gapps))
    dp.add_handler(CommandHandler("notificaciones", commands.notificaciones))
    dp.add_handler(CommandHandler("grupos", resources.grupos))
    dp.add_handler(CommandHandler("gcam", resources.gcam))
    dp.add_handler(CommandHandler("selinux", resources.selinux))
    dp.add_handler(CommandHandler("tuto", resources.roms))
    dp.add_handler(CommandHandler("logcat", resources.logcat))
    dp.add_handler(CommandHandler("magisk", resources.magisk))
    dp.add_handler(CommandHandler("twrp", resources.twrp))
    dp.add_handler(CommandHandler("scam", resources.scam))
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
    dp.add_handler(CommandHandler("promote", commands.add_admin))