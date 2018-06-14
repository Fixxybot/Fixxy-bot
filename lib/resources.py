""""Resources for the bot"""

import telegram


def aosip(bot, update):
    bot.sendMessage(
        update.message.chat_id,
        ' *ROMs PARA LePro3 y LeMax2* ', parse_mode=telegram.ParseMode.MARKDOWN,
        reply_markup=telegram.InlineKeyboardMarkup(
            [
                [telegram.InlineKeyboardButton('📲LePro3', callback_data='LePro3'),
                 telegram.InlineKeyboardButton("📲LeMax2", callback_data='LeMax2')],
                [telegram.InlineKeyboardButton('AOSiP', url='http://get.aosiprom.com/zl1'),
                 telegram.InlineKeyboardButton("AOSiP", url='http://get.aosiprom.com/x2')],
                [telegram.InlineKeyboardButton('AOKP', url="http://aokp.co/"),
                 telegram.InlineKeyboardButton("AICP", url='http://dwnld.aicp-rom.com/?device=x2')],
                [telegram.InlineKeyboardButton('AEX', url='https://androidfilehost.com/?w=files&flid=261896'),
                 telegram.InlineKeyboardButton("DirtyUnicorns",
                                               url="https://drive.google.com/file/d/1w04FmjEdU8-AWgsoBCk1UFIy8feOcykm/view")],
                [telegram.InlineKeyboardButton('LineageOS', url='https://download.lineageos.org/zl1'),
                 telegram.InlineKeyboardButton("LineageOS", url='https://download.lineageos.org/x2')],
                [telegram.InlineKeyboardButton('AICP', url='http://dwnld.aicp-rom.com/?device=zl1'),
                 telegram.InlineKeyboardButton("AEX", url='https://downloads.aospextended.com/x2')],
                [telegram.InlineKeyboardButton('RR',
                                               url="https://sourceforge.net/projects/resurrectionremix-oreo/files/zl1/"),
                 telegram.InlineKeyboardButton("PixelExperience", url='https://download.pixelexperience.org/x2/')],
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

        bot.sendDocument(chat_id=query.message.chat_id, document="BQADBAADjQQAArffKVOQ6Qtts3CXrwI")
    if update.callback_query.data == "722":
        bot.edit_message_text(text="TWRP para el 722:", chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
        bot.sendDocument(chat_id=query.message.chat_id, document="BQADBAADiwQAArffKVMUyszyzmjYmAI")
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


def grupos(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="🌐*GRUPOS QUE TE PUEDEN INTERESAR:*\n\n🌐*LE PRO 3*\n├[📱LePro3](https://t.me/joinchat/CszTz0YaMuyR3MwBuzy-nw)\n├[📱LePro3x722](https://t.me/Leecox722)\n└[📱LePro3(Inglés)](https://t.me/leecolepro3roms)\n\n🌐*LE MAX 2*\n├[📱LeMax2AOSIP](https://t.me/AOSiP_x2)\n└[📱LeMax2INTERNACIONAL](https://t.me/lemax2xda)",
                     parse_mode=telegram.ParseMode.MARKDOWN)
