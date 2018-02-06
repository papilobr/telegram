#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json
from functools import wraps
from telegram import ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

LOCATION = 'credentials/telegram.json'

# Load Telegram Credentials from LOCATION
with open(LOCATION) as data_file:
    DATA = json.load(data_file)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        ADMIN_LIST = []
        user_id = update.effective_user.id
        arq = open('data/admin.list', 'r')
        for item in arq:
            ADMIN_LIST.append(int(item.rstrip('\r\n')))
        if user_id not in ADMIN_LIST:
            update.message.reply_text('You are not authorized to execute commands using this bot.')
            msg = "*WARNING:* Unauthorized access denied for {}.".format(user_id)
            # *bold* _italic_ `fixed width font` [link](http://google.com).",
            bot.send_message(chat_id='63990603', text=msg, parse_mode=ParseMode.MARKDOWN)

            return
        msg = "*INFO:* Admin Level Access granted to {}.".format(user_id)
        bot.send_message(chat_id='63990603', text=msg, parse_mode=ParseMode.MARKDOWN)
        return func(bot, update, *args, **kwargs)
    return wrapped

class Telebot:
    def __init__(self):
        self.updater = Updater(DATA['token'])

    def run(self):
        @restricted
        def start(bot, update):
            update.message.reply_text('*FEEDBACK:* Go ahead master, do your deal...', parse_mode=ParseMode.MARKDOWN)

        def error(bot, update, error):
            if update is None:
                logging.warning(error)
            else:
                logging.warning('Update "%s" caused error "%s"' % (update, error))

        self.updater.dispatcher.add_handler(CommandHandler('start', start))
        self.updater.dispatcher.add_error_handler(error)
        # Start the Bot
        self.updater.start_polling()
        # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
        self.updater.idle()
