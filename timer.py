# Таймер для поздравлений каждый день в определенное время (12.00)
import time
import telebot
import requests
import config


bot = telebot.TeleBot(config.TOKEN)
Main_User_Chat_ID = config.MAIN_USER_CHAT_ID

while True:
    time.sleep(3600)
    loc_tim = time.localtime()
    if loc_tim.tm_hour == 9:
        bot.send_message(Main_User_Chat_ID, f'<b>{loc_tim.tm_hour}</b>:{loc_tim.tm_min}     Поздравляю!',parse_mode='html')
        print(f'{loc_tim.tm_year}-{loc_tim.tm_mon}-{loc_tim.tm_mday}     {loc_tim.tm_hour}:{loc_tim.tm_min}   Поздравляю!')
    