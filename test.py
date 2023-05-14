import os.path
from pathlib import Path

import telebot.types
from telebot.async_telebot import AsyncTeleBot
import asyncio
from config import *
import random
from telebot.types import *

bot = AsyncTeleBot(TOKEN)

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(REPLY_LIST[0])
markup.add(REPLY_LIST[1])

listq=['']
lista=['']

bal = 0
def menu1():

    inline_markup = InlineKeyboardMarkup()

    i=1+1
    menu1.add(InlineKeyboardButton(text=lista[i],callback_data=str(i),row_width = 12))
    return menu1
@bot.message_handler(commands=['start'])
async def start(message):
    global markup
    await bot.send_message(message.chat.id ,text ='mfdjvsh;df',reply_markup=markup)

@bot.message_handler(commands=['quest'])
async def quest(message):
    for i in range(5):
         menu1(i)





@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call):
    if call.data == (1):
        print('ffgf')


        if call.data == 'саша':
            await bot.answer_callback_query(call.id, "тыц")
            await bot.send_poll(call.message.chat.id, reply_markup=markup)


asyncio.run(bot.polling())