"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.


"""
import ephem
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


#PROXY = {
#    'proxy_url': 'socks5://t1.learn.python.ru:1080',
#    'urllib3_proxy_kwargs': {
#        'username': 'learn',
#        'password': 'python'
#    }
#}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def name_planet(update, context):
    user_text = update.message.text.split()
    user_planet = user_text[1]
    ephem_plan = planet_dict.get(user_planet, None)
    if ephem_plan != None:
        constell = ephem.constellation(planet_dict[user_planet])
        update.message.reply_text(constell)
    else:
        update.message.reply_text("Я не понял! Какую планету?")


def main():
    mybot = Updater("5713453213:AAHMrfHBQEcdV84uoENMzREVrkIcjUBaPdg", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', name_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

today = datetime.now()
planet_dict = {'Mars' : ephem.Mars(today), 'Venus' : ephem.Venus(today), 'Saturn' : ephem.Saturn(today), 'Jupiter' : ephem.Jupiter(today), 'Neptune' : ephem.Neptune(today), 'Uranus' : ephem.Uranus(today), 'Mercury' : ephem.Mercury(today)}
if __name__ == "__main__":
    main()
