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
	bot.send_message(chat_id=update.message.chat_id, text="Hola, soy un bot creado con python, para el grupo del leeco le pro 3 x722.", reply_to_message_id=update.message.message_id)

def mention(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=random.choice(["QUE QUIERE", "KI TI PASA","Supongo que llevaras razon....", "Estaba claro....", "Me vas a hacer llorar :(", "jaja", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]), reply_to_message_id=update.message.message_id)

def id(bot, update):
	chat_id = update.message.chat_id
	bot.send_message(chat_id=update.message.chat_id, text="ID: "+str(chat_id), reply_to_message_id=update.message.message_id)

def aosip(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*Puedes descargar ultima AOSIP pulsando *[AQUÍ](http://get.aosiprom.com/zl1).", parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

def x2(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*Puedes descargar la ultima AOSIP para tu Leeco Le Max 2 pulsado *[AQUÍ](https://get.aosiprom.com/x2/)", parse_mode=telegram.ParseMode.MARKDOWN)




def link(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='El link de este grupo es: https://t.me/joinchat/EXE9HESRmd4ihACntQbtoA', reply_to_message_id=update.message.message_id)

def gat(bot, update):
	bot.send_document(chat_id=update.message.chat_id, document=BQADBAADIQYAAmYu6VGU1rcuxJqDlAI )


def hola(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=random.choice(["Hola, cuanto tiempo :D", "Hola", "Eyyy", "Hacia mucho tiempo que no te veia", "Holaaa!!! Cuanto tiempo tio?!?!?!?!", "No tengo nada que decir jajaja"]), reply_to_message_id=update.message.message_id)

def gapps(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*Estas son las diferentes GAPPS que hay para android 8:* \n\n[MINDTHEGAPPS](http://downloads.codefi.re/jdcteam/javelinanddart/gapps/)\n\n[OPENGAPPS](http://opengapps.org/)\n\n[MICROG](https://microg.org/download.html)",parse_mode=telegram.ParseMode.MARKDOWN)

def notificaciones(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*Si tienes problemas con las notificaciones sigue* [ESTE TUTORIAL](http://telegra.ph/NO-PERDER-NOTIFICACIONES-EN-EUI-03-30).", parse_mode=telegram.ParseMode.MARKDOWN)

def grupos(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="*GRUPOS RELACIONADOS:*\n\n[72x](https://t.me/joinchat/CszTz0YaMuyR3MwBuzy-nw)\n\n[ALMACEN](http://T.me/AlmacenLeEco)\n\n[GCAM](https://t.me/joinchat/AAAAAEa6HOjwRaWAbI8-lQ)\n\n[LeecoIngles](https://t.me/leecolepro3roms)", parse_mode=telegram.ParseMode.MARKDOWN)

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


def creador(bot, update):
	text = update.message.text
	bot.send_message(chat_id=-1001150392798, text=(text))


def new_user(bot, update):
	message_texts = []
	for user in (update.message.new_chat_members or [update.message.from_user]):
		if not user.is_bot:
			user_name = user.first_name or user.last_name or user.username
			user_name = ", {}".format(user_name) if user_name else ""
			message_texts.append("¡Bienvenido{} al grupo!".format(user_name))
	if message_texts:
		bot.send_message(chat_id=update.message.chat_id, text='\n'.join(message_texts))




#COSAS DE PRUEBA QUE DAN ERRORES

# invalid(bot, update):
#	bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, prueba con otro", reply_to_message_id=update.message.message_id)



restart = CommandHandler("r", restart)
start = CommandHandler("start", start)
mention = MessageHandler(Filters.entity("mention"), mention)
botid = CommandHandler("id", id)
aosip = CommandHandler("aosip", aosip)
link = CommandHandler("link", link)
#invalid = MessageHandler(Filters.command, invalid)
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
creador = MessageHandler(Filters.chat(292633884), creador)
x2 = CommandHandler("x2", x2)
new_user = MessageHandler(Filters.status_update.new_chat_members, new_user)




dispatcher = updater.dispatcher





dispatcher.add_handler(restart)
dispatcher.add_handler(start)
dispatcher.add_handler(mention)
dispatcher.add_handler(botid)
dispatcher.add_handler(aosip)
#dispatcher.add_handler(invalid)
dispatcher.add_handler(link)
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
dispatcher.add_handler(creador)
dispatcher.add_handler(x2)
dispatcher.add_handler(new_user)




updater.start_polling()

updater.idle()

while True:
    pass
