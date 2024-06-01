import telebot
import sqlite3

from telebot import types

from GeneratingModule.GeneratingModule import GeneratingModule

bot = telebot.TeleBot('6687156907:AAHoKEW1Cuw4XojERiJOweX0ae-S0dc_5tU')
SQL_BASE = 'infobase.sqlite'


@bot.message_handler(commands=['start'])
def start(message):
    send_request(SQL_BASE,
                 'CREATE TABLE IF NOT EXISTS on_task (chat_id INT PRIMARY KEY, task INT, prototipe INT, answer INT);')
    zero_level(message)


@bot.message_handler(commands=['help'])
def help(message):
    text = 'На данный момент вспомогательной информации нет)\n' \
           'Отправьте /start для начала работы с генерацией заданий'
    bot.send_message(message.chat.id, text)


def zero_level(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton("Сгенерировать определенное задание"))
    bot.send_message(message.chat.id, "Что мне выполнить?", reply_markup=markup)
    bot.register_next_step_handler(message, first_level)


def first_level(message):
    if check_commands(message):
        return
    match message.text.lower():
        case "сгенерировать определенное задание":
            task(message)
        case _:
            bot.send_message(message.chat.id, "Я вас не понимаю, выберите команду из списка")
            zero_level(message)


def task(message):
    if check_commands(message):
        return
    text = 'Напишите номер задания (от 1 до 21)'
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, task_choose)


def task_choose(message):
    if check_commands(message):
        return
    task_id = ''.join(i for i in message.text if i.isdigit())

    if task_id == '':
        text = 'Пожалуйста, напишите номер задания (от 1 до 21)'
        bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(message, task_choose)
        return

    task_id = int(task_id)

    if task_id > 21 or task_id < 1:
        text = 'Пожалуйста, напишите номер задания (от 1 до 21)'
        bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(message, task_choose)
    else:
        set_task_id(message.chat.id, task_id)
        display_task_variants(message)


def display_task_variants(message):
    if check_commands(message):
        return
    task_id = get_task_id(message.chat.id)[0][0]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1, GeneratingModule.get_prototipes_num(task_id) + 1):
        markup.add(types.KeyboardButton(f"{i}"))
    markup.row(types.KeyboardButton("Сгенерировать случайный прототип"))
    bot.send_message(message.chat.id, GeneratingModule.get_task_info(task_id))
    bot.send_message(message.chat.id, "Что хотите решать?", reply_markup=markup)
    bot.register_next_step_handler(message, display_task)


def display_task(message):
    if check_commands(message):
        return
    task_id = get_task_id(message.chat.id)[0][0]

    if message.text.lower() == "сгенерировать случайный прототип":
        task_obj = GeneratingModule.get_random_task(task_id)
    else:
        prototipe_id = ''.join(i for i in message.text if i.isdigit())
        if prototipe_id == "":
            prototipe_id = get_prototype(message.chat.id)[0][0]
        else:
            prototipe_id = int(prototipe_id)

        if 0 < prototipe_id <= GeneratingModule.get_prototipes_num(task_id):
            set_prototype(message.chat.id, prototipe_id)
            task_obj = GeneratingModule.get_task(task_id, prototipe_id)
        else:
            bot.send_message(message.chat.id, "Такого прототипа не существует, введите один из номеров, указанных выше")
            bot.register_next_step_handler(message, display_task)
            return



    set_answer(message.chat.id, task_obj.Answer)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton("Показать ответ"))

    task_image = task_obj.get_image()
    if task_image is not None:
        bot.send_photo(message.chat.id, task_image)
    bot.send_message(message.chat.id, task_obj.get_text(), reply_markup=markup)
    bot.register_next_step_handler(message, answer_choose)


def answer_choose(message):
    if check_commands(message):
        return
    answer = message.text
    if answer.lower() == "показать ответ":
        show_answer(message)
        return

    special_symbols = ',.-'
    answer = ''.join(i for i in answer if i.isdigit() or i in special_symbols).replace(',', '.')
    if answer == "":
        bot.send_message(message.chat.id, "Чтобы дать ответ, необходимо написать число")
        bot.register_next_step_handler(message, answer_choose)
        return

    if float(answer) == float(get_answer(message.chat.id)[0][0]):
        bot.send_message(message.chat.id, "Этот ответ правильный!")
        show_answer(message, True)
    else:
        bot.send_message(message.chat.id, "Ответ неправильный")
        bot.register_next_step_handler(message, answer_choose)


def show_answer(message, answer_is_correct=False):
    if check_commands(message):
        return
    reply = ''
    if not answer_is_correct:
        reply += f'Правильный ответ: {get_answer(message.chat.id)[0][0]}\n'
    reply += 'Хотите решить еще одно задание?'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton("Вернуться на выбор задания"))
    markup.row(types.KeyboardButton("Вернуться к выбору прототипа"))
    markup.row(types.KeyboardButton("Сгенерировать похожее задание"))
    markup.row(types.KeyboardButton("Сгенерировать случайный прототип"))

    bot.send_message(message.chat.id, reply, reply_markup=markup)
    bot.register_next_step_handler(message, choose_next_step)


def choose_next_step(message):
    if check_commands(message):
        return
    match message.text.lower():
        case "вернуться на выбор задания":
            task(message)
        case "вернуться к выбору прототипа":
            display_task_variants(message)
        case "сгенерировать похожее задание":
            display_task(message)
        case "сгенерировать случайный прототип":
            display_task(message)
        case _:
            bot.send_message(message.chat.id, "Я вас не понимаю, пожалуйста, введите одну из команд в меню")
            bot.register_next_step_handler(message, choose_next_step)


@bot.message_handler()
def main(message):
    print('lol')


def get_task_id(chat_id):
    return send_select_request(SQL_BASE, f"SELECT task from on_task WHERE chat_id={chat_id}")


def set_task_id(chat_id, task_id):
    if len(get_task_id(chat_id)) == 0:
        request = f'INSERT INTO on_task (chat_id, task) VALUES ({chat_id}, {task_id})'
    else:
        request = f'UPDATE on_task SET task={task_id} WHERE chat_id={chat_id}'
    send_request(SQL_BASE, request)


def get_answer(chat_id):
    return send_select_request(SQL_BASE, f"SELECT answer from on_task WHERE chat_id={chat_id}")


def set_answer(chat_id, answer):
    if get_answer(chat_id) is None:
        send_request(SQL_BASE, f'INSERT INTO on_task (chat_id, answer) VALUES ({chat_id}, {answer})')
    else:
        send_request(SQL_BASE, f'UPDATE on_task SET answer={answer} WHERE chat_id={chat_id}')


def get_prototype(chat_id):
    return send_select_request(SQL_BASE, f"SELECT prototipe from on_task WHERE chat_id={chat_id}")


def set_prototype(chat_id, prototype):
    if get_answer(chat_id) is None:
        send_request(SQL_BASE, f'INSERT INTO on_task (chat_id, prototipe) VALUES ({chat_id}, {prototype})')
    else:
        send_request(SQL_BASE, f'UPDATE on_task SET prototipe={prototype} WHERE chat_id={chat_id}')


def send_request(base, request):
    connection = sqlite3.connect(base)
    cursor = connection.cursor()
    cursor.execute(request)
    connection.commit()
    cursor.close()
    connection.close()


def send_select_request(base, request):
    connection = sqlite3.connect(base)
    cursor = connection.cursor()
    cursor.execute(request)
    info = cursor.fetchall()
    cursor.close()
    connection.close()
    return info

def check_commands(message):
    match message.text.lower():
        case "/start":
            zero_level(message)
            return True
        case "/help":
            help(message)
            return True
        case _:
            return False


bot.polling(none_stop=True)
