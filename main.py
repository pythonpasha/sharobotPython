import telebot
import config
import random
import os

list_one = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
list_word = list(['three', 'horse', 'dog', 'four', 'cat', 'rat', 'mouse', 'milk', 'sleep', 'pen'])
list_otvet = list(['3', 'лошадь', 'собака', '4', 'кошка', 'крыса', 'мышь', 'молоко', 'спать', 'ручка'])
otvetall = 0
randoma = random.randint(0, 9)
randoma2 = randoma
word = list_word[randoma2]
otvet = list_otvet[randoma2]
promcol = list_one[randoma2]
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    global word
    global otvet
    global randoma
    global promcol
    global randoma2

    global list_one
    global list_word
    global list_otvet
    randoma = random.randint(0, 9)
    randoma2 = randoma
    word = list_word[randoma2]
    otvet = list_otvet[randoma2]
    promcol = list_one[randoma2]

    bot.send_message(message.chat.id,
                     'привет,{1.first_name}\n я мега бот магистра моё имя {2.first_name} переведи слово '.format(
                         message.from_user, message.from_user, bot.get_me()), parse_mode='markdown')
    bot.send_message(message.chat.id, word.format(message.from_user, message.from_user, bot.get_me()),
                     parse_mode='markdown')


@bot.message_handler(content_types=['text'])
def echo(message):
    global list_word
    global word
    global randoma2
    global otvet
    global promcol
    global otvetall
    a = message.from_user.last_name
    print(a)
    w = message.text
    if w.lower() == otvet:
        otvetall = otvetall + 1
        list_one.insert(promcol, list_one[randoma2] + 1)

        bot.send_message(message.chat.id, 'молодец, {1.first_name}'.format(message.from_user, message.from_user),
                         parse_mode='markdown')
        bot.send_message(message.chat.id, 'твои баллы:'.format(message.from_user, message.from_user, bot.get_me()),
                         parse_mode='markdown')
        bot.send_message(message.chat.id, otvetall)
        bot.send_message(message.chat.id,
                         'твои баллы на это слово:'.format(message.from_user, message.from_user, bot.get_me()),
                         parse_mode='markdown')
        bot.send_message(message.chat.id, list_one[promcol])
        for i in range(len(list_one)):
            if list_one[i] == 5:
                path = 'webp\\animals\\webp\\'
                liststickers = os.listdir(path)
                print(liststickers)
                size = len(liststickers)
                num = random.randint(0, size)
                pathst = path + liststickers[num]
                sstickers = open(pathst, 'rb')
                bot.send_sticker(message.chat.id, sstickers)
                bot.send_message(message.chat.id,
                                 'поздравляю ты выучил это слово'.format(message.from_user, message.from_user,
                                                                         bot.get_me()), parse_mode='markdown')
                print(otvet, word)

        randoma = random.randint(0, 9)
        randoma2 = randoma
        word = list_word[randoma2]
        otvet = list_otvet[randoma2]
        promcol = list_one[randoma2]
        bot.send_message(message.chat.id,
                         'привет,{1.first_name}\n я мега бот магистра моё имя {2.first_name} переведи слово '.format(
                             message.from_user, message.from_user, bot.get_me()), parse_mode='markdown')
        bot.send_message(message.chat.id, word.format(message.from_user, message.from_user, bot.get_me()),
                         parse_mode='markdown')

    else:
        bot.send_message(message.chat.id,
                         '{1.first_name} не правильно правильный ответ-'.format(message.from_user, message.from_user),
                         parse_mode='markdown')
        bot.send_message(message.chat.id, otvet.format(message.from_user, message.from_user), parse_mode='markdown')
        bot.send_message(message.chat.id, 'твои баллы:'.format(message.from_user, message.from_user, bot.get_me()),
                         parse_mode='markdown')
        bot.send_message(message.chat.id, otvetall)

        randoma = random.randint(0, 9)
        randoma2 = randoma
        word = list_word[randoma2]
        otvet = list_otvet[randoma2]
        promcol = list_one[randoma2]

        bot.send_message(message.chat.id,
                         ' переведи слово '.format(
                             message.from_user, message.from_user, bot.get_me()), parse_mode='markdown')
        bot.send_message(message.chat.id, word.format(message.from_user, message.from_user, bot.get_me()),
                         parse_mode='markdown')


bot.polling(none_stop=True)
