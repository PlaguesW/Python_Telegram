from telegram.ext import Updater, CommandHandler, MessageHandler
import logging

# Установка уровня логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция, которая будет вызвана при получении команды /start
def start(update, context):
    update.message.reply_text('Привет! Я начну сбор ваших сообщений в группах Telegram.')

# Функция, которая будет вызвана при получении сообщения
def collect_messages(update, context):
    message = update.message

    # Проверяем, что сообщение от пользователя
    if message.from_user and message.from_user.is_self:
        # Здесь вы можете сохранить нужные вам данные в базе данных или файле
        with open('collected_messages.txt', 'a') as file:
            file.write(f'{message.date} - {message.text}\n')

# Основная функция
def main():
    # Получение токена бота
    token = ''

    # Инициализация объекта Updater с использованием токена бота
    updater = Updater(token=token, use_context=True)

    # Получение объекта диспетчера для обработки команд и сообщений
    dp = updater.dispatcher

    # Добавление обработчиков команд и сообщений
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.all, collect_messages))

    # Запуск бота
    updater.start_polling()

    # Завершение работы бота по Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
