# IMPORTS
import configparser
import logging
import os
import random
import sys
from functools import wraps
from threading import Thread
import git

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


def test(bot, update):
    test1 = bot.sendDocument(chat_id=update.message.chat_id, document="BQADBAADiwQAArffKVMaFJv2M4D-UQI")
    test2 = bot.sendDocument(chat_id=update.message.chat_id, document="BQADBAADjQQAArffKVMb20GYGes-CwI")
    print(test1, test2)


def restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            bot.send_message(chat_id=update.message.chat_id, text="No tienes permiso para hacer eso.",
                             parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
            return
        return func(bot, update, *args, **kwargs)

    return wrapped


def get_admin_ids(bot, chat_id):
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]


@restricted
def broadcast(bot, update):
    pass
    to_send = update.effective_message.text.split(None, 1)
    for x in CHAT_IDS_ES:
        try:
            bot.send_message(chat_id=x, text=to_send[1], parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            bot.send_message(chat_id=update.message.chat_id, text="*No he podido mandar el mensaje a *" + str(x),
                             parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


@restricted
def di(bot, update):
    pass
    chat_id = update.effective_message.text.split(None, 1)
    to_send = update.effective_message.text.split(None, 2)
    try:
        bot.send_message(chat_id=chat_id[1], text=to_send[2])
        bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    except:
        bot.send_message(chat_id=update.message.chat_id, text="*No he podido mandar el mensaje.*",
                         parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


def puto(bot, update):
    mensaje = update.message.text
    recibe = mensaje.upper()
    if "PUTO" in recibe:
        bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    if "MEJOR ROM" in recibe:
        bot.send_message(chat_id=update.message.chat_id, text="*No hay ninguna rom mejor que otra .-.*",
                         parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


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
    print("x")


def id(bot, update):
    chat_id = update.message.chat_id
    chat = update.effective_chat
    user_id = update.effective_user.id
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    code = update.message.from_user.language_code
    is_bot = update.message.from_user.is_bot
    is_group = chat.type != "private" and chat.type != "channel"
    # if is_group:
    bot.send_message(chat_id=update.message.chat_id,
                     text="*ID del grupo:* " + str(chat_id) + "\n*Tu ID: *" + str(user_id) + "\nUsername: @" + str(
                         username) + "\nNombre: " + str(first_name) + "\nApellido: " + str(
                         last_name) + "\nLenguaje:" + str(code) + "\nBot: " + str(is_bot),
                     parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
    # else:
    bot.send_message(chat_id=update.message.chat_id, text="Tu ID:" + str(chat_id))


def aosip(bot, update):
    bot.sendMessage(
        update.message.chat_id,
        '🔽🔽 *ROMs PARA LePro3 y LeMax2* 🔽🔽', parse_mode=telegram.ParseMode.MARKDOWN,
        reply_markup=telegram.InlineKeyboardMarkup(
            [
                [telegram.InlineKeyboardButton('🔽📲LePro3🔽', callback_data='LePro3'),
                 telegram.InlineKeyboardButton("🔽📲LeMax2🔽", callback_data='LeMax2')],
                [telegram.InlineKeyboardButton('🔽📲x720🔽', callback_data="x720"),
                 telegram.InlineKeyboardButton("🔽📲x722🔽", callback_data='X722'),
                 telegram.InlineKeyboardButton("🔽x820🔽", callback_data='x820'),
                 telegram.InlineKeyboardButton("🔽x829🔽", callback_data='x829')],
                [telegram.InlineKeyboardButton('🗂AOSiP', url='http://get.aosiprom.com/zl1'),
                 telegram.InlineKeyboardButton("🗂AOSiP", url='http://get.aosiprom.com/x2')],
                [telegram.InlineKeyboardButton('🗂AOKP', url="google.es"),
                 telegram.InlineKeyboardButton("🗂AICP", url='http://dwnld.aicp-rom.com/?device=x2')],
                [telegram.InlineKeyboardButton('🗂AEX', url='https://androidfilehost.com/?w=files&flid=261896'),
                 telegram.InlineKeyboardButton("🗂DirtyUnicorns", url="google.es")],
                [telegram.InlineKeyboardButton('🗂LineageOS', url='https://download.lineageos.org/zl1'),
                 telegram.InlineKeyboardButton("🗂LineageOS", url='https://download.lineageos.org/x2')],
                [telegram.InlineKeyboardButton('🗂AICP', url='http://dwnld.aicp-rom.com/?device=zl1'),
                 telegram.InlineKeyboardButton("🗂AEX", url='https://downloads.aospextended.com/x2')],
                [telegram.InlineKeyboardButton('❌"', callback_data='Hueco8'),
                 telegram.InlineKeyboardButton("🗂PixelExperience", url='https://download.pixelexperience.org/x2/')],
                [telegram.InlineKeyboardButton("Cerrar menú", callback_data="Cerrar")]
            ]
        )
    )


def callback(bot, update):
    query = update.callback_query
    if update.callback_query.data == 'LePro3':
        bot.answer_callback_query(update.callback_query.id, text='ROMs para el LeEco LePro3', show_alert=True)
    if update.callback_query.data == 'LeMax2':
        bot.answer_callback_query(update.callback_query.id, text='ROMs para el LeEco LeMax2', show_alert=True)
    if update.callback_query.data == "X720":
        bot.answer_callback_query(update.callback_query.id,
                                  text="En este lado las roms para la version x720, si esta en medio, es que es compatible con las 2 versiones",
                                  show_alert=True)
    if update.callback_query.data == 'X722':
        bot.answer_callback_query(update.callback_query.id,
                                  text="En este lado las ROMs para la version x722, si esta en medio, es que es compatible para las 2 versiones",
                                  show_alert=True)
    if update.callback_query.data == 'x820':
        bot.answer_callback_query(update.callback_query.id,
                                  text="En este lado las ROMs para la version x820, si esta en medio, es que es compatible para las 2 versiones",
                                  show_alert=True)
    if update.callback_query.data == 'x829':
        bot.answer_callback_query(update.callback_query.id,
                                  text="En este lado las ROMs para la version x829, si esta en medio, es que es compatible para las 2 versiones",
                                  show_alert=True)
    if update.callback_query.data == 'Hueco8':
        bot.answer_callback_query(update.callback_query.id, text="*HUECO VACÍO*\n *¡PON AQUÍ TU ROM!", show_alert=True)
    if update.callback_query.data == "Cerrar":
        bot.edit_message_text(text="❌", chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    if update.callback_query.data == "Le3":
        bot.edit_message_text(text="Selecciona tu version: ", chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              reply_markup=telegram.InlineKeyboardMarkup(
                                  [
                                      [telegram.InlineKeyboardButton('📲x720', callback_data='720'),
                                       telegram.InlineKeyboardButton("📲X722", callback_data='722')],
                                      [telegram.InlineKeyboardButton("◀️Volver atrás", callback_data="Atrás")]
                                  ]
                              )
                              )
    if update.callback_query.data == "720":
        bot.edit_message_text(text="TWRP para el 720:", chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
        bot.sendDocument(chat_id=query.message.chat_id, document="BQADBAADiwQAArffKVMaFJv2M4D-UQI")
    if update.callback_query.data == "722":
        bot.edit_message_text(text="TWRP para el 722:", chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
        bot.sendDocument(chat_id=query.message.chat_id, document="BQADBAADjQQAArffKVMb20GYGes-CwI")
    if update.callback_query.data == "Atrás":
        bot.edit_message_text(text="Selecciona tu version: ", chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              reply_markup=telegram.InlineKeyboardMarkup(
                                  [
                                      [telegram.InlineKeyboardButton('📲LePro3', callback_data='Le3'),
                                       telegram.InlineKeyboardButton("📲LeMax2", callback_data='Le2')],
                                      [telegram.InlineKeyboardButton("❌Cerrar menú", callback_data="Cerrar")]
                                  ]
                              )
                              )


def cat(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=random.choice(
        ["https://bit.ly/2JEJG3A", "https://bit.ly/2v5Rb0r", "https://bit.ly/2IK1s4k", "https://bit.ly/2v4PIrg",
         "https://bit.ly/2GPo6rp", "https://bit.ly/2qnF3SU"]))


def hola(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=random.choice(
        ["*Hola*, cuanto tiempo :D", "*Hola*", "Eyyy", "Hacia mucho tiempo que no te veia",
         "*Holaaa*!!! Cuanto tiempo tio?!?", "Hace mucho que no te veo."]), parse_mode=telegram.ParseMode.MARKDOWN,
                     reply_to_message_id=update.message.message_id)


def gapps(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="🌐*Estas son las diferentes GAPPS que hay para android 8(oreo):*\n├[💊OPENGAPPS](http://opengapps.org/)\n|\n├[💊MICROG](https://microg.org/download.html)\n|\n└[💊MindTheGapps](http://downloads.codefi.re/jdcteam/javelinanddart/gapps/)",
                     parse_mode=telegram.ParseMode.MARKDOWN)


def notificaciones(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="*Si tienes problemas con las notificaciones sigue* [ESTE TUTORIAL](http://telegra.ph/NO-PERDER-NOTIFICACIONES-EN-EUI-03-30).",
                     parse_mode=telegram.ParseMode.MARKDOWN)


def ban(bot, update):
    chat_id = update.message.chat_id
    chat = update.effective_chat
    is_group = chat.type != "private" and chat.type != "channel"
    if is_group:
        if update.message.from_user.id in get_admin_ids(bot, update.message.chat_id):
            user_id = update.effective_message.text.split(None, 1)
            if update.message.reply_to_message:
                prev_user = update.message.reply_to_message.from_user.id
                if prev_user:
                    try:
                        bot.kick_chat_member(chat_id=chat_id, user_id=prev_user)
                        bot.send_message(chat_id=chat_id, text="*Baneado!*", parse_mode=telegram.ParseMode.MARKDOWN,
                                         reply_to_message_id=update.message.message_id)
                    except:
                        bot.send_message(chat_id=chat_id, text="*No puedo banear administradores.*",
                                         parse_mode=telegram.ParseMode.MARKDOWN,
                                         reply_to_message_id=update.message.message_id)
                else:
                    bot.send_message(chat_id=chat_id, text="*No has referido ningun usuario.*",
                                     parse_mode=telegram.ParseMode.MARKDOWN,
                                     reply_to_message_id=update.message.message_id)
            else:
                try:
                    if user_id[1]:
                        try:
                            bot.kick_chat_member(chat_id=chat_id, user_id=user_id[1])
                            bot.send_message(chat_id=chat_id, text="*Baneado!*", parse_mode=telegram.ParseMode.MARKDOWN,
                                             reply_to_message_id=update.message.message_id)
                        except:
                            bot.send_message(chat_id=chat_id, text="*No puedo banear admins.*",
                                             parse_mode=telegram.ParseMode.MARKDOWN,
                                             reply_to_message_id=update.message.message_id)
                except:
                    bot.send_message(chat_id=chat_id,
                                     text="*Mal ejecutado, responde a un mensaje, o utiliza:*\n*/ban <user_id>.*",
                                     parse_mode=telegram.ParseMode.MARKDOWN,
                                     reply_to_message_id=update.message.message_id)
        else:
            bot.send_message(chat_id=chat_id, text="*No eres admin, y me estas diciendo lo que tengo que hacer -.-.*",
                             parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
    else:
        bot.send_message(chat_id=chat_id, text="*Comando solo válido para grupos.*",
                         parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


@restricted
def kick(bot, update):
    pass
    chat_id = update.message.chat_id
    user = update.effective_message.text.split(None, 1)
    try:
        bot.kick_chat_member(chat_id=chat_id, user_id=update.message.reply_to_message.from_user.id)
        bot.unban_chat_member(chat_id=chat_id, user_id=update.message.reply_to_message.from_user.id)
        bot.send_message(chat_id=chat_id, text="*Expulsado!*", parse_mode=telegram.ParseMode.MARKDOWN,
                         reply_to_message_id=update.message.message_id)
    except:
        try:
            bot.kick_chat_member(chat_id=chat_id, user_id=user[1])
            bot.unban_chat_member(chat_id=chat_id, user_id=user[1])
            bot.send_message(chat_id=chat_id, text="*Expulsado!*", parse_mode=telegram.ParseMode.MARKDOWN,
                             reply_to_message_id=update.message.message_id)
        except:
            bot.send_message(chat_id=chat_id, text="Vaya, No puedo expulsar a ese usuario :(",
                             reply_to_message_id=update.message.message_id)


@restricted
def unban(bot, update):
    pass
    chat_id = update.message.chat_id
    bot_id = [519150573, 570971980, 519150573]
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
                bot.send_message(chat_id=chat_id, text="*Desbaneado!", parse_mode=telegram.ParseMode.MARKDOWN,
                                 reply_to_message_id=update.message.message_id)
            except:
                bot.send_message(chat_id=chat_id, text="No puedo desbanear a ese usuario!",
                                 reply_to_message_id=update.message.message_id)


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
            bot.send_message(chat_id=update.message.chat_id, text="*No tengo permisos!*",
                             parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


def twrp(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Selecciona tu dispositivo: ",
                     parse_mode=telegram.ParseMode.MARKDOWN,
                     reply_markup=telegram.InlineKeyboardMarkup(
                         [
                             [telegram.InlineKeyboardButton('📲LePro3', callback_data='Le3'),
                              telegram.InlineKeyboardButton("📲LeMax2", callback_data='Le2')],
                             [telegram.InlineKeyboardButton("❌Cerrar menú", callback_data="Cerrar")]
                         ]
                     )
                     )


def scam(bot, update):
    bot.forward_message(chat_id=update.message.chat_id, from_chat_id=292633884, message_id=2158)


def rr(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="*Puedes descargar la ultima RR desde *[AQUÍ](https://sourceforge.net/projects/resurrectionremix-oreo/files/zl1/)",
                     parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


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


def efbot(bot, update):
    prohibited = ["http://tinyurl.com", "https://t.me", "http://t.me"]
    mensaje = update.message.text
    username = update.message.from_user.username
    id = update.message.from_user.id
    chat_title = update.message.chat.title
    print(username, id, chat_title)
    for x in prohibited:
        if x in mensaje:
            # bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.effective_user.id)
            bot.forward_message(chat_id=-1001122754147, from_chat_id=update.message.chat_id,
                                message_id=update.message.message_id)
            bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
            bot.send_message(chat_id=-1001122754147,
                             text="*USERNAME:* @{}\n*ID:* {}\n*Ha hecho spam en el chat:* {}".format(username, id,
                                                                                                     chat_title),
                             parse_mode=telegram.ParseMode.MARKDOWN)


def new_user(bot, update):
    message_texts = []
    for user in (update.message.new_chat_members or [update.message.from_user]):
        if not user.is_bot:
            user_name = user.first_name or user.last_name or user.username
            user_name = ", {}".format(user_name) if user_name else ""
            message_texts.append("*¡Bienvenid@*{}*, al grupo!*".format(user_name))
    if message_texts:
        bot.send_message(chat_id=update.message.chat_id, text='\n'.join(message_texts),
                         parse_mode=telegram.ParseMode.MARKDOWN)


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
            bot.send_message(chat_id=update.message.chat_id, text="*No puedo anclarlo!*",
                             parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)


# CommandHandler
restart = CommandHandler("r", restart)
start = CommandHandler("start", start)
botid = CommandHandler("id", id)
aosip = CommandHandler("aosip", aosip)
callback = CallbackQueryHandler(callback)
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
test = CommandHandler("test", test)
BROADCAST_HANDLER = CommandHandler("broadcast", broadcast)
ACTUALIZANDO = CommandHandler("actualizar", pull)
efbot = MessageHandler(Filters.entity("url"), efbot)
puto = MessageHandler(Filters.all, puto)

dispatcher = updater.dispatcher

dispatcher.add_handler(restart)
dispatcher.add_handler(start)
dispatcher.add_handler(botid)
dispatcher.add_handler(aosip)
dispatcher.add_handler(callback)
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
dispatcher.add_handler(efbot)
dispatcher.add_handler(new_user)
dispatcher.add_handler(ancla)
dispatcher.add_handler(di)
dispatcher.add_handler(ban)
dispatcher.add_handler(test)
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
