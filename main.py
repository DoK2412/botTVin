import telebot
import user
import datetime


from settings import token_bot, password
from telebot import types


import logging.config
from logger import logger_config

bot = telebot.TeleBot(token_bot)


logging.config.dictConfig(logger_config)  # подключение файла логеров
log_error = logging.getLogger('app_error')  # создание сборщика ошибок
log_info = logging.getLogger('app_info')
date_of_creation = datetime.datetime.now()


@bot.message_handler(commands=['start', 'привет', 'меню'])
def start_handler(message):
  try:

    users = user.Users.get_user(message.from_user.id,
                        message.from_user.first_name,
                        message.from_user.username,
                        message.from_user.last_name)

    log_info.info(f'{users.name} {users.last_name}  Ник: {users.surname}  ')

    keyboard = types.InlineKeyboardMarkup()
    bottum1 = types.InlineKeyboardButton("Настройка и установка TV", callback_data="тв")
    bottum2 = types.InlineKeyboardButton("Установка и настройка интернета", callback_data="интернет")
    bottum3 = types.InlineKeyboardButton("Скупка продажа БУ техники", callback_data="бу")
    bottum4 = types.InlineKeyboardButton("Консультации", callback_data="консультации")
    bottum5 = types.InlineKeyboardButton("Подбор новой техники", callback_data="новая")
    bottum6 = types.InlineKeyboardButton("Видеонаблюдение", callback_data="видео")
    bottum7 = types.InlineKeyboardButton("О нас", callback_data="нас")
    bottum8 = types.InlineKeyboardButton("Контакты", callback_data="контакты")
    bottum9 = types.InlineKeyboardButton("Статистика", callback_data="статистика")
    keyboard.add(bottum1)
    keyboard.add(bottum2)
    keyboard.add(bottum3)
    keyboard.add(bottum4)
    keyboard.add(bottum5)
    keyboard.add(bottum6)
    keyboard.add(bottum7)
    keyboard.add(bottum8)
    keyboard.add(bottum9)
    bot.send_message(message.chat.id, 'TVin - телевидение и интерент.\nДобро пожаловать {0}!'.format(message.from_user.first_name), reply_markup=keyboard)
  except:
    log_error.error('произошла ошибка: ', exc_info=True)


@bot.callback_query_handler(func=lambda call: call.data in ['тв'])
def television(message):
  try:
    keyboar = types.InlineKeyboardMarkup()
    bottum = types.InlineKeyboardButton("меню", callback_data="меню")
    keyboar.add(bottum)

    user.Users.get_user(message.from_user.id,
                        message.from_user.first_name,
                        message.from_user.username,
                        message.from_user.last_name)

    bot.send_message(message.from_user.id, "'Настройка и установка спутникового, цифрового"
                                           " и интерактивного TV'\n\n    Установим и настроим "
                                           "(а так же научим пользоваться) спутниковое, цифровое"
                                           " и интерактивное TV.\n    Подберем телевидение под Ваш"
                                           " вкус каналов и желаемому месту установки.\n    Так же"
                                           " настроим ранее установленные комплекты, настроим "
                                           "комплекты по специальному прибору.\n    Поможем разобраться"
                                           " с надписью 'Нет сигнала' и перебоями (квадратиками) при"
                                           " просмотре.", reply_markup=keyboar)

  except:
    log_error.error('произошла ошибка: ', exc_info=True)


@bot.callback_query_handler(func=lambda call: call.data in ['интернет'])
def internet(message):
  try:
    keyboar = types.InlineKeyboardMarkup()
    bottum = types.InlineKeyboardButton("меню", callback_data="меню")
    keyboar.add(bottum)

    user.Users.get_user(message.from_user.id,
                        message.from_user.first_name,
                        message.from_user.username,
                        message.from_user.last_name)

    bot.send_message(message.from_user.id, "'Установка и настройка интернета'"
                                           "\n\nНастраиваем и устанавливаем, а так же подбираем комплекты и тарифы"
                                           " мобильного интернета в Ваш дом, дачу или квартиру которая полностью "
                                           "удивлетворит Ваши потребности касаемо интернета.\n    Помимо подбора "
                                           "комплекта персонально под Вас есть и готовые комплекты под ключ которые "
                                           "состоят из:\n   - внешняя антера;\n   - модем;\n   - роутер;\n   - СИМ карта"
                                           " с безлимитным интернетом\n      без ограничения скорости.\n\n    Стоимость "
                                           "установки и настройки нашего комплекта под ключ составляет 19 400 р.", reply_markup=keyboar)
  except:
    log_error.error('произошла ошибка: ', exc_info=True)


@bot.callback_query_handler(func=lambda call: call.data in ['бу'])
def television(message):
  try:
    keyboar = types.InlineKeyboardMarkup()
    bottum = types.InlineKeyboardButton("меню", callback_data="меню")
    keyboar.add(bottum)

    user.Users.get_user(message.from_user.id,
                        message.from_user.first_name,
                        message.from_user.username,
                        message.from_user.last_name)

    bot.send_message(message.from_user.id, "'Скупка продажа БУ техники'\n\n      "
                                           "Если у Вас завалялась ненужная или не рабочая техника"
                                           " вы можете обратиться к нам.\n      Мы приедем, осмотрим"
                                           " и оценим Вашу технику. Предложим свои условия по выкупу,"
                                           " а так же выслушаем Ваши.\n      Так же если Вам необходима"
                                           " недорогая техника поможем Вам подобрать или предложим то"
                                           " что есть в наличии.", reply_markup=keyboar)
  except:
    log_error.error('произошла ошибка: ', exc_info=True)


@bot.callback_query_handler(func=lambda call: call.data in ['консультации'])
def television(message):
  try:
    keyboar = types.InlineKeyboardMarkup()
    bottum = types.InlineKeyboardButton("меню", callback_data="меню")
    keyboar.add(bottum)

    user.Users.get_user(message.from_user.id,
                        message.from_user.first_name,
                        message.from_user.username,
                        message.from_user.last_name)

    bot.send_message(message.from_user.id, "'Консультации'\n\n     По всем интересующим Вас вопросам"
                                           " и для решения проблем удаленно вы можете обращаться по"
                                           " нашим контактам.", reply_markup=keyboar)
  except:
    log_error.error('произошла ошибка: ', exc_info=True)


@bot.callback_query_handler(func=lambda call: call.data in ['новая'])
def television(message):
  try:
    keyboar = types.InlineKeyboardMarkup()
    bottum = types.InlineKeyboardButton("меню", callback_data="меню")
    keyboar.add(bottum)

    user.Users.get_user(message.from_user.id,
                        message.from_user.first_name,
                        message.from_user.username,
                        message.from_user.last_name)

    bot.send_message(message.from_user.id, "'Подбор новой тхники'\n\n     Если Вы не распологаете достаточным"
                                           " временем или хотите быть уверенным в своей покупке всегда можете"
                                           " обращаться к нам.\n      Мы подберем качественную, подходящую по"
                                           " Вашим требованиям технику, а так же доставим ее и при необходимости"
                                           " осуществим установку и настройку.", reply_markup=keyboar)
  except:
    log_error.error('произошла ошибка: ', exc_info=True)


@bot.callback_query_handler(func=lambda call: call.data in ['видео'])
def television(message):
  try:
    keyboar = types.InlineKeyboardMarkup()
    bottum = types.InlineKeyboardButton("меню", callback_data="меню")
    keyboar.add(bottum)

    user.Users.get_user(message.from_user.id,
                        message.from_user.first_name,
                        message.from_user.username,
                        message.from_user.last_name)

    bot.send_message(message.from_user.id, "'Видеонаблюдение'\n\n     Установим и настроим видеонаблюдение что"
                                           " бы Вы были спокойны когда оставляете свой дом на долгое "
                                           "время.\n      Вы можете удаленно наблюдать за тем что происходит у"
                                           " Вас как внутри дома так и на всей территории.", reply_markup=keyboar)
  except:
    log_error.error('произошла ошибка: ', exc_info=True)


@bot.callback_query_handler(func=lambda call: call.data in ['нас'])
def television(message):
  try:
    keyboar = types.InlineKeyboardMarkup()
    bottum = types.InlineKeyboardButton("меню", callback_data="меню")
    keyboar.add(bottum)

    user.Users.get_user(message.from_user.id,
                        message.from_user.first_name,
                        message.from_user.username,
                        message.from_user.last_name)

    bot.send_message(message.from_user.id, "'О нас'\n\n     Нас зовут Артур и Николай мы долгое время проработали"
                                           " в магазине цифровой техники (опыт более 7ми лет) так же в течении 5 лет"
                                           " подрабатывали установкой телевидения и интернета.\n      Имея большую"
                                           " клиентскую базурешили полностью отдаться делу которое нам очень нравится,"
                                           " а именно установке, настройки и подбору техники, а так же общению с хорошими"
                                           " людьми.\n      Работаем по Можайскому, Наро-Фоминскому, Одинцовскому и"
                                           " Рузскому районам.", reply_markup=keyboar)
  except:
    log_error.error('произошла ошибка: ', exc_info=True)


@bot.callback_query_handler(func=lambda call: call.data in ['контакты'])
def television(message):
  try:
    keyboar = types.InlineKeyboardMarkup()
    bottum = types.InlineKeyboardButton("меню", callback_data="меню")
    keyboar.add(bottum)

    user.Users.get_user(message.from_user.id,
                        message.from_user.first_name,
                        message.from_user.username,
                        message.from_user.last_name)

    bot.send_message(message.from_user.id, "'О нас'\n\n     "
                                           "Артур\n\n      +79778173256\n\n      "
                                           "Николай\n\n      +79990041293", reply_markup=keyboar)
    # bot.send_message(message.from_user.id, "+79778173256")
    # bot.send_message(message.from_user.id, "Николай, reply_markup=keyboar)")
    # bot.send_message(message.from_user.id, "+79778173256")
  except:
    log_error.error('произошла ошибка: ', exc_info=True)


@bot.callback_query_handler(func=lambda call: call.data in ['статистика'])
def statistic(message):
  try:
    passwords = bot.send_message(message.from_user.id, 'Введите пароль для получения статистики:')
    bot.register_next_step_handler(passwords, statistic_out)
  except:
    log_error.error('произошла ошибка: ', exc_info=True)


def statistic_out(massage):
  try:
    if massage.text == password:
      with open('/root/botTVin/loggins/info.log', 'r', encoding='utf-8') as info:
        statistics = info.read()
        bot.send_message(massage.from_user.id, statistics)
        past_days= str(date_of_creation - datetime.datetime.now()).split()[0]
      if abs(int(past_days)) % 7 == 0:
        with open('/root/botTVin/loggins/info.log', 'w', encoding='utf-8') as info:
          info.write(f'Файл был очищен {datetime.datetime.now()}\n')
    else:
      bot.send_message(massage.from_user.id, 'Пароль не верен. В доступе отказано.')
      statistic(massage)

  except:
    log_error.error('произошла ошибка: ', exc_info=True)


@bot.callback_query_handler(func=lambda call: call.data in ['меню'])
def meny(message):
  try:
    keyboard = types.InlineKeyboardMarkup()
    bottum1 = types.InlineKeyboardButton("Настройка и установка TV", callback_data="тв")
    bottum2 = types.InlineKeyboardButton("Установка и настройка интернета", callback_data="интернет")
    bottum3 = types.InlineKeyboardButton("Скупка продажа БУ техники", callback_data="бу")
    bottum4 = types.InlineKeyboardButton("Консультации", callback_data="консультации")
    bottum5 = types.InlineKeyboardButton("Подбор новой техники", callback_data="новая")
    bottum6 = types.InlineKeyboardButton("Видеонаблюдение", callback_data="видео")
    bottum7 = types.InlineKeyboardButton("О нас", callback_data="нас")
    bottum8 = types.InlineKeyboardButton("Контакты", callback_data="контакты")
    bottum9 = types.InlineKeyboardButton("Статистика", callback_data="статистика")
    keyboard.add(bottum1)
    keyboard.add(bottum2)
    keyboard.add(bottum3)
    keyboard.add(bottum4)
    keyboard.add(bottum5)
    keyboard.add(bottum6)
    keyboard.add(bottum7)
    keyboard.add(bottum8)
    keyboard.add(bottum9)
    bot.send_message(message.from_user.id,
                     'TVin - телевидение и интерент.\nДобро пожаловать {0}!'.format(message.from_user.first_name),
                     reply_markup=keyboard)

  except:
    log_error.error('произошла ошибка: ', exc_info=True)


bot.polling(none_stop=True, interval=0)