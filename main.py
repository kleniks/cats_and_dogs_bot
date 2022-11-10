import requests
import telebot
from telebot import types
from auth_date import token, api_key_cats, api_key_dogs

def get_cats():
    req = requests.get(f'https://api.thecatapi.com/v1/images/search?api_key={api_key_cats}')
    response = req.json()
    url_image = response[0]["url"]
    return url_image


def get_dogs():
    req = requests.get(f'https://api.thedogapi.com/v1/images/search?api_key={api_key_dogs}')
    response = req.json()
    url_image = response[0]["url"]
    return url_image


def telegram_bot(token):
    
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 
        f"Приветствую! Хочешь посмотреть на котиков и собачек? ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("Котикиииии")
        item1 = types.KeyboardButton("Собачкииии")
        markup.add(item, item1)
        bot.send_message(message.chat.id,'Выбери что хочешь',reply_markup=markup)


    @bot.message_handler(content_types=["text"])
    def send_image(message):
        if message.text == "Котикиииии":
            bot.send_photo(message.chat.id, get_cats())
        elif message.text == "Собачкииии":
            bot.send_photo(message.chat.id, get_dogs())    


    bot.polling()   


if __name__ == '__main__':
    telegram_bot(token)    
