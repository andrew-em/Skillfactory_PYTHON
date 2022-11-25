import telebot
from config import money, TOKEN
from extensions import ConvertException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message: telebot.types.Message):
    text = "Введите команду в формате:\n <имя валюты> \
        <имя валюты в которую надо конвентировать> \
         <количество конвентируемой валюты>\n" \
         'Увидеть список всех доступных валют: /values \n \
           Информация о работе бота: /help'

    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def handle_help(message: telebot.types.Message):
    text = 'Конвертер валют выполняет:  \n  \
           -Показывает список доступных валют через команду: /values  \n  \
           -Конвертирует валюту через команду: <имя валюты> <имя валюты в которую надо конвентировать>\n \
           <количество конвентируемой валюты>'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in money.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertException('Введите меньше параметров.')

        quote, base, amount = values
        total_base = CurrencyConverter.get_price(quote, base, amount)

    except ConvertException as exc:
        bot.reply_to(message, f'Ошибка пользователя\n {exc}')

    except Exception as exc:
        bot.reply_to(message, f'Не удалось обработать команду\n {exc}')

    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()
