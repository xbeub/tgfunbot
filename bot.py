import telebot

# Создаем экземпляр бота
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я прикольный бот. Чем могу помочь?')

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, 'Вы сказали: ' + message.text)

# Запускаем бота
bot.polling()
