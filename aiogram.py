import os.path
from pathlib import Path

import telebot.types
from telebot.async_telebot import AsyncTeleBot
import asyncio
from config import *
import random
from telebot.types import *

# Инициализировали бота
bot = AsyncTeleBot(TOKEN)
listname = []
listchat = []
answer = 0

a = 0
b = 0


def menu1():
    menu1 = InlineKeyboardMarkup()
    menu1.add(InlineKeyboardButton(text='pavel', callback_data='god', row_width=123))
    menu1.add(InlineKeyboardButton(text='саша', callback_data='саша', row_width=233))
    return menu1


@bot.message_handler(commands=['start'])
async def start(message):
    global markup
    global chat_id
    global answerlist
    global answerlist2
    answerlist = ['спорт', 'искуство']
    answerlist2 = ['да', 'да']
    chat_id = message.chat.id
    last_name = message.from_user.last_name
    first_name = message.from_user.first_name
    print(chat_id)
    # Клавиатура
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    # await bot.send_message(chat_id, "Бодро пожаловать, *{0}* _{1}_!\nЯ - *{2}*, бот."
    #                       .format(last_name, first_name, bot.get_me().first_name), parse_mode='markdown')

    await bot.send_message(message.chat.id, text='hello', reply_markup=menu1())


@bot.message_handler(content_types=['sticker'])
async def echo_sticker(message):
    file_u_id = message.sticker.file_unique_id
    with open('sticker_file.txt', 'r') as file:
        memory_stiker_list = file.readlines()
    with open('sticker_file.txt', 'a+') as file:
        file.write(file_u_id + '\n')

    for file_id in memory_stiker_list:
        if file_id.replace("\n", "") == file_u_id:
            await bot.send_message(message.chat.id, text='😜😜😜')
            break
        else:
            with open('sticker_file.txt', 'a+') as file:
                file.write(file_u_id + '\n')
            await bot.send_message(message.chat.id, text='😜😜')
            break


@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call):
    if call.data == "god":
        global a
        global b
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        await bot.answer_callback_query(call.id, text='сколько будет' + str(a) + '+' + str(b))
        await bot.send_poll(chat_id=chat_id, question='балет это спорт или искуство', options=answerlist,
                            is_anonymous=False, allows_multiple_answers=False, reply_markup=markup)
    if call.data == 'саша':
        await bot.answer_callback_query(call.id, "тыц")
        await bot.send_poll(chat_id=chat_id, question='ты гей?', options=answerlist2,
                            is_anonymous=False, allows_multiple_answers=False, reply_markup=markup)


@bot.message_handler(content_types=['text'])
async def echo(message):
    global a
    w = message.text
    e = message.from_user.first_name
    if e == 'Паша':
        while 1:
            await bot.send_message(chat_id=-1001906690561, text=w)

    chat = message.chat.id
    print(chat)
    global b
    if message.text == (str(a + b)):
        await bot.send_message(message.chat.id, text='верно')
    await bot.send_message(message.chat.id, text=message.text, disable_notification=True, reply_markup=menu1())
    if message.text == 'красная кнопка':
        await bot.send_message(message.chat.id, 'b💣💣mmm', reply_markup=menu1())

    if message.text == 'синяя кнопка':
        await bot.send_message(message.chat.id, 'поздравляю ты спас мир', reply_markup=menu1())


@bot.message_handler(content_types=['sticker'])
async def answer_for_sticker(message):
    await bot.send_sticker(message.chat.id, message.sticker.file_id)
    await bot.send_message(message.chat.id, 'хватит спамить')


asyncio.run(bot.polling())
