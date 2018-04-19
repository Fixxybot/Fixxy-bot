
#IMPORTS
import configparser
import logging
import os
import random
import sys
import git
from functools import wraps
from threading import Thread

import telegram
from telegram.ext import *


config = configparser.ConfigParser()
config.read('token.txt')

bot = telegram.Bot(token=config['KEYS']['bot_api'])

logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.INFO)

updater = Updater(bot.token)
# Gather group ids to broadcast messages
CHAT_IDS_ES = [-1001074112167, -1001176122092, "@Leecox722", "@AOSiP_x2"]
# List of admins
LIST_OF_ADMINS = [37757673, 223502407, 292633884]
CHAT_IDS_ES_LEN = len(CHAT_IDS_ES)


def restricted(func):
	@wraps(func)
	def wrapped(bot, update, *args, **kwargs):
		user_id = update.effective_user.id
		if user_id not in LIST_OF_ADMINS:
			bot.send_message(chat_id=update.message.chat_id, text="No tienes permiso para hacer eso.", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
			return
		return func(bot, update, *args, **kwargs)

	return wrapped

@restricted
def broadcast(bot, update):
	pass
	to_send = update.effective_message.text.split(None, 1)
	for x in CHAT_IDS_ES:
		try:
			bot.send_message(chat_id=x, text=to_send[1], parse_mode=telegram.ParseMode.MARKDOWN)
		except:
			bot.send_message(chat_id=update.message.chat_id, text="*No he podido mandar el mensaje a *" +str(x), parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
@restricted
def di(bot, update):
	pass
	chat_id=update.effective_message.text.split(None, 1)
	to_send = update.effective_message.text.split(None, 2)
	try:
		bot.send_message(chat_id=chat_id[1], text=to_send[2])
		bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
	except:
		bot.send_message(chat_id=update.message.chat_id, text="*No he podido mandar el mensaje.*", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


def puto(bot, update):
	mensaje = update.message.text
	prohibido = ["Aguacate","Arroz","hola","Gabriel"]
	if mensaje in prohibido:
		bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)

def stop_and_restart():
	updater.stop()
	os.execl(sys.executable, sys.executable, *sys.argv)


@restricted
def restart(bot, update):
	pass
	update.message.reply_text('El bot se esta reiniciando....')
	Thread(target=stop_and_restart).start()

@restricted
def pull(bot, update):
	pass
	g = git.cmd.Git('~/leeco')
	g.pull()
	bot.send_message(chat_id=update.message.chat_id, text="*Actualizado*",
	                 parse_mode=telegram.ParseMode.MARKDOWN,
	                 reply_to_message_id=update.message.message_id)
	Thread(target=stop_and_restart).start()

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Comandos útiles:\n\n/aosip - Ultima AOSIP\n\n/Gapps - Link para distintas GAPPS\n\n/gat - Fotos de gatos adorables xd\n\n/notificaciones - Sigue este tutorial si no te llegan notificaciones en EUI\n\n/grupos - Grupos que pueden ser de utilidad\n\n/gcam - ultima camara de google\n\n/selinux - Para cambiar a permisive etc\n\n/roms - Tutorial para instalar ROMS\n\n/logcat - Como hacer un logcat para que se puedan corregir esos errores\n\n/magisk - descargar magisk manager\n\nSI QUIERES ENVIAR ALGUNA SUGERENCIA, CONTACTA CON @KarloMoDZz o @Gabronog", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

def id(bot, update):
	chat_id = update.message.chat_id
	chat = update.effective_chat
	user_id = update.effective_user.id
	is_group = chat.type != "private" and chat.type != "channel"
	if is_group:
	 bot.send_message(chat_id=update.message.chat_id, text="*ID del grupo:* " + str(chat_id) + "\n*Tu ID: *" + str(user_id), parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
	else:
		bot.send_message(chat_id=update.message.chat_id, text="Tu ID:" + str(chat_id))


def aosip(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
	                 text="🌐 *LINK PARA ULTIMA AOSIP:*\n├[🗂LEPRO3](http://get.aosiprom.com/zl1)\n└[🗂LEMAX2](http://get.aosiprom.com/x2)",
	                 parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


def cat(bot, update):
	bot.send_photo(chat_id=update.message.chat_id, photo=random.choice(
		["https://bit.ly/2JEJG3A","https://bit.ly/2v5Rb0r","https://bit.ly/2IK1s4k","https://bit.ly/2v4PIrg","https://bit.ly/2GPo6rp","https://bit.ly/2qnF3SU"]))


def hola(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=random.choice(
		["*Hola*, cuanto tiempo :D", "*Hola*", "Eyyy", "Hacia mucho tiempo que no te veia", "*Adios.*",
		 "*Holaaa*!!! Cuanto tiempo tio?!?", "No tengo nada que decir jajaja", "Hace mucho que no te veo."]), parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


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
	user_id = update.effective_message.text.split(None, 1)
	try:
		bot.kick_chat_member(chat_id=chat_id, user_id=update.message.reply_to_message.from_user.id)
		bot.send_message(chat_id=chat_id, text="*Baneado!*", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
	except:
		try:
			bot.kick_chat_member(chat_id=chat_id, user_id=user_id[1])
			bot.send_message(chat_id=chat_id, text="*Baneado!*", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
		except:
			bot.send_message(chat_id=chat_id, text="*No puedo hacer eso.*", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


@restricted
def kick(bot, update):
	pass
	chat_id = update.message.chat_id
	user = update.effective_message.text.split(None, 1)
	try:
		bot.kick_chat_member(chat_id=chat_id, user_id=update.message.reply_to_message.from_user.id)
		bot.unban_chat_member(chat_id=chat_id, user_id=update.message.reply_to_message.from_user.id)
		bot.send_message(chat_id=chat_id, text="*Expulsado!*", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
	except:
		try:
			bot.kick_chat_member(chat_id=chat_id, user_id=user[1])
			bot.unban_chat_member(chat_id=chat_id, user_id=user[1])
			bot.send_message(chat_id=chat_id, text="*Expulsado!*", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
		except:
			bot.send_message(chat_id=chat_id, text="Vaya, No puedo expulsar a ese usuario :(", reply_to_message_id=update.message.message_id)

@restricted
def unban(bot, update):
	pass
	chat_id = update.message.chat_id
	bot_id = [519150573,570971980,519150573]
	from_user_id = update.message.reply_to_message.from_user.id
	user = update.effective_message.text.split(None, 1)
	if from_user_id in bot_id:
		bot.send_message(chat_id=chat_id, text="Que intentas! xD", reply_to_message_id=update.message.message_id)
	else:
		try:
			bot.unban_chat_member(chat_id=chat_id, user_id=update.message.reply_to_message.from_user.id)
			bot.send_message(chat_id=chat_id, text="Desbaneado!", reply_to_message_id=update.message.message_id)
		except:
			try:
				bot.unban_chat_member(chat_id=chat_id, user_id=user[1])
				bot.send_message(chat_id=chat_id, text="*Desbaneado!", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
			except:
				bot.send_message(chat_id=chat_id, text="No puedo desbanear a ese usuario!", reply_to_message_id=update.message.message_id)
@restricted
def delete(bot, update):
	pass
	prev_message = update.effective_message.reply_to_message
	print(prev_message.message_id)
	if prev_message.message_id:
		try:
			bot.delete_message(chat_id=update.message.chat_id, message_id=prev_message.message_id)
			bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
		except:
			bot.send_message(chat_id=update.message.chat_id, text="*No tengo permisos!*", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

def twrp(bot, update):
	bot.forward_message(chat_id=update.message.chat_id, from_chat_id=292633884, message_id=2233)
	bot.forward_message(chat_id=update.message.chat_id, from_chat_id=292633884, message_id=2234)

def scam(bot, update):
	bot.forward_message(chat_id=update.message.chat_id, from_chat_id=292633884, message_id=2158)

def rr(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*Puedes descargar la ultima RR desde *[AQUÍ](https://sourceforge.net/projects/resurrectionremix-oreo/files/zl1/)", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)




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
	prohibited = ["http://tinyurl.com","https://t.me"]
	mensaje = update.message.text
	if mensaje in prohibited:
		try:
			bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.effective_user.id)
			bot.forward_message(chat_id=-1001122754147, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
			bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
			bot.send_message(chat_id=update.message.chat_id, text="Eso no esta permitido.")
		except:
			bot.send_message(chat_id=update.message.chat_id, text="*No puedo borrar el spam!*", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)





def new_user(bot, update):
	message_texts = []
	for user in (update.message.new_chat_members or [update.message.from_user]):
		if not user.is_bot:
			user_name = user.first_name or user.last_name or user.username
			user_name = ", {}".format(user_name) if user_name else ""
			message_texts.append("*¡Bienvenid@*{}*, al grupo!*".format(user_name))
	if message_texts:
		bot.send_message(chat_id=update.message.chat_id, text='\n'.join(message_texts), parse_mode=telegram.ParseMode.MARKDOWN)





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
		try:
			bot.pin_chat_message(chat_id=update.message.chat_id, message_id=prev_message.message_id)
		except:
			bot.send_message(chat_id=update.message.chat_id, text="*No puedo anclarlo!*", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)



























# CommandHandler
restart = CommandHandler("r", restart)
start = CommandHandler("start", start)
botid = CommandHandler("id", id)
aosip = CommandHandler("aosip", aosip)
rr = CommandHandler("rr", rr)
cat = CommandHandler("cat", cat)
hola = RegexHandler("Hola", hola)
gapps = CommandHandler("gapps", gapps)
noti = CommandHandler("notificaciones", notificaciones)
grupos = CommandHandler("grupos", grupos)
ban = CommandHandler("ban", ban)
di = CommandHandler("di", di)
kick = CommandHandler("kick", kick)
unban = CommandHandler("unban", unban)
dele = CommandHandler("del", delete)
gcam = CommandHandler("gcam", gcam)
selinux = CommandHandler("selinux", selinux)
roms = CommandHandler("roms", roms)
logcat = CommandHandler("logcat", logcat)
magisk = CommandHandler("magisk", magisk)
twrp = CommandHandler("twrp", twrp)
scam = CommandHandler("scam", scam)
new_user = MessageHandler(Filters.status_update.new_chat_members, new_user)
ancla = CommandHandler("pin", ancla)
BROADCAST_HANDLER = CommandHandler("broadcast", broadcast)
ACTUALIZANDO = CommandHandler("actualizar", pull)
kickthefbot = MessageHandler(Filters.entity("url"), kickthefbot)
puto = MessageHandler(Filters.all, puto)












dispatcher = updater.dispatcher

dispatcher.add_handler(restart)
dispatcher.add_handler(start)
dispatcher.add_handler(botid)
dispatcher.add_handler(aosip)
dispatcher.add_handler(rr)
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
dispatcher.add_handler(twrp)
dispatcher.add_handler(scam)
dispatcher.add_handler(kickthefbot)
dispatcher.add_handler(new_user)
dispatcher.add_handler(ancla)
dispatcher.add_handler(di)
dispatcher.add_handler(ban)
dispatcher.add_handler(kick)
dispatcher.add_handler(unban)
dispatcher.add_handler(dele)
dispatcher.add_handler(BROADCAST_HANDLER)
dispatcher.add_handler(ACTUALIZANDO)
dispatcher.add_handler(puto)

updater.start_polling()

updater.idle()

while True:
	pass
