#импорт библиотек
import telebot 
from telebot import types
from glob import glob 
from random import choice
import random

# универсальный токен 
token='Ваш токен'

bot=telebot.TeleBot(token)  # 1 бот 


@bot.message_handler(commands=['start'])  #ответ на команду start
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    postcard_btn = types.InlineKeyboardButton(text='Открытка')
    markup.add(postcard_btn)
    end_btn = types.InlineKeyboardButton(text='Конец света')
    markup.add(end_btn)
    bot.send_message(message.chat.id,text='Привет, {0.first_name}! Я добрутро_бот. Я могу: отправить открытку (Напиши "Открытка"); сказать сколько осталось дней до конца света (Напиши "Конец света") '.format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['help'])  #овет на команду help
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    postcard_btn = types.InlineKeyboardButton(text='Открытка')
    markup.add(postcard_btn)
    end_btn = types.InlineKeyboardButton(text='Конец света')
    markup.add(end_btn)
    bot.send_message(message.chat.id,text='Я могу: отправить открытку (Напиши "Открытка"); сказать сколько осталось дней до конца света (Напиши "Конец света") '.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])  #обработка сообщений пользователя
def get_text_messages(message):
    if (message.text == 'Открытка'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            day_btn = types.InlineKeyboardButton(text='Доброе утро')
            markup.add(day_btn)
            night_btn = types.InlineKeyboardButton(text='Спокойной ночи')
            markup.add(night_btn)
            back_btn = types.InlineKeyboardButton(text='Назад')
            markup.add(back_btn)
            bot.send_message(message.chat.id,text="Выберите какие открытки хотите видеть".format(message.from_user), reply_markup=markup)
    elif (message.text == 'Доброе утро'):
            lists = glob('img/*')  #создаёт список из изображений в папке img
            picture = choice(lists)  #выбирает рандомное изображение из списка
            with open(picture, 'rb') as f:  #открывает выбранное избражение
                bot.send_photo(message.chat.id, f)  #отправляет изображение
    elif (message.text == 'Спокойной ночи'):  #всё тоже самое с файлами из другой папки
            lists = glob('img_night/*')
            picture = choice(lists)
            with open(picture, 'rb') as d:
                bot.send_photo(message.chat.id, d)
    elif (message.text == 'Конец света'):
            bot.send_message(message.chat.id,text="Количество дней до следующего конца света:".format(message.from_user))
            bot.send_message(message.chat.id, random.randint(1, 1000))  #отправляет рандомное чисо из диапазона
    elif (message.text == 'Назад'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            postcard_btn = types.InlineKeyboardButton(text='Открытки')
            markup.add(postcard_btn)
            end_btn = types.InlineKeyboardButton(text='Конец света')
            markup.add(end_btn)
            bot.send_message(message.chat.id,text="Вот что я могу:".format(message.from_user), reply_markup=markup)

            
bot.infinity_polling()
    


