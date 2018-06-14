""""Commands of the bot"""

import os
import random
import sys
from functools import wraps
from threading import Thread
from . import Db
import git
import telegram
from config import botconfig
import bot


def restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in get_admin():
            bot.send_message(chat_id=update.message.chat_id, text="No tienes permiso para hacer eso.",
                             parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
            return
        return func(bot, update, *args, **kwargs)

    return wrapped


@restricted
def add_admin(bot, update):
    pass
    user_id = update.effective_message.text.split(None, 1)
    if update.message.reply_to_message is not None:
        prev_user = update.message.reply_to_message.from_user.id
        prev_name = update.message.reply_to_message.from_user.username
        if prev_user:
            if prev_user not in get_admin():
                Db.Admin.create(id=prev_name)
                bot.send_message(chat_id=update.message.chat_id, text="Promocionado " + prev_name,
                                 reply_to_message_id=update.message.message_id)
            else:
                bot.send_message(chat_id=update.message.chat_id, text="El usuario " + prev_name + "ya es un admin",
                                 reply_to_message_id=update.message.message_id)
        else:
            if user_id[1]:
                Db.Admin.create(id=user_id[1])


def get_admin_ids(bot, chat_id):
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]


def get_admin():
    admins = Db.Admin.select()
    listofadmin = []
    for entry in admins:
        listofadmin.append(entry.id)
    return listofadmin


@restricted
def broadcast(bot, update):
    pass
    to_send = update.effective_message.text.split(None, 1)
    for x in botconfig.CHAT_IDS_ES:
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
    bot.Updater(token=botconfig.bot_token)
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
    # chat = update.effective_chat
    user_id = update.effective_user.id
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    code = update.message.from_user.language_code
    is_bot = update.message.from_user.is_bot
    # is_group = chat.type != "private" and chat.type != "channel"
    # if is_group:
    bot.send_message(chat_id=update.message.chat_id,
                     text="*ID del grupo:* " + str(chat_id) + "\n*Tu ID: *" + str(user_id) + "\nUsername: @" + str(
                         username) + "\nNombre: " + str(first_name) + "\nApellido: " + str(
                         last_name) + "\nLenguaje:" + str(code) + "\nBot: " + str(is_bot),
                     parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
    # else:
    bot.send_message(chat_id=update.message.chat_id, text="Tu ID:" + str(chat_id))


def cat(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo="https://giphy.com/gifs/cat-weird-bra-p4xp4BjHIdane")


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
            if update.message.reply_to_message is not None:
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
    # user = update.effective_user
    # message = update.effective_message
    is_group = chat.type != "private" and chat.type != "channel"
    prev_message = update.effective_message.reply_to_message
    # is_silent = False

    if prev_message and is_group:
        try:
            bot.pin_chat_message(chat_id=update.message.chat_id, message_id=prev_message.message_id)
        except:
            bot.send_message(chat_id=update.message.chat_id, text="*No puedo anclarlo!*",
                             parse_mode=telegram.ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)
