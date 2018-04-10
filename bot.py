import configparser
import os
import random
import sys
from functools import wraps
from threading import Thread

import telegram
from telegram.ext import *

config = configparser.ConfigParser()
config.read('token.txt')

bot = telegram.Bot(token=config['KEYS']['bot_api'])

updater = Updater(bot.token)
#Gather group ids to broadcast messages
CHAT_IDS_ES = [-1001074112167, -1001176122092, -1001150392798, -1001096142689]
# List of admins
LIST_OF_ADMINS = [37757673, 223502407, 292633884]
CHAT_IDS_ES_LEN = len(CHAT_IDS_ES) + 1

def restricted(func):
	@wraps(func)
	def wrapped(bot, update, *args, **kwargs):
		user_id = update.effective_user.id
		if user_id not in LIST_OF_ADMINS:
			bot.send_message(chat_id=update.message.chat_id, text="No tienes permiso para hacer eso.",
			                 reply_to_message_id=update.message.message_id)
			return
		return func(bot, update, *args, **kwargs)

	return wrapped

@restricted
def broadcast(bot, update):
	pass
	to_send = update.effective_message.text.split(None, 1)
	for x in range(0, CHAT_IDS_ES_LEN):
		bot.send_message(chat_id=CHAT_IDS_ES[x], text=to_send[1])


def stop_and_restart():
	updater.stop()
	os.execl(sys.executable, sys.executable, *sys.argv)


@restricted
def restart(bot, update):
	pass
	update.message.reply_text('El bot se esta reiniciando....')
	Thread(target=stop_and_restart).start()


def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
	                 text="*Comandos útiles:*\n\n/aosip - Ultima AOSIP\n\n/Gapps - Link para distintas GAPPS\n\n/gat - Fotos de gatos adorables xd\n\n/notificaciones - Sigue este tutorial si no te llegan notificaciones en EUI\n\n/grupos - Grupos que pueden ser de utilidad\n\n/gcam - ultima camara de google\n\n/selinux - Para cambiar a permisive etc\n\n/roms - Tutorial para instalar ROMS\n\n/logcat - Como hacer un logcat para que se puedan corregir esos errores\n\n/magisk - descargar magisk manager\n\n*SI QUIERES ENVIAR ALGUNA SUGERENCIA, CONTACTA CON* @KarloMoDZz *o* @Gabronog",
	                 parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)



def id(bot, update):
	chat_id = update.message.chat_id
	bot.send_message(chat_id=update.message.chat_id, text="ID: " + str(chat_id),
	                 reply_to_message_id=update.message.message_id)


def aosip(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
	                 text="🌐 *LINK PARA ULTIMA AOSIP:*\n├[🗂LEPRO3](http://get.aosiprom.com/zl1)\n└[🗂LEMAX2](http://get.aosiprom.com/x2)",
	                 parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

def cat(bot, update):
	bot.send_photo(chat_id=update.message.chat_id, photo=random.choice(
		['https://cdn2www.mundo.com/fotos/201504/Un-adorable-gato-disfrazado-de-conejo1-600x400.jpg',
		 "http://www.abc.es/media/sociedad/2018/03/10/miau-kJkG--1240x698@abc.jpg",
		 "https://i.pinimg.com/originals/3d/c0/ab/3dc0ab8e387f66f17a180d1bd89af055.jpg",
		 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoPyX7KJTVTz1CWdnhKd2hAXIA0XVLIBDkivXONvddGqa5eIwT",
		 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTn0klvfUNyZfHR3IBAWaPnpSFLj8be4KOkmxH1auaC_vuMGe3l",
		 "http://www.mujerhoy.com/multimedia/201710/30/media/gatos/12.jpg"]))


def hola(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=random.choice(
		["Hola, cuanto tiempo :D", "Hola", "Eyyy", "Hacia mucho tiempo que no te veia", "Adios",
		 "Holaaa!!! Cuanto tiempo tio?!?!?!?!", "No tengo nada que decir jajaja", "Hace mucho que no te veo."]),
	                 reply_to_message_id=update.message.message_id)



def gapps(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
	                 text="🌐*Estas son las diferentes GAPPS que hay para android 8:*\n├[💊OPENGAPPS](http://opengapps.org/)\n|\n├[💊MICROG](https://microg.org/download.html)\n|\n└[💊MindTheGapps](http://downloads.codefi.re/jdcteam/javelinanddart/gapps/)",
	                 parse_mode=telegram.ParseMode.MARKDOWN)


def notificaciones(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
	                 text="*Si tienes problemas con las notificaciones sigue* [ESTE TUTORIAL](http://telegra.ph/NO-PERDER-NOTIFICACIONES-EN-EUI-03-30).",
	                 parse_mode=telegram.ParseMode.MARKDOWN)


@restricted
def ban(bot, update):
	pass
	chat_id = update.message.chat_id
	bot.kick_chat_member(chat_id=chat_id, user_id=update.message.reply_to_message.from_user.id)
	bot.send_message(chat_id=chat_id, text="Baneado correctamente!", reply_to_message_id=update.message.message_id)


def grupos(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
	                 text="🌐*GRUPOS QUE TE PUEDEN INTERESAR:*\n\n🌐*LE PRO 3*\n├[📱LePro3](https://t.me/joinchat/CszTz0YaMuyR3MwBuzy-nw)\n├[📱LePro3x722](https://t.me/Leecox722)\n└[📱LePro3(Inglés)](https://t.me/leecolepro3roms)\n\n🌐*LE MAX 2*\n├[📱LeMax2AOSIP](https://t.me/AOSiP_x2)\n└[📱LeMax2INTERNACIONAL](https://t.me/lemax2xda)",
	                 parse_mode=telegram.ParseMode.MARKDOWN)

def gcam(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
	                 text="*PUEDES DESCARGAR LA CAMARA DE GOOGLE DESDE *[AQUÍ](https://www.celsoazevedo.com/files/android/google-camera)",
	                 parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

def selinux(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
	                 text="*SELinuxModeChanger v10.0, Para poner el telefono en PERMISIVO*\n\n\n*Puedes descargarlo desde* [AQUÍ](https://github.com/MrBIMC/SELinuxModeChanger/releases/download/10.0/app-release-v10.apk)",
	                 parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

def roms(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
	                 text="*TUTORIAL PARA INSTALAR ROMS, GRACIAS A CARLOS*\n\n*PUEDES VERLO *[AQUÍ](https://drive.google.com/open?id=1VXrKxWp4Kan4tvycnXhd0SR3npv3OwXT)",
	                 parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


def logcat(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
	                 text="*COMO HACER UN LOG*\n\n[AQUÍ](https://wiki.lineageos.org/logcat.html)",
	                 parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

def magisk(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
	                 text="*PUEDES DESCARGAR MAGISK DESDE *[AQUÍ](http://tiny.cc/latestmagisk)",
	                 parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


def kickthefbot(bot, update):
	bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.effective_user.id)
	bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
	bot.send_message(chat_id=update.message.chat_id, text="Eso no esta permitido.")


def new_user(bot, update):
	message_texts = []
	for user in (update.message.new_chat_members or [update.message.from_user]):
		if not user.is_bot:
			user_name = user.first_name or user.last_name or user.username
			user_name = ", {}".format(user_name) if user_name else ""
			message_texts.append("¡Bienvenid@{} ,al grupo de Leeco!".format(user_name))
	if message_texts:
		bot.send_message(chat_id=update.message.chat_id, text='\n'.join(message_texts))


@restricted
def ancla(bot, update):
	pass
	chat = update.effective_chat
	user = update.effective_user
	message = update.effective_message
	is_group = chat.type != "private" and chat.type != "channel"
	prev_message = update.effective_message.reply_to_message
	is_silent = True

	if prev_message and is_group:
		bot.pin_chat_message(chat_id=update.message.chat_id, message_id=prev_message.message_id)


# CommandHandler
restart = CommandHandler("r", restart)
start = CommandHandler("start", start)
botid = CommandHandler("id", id)
aosip = CommandHandler("aosip", aosip)
cat = CommandHandler("cat", cat)
hola = RegexHandler("Hola", hola)
gapps = CommandHandler("gapps", gapps)
noti = CommandHandler("notificaciones", notificaciones)
grupos = CommandHandler("grupos", grupos)
ban = CommandHandler("ban", ban)
gcam = CommandHandler("gcam", gcam)
selinux = CommandHandler("selinux", selinux)
roms = CommandHandler("roms", roms)
logcat = CommandHandler("logcat", logcat)
magisk = CommandHandler("magisk", magisk)
new_user = MessageHandler(Filters.status_update.new_chat_members, new_user)
ancla = CommandHandler("pin", ancla)
BROADCAST_HANDLER = CommandHandler("broadcast", broadcast)
kickthefbot = RegexHandler("http://tinyurl.com", kickthefbot)

dispatcher = updater.dispatcher

dispatcher.add_handler(restart)
dispatcher.add_handler(start)
dispatcher.add_handler(botid)
dispatcher.add_handler(aosip)
dispatcher.add_handler(cat)
dispatcher.add_handler(hola)
dispatcher.add_handler(gapps)
dispatcher.add_handler(noti)
dispatcher.add_handler(grupos)
dispatcher.add_handler(gcam)
dispatcher.add_handler(selinux)
dispatcher.add_handler(roms)
dispatcher.add_handler(logcat)
dispatcher.add_handler(magisk)
dispatcher.add_handler(kickthefbot)
dispatcher.add_handler(new_user)
dispatcher.add_handler(ancla)
dispatcher.add_handler(ban)
dispatcher.add_handler(BROADCAST_HANDLER)

updater.start_polling()

updater.idle()

while True:
	pass
