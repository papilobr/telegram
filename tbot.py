#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.telebot import Telebot

'''
"message": 
{"message_id":22,"from":
{"id":63990603,
"is_bot":false,
"first_name":"Robson",
"last_name":"Eisinger",
"username":"reisinger",
"language_code":"pt-BR"},
"chat":
{"id":63990603,"first_name":"Robson","last_name":"Eisinger","username":"reisinger","type":"private"},
"date":1504108216,
"text":"oi"}}]}

'''
def main():
    bot = Telebot()
    print 'Starting Telegram Bot Server'
    bot.run()

if __name__ == "__main__":
    main()





