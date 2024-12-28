
import telebot
from config import keys, TOKEN
from extensions import CriptoConvertor, ConvertionException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя волюты> \
    <в какую валюту перевести> \
    <количество переводимой волюты> \n Увидеть все доступные валюты /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text='Доступые волюты'
    for key in keys.keys():
        text =  '\n'.join((text, key ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convert (message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров')

        quote,base,amount = values
        total = CriptoConvertor.convert(quote, base, amount )
    except ConvertionException as e:
        bot.reply_to(message,f'Ошибка пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        a = total*float(amount)

        text = f'Цена {amount} {quote} в {base} - {a}'
        bot.send_message(message.chat.id, text)
bot.polling()

