import telegram
from telegram.ext import *
import logging
import random
import os
import sys
from threading import Thread

bot = telegram.Bot(token="TOKEN")

updater = Updater(bot.token)



def stop_and_restart():
	updater.stop()
	os.execl(sys.executable, sys.executable, *sys.argv)


def restart(bot, update):
	update.message.reply_text('El bot se esta reiniciando....')
	Thread(target=stop_and_restart).start()



def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*Comandos útiles:*\n\n/aosip - Ultima AOSIP\n\n/Gapps - Link para distintas GAPPS\n\n/gat - Fotos de gatos adorables xd\n\n/notificaciones - Sigue este tutorial si no te llegan notificaciones en EUI\n\n/grupos - Grupos que pueden ser de utilidad\n\n/gcam - ultima camara de google\n\n/selinux - Para cambiar a permisive etc\n\n/roms - Tutorial para instalar ROMS\n\n/logcat - Como hacer un logcat para que se puedan corregir esos errores\n\n/magisk - descargar magisk manager\n\n*SI QUIERES ENVIAR ALGUNA SUGERENCIA, CONTACTA CON* @KarloMoDZz *o* @Gabronog", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

def mention(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=random.choice(["QUE QUIERE", "KI TI PASA","Supongo que llevaras razon....", "Estaba claro....", "Me vas a hacer llorar :(", "jaja", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]), reply_to_message_id=update.message.message_id)

def id(bot, update):
	chat_id = update.message.chat_id
	bot.send_message(chat_id=update.message.chat_id, text="ID: "+str(chat_id), reply_to_message_id=update.message.message_id)

def aosip(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="🌐 *LINK PARA ULTIMA AOSIP:*\n├[🗂LEPRO3](http://get.aosiprom.com/zl1)\n└[🗂LEMAX2](http://get.aosiprom.com/x2)", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)



def gat(bot, update):
	bot.send_photo(chat_id=update.message.chat_id, photo=random.choice(['https://cdn2www.mundo.com/fotos/201504/Un-adorable-gato-disfrazado-de-conejo1-600x400.jpg', "http://www.abc.es/media/sociedad/2018/03/10/miau-kJkG--1240x698@abc.jpg", "https://i.pinimg.com/originals/3d/c0/ab/3dc0ab8e387f66f17a180d1bd89af055.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoPyX7KJTVTz1CWdnhKd2hAXIA0XVLIBDkivXONvddGqa5eIwT", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTn0klvfUNyZfHR3IBAWaPnpSFLj8be4KOkmxH1auaC_vuMGe3l", "http://www.mujerhoy.com/multimedia/201710/30/media/gatos/12.jpg"]))

def hola(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=random.choice(["Hola, cuanto tiempo :D", "Hola", "Eyyy", "Hacia mucho tiempo que no te veia", "adios", "Holaaa!!! Cuanto tiempo tio?!?!?!?!", "No tengo nada que decir jajaja"]), reply_to_message_id=update.message.message_id)

def gapps(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="🌐*Estas son las diferentes GAPPS que hay para android 8:*\n├[💊OPENGAPPS](http://opengapps.org/)\n|\n├[💊MICROG](https://microg.org/download.html)\n|\n└[💊MindTheGapps](http://downloads.codefi.re/jdcteam/javelinanddart/gapps/)",parse_mode=telegram.ParseMode.MARKDOWN)

def notificaciones(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*Si tienes problemas con las notificaciones sigue* [ESTE TUTORIAL](http://telegra.ph/NO-PERDER-NOTIFICACIONES-EN-EUI-03-30).", parse_mode=telegram.ParseMode.MARKDOWN)

def grupos(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="🌐*GRUPOS QUE TE PUEDEN INTERESAR:*\n\n🌐*LE PRO 3*\n├[📱LePro3](https://t.me/joinchat/CszTz0YaMuyR3MwBuzy-nw)\n├[📱LePro3x722](https://t.me/Leecox722)\n└[📱LePro3(Inglés)](https://t.me/leecolepro3roms)\n\n🌐*LE MAX 2*\n├[📱LeMax2AOSIP](https://t.me/AOSiP_x2)\n└[📱LeMax2INTERNACIONAL](https://t.me/lemax2xda)", parse_mode=telegram.ParseMode.MARKDOWN)

def gcam(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*PUEDES DESCARGAR LA CAMARA DE GOOGLE DESDE *[AQUÍ](https://www.celsoazevedo.com/files/android/google-camera)", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

def selinux(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*SELinuxModeChanger v10.0, Para poner el telefono en PERMISIVO*\n\n\n*Puedes descargarlo desde* [AQUÍ](https://github.com/MrBIMC/SELinuxModeChanger/releases/download/10.0/app-release-v10.apk)", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

def roms(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*TUTORIAL PARA INSTALAR ROMS, GRACIAS A CARLOS*\n\n*PUEDES VERLO *[AQUÍ](https://drive.google.com/open?id=1VXrKxWp4Kan4tvycnXhd0SR3npv3OwXT)", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

def logcat(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*COMO HACER UN LOG*\n\n[AQUÍ](https://wiki.lineageos.org/logcat.html)", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


def magisk(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*PUEDES DESCARGAR MAGISK DESDE *[AQUÍ](http://tiny.cc/latestmagisk)", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)





def new_user(bot, update):
	message_texts = []
	for user in (update.message.new_chat_members or [update.message.from_user]):
		if not user.is_bot:
			user_name = user.first_name or user.last_name or user.username
			user_name = ", {}".format(user_name) if user_name else ""
			message_texts.append("¡*Bienvenid@{} ,al grupo de Leeco!".format(user_name))
	if message_texts:
		bot.send_message(chat_id=update.message.chat_id, text='\n'.join(message_texts))

def ancla(bot, update):
	bot.pin_chat_message(chat_id=update.message.chat_id, message_id=update.message.message_id)










restart = CommandHandler("r", restart)
start = CommandHandler("start", start)
mention = MessageHandler(Filters.entity("mention"), mention)
botid = CommandHandler("id", id)
aosip = CommandHandler("aosip", aosip)
gat = CommandHandler("gat", gat)
hola = RegexHandler("Hola", hola)
gapps = CommandHandler("gapps", gapps)
noti = CommandHandler("notificaciones", notificaciones)
grupos = CommandHandler("grupos", grupos)
gcam = CommandHandler("gcam", gcam)
selinux = CommandHandler("selinux", selinux)
roms = CommandHandler("roms", roms)
logcat = CommandHandler("logcat", logcat)
magisk = CommandHandler("magisk", magisk)
new_user = MessageHandler(Filters.status_update.new_chat_members, new_user)
ancla = RegexHandler("Anclado:", ancla)




dispatcher = updater.dispatcher





dispatcher.add_handler(restart)
dispatcher.add_handler(start)
dispatcher.add_handler(mention)
dispatcher.add_handler(botid)
dispatcher.add_handler(aosip)
dispatcher.add_handler(gat)
dispatcher.add_handler(hola)
dispatcher.add_handler(gapps)
dispatcher.add_handler(noti)
dispatcher.add_handler(grupos)
dispatcher.add_handler(gcam)
dispatcher.add_handler(selinux)
dispatcher.add_handler(roms)
dispatcher.add_handler(logcat)
dispatcher.add_handler(magisk)
dispatcher.add_handler(new_user)
dispatcher.add_handler(ancla)





updater.start_polling()

updater.idle()

while True:
    pass
